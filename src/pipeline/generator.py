"""
Válasz- / ajánlatszöveg-generálás — Anthropic Claude Sonnet.

Miért Sonnet a végső generáláshoz?
- Haiku-nál jobb minőségű, strukturált szöveg (ajánlatnál ez számít)
- Grounding: ha nincs releváns forrás, kimondja — nem talál ki tartalmat
- Forrásokat kötelezően hivatkozza (doc_title + source_url)
"""
import anthropic
from src.config import ANTHROPIC_API_KEY, GENERATION_MODEL

client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

SYSTEM_PROMPT = """Te az NRC piackutató cég AI asszisztense vagy, aki ajánlatok szövegezésében segít.

Feladatod: a megadott kontextus-dokumentumok alapján írj szakmai ajánlatszöveg-részletet vagy válaszolj a kérdésre.

Szabályok:
1. CSAK a megadott forrásokban szereplő információt használd.
2. Ha a forrásokban nincs elegendő információ, mondd ki egyértelműen:
   "A rendelkezésre álló tudásbázisban nincs elegendő információ erről."
3. Minden állítás után jelöld a forrást: [Forrás: <dokumentum cím>]
4. Ne találj ki árazást, mintaméretet vagy konkrét számot, ha az nincs a forrásban.
5. Stílus: szakmai, tömör, NRC hangvételű — nem marketinges, hanem hiteles.
Magyar nyelven írj."""


def generate_answer(question: str, context_chunks: list[dict]) -> dict:
    """
    Generál ajánlatszöveg-részletet a retrieval által visszahozott chunkokból.

    Visszaad:
        answer: str — a generált szöveg
        sources: list — hivatkozott források
        has_answer: bool — volt-e elegendő kontextus
    """
    if not context_chunks:
        return {
            "answer": "A rendelkezésre álló tudásbázisban nincs elegendő információ erről.",
            "sources": [],
            "has_answer": False,
        }

    context_text = "\n\n---\n\n".join(
        f"[Forrás: {c['doc_title']} | {c['source_url']}]\n{c['content']}"
        for c in context_chunks
    )

    response = client.messages.create(
        model=GENERATION_MODEL,
        max_tokens=1000,
        system=SYSTEM_PROMPT,
        messages=[
            {
                "role": "user",
                "content": f"Kontextus dokumentumok:\n\n{context_text}\n\n---\n\nKérdés / feladat: {question}",
            }
        ],
    )

    answer = response.content[0].text

    # Grounding ellenőrzés: ha az agent kimondja, hogy nincs adat
    has_answer = "nincs elegendő információ" not in answer.lower()

    sources = [
        {"title": c["doc_title"], "url": c["source_url"]}
        for c in context_chunks
    ]

    return {
        "answer": answer,
        "sources": sources,
        "has_answer": has_answer,
    }
