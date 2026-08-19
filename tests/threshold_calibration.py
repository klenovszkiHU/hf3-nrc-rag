"""
Küszöbmérő kalibráció — a kuszob-kerdeskeszlet.md kérdéseit végigfuttatja
a teljes pipeline-on, és kigyűjti a top rerank score-t kategóriánként.

Futtatás:
    python tests/threshold_calibration.py
"""
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from rich import print as rprint  # noqa: E402
from src.pipeline.pipeline import run  # noqa: E402

QUESTIONS_FILE = ROOT / "kuszob-kerdeskeszlet.md"
OUTPUT_FILE = ROOT / "threshold_results.csv"

CATEGORY_RE = re.compile(r"^##\s+(.+)$")
QUESTION_RE = re.compile(r"^\d+\.\s+(.+)$")


def load_questions(path: Path) -> list[dict]:
    """Beolvassa a ## kategória fejléceket és a számozott kérdéseket."""
    questions = []
    current_category = None

    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        cat_match = CATEGORY_RE.match(line)
        if cat_match:
            current_category = cat_match.group(1).strip()
            continue

        q_match = QUESTION_RE.match(line)
        if q_match and current_category is not None:
            questions.append({
                "kategoria": current_category,
                "kerdes": q_match.group(1).strip(),
            })

    return questions


def run_calibration(questions: list[dict]) -> list[dict]:
    rows = []
    for i, q in enumerate(questions, start=1):
        rprint(f"\n[bold]{i}/{len(questions)}[/bold] [{q['kategoria']}] {q['kerdes']}")
        try:
            result = run(q["kerdes"], debug=True)
        except Exception as e:
            rprint(f"  [red]HIBA:[/red] {e}")
            rows.append({
                "kategoria": q["kategoria"],
                "kerdes": q["kerdes"],
                "top_rerank_score": "",
                "top_forras": "",
                "valasz_eleje": f"HIBA: {e}",
            })
            continue

        reranked = result.get("debug_info", {}).get("reranked", [])
        if reranked:
            top_rerank_score = reranked[0]["rerank_score"]
            top_forras = reranked[0]["title"]
        else:
            top_rerank_score = ""
            top_forras = ""

        answer = result.get("answer", "")
        rows.append({
            "kategoria": q["kategoria"],
            "kerdes": q["kerdes"],
            "top_rerank_score": top_rerank_score,
            "top_forras": top_forras,
            "valasz_eleje": answer[:200],
        })
        rprint(f"  → rerank_score={top_rerank_score} forras={top_forras!r}")

    return rows


def write_csv(rows: list[dict], path: Path) -> None:
    fieldnames = ["kategoria", "kerdes", "top_rerank_score", "top_forras", "valasz_eleje"]
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def print_summary(rows: list[dict]) -> None:
    by_category: dict[str, list[float]] = {}
    for row in rows:
        score = row["top_rerank_score"]
        if score == "" or score is None:
            continue
        by_category.setdefault(row["kategoria"], []).append(float(score))

    rprint("\n[bold]Kategóriánkénti top_rerank_score statisztika:[/bold]")
    for category, scores in by_category.items():
        if not scores:
            rprint(f"  {category}: nincs érvényes score")
            continue
        rprint(
            f"  {category}: min={min(scores):.4f}  "
            f"avg={sum(scores) / len(scores):.4f}  max={max(scores):.4f}  (n={len(scores)})"
        )


if __name__ == "__main__":
    output_path = Path(sys.argv[1]) if len(sys.argv) > 1 else OUTPUT_FILE

    questions = load_questions(QUESTIONS_FILE)
    rprint(f"[bold]{len(questions)} kérdés betöltve[/bold] a {QUESTIONS_FILE.name} fájlból.")

    rows = run_calibration(questions)
    write_csv(rows, output_path)
    rprint(f"\n[green]Eredmények elmentve:[/green] {output_path}")

    print_summary(rows)
