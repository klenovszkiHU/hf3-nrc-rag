"""
Vektor retrieval — pgvector cosine similarity.
"""
from sqlalchemy import text
from src.db import get_session
from src.ingest.embedder import embed_single
from src.config import RETRIEVAL_TOP_K, SIMILARITY_THRESHOLD


def retrieve(query_text: str, top_k: int = RETRIEVAL_TOP_K) -> list[dict]:
    embedding = embed_single(query_text)
    vec_str = "[" + ",".join(str(x) for x in embedding) + "]"

    session = get_session()
    try:
        rows = session.execute(
            text("""
                SELECT
                    content, doc_title, section_header,
                    source_url, source_name,
                    1 - (embedding <=> CAST(:vec AS vector)) AS score
                FROM chunks
                WHERE 1 - (embedding <=> CAST(:vec AS vector)) > :threshold
                ORDER BY embedding <=> CAST(:vec AS vector)
                LIMIT :top_k
            """),
            {"vec": vec_str, "threshold": SIMILARITY_THRESHOLD, "top_k": top_k},
        ).fetchall()
    finally:
        session.close()

    return [
        {
            "content": r.content,
            "doc_title": r.doc_title,
            "section_header": r.section_header,
            "source_url": r.source_url,
            "source_name": r.source_name,
            "score": float(r.score),
        }
        for r in rows
    ]
