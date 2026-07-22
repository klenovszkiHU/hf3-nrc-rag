"""
onlinekutatas.hu crawler — WordPress REST API alapú.

Miért REST API és nem HTML scraping?
- Tiszta JSON válasz, nincs navigációs zaj
- Pagination egyszerű (per_page + page paraméter)
- content.rendered mezőben van a teljes HTML tartalom
- Változásérzékelés: modified mező alapján tudni fogjuk, mikor változott

Crawlolt tartalom:
- /wp/v2/posts (blog, módszertani cikkek)
- /wp/v2/pages (szolgáltatáslapok, omnibusz, Netpanel stb.)
"""
import time
import hashlib
import requests
from markdownify import markdownify as md
from typing import Iterator
from dataclasses import dataclass
from rich import print as rprint


@dataclass
class RawDocument:
    title: str
    url: str
    source_name: str
    source_type: str
    content_md: str      # HTML → Markdown konvertálva
    modified: str        # ISO dátum, változásérzékeléshez
    content_hash: str


def _fetch_all_pages(endpoint: str, delay: float = 0.5) -> list[dict]:
    """
    Paginálja végig a WordPress REST API-t.
    100 elem/oldal a maximum — az összes oldalt bejárjuk.
    """
    results = []
    page = 1
    while True:
        resp = requests.get(
            endpoint,
            params={"per_page": 100, "page": page, "_fields": "id,title,link,content,modified"},
            timeout=30,
            headers={"User-Agent": "NRC-RAG-Ingest/1.0"},
        )
        if resp.status_code == 400:
            # WordPress 400-at ad, ha page > total pages
            break
        resp.raise_for_status()
        batch = resp.json()
        if not batch:
            break
        results.extend(batch)
        total_pages = int(resp.headers.get("X-WP-TotalPages", 1))
        rprint(f"  [dim]Oldal {page}/{total_pages}, eddig {len(results)} dok[/dim]")
        if page >= total_pages:
            break
        page += 1
        time.sleep(delay)
    return results


def _to_markdown(html: str) -> str:
    """HTML → tiszta Markdown. Képeket, linkeket megtartjuk szövegként."""
    return md(html, heading_style="ATX", strip=["script", "style", "nav", "footer"])


def _make_hash(content: str) -> str:
    return hashlib.sha256(content.encode()).hexdigest()


def crawl_onlinekutatas() -> Iterator[RawDocument]:
    """
    Bejárja az onlinekutatas.hu összes posztját és oldalát.
    Yields: RawDocument objektumok.
    """
    from src.config import SOURCES
    base = SOURCES["onlinekutatas"]

    for endpoint_type, endpoint_url in [
        ("posts", base["api_posts"]),
        ("pages", base["api_pages"]),
    ]:
        rprint(f"\n[bold]Crawling {endpoint_type}...[/bold]")
        items = _fetch_all_pages(endpoint_url)
        rprint(f"  → {len(items)} {endpoint_type} letöltve")

        for item in items:
            html = item.get("content", {}).get("rendered", "")
            if not html or len(html) < 100:
                # Üres vagy navigációs lapok kihagyása
                continue

            content_md = _to_markdown(html)
            title = item.get("title", {}).get("rendered", "Cím nélkül")

            yield RawDocument(
                title=title,
                url=item.get("link", ""),
                source_name="onlinekutatas.hu",
                source_type="wordpress",
                content_md=content_md,
                modified=item.get("modified", ""),
                content_hash=_make_hash(content_md),
            )
