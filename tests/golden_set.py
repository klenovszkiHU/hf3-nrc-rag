"""
Golden test set — NRC piackutatási domain.

5 pozitív kérdés + 1 negatív teszt.
Minden kérdésnél dokumentált az elvárt viselkedés.

Futtatás:
    python tests/golden_set.py --mode full    # teljes pipeline (HyDE + rerank)
    python tests/golden_set.py --mode raw     # csak nyers vektorkeresés
    python tests/golden_set.py --compare      # mindkettő, táblázatos összehasonlítás
"""
import argparse
from rich.table import Table
from rich import print as rprint
from src.pipeline.pipeline import run, run_raw_only

GOLDEN_QUESTIONS = [
    {
        "id": 1,
        "question": "Milyen módszertannal mérhető a márkaismertség és a márkakép?",
        "expected_keywords": ["brand tracking", "spontán", "supported", "kvantitatív"],
        "expect_answer": True,
        "note": "Alapkérdés — brand tracking módszertan legyen a forrásban",
    },
    {
        "id": 2,
        "question": "Mi az omnibusz kutatás és mikor érdemes alkalmazni ad hoc kutatás helyett?",
        "expected_keywords": ["omnibusz", "ad hoc", "minta", "gyors"],
        "expect_answer": True,
        "note": "Szolgáltatás-összehasonlítás — onlinekutatas.hu omnibusz lapja",
    },
    {
        "id": 3,
        "question": "Hogyan zajlik a Netpanel online panel mintavétele és hogyan biztosítják a representativitást?",
        "expected_keywords": ["Netpanel", "panel", "reprezentatív", "minta", "súlyozás"],
        "expect_answer": True,
        "note": "Netpanel metodológia kérdés",
    },
    {
        "id": 4,
        "question": "Milyen kvalitatív kutatási módszereket kínál az NRC és mikor melyiket érdemes választani?",
        "expected_keywords": ["fókuszcsoport", "mélyinterjú", "online", "kvalitatív"],
        "expect_answer": True,
        "note": "Kvalitatív módszertan — onlinekutatas.hu Qualipool, online kvali lapok",
    },
    {
        "id": 5,
        "question": "Mi az Online Bulletin Board (OBB) módszer és miben különbözik a hagyományos fókuszcsoporttól?",
        "expected_keywords": ["bulletin board", "OBB", "aszinkron", "online"],
        "expect_answer": True,
        "note": "Specifikus módszer — van blog poszt az onlinekutatas.hu-n",
    },
    {
        "id": 6,
        "question": "Mi az NRC konkrét árazása egy 1000 fős kvantitatív kutatáshoz?",
        "expected_keywords": [],
        "expect_answer": False,
        "note": "NEGATÍV TESZT — árazás nincs a tudásbázisban, az agentnek kimondja",
    },
]


def run_golden_set(mode: str = "full") -> list[dict]:
    results = []
    for q in GOLDEN_QUESTIONS:
        rprint(f"\n[bold]Q{q['id']}:[/bold] {q['question']}")
        if mode == "full":
            result = run(q["question"], debug=False)
        else:
            result = run_raw_only(q["question"])

        passed = result["has_answer"] == q["expect_answer"]
        results.append({
            "id": q["id"],
            "question": q["question"],
            "has_answer": result["has_answer"],
            "expect_answer": q["expect_answer"],
            "passed": passed,
            "answer_preview": result["answer"][:150],
            "sources": result.get("sources", []),
            "note": q["note"],
        })
        status = "[green]PASS[/green]" if passed else "[red]FAIL[/red]"
        rprint(f"  → {status} | has_answer={result['has_answer']} (elvárt: {q['expect_answer']})")
        if result["sources"]:
            rprint(f"  → Forrás: {result['sources'][0]['title'][:60]}")

    return results


def compare_modes():
    """Összehasonlítja a raw vs full pipeline teljesítményét."""
    rprint("\n[bold]RAW RETRIEVAL futtatása...[/bold]")
    raw_results = run_golden_set("raw")

    rprint("\n[bold]TELJES PIPELINE futtatása...[/bold]")
    full_results = run_golden_set("full")

    table = Table(title="Raw vs Full Pipeline összehasonlítás")
    table.add_column("Q#", style="dim")
    table.add_column("Kérdés (rövidítve)", max_width=35)
    table.add_column("Raw forrás", max_width=30)
    table.add_column("Full forrás", max_width=30)
    table.add_column("Raw OK", justify="center")
    table.add_column("Full OK", justify="center")

    for r, f in zip(raw_results, full_results):
        raw_src = r["sources"][0]["title"][:28] if r["sources"] else "—"
        full_src = f["sources"][0]["title"][:28] if f["sources"] else "—"
        table.add_row(
            str(r["id"]),
            r["question"][:33] + "…",
            raw_src,
            full_src,
            "✓" if r["passed"] else "✗",
            "✓" if f["passed"] else "✗",
        )

    rprint(table)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=["full", "raw", "compare"], default="full")
    args = parser.parse_args()

    if args.mode == "compare":
        compare_modes()
    else:
        run_golden_set(args.mode)
