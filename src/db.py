"""
PostgreSQL + pgvector séma és kapcsolat.
"""
from sqlalchemy import create_engine, text, Column, String, Text, Float, DateTime, Integer
from sqlalchemy.orm import declarative_base, sessionmaker
from pgvector.sqlalchemy import Vector
from datetime import datetime
from src.config import DATABASE_URL, EMBEDDING_DIM

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Chunk(Base):
    """
    Egy chunk = egy önálló tudásegység a tudásbázisban.

    A content_hash az inkrementális frissítés alapja:
    ha a forrás URL + hash nem változott, nem vektorizáljuk újra.
    """
    __tablename__ = "chunks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    # Forrás azonosítás (grounding + karbantartás)
    source_type = Column(String(50), nullable=False)   # wordpress | markdown | pdf
    source_name = Column(String(200), nullable=False)  # pl. "onlinekutatas.hu"
    source_url = Column(String(500))                   # URL vagy fájlnév
    doc_title = Column(String(500))                    # Szülő dokumentum címe
    section_header = Column(String(500))               # Szülő H2 (context-enriched)

    # Tartalom
    content = Column(Text, nullable=False)
    chunk_index = Column(Integer)                      # Sorrend a forrásdokon belül
    token_count = Column(Integer)

    # Inkrementális frissítéshez
    content_hash = Column(String(64), index=True)      # SHA-256 az újraindexelés detektálásához
    indexed_at = Column(DateTime, default=datetime.utcnow)

    # Vektor
    embedding = Column(Vector(EMBEDDING_DIM))


def init_db():
    """Létrehozza a pgvector extension-t és a táblát, ha még nem léteznek."""
    with engine.connect() as conn:
        conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))
        conn.commit()
    Base.metadata.create_all(engine)
    print("DB inicializálva.")


def get_session():
    return Session()
