"""
Manuálisan bemásolt tartalmak betöltése.

Az nrc.hu és nrcdata.hu tartalmai, amelyeket nem lehet crawlolni,
markdown fájlokként kerülnek ide: data/raw/manual/

Fájlelnevezési konvenció:
  nrc_omnibusz.md, nrc_netpanel.md, nrcdata_brandtracking.md stb.
A forrás neve a fájlnév prefix-ből automatikusan kiderül.
"""
import re
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


_INLINE_BOLD_RE = re.compile(
    r'\*\*(FEJLESZTŐI INSTRUKCIÓ|BEKÉRENDŐ az NRC-től):\s*\*\*.*?(?=\n\s*\n|\n#{1,6}\s|\Z)',
    re.DOTALL,
)

_JSON_LD_RE = re.compile(
    r'<script type="application/ld\+json">.*?</script>',
    re.DOTALL,
)

_SECTION_HEADING_MARKERS = (
    "Az NRC-től bekérendő",
    "A fejlesztőnek küldendő:",
    "Külső forrásból ellenőrizendő:",
    "Fejlesztői brief",       # ".ics generálás" fejlesztői brief szekció
    "Event schema markup",
)

_HEADING_RE = re.compile(r'^(#{1,6})\s+(.*)$')


def _strip_named_sections(text: str) -> str:
    """Kivágja a megnevezett szekciókat a heading sorától a következő
    azonos vagy magasabb szintű headingig (kizárólag)."""
    lines = text.split("\n")
    out = []
    skip_until_level = None
    for line in lines:
        m = _HEADING_RE.match(line)
        if skip_until_level is not None:
            if m and len(m.group(1)) <= skip_until_level:
                skip_until_level = None
            else:
                continue
        if skip_until_level is None and m:
            level = len(m.group(1))
            title = m.group(2)
            if any(marker in title for marker in _SECTION_HEADING_MARKERS):
                skip_until_level = level
                continue
        out.append(line)
    return "\n".join(out)


def strip_dev_content(text: str) -> str:
    """
    Eltávolítja a CMS-fejlesztésre szánt tartalmat (fejlesztői instrukciók,
    JSON-LD schema kódok, NRC-nek szánt döntési dobozok) a nyers markdownból,
    a chunkolás ELŐTT — így a chunk-határ nem viszi magával a mellette
    álló ügyfél-releváns szöveget.
    """
    text = _strip_named_sections(text)
    text = _JSON_LD_RE.sub("", text)
    text = _INLINE_BOLD_RE.sub("", text)
    return text


def load_manual_files(manual_dir: str = "data/raw/manual") -> list[Chunk]:
    """Minden .md fájlt betölt és chunk-ol."""
    all_chunks = []
    md_files = list(Path(manual_dir).rglob("*.md"))

    for md_file in md_files:
        content = md_file.read_text(encoding="utf-8")
        if not content.strip():
            continue

        content = strip_dev_content(content)

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
