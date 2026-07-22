"""Ingest belépési pont: python ingest_run.py [--force]"""
import argparse
from rich import print as rprint
from src.db import init_db, get_session
from src.ingest.crawler import crawl_onlinekutatas
from src.ingest.pdf_processor import process_all_pdfs
from src.ingest.manual_loader import load_manual_files
from src.ingest.chunker import chunk_web
from src.ingest.embedder import embed_texts
from src.db import Chunk as ChunkModel


def ingest_all(skip_existing: bool = True):
    init_db()
    session = get_session()
    all_chunks = []

    rprint("\n[bold green]1. onlinekutatas.hu crawl[/bold green]")
    for raw_doc in crawl_onlinekutatas():
        chunks = list(chunk_web(raw_doc.title, raw_doc.content_md, raw_doc.url, raw_doc.source_name))
        all_chunks.extend(chunks)

    rprint("\n[bold green]2. Manuális markdown fájlok[/bold green]")
    all_chunks.extend(load_manual_files())

    rprint("\n[bold green]3. PDF desk research[/bold green]")
    all_chunks.extend(process_all_pdfs())

    rprint(f"\n[bold]Összesen: {len(all_chunks)} chunk[/bold]")

    if skip_existing:
        existing_hashes = {row[0] for row in session.query(ChunkModel.content_hash).all()}
        new_chunks = [c for c in all_chunks if c.content_hash not in existing_hashes]
        rprint(f"Új chunk: {len(new_chunks)}")
    else:
        new_chunks = all_chunks

    rprint(f"\n[bold green]Embedding + tárolás ({len(new_chunks)} chunk)...[/bold green]")
    BATCH = 50
    for i in range(0, len(new_chunks), BATCH):
        batch = new_chunks[i:i + BATCH]
        embeddings = embed_texts([c.content for c in batch])
        for chunk, emb in zip(batch, embeddings):
            session.add(ChunkModel(
                source_type=chunk.source_type, source_name=chunk.source_name,
                source_url=chunk.source_url, doc_title=chunk.doc_title,
                section_header=chunk.section_header, content=chunk.content,
                chunk_index=chunk.chunk_index, token_count=chunk.token_count,
                content_hash=chunk.content_hash, embedding=emb,
            ))
        session.commit()
        rprint(f"  {min(i+BATCH, len(new_chunks))}/{len(new_chunks)} chunk mentve")

    session.close()
    rprint("\n[bold green]✓ Ingest kész.[/bold green]")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    ingest_all(skip_existing=not args.force)
