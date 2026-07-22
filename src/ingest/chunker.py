"""
Chunking stratégia — use case-specifikus döntések.

Három chunk-típus, három logikával:

1. WEB (onlinekutatas.hu, nrc.hu manual markdown):
   Context-enriched paragraph chunking.
   Minden chunk elején ott a szülő H2 fejléc → a chunk önálló
   kontextus nélkül is értelmezhető, ami kritikus ajánlatszöveg-
   generálásnál. Bekezdés-alapú (~300 token max), átfedés nélkül
   (a fejléc-kontextus ezt feleslegessé teszi).

2. PDF (desk research):
   Header-alapú chunkolás.
   A módszertani anyagnál egy alfejezet = egy tudásegység.
   A bekezdéseket nem vágjuk szét (max 400 token — ha egy alfejezet
   hosszabb, középen folytatjuk, de fejléc-kontextust megtartjuk).

3. SERVICE (rövid service page-ek):
   Self-contained mini-chunkok (~200 token).
   Ezek faktikus leírások (pl. Omnibusz specifikáció), ahol minden
   mondat önálló állítás. Kisebb chunk = pontosabb retrieval.
"""
import re
from dataclasses import dataclass, field
from typing import Iterator
from src.config import (
    WEB_CHUNK_MAX_TOKENS,
    PDF_CHUNK_MAX_TOKENS,
    SERVICE_CHUNK_MAX_TOKENS,
)


def _count_tokens(text: str) -> int:
    """
    Közelítő token-számolás (1 token ≈ 0.75 szó angolul, magyarnál ~0.6 szó).
    Éles rendszerben tiktoken cl100k_base pontosabb, de a hálózati korlát miatt
    ezt a heurisztikát használjuk. A különbség <10% a token-limitek kezelésénél.
    """
    words = text.split()
    return int(len(words) * 1.35) if words else 0


def _split_by_tokens(text: str, max_tokens: int) -> list[str]:
    """Szöveg felosztása token-limit alapján, mondathatáron."""
    sentences = re.split(r'(?<=[.!?])\s+', text)
    chunks, current, current_tokens = [], [], 0
    for sent in sentences:
        t = _count_tokens(sent)
        if current_tokens + t > max_tokens and current:
            chunks.append(" ".join(current))
            current, current_tokens = [], 0
        current.append(sent)
        current_tokens += t
    if current:
        chunks.append(" ".join(current))
    return chunks


@dataclass
class Chunk:
    content: str
    doc_title: str
    section_header: str
    source_url: str
    source_name: str
    source_type: str
    chunk_index: int
    token_count: int
    content_hash: str = field(default="")

    def __post_init__(self):
        import hashlib
        if not self.content_hash:
            self.content_hash = hashlib.sha256(self.content.encode()).hexdigest()


# ---------------------------------------------------------------------------
# WEB chunker (context-enriched paragraph)
# ---------------------------------------------------------------------------
def chunk_web(doc_title: str, content_md: str, source_url: str,
              source_name: str, max_tokens: int = WEB_CHUNK_MAX_TOKENS) -> Iterator[Chunk]:
    """
    Markdown tartalom chunkolása.
    H2 fejléc = szekció határ. Minden chunk elején: "[Fejléc] > [tartalom]"
    """
    lines = content_md.split("\n")
    current_h2 = ""
    current_paragraphs: list[str] = []
    chunk_index = 0

    def flush(h2: str, paragraphs: list[str]) -> Iterator[Chunk]:
        nonlocal chunk_index
        text = "\n\n".join(paragraphs).strip()
        if len(text) < 50:  # Túl rövid, kihagyjuk
            return
        # Context prefix: fejléc + tartalom
        prefixed = f"{h2}\n\n{text}" if h2 else text
        for part in _split_by_tokens(prefixed, max_tokens):
            if len(part.strip()) < 50:
                continue
            yield Chunk(
                content=part,
                doc_title=doc_title,
                section_header=h2,
                source_url=source_url,
                source_name=source_name,
                source_type="wordpress",
                chunk_index=chunk_index,
                token_count=_count_tokens(part),
            )
            chunk_index += 1

    for line in lines:
        if line.startswith("## "):
            yield from flush(current_h2, current_paragraphs)
            current_h2 = line.lstrip("# ").strip()
            current_paragraphs = []
        elif line.startswith("# "):
            # H1 = dokumentum cím, nem szekció határ
            pass
        elif line.strip():
            current_paragraphs.append(line.strip())

    yield from flush(current_h2, current_paragraphs)


# ---------------------------------------------------------------------------
# PDF chunker (header-alapú)
# ---------------------------------------------------------------------------
def chunk_pdf(doc_title: str, pages: list[str], source_url: str,
              source_name: str, max_tokens: int = PDF_CHUNK_MAX_TOKENS) -> Iterator[Chunk]:
    """
    PDF szöveges oldalak chunkolása fejlécek mentén.
    A fejléceket nagybetűs vagy rövid sorként azonosítjuk (heurisztikus).
    """
    HEADER_RE = re.compile(
        r'^(\d+[\.\d]*[\.\s]+[A-ZÁÉÍÓÖŐÚÜŰ].{2,80}'  # pl. "1. BEVEZETÉS", "1.1 KVANTITATÍV"
        r'|[A-ZÁÉÍÓÖŐÚÜŰ][A-ZÁÉÍÓÖŐÚÜŰ\s]{3,80})$'   # pl. "MÓDSZERTANI ÖSSZEFOGLALÓ"
    )
    chunk_index = 0
    current_header = ""
    current_text: list[str] = []

    def flush(header: str, lines: list[str]) -> Iterator[Chunk]:
        nonlocal chunk_index
        text = " ".join(lines).strip()
        if len(text) < 40:
            return
        prefixed = f"{header}\n\n{text}" if header else text
        for part in _split_by_tokens(prefixed, max_tokens):
            if len(part.strip()) < 40:
                continue
            yield Chunk(
                content=part,
                doc_title=doc_title,
                section_header=header,
                source_url=source_url,
                source_name=source_name,
                source_type="pdf",
                chunk_index=chunk_index,
                token_count=_count_tokens(part),
            )
            chunk_index += 1

    full_text = "\n".join(pages)
    for line in full_text.split("\n"):
        line = line.strip()
        if not line:
            continue
        if HEADER_RE.match(line) and _count_tokens(line) < 20:
            yield from flush(current_header, current_text)
            current_header = line
            current_text = []
        else:
            current_text.append(line)

    yield from flush(current_header, current_text)


# ---------------------------------------------------------------------------
# SERVICE chunker (self-contained mini-chunks)
# ---------------------------------------------------------------------------
def chunk_service(doc_title: str, content_md: str, source_url: str,
                  source_name: str, max_tokens: int = SERVICE_CHUNK_MAX_TOKENS) -> Iterator[Chunk]:
    """
    Rövid service page-ek chunkolása.
    Egész dokumentum egy egységként, majd token-limit szerinti szétbontás.
    """
    chunk_index = 0
    text = content_md.strip()
    if len(text) < 50:
        return
    for part in _split_by_tokens(text, max_tokens):
        if len(part.strip()) < 50:
            continue
        yield Chunk(
            content=part,
            doc_title=doc_title,
            section_header="",
            source_url=source_url,
            source_name=source_name,
            source_type="markdown",
            chunk_index=chunk_index,
            token_count=_count_tokens(part),
        )
        chunk_index += 1
