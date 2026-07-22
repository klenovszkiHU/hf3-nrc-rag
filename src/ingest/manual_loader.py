"""
Manuálisan bemásolt tartalmak betöltése.

Az nrc.hu és nrcdata.hu tartalmai, amelyeket nem lehet crawlolni,
markdown fájlokként kerülnek ide: data/raw/manual/

Fájlelnevezési konvenció:
  nrc_omnibusz.md, nrc_netpanel.md, nrcdata_brandtracking.md stb.
A forrás neve a fájlnév prefix-ből automatikusan kiderül.
"""
from pathlib import Path
from src.ingest.crawler import RawDocument
from src.ingest.chunker import chunk_web, chunk_service, Chunk
import hashlib


def _detect_source(filename: str) -> tuple[str, str]:
    """Fájlnévből forrás neve és típusa."""
    name = filename.lower()
    if name.startswith("nrcdata"):
        return "nrcdata.hu", "markdown"
    elif name.startswith("nrc"):
        return "nrc.hu", "markdown"
    return "manual", "markdown"


def load_manual_files(manual_dir: str = "data/raw/manual") -> list[Chunk]:
    """Minden .md fájlt betölt és chunk-ol."""
    all_chunks = []
    md_files = list(Path(manual_dir).rglob("*.md"))

    for md_file in md_files:
        content = md_file.read_text(encoding="utf-8")
        if not content.strip():
            continue

        source_name, source_type = _detect_source(md_file.name)
        doc_title = md_file.stem.replace("_", " ").replace("-", " ").title()

        # Service page-ek (rövid, ~500 szó alatt) vs hosszabb tartalmak
        word_count = len(content.split())
        if word_count < 400:
            chunks = list(chunk_service(
                doc_title=doc_title,
                content_md=content,
                source_url=str(md_file),
                source_name=source_name,
            ))
        else:
            chunks = list(chunk_web(
                doc_title=doc_title,
                content_md=content,
                source_url=str(md_file),
                source_name=source_name,
            ))

        all_chunks.extend(chunks)

    return all_chunks
