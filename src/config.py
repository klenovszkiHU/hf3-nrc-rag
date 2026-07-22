"""
Central configuration — minden API kulcs és paraméter egy helyen.
"""
import os
from dotenv import load_dotenv

load_dotenv()

# --- API Keys --- (None ha hiányzik — a kliens inicializáláskor fog hibát dobni)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

# --- Database ---
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@localhost:5432/nrc_rag"
)

# --- Multi-provider szereposztás ---
# OpenAI: embedding (text-embedding-3-small — multilingual, 1536 dim, olcsó)
EMBEDDING_MODEL = "text-embedding-3-small"
EMBEDDING_DIM = 1536

# Anthropic Haiku: HyDE hipotézis-generálás (gyors, olcsó)
HYDE_MODEL = "claude-haiku-4-5-20251001"

# Cohere: reranking (natív magyar nyelvi támogatás)
RERANK_MODEL = "rerank-multilingual-v3.0"
RERANK_TOP_N = 5

# Anthropic Sonnet: végső ajánlatszöveg-generálás
GENERATION_MODEL = "claude-sonnet-4-6"

# --- Chunking paraméterek ---
# Web (onlinekutatas.hu, nrc.hu manual) — context-enriched paragraph chunking
WEB_CHUNK_MAX_TOKENS = 300
WEB_CHUNK_OVERLAP = 50

# Desk research PDF — header-alapú chunkolás
PDF_CHUNK_MAX_TOKENS = 400  # Módszertani leírásoknál nagyobb egység kell

# Service pages — rövid, faktikus tartalom
SERVICE_CHUNK_MAX_TOKENS = 200

# --- Ingest forrás konfigurációk ---
SOURCES = {
    "onlinekutatas": {
        "base_url": "https://onlinekutatas.hu",
        "api_posts": "https://onlinekutatas.hu/wp-json/wp/v2/posts",
        "api_pages": "https://onlinekutatas.hu/wp-json/wp/v2/pages",
        "type": "wordpress",
    },
    "nrc_manual": {
        "path": "data/raw/manual/",
        "type": "markdown",
    },
    "nrcdata": {
        "path": "data/raw/manual/nrcdata/",
        "type": "markdown",
    },
    "desk_research": {
        "path": "data/raw/pdf/",
        "type": "pdf",
    },
}

# --- Retrieval paraméterek ---
RETRIEVAL_TOP_K = 20       # Hány chunkat hozunk vissza vektorkereséssel
RERANK_TOP_N = 5           # Hányat adunk át a generátornak rerank után
SIMILARITY_THRESHOLD = 0.3 # Ez alatt nem tekintjük relevánsnak (grounding)
