"""
Unit tesztek a chunker modulhoz.
A chunking determinisztikus → tesztelhető.
"""
import pytest
from src.ingest.chunker import chunk_web, chunk_pdf, chunk_service, _count_tokens

# --- Teszt adatok ---

SAMPLE_WEB_MD = """# Omnibusz kutatás

## Mi az omnibusz kutatás?

Az omnibusz kutatás egy olyan kvantitatív adatfelvételi forma, amelyben több megrendelő kérdései
szerepelnek egyidejűleg ugyanazon kérdőívben. Ez lehetővé teszi az egyedi kutatási költségek
megosztását a résztvevők között.

## Mikor érdemes választani?

Az omnibusz ideális megoldás, ha gyorsan, költséghatékonyan szeretnénk reprezentatív adatokat
kapni. Különösen hasznos, ha a kérdések száma korlátozott, és nincs szükség teljesen egyedi
kérdőívre.

## Mintavétel

Az NRC omnibusz kutatásai a 18-69 éves magyar internetező lakosságot reprezentálják.
A mintaméret általában 500-1000 fő között mozog.
"""

SAMPLE_PDF_PAGES = [
    "1. BEVEZETÉS\n\nA piackutatás az üzleti döntések megalapozásának egyik legfontosabb eszköze.",
    "1.1 KVANTITATÍV MÓDSZEREK\n\nA kvantitatív kutatások célja számszerűsíthető adatok gyűjtése nagy mintán.",
    "1.2 KVALITATÍV MÓDSZEREK\n\nA kvalitatív kutatások mélyebb megértést nyújtanak kisebb mintán keresztül.",
]


class TestWebChunker:
    def test_creates_chunks(self):
        chunks = list(chunk_web("Omnibusz", SAMPLE_WEB_MD, "https://test.hu", "test"))
        assert len(chunks) > 0

    def test_chunk_has_section_header(self):
        chunks = list(chunk_web("Omnibusz", SAMPLE_WEB_MD, "https://test.hu", "test"))
        headers = [c.section_header for c in chunks if c.section_header]
        assert len(headers) > 0, "Legalább egy chunknak kell legyen section_header-je"

    def test_chunk_respects_token_limit(self):
        chunks = list(chunk_web("Omnibusz", SAMPLE_WEB_MD, "https://test.hu", "test", max_tokens=200))
        for chunk in chunks:
            assert chunk.token_count <= 220, f"Chunk túl hosszú: {chunk.token_count} token"

    def test_chunk_content_not_empty(self):
        chunks = list(chunk_web("Omnibusz", SAMPLE_WEB_MD, "https://test.hu", "test"))
        for chunk in chunks:
            assert len(chunk.content.strip()) >= 50

    def test_header_prefix_in_content(self):
        """A szülő H2 fejléc benne van a chunk tartalmában (context-enriched)."""
        chunks = list(chunk_web("Omnibusz", SAMPLE_WEB_MD, "https://test.hu", "test"))
        headers_in_content = [
            c for c in chunks
            if c.section_header and c.section_header in c.content
        ]
        assert len(headers_in_content) > 0

    def test_empty_doc_returns_no_chunks(self):
        chunks = list(chunk_web("Üres", "", "https://test.hu", "test"))
        assert len(chunks) == 0

    def test_chunk_index_sequential(self):
        chunks = list(chunk_web("Omnibusz", SAMPLE_WEB_MD, "https://test.hu", "test"))
        indices = [c.chunk_index for c in chunks]
        assert indices == list(range(len(indices)))


class TestPdfChunker:
    def test_creates_chunks(self):
        chunks = list(chunk_pdf("Desk Research", SAMPLE_PDF_PAGES, "dr.pdf", "desk_research"))
        assert len(chunks) > 0

    def test_header_detected(self):
        chunks = list(chunk_pdf("Desk Research", SAMPLE_PDF_PAGES, "dr.pdf", "desk_research"))
        headers = [c.section_header for c in chunks if c.section_header]
        assert len(headers) > 0

    def test_source_type_is_pdf(self):
        chunks = list(chunk_pdf("Desk Research", SAMPLE_PDF_PAGES, "dr.pdf", "desk_research"))
        for chunk in chunks:
            assert chunk.source_type == "pdf"


class TestServiceChunker:
    def test_short_content_one_chunk(self):
        short = "Az NRC omnibusz kutatás 500 főre épülő, gyors adatfelvételi megoldás."
        chunks = list(chunk_service("Service", short, "https://nrc.hu", "nrc.hu"))
        assert len(chunks) >= 1

    def test_token_limit_respected(self):
        long_content = " ".join(["Ez egy teszt mondat."] * 100)
        chunks = list(chunk_service("Long", long_content, "https://nrc.hu", "nrc.hu", max_tokens=100))
        for chunk in chunks:
            assert chunk.token_count <= 120


class TestTokenCounter:
    def test_empty_string(self):
        assert _count_tokens("") == 0

    def test_known_length(self):
        # "hello" = 1 token cl100k alapján
        assert _count_tokens("hello") == 1
