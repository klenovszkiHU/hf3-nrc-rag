# NRC RAG Agent

RAG pipeline NRC piackutatási ajánlatszöveg-generáláshoz.  
**Házifeladat HF3** — Robot Dreams / LABA AI-ágensfejlesztés kurzus.

## Use case

Az NRC belső kalkulátor eszközének AI-összetevője: ajánlatszöveg-részleteket
generál a kvantitatív és kvalitatív piackutatási módszertani tudásbázis alapján.
Grounding: ha a kérdéshez nincs forrás, az agent ezt kimondja — nem talál ki tartalmat.

## Multi-provider szereposztás

| Provider | Modell | Szerep | Indoklás |
|---|---|---|---|
| OpenAI | `text-embedding-3-small` | Embedding | Multilingual, olcsó ($0.02/1M token), 1536 dim |
| Anthropic | `claude-haiku-4-5-20251001` | HyDE hipotézis | Gyors, olcsó, elegendő a hipotézis-generáláshoz |
| Cohere | `rerank-multilingual-v3.0` | Reranking | Natív magyar nyelvi támogatás |
| Anthropic | `claude-sonnet-4-6` | Válaszgenerálás | Magasabb minőségű, strukturált szöveg ajánlathoz |

## Tudásbázis forrásai

- **onlinekutatas.hu** — WordPress REST API crawl (blog + service page-ek)
- **nrc.hu** — manuális markdown (robots.txt tiltja a crawlert)
- **nrcdata.hu** — manuális markdown (új oldal, tartalom folyamatosan épül)
- **Desk research PDF** — több száz oldalas módszertani anyag, header-alapú chunkolás

## Chunking stratégia

**Web tartalom** (onlinekutatas.hu, nrc.hu manual):
Context-enriched paragraph chunking — minden chunk elején a szülő H2 fejléc.
Max 300 token. Indoklás: ajánlatszöveg-generálásnál a chunk kontextus nélkül
is értelmezhető kell legyen; a fejléc biztosítja ezt.

**PDF desk research:**
Header-alapú chunkolás — egy alfejezet = egy chunk. Max 400 token.
Indoklás: módszertani anyagnál a fejezetstruktúra a természetes tudáshatár.

**Service page-ek** (rövid faktikus lapok):
Self-contained mini-chunkok, max 200 token.
Indoklás: faktikus leírásoknál pontosabb retrieval érhető el kisebb egységekkel.

## Felállítás

```bash
# Környezet
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Konfiguráció
cp .env.example .env
# Töltsd ki az API kulcsokat

# Adatbázis (OrbStack PostgreSQL szükséges)
createdb nrc_rag

# Ingest futtatása
python -m src.ingest

# Pipeline tesztelése
python -m src.pipeline.pipeline

# Golden set futtatása
python tests/golden_set.py --mode compare

# Unit tesztek
pytest tests/test_chunker.py -v
```

## Könyvtárstruktúra

```
nrc-rag-agent/
├── src/
│   ├── config.py          # API kulcsok, modell- és chunking paraméterek
│   ├── db.py              # pgvector séma (Chunk tábla)
│   ├── ingest/
│   │   ├── __init__.py    # Ingest orchestrátor (belépési pont)
│   │   ├── crawler.py     # onlinekutatas.hu WordPress REST API crawl
│   │   ├── pdf_processor.py # Desk research PDF → chunk
│   │   ├── manual_loader.py # Manuális markdown fájlok
│   │   ├── chunker.py     # Chunking logika (web / pdf / service)
│   │   └── embedder.py    # OpenAI embedding (batch)
│   └── pipeline/
│       ├── hyde.py        # HyDE hipotézis-generálás (Haiku)
│       ├── retriever.py   # pgvector cosine retrieval
│       ├── reranker.py    # Cohere reranking
│       ├── generator.py   # Ajánlatszöveg-generálás (Sonnet)
│       └── pipeline.py    # Teljes pipeline orchestrátor + debug mód
├── tests/
│   ├── test_chunker.py    # Unit tesztek (determinisztikus chunkolás)
│   ├── golden_set.py      # 5 pozitív + 1 negatív kérdés, raw vs full összehasonlítás
│   └── test_pipeline.py   # Integrációs tesztek
├── data/
│   └── raw/
│       ├── web/           # Crawl cache (opcionális)
│       ├── manual/        # nrc.hu + nrcdata.hu manuális markdown
│       └── pdf/           # Desk research PDF fájlok
└── docs/
    └── ARCHITEKTURA.md    # Tudásbázis-karbantartás terve + ábra
```

## Költségbecslés

**Ingest (egyszeri):**
- Becslés ~500 chunk × átlag 250 token = ~125 000 token
- OpenAI embedding: 125 000 / 1 000 000 × $0.02 = **~$0.003**

**Egy kérdés (teljes pipeline):**
- HyDE (Haiku): ~300 input + 200 output token ≈ $0.0001
- Embedding (1 hipotézis): ~200 token ≈ $0.000004
- Rerank (Cohere): 20 chunk × ~250 token ≈ $0.0002
- Generálás (Sonnet): ~2000 input + 500 output token ≈ $0.01
- **Kérdésenkénti teljes költség: ~$0.010-0.012**
