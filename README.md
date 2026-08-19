# NRC RAG Agent — Ügyfélirányú belépőpont

**Házifeladat HF5** — Robot Dreams / LABA AI-ágensfejlesztés kurzus.
Az NRC belső RAG-asszisztens (HF3) ügyfélirányú kiterjesztése.

## 1. Mit csinál

Ez a projekt a meglévő, belső használatra épített NRC RAG-asszisztenst
(HF3) terjeszti ki egy **ügyfélirányú belépőponttal**. Az NRC megbízója
szabad szöveggel leírja az üzleti kérdését vagy kutatási problémáját, és
egy módszertani javaslatot kap — omnibusz kutatás esetén indikatív
listaárral kiegészítve —, mindig forrásmegjelöléssel a tudásbázisból, és
**mindig kutatói jóváhagyás után** jut el az ügyfélhez. Ez **nem egy új
rendszer**: ugyanaz a tudásbázis és ugyanaz a kereső-lánc (HyDE → pgvector
retrieval → Cohere rerank → Sonnet generálás) szolgálja ki, csak egy új,
ügyfélnek szánt bejárattal és a köré épített biztonsági/jóváhagyási
réteggel.

## 2. Milyen fájdalmat old meg — és mit nem

**Megoldja:**
- **Munkaidőn kívüli elérhetőség** — az ügyfél éjjel vagy hétvégén is kap egy első, forrással alátámasztott választ, nem kell reggelig várnia egy kollégára.
- **Ismétlődő kérdések terhe** — a gyakori, jól dokumentált módszertani és árazási kérdéseket (pl. "mennyi az omnibusz mintája", "mikor indul a következő hullám") a rendszer önállóan, konzisztensen megválaszolja.
- **A személyre szabás küszöbe** — olyan alacsony értékű, standard kérdéseknél is gyors választ ad, ahol egy kutató ideje nem térülne meg egyedi válasz megírására.
- **Az ajánlati kör hossza** — az első, tájékozódó kör (mire jó az omnibusz, mennyibe kerül nagyságrendileg) lerövidül, mielőtt egy kutató bekapcsolódna.

**Nem oldja meg (tudatosan, ebben a körben):**
- **Ügystátusz-követés** — nem tudja megmondani, hol tart egy már futó megrendelés.
- **Sürgősségi triage** — nem rangsorolja/priorizálja a beérkező kérdéseket üzleti súly szerint.
- **Lemorzsolódás-előrejelzés** — nem következtet ügyfél-elvándorlási kockázatra a kérdésekből.

## 3. Architektúra

```
Ügyfél kérdése
    │
    ▼
PII-szűrő (src/client/pii.py)
    │  e-mail, telefon, adószám, adóazonosító, TAJ, bankszámlaszám maszkolása
    ▼
Szabály alapú eszkaláció-ellenőrzés (src/client/escalation.py)
    │  kulcsszó: egyedi árazás, kedvezmény, keretszerződés, garancia, NDA
    │  ha talál → NEM megy tovább, kollégához irányít
    ▼
HyDE (src/pipeline/hyde.py — Claude Haiku)
    │  hipotézis-dokumentum generálása a kérdésre
    ▼
pgvector retrieval (src/pipeline/retriever.py)
    │  top-K legközelebbi chunk a tudásbázisból
    ▼
Cohere rerank (src/pipeline/reranker.py)
    │  relevancia szerinti átrendezés, top-N + rerank score
    ▼
Score alapú eszkaláció-ellenőrzés (src/client/escalation.py)
    │  ha a top rerank score < 0.3 → NEM generál választ, kollégához irányít
    ▼
Sonnet generálás (src/pipeline/generator.py)
    │  válasz + forráshivatkozások
    ▼
run_log (src/db.py — PostgreSQL tábla)
    │  minden lefutás naplózva: maszkolt kérdés, score, forrás, kimenet
    ▼
Jóváhagyási kapu (approve_demo.py)
       kutató jóváhagyja / szerkeszti / elutasítja, mielőtt kimegy az ügyfélnek
```

A meglévő pipeline-komponenseket (`hyde.py`, `retriever.py`, `reranker.py`,
`generator.py`) a kiterjesztés nem módosítja — csak felhasználja őket.

## 4. Hogyan indul

```bash
# Környezet
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Konfiguráció
cp .env.example .env
# Töltsd ki az API kulcsokat és a DATABASE_URL-t

# Adatbázis — PostgreSQL pgvector kiterjesztéssel (pl. Docker konténerben)
# A tábla és a pgvector extension automatikusan létrejön az első futáskor

# Tudásbázis feltöltése
python ingest_run.py

# Ügyfélnézet
python client_demo.py

# Jóváhagyói nézet (külön terminálban, a client_demo.py után)
python approve_demo.py
```

**A demó két esete:**

1. **Végigvitt omnibusz-kérdés** — pl. *"Mikor indul a következő omnibusz hullám?"*
   A kérdés végigmegy a teljes láncon, magas rerank score-t kap, a Sonnet
   generál egy forrással alátámasztott választ, és a rendszer `pending`
   státusszal a `run_log`-ba írja. Az `approve_demo.py`-ban ez megjelenik
   jóváhagyásra: a kutató láthatja a kérdést, a választ és a top forrást,
   majd jóváhagyja, szerkeszti vagy elutasítja.

2. **Szabály alapú eszkaláció** — pl. *"Mennyi kedvezményt tudtok adni éves
   keretszerződés esetén?"* A kulcsszó-ellenőrzés (`kedvezmény`,
   `keretszerződés`) még a pipeline elindítása előtt kiszűri a kérdést: a
   rendszer nem generál választ, az ügyfél egy eszkalációs üzenetet lát, és
   a `run_log`-ba `outcome='escalated'` kerül, jóváhagyásra váró tartalom
   nélkül.

## 5. Mi kell hozzá

- **Anthropic API kulcs** (HyDE hipotézis + válaszgenerálás)
- **OpenAI API kulcs** (embedding)
- **Cohere API kulcs** (reranking)
- **Python 3.11+** környezet a `requirements.txt` csomagjaival
- **PostgreSQL** `pgvector` kiterjesztéssel (a `chunks` és `run_log` táblákhoz)

## 6. Mérési adat: az eszkalációs küszöb

A score alapú eszkalációs küszöb (**0.3**, `src/client/escalation.py`)
nem tetszőlegesen választott érték, hanem egy 24 kérdéses kalibrációs
kérdéskészletre (`kuszob-kerdeskeszlet.md`, 4 kategória: erős pozitív,
gyenge pozitív, negatív, szabály alapú eszkaláció) mért eredmény, **két
kalibrációs körben**:

- **1. kör** — `threshold_results.csv`
- **2. kör** — `threshold_results_v2.csv`

A két kör között két változás történt: a HyDE-prompt fogalmi kontextust
kapott (pl. hogy az "omnibusz" itt piackutatási termék, nem közlekedési
eszköz), és a tudásbázisból kiszűrésre került a nyers CMS-fejlesztési
tartalom (fejlesztői instrukciók, JSON-LD schema blokkok, NRC-nek szánt
döntési dobozok), ami korábban zajforrásként rontotta a retrieval
pontosságát. A második kör után a pozitív kategóriák átlagos rerank
score-ja jelentősen nőtt, a negatív és eszkalációs kategóriáké pedig
tovább csökkent — ez erősítette meg a 0.3-as küszöb választását.

A teljes mérési módszertan és az eredmények értelmezése: `meresi-terv.md`.

## 7. Tudatos PoC-korlátok

A következők **szándékosan nincsenek** a rendszerben — ez egy koncepció-
bizonyító demó, nem éles termék:

- **Autentikáció** — nincs bejelentkezés, bárki futtathatja a CLI-t.
- **Bérlői izoláció (multi-tenancy)** — nincs ügyfelenkénti adatelkülönítés.
- **Ügyfélspecifikus tartalom** — a tudásbázis egységes, nincs személyre szabott/szerződéses tartalom megbízónként.
- **Költségnaplózás** — a `run_log.cost_usd` mező a demóban mindig üres; nincs token-alapú pontos költségkövetés.
- **Webes felület** — a demó parancssori (CLI), nincs böngészős ügyfél- vagy jóváhagyói felület.

## 8. A repo tartalma

| Fájl | Tartalom |
|---|---|
| `00-scope.md` | A HF5 use case scope-specifikációja |
| `meresi-terv.md` | Teljes mérési terv: módszertan, kalibrációs kérdéskészlet, eredmény-értelmezés |
| `kerdeslap.md` | 6 kapott + 2 saját kérdés a use case-hez |
| `NRC-kutatastervezo-asszisztens.pptx` | Business case, 8 dia |
| `kuszob-kerdeskeszlet.md` | A 24 kalibrációs kérdés, 4 kategóriába sorolva |

## Könyvtárstruktúra

```
hf3-nrc-rag-agent/
├── client_demo.py          # Ügyfélnézet CLI — PII-szűrés, eszkaláció, pipeline hívás
├── approve_demo.py         # Jóváhagyói CLI — pending run_log sorok elbírálása
├── ingest_run.py           # Tudásbázis-feltöltés belépési pontja
├── src/
│   ├── config.py           # API kulcsok, modell- és chunking paraméterek
│   ├── db.py                # pgvector séma (Chunk + RunLog tábla)
│   ├── client/
│   │   ├── pii.py           # PII maszkolás/visszaállítás
│   │   └── escalation.py    # Szabály és score alapú eszkalációs logika
│   ├── ingest/               # Crawl, PDF-feldolgozás, manuális markdown betöltés, chunking
│   └── pipeline/
│       ├── hyde.py           # HyDE hipotézis-generálás (Haiku)
│       ├── retriever.py      # pgvector cosine retrieval
│       ├── reranker.py       # Cohere reranking
│       ├── generator.py      # Válaszgenerálás (Sonnet)
│       └── pipeline.py       # Teljes pipeline orchestrátor + debug mód
├── tests/
│   └── threshold_calibration.py  # Kalibrációs futtató a kuszob-kerdeskeszlet.md-re
├── 00-scope.md
├── meresi-terv.md
├── kerdeslap.md
├── kuszob-kerdeskeszlet.md
├── NRC-kutatastervezo-asszisztens.pptx
├── threshold_results.csv
└── threshold_results_v2.csv
```
