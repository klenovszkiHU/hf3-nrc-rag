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


class RunLog(Base):
    """
    Egy sor = egy ügyfél-kérdés végigfutása az ügyfél-belépőponton (client_demo.py).

    A napló CSAK maszkolt kérdésszöveget tárol (lásd src/client/pii.py) —
    a PII-szűrés a pipeline hívása ELŐTT fut, tehát ide sosem kerül nyers
    személyes adat.
    """
    __tablename__ = "run_log"

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    session_id = Column(String(100))

    # Kérdés és válasz (a kérdés mindig PII-maszkolt)
    question_masked = Column(Text, nullable=False)
    answer_text = Column(Text)

    # Pipeline-metrikák a debug_info-ból
    top_rerank_score = Column(Float)
    top_source = Column(String(500))
    latency_ms = Column(Integer)
    cost_usd = Column(Float)

    # Eszkalációs döntés
    outcome = Column(String(20))            # "answered" | "escalated"
    escalation_reason = Column(String(200))  # pl. "low_score" | "pricing_keyword"

    # Emberi jóváhagyás (approve_demo.py tölti ki)
    # pending|approved|edited|rejected — NULL, ha nem volt generált válasz
    # (eszkalált eset). Nincs oszlop-szintű default: a SQLAlchemy default
    # explicit None esetén is lefutna, és felülírná az eszkalált sorokat.
    approval_status = Column(String(20))
    approver = Column(String(100))
    approved_at = Column(DateTime)
    edit_distance = Column(Integer)


def init_db():
    """Létrehozza a pgvector extension-t és a táblát, ha még nem léteznek."""
    with engine.connect() as conn:
        conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))
        conn.commit()
    Base.metadata.create_all(engine)
    print("DB inicializálva.")


def get_session():
    return Session()
