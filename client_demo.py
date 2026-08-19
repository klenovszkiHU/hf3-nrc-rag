"""
Ügyfél-belépőpont a RAG pipeline-ra (demó).

Nem módosítja a meglévő pipeline logikát (hyde/retriever/reranker/generator) —
csak felhasználja ezeket, és köréjük épít egy PII-szűrőt + eszkalációs
kapcsolót + naplózást.

Folyamat egy kérdésre:
  1. PII-maszkolás (a pipeline SOSE lát nyers e-mailt/telefonszámot/stb.)
  2. szabály alapú eszkaláció-ellenőrzés (kulcsszó) — ha talál, NEM megy tovább
  3. ha nem eszkalált: HyDE + retrieve + rerank lefut, megnézzük a top score-t
  4. score alapú eszkaláció-ellenőrzés — ha a score gyenge, NEM generálunk választ
  5. ha idáig eljutottunk: generálás, válasz kiírása forrásokkal,
     jelezve, hogy emberi jóváhagyásra vár
  6. minden esetben egy run_log sor kerül az adatbázisba

Futtatás: python client_demo.py
"""
import time
import uuid
from datetime import datetime

from rich import print as rprint

from src.db import init_db, get_session, RunLog
from src.client.pii import mask, unmask
from src.client.escalation import check_rule_based, check_score_based, SCORE_THRESHOLD
from src.pipeline.hyde import generate_hypothesis
from src.pipeline.retriever import retrieve
from src.pipeline.reranker import rerank
from src.pipeline.generator import generate_answer

ESCALATION_MESSAGE = (
    "Ezt a kérdést egy kollégánk fogja megválaszolni — továbbítottuk a "
    "csapatnak, hamarosan jelentkezünk."
)


def handle_question(question: str, session_id: str) -> None:
    t0 = time.time()
    db_session = get_session()

    # 1. PII-maszkolás — a pipeline innentől csak maszkolt szöveget lát
    masked_question, mapping = mask(question)

    answer_text = None
    top_rerank_score = None
    top_source = None
    sources = []

    # 2. szabály alapú eszkaláció — nem fut le a pipeline
    rule_reason = check_rule_based(masked_question)

    if rule_reason:
        outcome = "escalated"
        escalation_reason = rule_reason
        approval_status = None  # nincs mit jóváhagyni, nem generáltunk választ
    else:
        # 3. HyDE + retrieve + rerank — csak eddig megyünk, generálás előtt
        hypothesis = generate_hypothesis(masked_question)
        raw_results = retrieve(hypothesis)
        reranked = rerank(masked_question, raw_results)

        if reranked:
            top_rerank_score = reranked[0]["rerank_score"]
            top_source = reranked[0]["doc_title"]

        # 4. score alapú eszkaláció
        score_reason = check_score_based(top_rerank_score)

        if score_reason:
            outcome = "escalated"
            escalation_reason = score_reason
            approval_status = None
        else:
            # 5. generálás — csak akkor, ha egyik eszkalációs ok sem állt fenn
            result = generate_answer(masked_question, reranked)
            answer_text = unmask(result["answer"], mapping)
            sources = result["sources"]
            outcome = "answered"
            escalation_reason = None
            approval_status = "pending"

    latency_ms = int((time.time() - t0) * 1000)

    # --- kiírás az ügyfélnek ---
    if outcome == "escalated":
        rprint(f"\n[yellow]{ESCALATION_MESSAGE}[/yellow]")
        rprint(f"[dim](eszkalációs ok: {escalation_reason})[/dim]")
    else:
        rprint(f"\n[bold]Válasz:[/bold]\n{answer_text}")
        if sources:
            rprint("\n[bold]Források:[/bold]")
            for s in sources:
                rprint(f"  - {s['title']} ({s['url']})")
        rprint("\n[yellow]Ez a válasz még emberi jóváhagyásra vár, mielőtt kiküldjük.[/yellow]")

    # --- naplózás — mindig maszkolt kérdésszöveggel ---
    log_row = RunLog(
        created_at=datetime.utcnow(),
        session_id=session_id,
        question_masked=masked_question,
        answer_text=answer_text,
        top_rerank_score=top_rerank_score,
        top_source=top_source,
        latency_ms=latency_ms,
        cost_usd=None,  # nincs pontos token-alapú költségszámítás ebben a demóban
        outcome=outcome,
        escalation_reason=escalation_reason,
        approval_status=approval_status,
    )
    db_session.add(log_row)
    db_session.commit()
    db_session.close()


def main() -> None:
    init_db()
    session_id = str(uuid.uuid4())[:8]

    rprint("[bold cyan]NRC ügyfél-demó[/bold cyan] — írj be egy kérdést (kilépés: 'exit')\n")

    while True:
        question = input("Kérdés: ").strip()
        if not question:
            continue
        if question.lower() in ("exit", "quit"):
            break

        handle_question(question, session_id)
        print()


if __name__ == "__main__":
    main()
