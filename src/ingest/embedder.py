"""
Embedding — OpenAI text-embedding-3-small.

Miért ez a modell?
- Multilingual: magyarul is elfogadható teljesítmény
- 1536 dim (kisebb, mint large) → olcsóbb tárolás és retrieval
- $0.02/1M token → nagy tudásbázison is negligibilis ingest-költség
"""
import time
from openai import OpenAI
from src.config import OPENAI_API_KEY, EMBEDDING_MODEL

client = OpenAI(api_key=OPENAI_API_KEY)


def embed_texts(texts: list[str], batch_size: int = 100) -> list[list[float]]:
    """
    Batch embedding. Rate limit miatt 0.5s delay batch-ek között.
    Visszaad: float lista lista, ugyanolyan sorrendben mint a bemenet.
    """
    all_embeddings = []
    for i in range(0, len(texts), batch_size):
        batch = texts[i:i + batch_size]
        response = client.embeddings.create(
            model=EMBEDDING_MODEL,
            input=batch,
        )
        all_embeddings.extend([r.embedding for r in response.data])
        if i + batch_size < len(texts):
            time.sleep(0.5)
    return all_embeddings


def embed_single(text: str) -> list[float]:
    return embed_texts([text])[0]
