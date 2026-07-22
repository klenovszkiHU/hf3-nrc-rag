"""
PDF feldolgozó — desk research anyaghoz.

Stratégia: pdfplumber szöveges kinyerés oldalanként,
majd chunk_pdf() header-alapú szétbontása.

Miért pdfplumber és nem pypdf?
- Jobban kezeli a táblázatokat és a multi-column layoutot
- Magyar ékezetes karakterek megbízhatóbb kinyerése
"""
import os
import pdfplumber
from pathlib import Path
from src.ingest.chunker import chunk_pdf, Chunk
from rich import print as rprint


def process_pdf(pdf_path: str) -> list[Chunk]:
    """
    Egy PDF fájlt dolgoz fel és visszaadja a chunk listát.
    """
    path = Path(pdf_path)
    doc_title = path.stem.replace("_", " ").replace("-", " ").title()

    rprint(f"  PDF feldolgozás: [bold]{path.name}[/bold]")

    pages_text = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                pages_text.append(text)

    rprint(f"    → {len(pages_text)} oldal szöveg kinyerve")

    chunks = list(chunk_pdf(
        doc_title=doc_title,
        pages=pages_text,
        source_url=path.name,
        source_name="desk_research",
    ))

    rprint(f"    → {len(chunks)} chunk létrehozva")
    return chunks


def process_all_pdfs(pdf_dir: str = "data/raw/pdf") -> list[Chunk]:
    """Minden PDF fájlt feldolgoz a megadott könyvtárból."""
    all_chunks = []
    pdf_files = list(Path(pdf_dir).glob("*.pdf"))

    if not pdf_files:
        rprint(f"[yellow]Figyelem: Nem találtam PDF fájlt a {pdf_dir} könyvtárban.[/yellow]")
        return []

    for pdf_file in pdf_files:
        chunks = process_pdf(str(pdf_file))
        all_chunks.extend(chunks)

    rprint(f"\n[green]Összesen {len(all_chunks)} chunk {len(pdf_files)} PDF-ből[/green]")
    return all_chunks
