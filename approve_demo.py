"""
Jóváhagyói CLI a client_demo.py által generált válaszokhoz (demó).

Kilistázza a run_log 'pending' státuszú sorait, megmutatja a kérdést,
a generált választ és a top forrást, majd a jóváhagyó eldönti:
  [j]óváhagy  — approval_status = 'approved'
  [s]zerkeszt — új szöveget kér, edit_distance-t számol, approval_status = 'edited'
  [e]lutasít  — approval_status = 'rejected'

Futtatás: python approve_demo.py

Megjegyzés: a run_log csak a TOP forrást tárolja (top_source mező), nem a
teljes forráslistát — a séma erre lett megadva, ezért csak azt tudjuk
megmutatni jóváhagyáskor.
"""
from datetime import datetime

from rich import print as rprint

from src.db import init_db, get_session, RunLog


def levenshtein(a: str, b: str) -> int:
    """Egyszerű szerkesztési távolság (szóközönkénti, nem karakterenkénti,
    hogy hosszabb szövegeken is gyors legyen)."""
    a_words = a.split()
    b_words = b.split()
    n, m = len(a_words), len(b_words)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = 0 if a_words[i - 1] == b_words[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,       # törlés
                dp[i][j - 1] + 1,       # beszúrás
                dp[i - 1][j - 1] + cost,  # csere
            )
    return dp[n][m]


def review_row(row: RunLog, approver: str) -> None:
    rprint(f"\n[bold cyan]--- #{row.id} ---[/bold cyan] ({row.created_at})")
    rprint(f"[bold]Kérdés (maszkolt):[/bold] {row.question_masked}")
    rprint(f"[bold]Válasz:[/bold]\n{row.answer_text}")
    rprint(f"[bold]Top forrás:[/bold] {row.top_source} (rerank score: {row.top_rerank_score})")

    action = input("\n[j]óváhagy / [s]zerkeszt / [e]lutasít: ").strip().lower()

    db_session = get_session()
    try:
        db_row = db_session.query(RunLog).filter(RunLog.id == row.id).one()

        if action == "j":
            db_row.approval_status = "approved"
        elif action == "s":
            rprint("Írd be az új választ (Enter a végén lezárja):")
            new_answer = input("> ").strip()
            db_row.edit_distance = levenshtein(row.answer_text or "", new_answer)
            db_row.answer_text = new_answer
            db_row.approval_status = "edited"
        elif action == "e":
            db_row.approval_status = "rejected"
        else:
            rprint("[red]Ismeretlen választás, ez a tétel kimarad — próbáld újra később.[/red]")
            return

        db_row.approver = approver
        db_row.approved_at = datetime.utcnow()
        db_session.commit()
        rprint(f"[green]Mentve: #{row.id} -> {db_row.approval_status}[/green]")
    finally:
        db_session.close()


def main() -> None:
    init_db()

    db_session = get_session()
    pending = (
        db_session.query(RunLog)
        .filter(RunLog.approval_status == "pending")
        .order_by(RunLog.created_at)
        .all()
    )
    db_session.close()

    if not pending:
        rprint("[dim]Nincs jóváhagyásra váró tétel.[/dim]")
        return

    approver = input("Jóváhagyó neve: ").strip() or "ismeretlen"

    rprint(f"\n[bold]{len(pending)} jóváhagyásra váró tétel.[/bold]")
    for row in pending:
        review_row(row, approver)


if __name__ == "__main__":
    main()
