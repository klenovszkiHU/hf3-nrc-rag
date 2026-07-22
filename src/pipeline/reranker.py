"""
Reranking — Cohere rerank-multilingual-v3.0.

Miért Cohere és nem cross-encoder?
- Natív multilingual (magyar szöveg nem degradálódik)
- API-alapú: nincs GPU követelmény
- rerank-multilingual-v3.0 érti a kérdés-dokumentum relevancia finomságait,
  amit a cosine similarity nem: pl. "omnibusz vs ad hoc" különbség

A reranker pontosabban ítéli meg, melyik chunk valóban válaszolja meg
a kérdést — ez különösen fontos ajánlatszöveg-generálásnál, ahol
nem elég a szótári hasonlóság, szemantikai egyezés kell.
"""
import cohere
from src.config import COHERE_API_KEY, RERANK_MODEL, RERANK_TOP_N

co = cohere.Client(api_key=COHERE_API_KEY)


def rerank(query: str, documents: list[dict], top_n: int = RERANK_TOP_N) -> list[dict]:
    """
    Átrendezi a dokumentumokat a query relevanciája szerint.
    Visszaad top_n darabot, Cohere relevance_score-ral kiegészítve.
    """
    if not documents:
        return []

    texts = [d["content"] for d in documents]
    results = co.rerank(
        model=RERANK_MODEL,
        query=query,
        documents=texts,
        top_n=top_n,
    )

    reranked = []
    for r in results.results:
        doc = documents[r.index].copy()
        doc["rerank_score"] = r.relevance_score
        reranked.append(doc)

    return reranked
