"""
Teljes RAG pipeline orchestrátor.

Adatfolyam:
  kérdés
    → HyDE (Haiku): hipotézis-dokumentum generálás
    → embed (OpenAI): hipotézis vektorizálása
    → retrieve (pgvector): top-K chunk lekérés
    → rerank (Cohere): relevancia szerinti átrendezés, top-N
    → generate (Sonnet): ajánlatszöveg + grounding
    → válasz forrásokkal

Debug mód: minden lépés kimenetét logolja — "vakon fejleszteni RAG-ot
rossz döntés" (HF3 útmutató tanácsa alapján).
"""
from src.pipeline.hyde import generate_hypothesis
from src.pipeline.retriever import retrieve
from src.pipeline.reranker import rerank
from src.pipeline.generator import generate_answer
from src.ingest.embedder import embed_single
from rich import print as rprint


def run(question: str, debug: bool = False) -> dict:
    """
    Lefuttatja a teljes pipeline-t egy kérdésre.

    Visszaad:
        answer: str
        sources: list[dict]
        has_answer: bool
        debug_info: dict (ha debug=True)
    """
    debug_info = {}

    # 1. HyDE — hipotézis generálás
    hypothesis = generate_hypothesis(question)
    if debug:
        rprint(f"\n[bold cyan]HyDE hipotézis:[/bold cyan]\n{hypothesis}")
        debug_info["hypothesis"] = hypothesis

    # 2. Embedding — a hipotézist vektorizáljuk, nem a kérdést
    hypothesis_vec = embed_single(hypothesis)
    if debug:
        rprint(f"\n[dim]Embedding dim: {len(hypothesis_vec)}[/dim]")

    # 3. Raw retrieval — top-K chunk pgvector-ból
    raw_results = retrieve(hypothesis)
    if debug:
        rprint(f"\n[bold cyan]Raw retrieval ({len(raw_results)} chunk):[/bold cyan]")
        for i, r in enumerate(raw_results[:5]):
            rprint(f"  {i+1}. [{r['score']:.3f}] {r['doc_title'][:60]}")
        debug_info["raw_retrieval"] = [
            {"rank": i+1, "score": r["score"], "title": r["doc_title"], "url": r["source_url"]}
            for i, r in enumerate(raw_results)
        ]

    # 4. Rerank — Cohere átrendezi
    reranked = rerank(question, raw_results)
    if debug:
        rprint(f"\n[bold cyan]Rerank után (top-{len(reranked)}):[/bold cyan]")
        for i, r in enumerate(reranked):
            rprint(f"  {i+1}. [rerank: {r['rerank_score']:.3f}] {r['doc_title'][:60]}")
        debug_info["reranked"] = [
            {"rank": i+1, "rerank_score": r["rerank_score"], "title": r["doc_title"]}
            for i, r in enumerate(reranked)
        ]

    # 5. Generálás
    result = generate_answer(question, reranked)
    result["debug_info"] = debug_info if debug else {}

    return result


def run_raw_only(question: str) -> dict:
    """
    Csak nyers vektorkeresés (HyDE + embed + retrieve, rerank és generate nélkül).
    A golden set összehasonlításhoz.
    """
    hypothesis = generate_hypothesis(question)
    raw_results = retrieve(hypothesis)
    # Mock generálás: csak az első chunk tartalmát adjuk vissza
    if not raw_results:
        return {"answer": "Nincs találat.", "sources": [], "has_answer": False, "raw_chunks": []}
    top = raw_results[0]
    return {
        "answer": top["content"],
        "sources": [{"title": top["doc_title"], "url": top["source_url"]}],
        "has_answer": True,
        "raw_chunks": raw_results,
    }
