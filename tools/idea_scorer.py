#!/usr/bin/env python3
"""
idea_scorer.py — Interactive CLI for scoring digital product ideas
                 against the 50-point starving-crowd rubric.

Usage:
    python idea_scorer.py
    python idea_scorer.py --idea "Help SuiteDash users deploy faster"
    python idea_scorer.py --batch ideas.txt   # one idea per line

The output is a fully-formatted backlog entry that can be appended to
01-market-research/idea-discovery/idea-backlog.md.
"""

from __future__ import annotations

import argparse
import datetime as dt
import sys
import textwrap
from dataclasses import dataclass, field
from pathlib import Path

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.prompt import Prompt, IntPrompt, Confirm
    from rich.table import Table
except ImportError:
    print("Missing 'rich'. Install: pip install -r requirements.txt", file=sys.stderr)
    sys.exit(1)

console = Console()

REPO_ROOT = Path(__file__).resolve().parent.parent
BACKLOG_PATH = REPO_ROOT / "01-market-research" / "idea-discovery" / "idea-backlog.md"
RUBRIC_PATH = REPO_ROOT / "01-market-research" / "idea-discovery" / "scoring-rubric.md"


DIMENSIONS = [
    {
        "name": "Massive Pain",
        "key": "pain",
        "question": "How badly does the buyer want this fixed?",
        "anchors": {
            10: "Buyer would pay $1K+ today. Has spent real money on failed attempts. 3+ verbatim quotes available.",
            8: "Buyer would pay several hundred dollars. Tried 2+ solutions. Pattern in 10+ threads.",
            6: "Buyer is annoyed. Complained but not paid. Pattern in 3-5 sources.",
            4: "Mild frustration. Exists but hasn't escalated.",
            2: "Theoretical pain. No behavioral evidence.",
            0: "No actual pain. You're inventing the need.",
        },
        "test": "Find at least 3 verbatim quotes from real people. If you can't, score ≤ 4.",
    },
    {
        "name": "Purchasing Power",
        "key": "power",
        "question": "Can the audience pay $49–$497 without thinking hard?",
        "anchors": {
            10: "B2B, expensable, audience already buying $100+ tools regularly.",
            8: "B2B-adjacent or professional context. $50K+ revenue solopreneurs / freelancers.",
            6: "Side-hustle context. Disposable income, but every $99 is a deliberation.",
            4: "Hobbyist or aspirational. Wants to spend, rarely does.",
            2: "Pre-revenue, students, strict budget contexts.",
            0: "Audience cannot or will not pay at this price.",
        },
        "test": "Identify 3 paid products this audience already buys at $49+. If you can't, ≤ 4.",
    },
    {
        "name": "Easy to Target",
        "key": "target",
        "question": "Can you identify and reach this audience?",
        "anchors": {
            10: "5+ specific named watering holes. You can name them immediately.",
            8: "3-4 clear watering holes. You know how to find them.",
            6: "Audience exists but is scattered. 2-3 channels needed.",
            4: "Need paid ads or significant outbound to reach.",
            2: "Theoretical avatar — can describe, not point to.",
            0: "'Everyone on the internet' / 'small business owners' / similar.",
        },
        "test": "Name 5 specific places this audience already gathers. If you can't, ≤ 4.",
    },
    {
        "name": "Growing Market",
        "key": "growth",
        "question": "Is the underlying demand expanding?",
        "anchors": {
            10: "Search/community/revenue all up 30%+ in 24 months. Accelerating.",
            8: "Clear upward trajectory. Steady, well-documented.",
            6: "Stable. Not growing fast, not declining.",
            4: "Mixed signals.",
            2: "Flat or slightly declining.",
            0: "Demonstrably shrinking.",
        },
        "test": "Pull Google Trends + community size + 1 third-party signal. Need 2+ growth signals for 6+.",
    },
    {
        "name": "Personal Fit / Unfair Advantage",
        "key": "fit",
        "question": "Are *you* uniquely positioned to ship this?",
        "anchors": {
            10: "Lived the problem deeply. Proprietary knowledge or audience access.",
            8: "Done relevant work. Authority is provable. Natural extension of current work.",
            6: "Can produce credibly with research. No advantage, no major weakness.",
            4: "Learning alongside the buyer. Honest but not authoritative.",
            2: "Far outside experience. Significant outside help needed.",
            0: "Wrong person to ship this. Refer or kill.",
        },
        "test": "Can you write 3 paragraphs of useful content right now without research? Yes = 6+. No = ≤ 4.",
    },
]


@dataclass
class IdeaScore:
    name: str
    source: str = ""
    avatar: str = ""
    pitch: str = ""
    format_guess: str = "PDF"
    price_guess: int = 49
    watering_holes: list[str] = field(default_factory=list)
    quotes: list[str] = field(default_factory=list)
    scores: dict[str, int] = field(default_factory=dict)
    justifications: dict[str, str] = field(default_factory=dict)
    notes: str = ""

    @property
    def total(self) -> int:
        return sum(self.scores.values())

    @property
    def decision(self) -> str:
        t = self.total
        if t >= 40:
            return "Active sprint candidate (validate then sprint)"
        if t >= 30:
            return "Strong (pre-sale validate before sprinting)"
        if t >= 25:
            return "Backlog (re-score quarterly)"
        if t >= 15:
            return "Weak (park; promote only if dimensions improve)"
        return "Killed (don't build)"

    @property
    def status_bucket(self) -> str:
        t = self.total
        if t >= 40:
            return "Active Sprint Candidate"
        if t >= 30:
            return "Strong"
        if t >= 25:
            return "Backlog"
        if t >= 15:
            return "Weak"
        return "Killed"


def show_dimension(dim: dict) -> None:
    """Print scoring guidance for a dimension."""
    table = Table(show_header=False, box=None, padding=(0, 1))
    table.add_column(style="bold cyan", no_wrap=True)
    table.add_column()
    for score, anchor in dim["anchors"].items():
        table.add_row(f"{score}/10", anchor)
    console.print(
        Panel(
            table,
            title=f"[bold]Dimension: {dim['name']}[/bold]",
            subtitle=f"[dim]{dim['question']}[/dim]",
            expand=False,
        )
    )
    console.print(f"[yellow]Test:[/yellow] {dim['test']}\n")


def score_dimension(dim: dict) -> tuple[int, str]:
    """Prompt for one dimension's score + justification."""
    show_dimension(dim)
    score = IntPrompt.ask(
        f"[bold green]Score for {dim['name']}[/bold green] (0-10)",
        default=5,
    )
    score = max(0, min(10, score))
    justification = Prompt.ask(
        "[bold]One-sentence justification[/bold] (what's the evidence?)"
    )
    return score, justification


def collect_idea_metadata() -> IdeaScore:
    """Interactively collect the idea metadata before scoring."""
    console.print(
        Panel.fit(
            "[bold cyan]Dynasty Empire — Digital Product Idea Scorer[/bold cyan]\n"
            "Score against the 50-point starving-crowd rubric.",
            border_style="cyan",
        )
    )
    console.print()

    name = Prompt.ask("[bold]Idea name[/bold] (5-8 words)")
    source = Prompt.ask("[bold]Source[/bold] (URL, 'audience reply', 'AppSumo Q&A', etc.)")
    avatar = Prompt.ask(
        "[bold]Avatar[/bold] (specific — job title, revenue range, tools)\n"
        "[dim]e.g., 'Solo SaaS founders at $5K-$20K MRR running on Stripe'[/dim]"
    )
    pitch = Prompt.ask(
        "[bold]One-sentence pitch[/bold]\n"
        "[dim]Format: 'I help [avatar] solve [problem] without [objection].'[/dim]"
    )
    format_guess = Prompt.ask(
        "[bold]Format guess[/bold]",
        choices=["PDF", "Template", "Mini-course", "Notion template", "Spreadsheet", "Other"],
        default="PDF",
    )
    price_guess = IntPrompt.ask("[bold]Price guess[/bold] (USD)", default=49)

    console.print("\n[bold]Watering holes[/bold] (3+ specific places this audience gathers):")
    holes = []
    for i in range(1, 6):
        h = Prompt.ask(f"  {i}.", default="")
        if not h:
            break
        holes.append(h)

    console.print("\n[bold]Verbatim pain-point quotes[/bold] (paste 1-3 if you have them):")
    quotes = []
    for i in range(1, 4):
        q = Prompt.ask(f"  Quote {i}", default="")
        if not q:
            break
        quotes.append(q)

    return IdeaScore(
        name=name,
        source=source,
        avatar=avatar,
        pitch=pitch,
        format_guess=format_guess,
        price_guess=price_guess,
        watering_holes=holes,
        quotes=quotes,
    )


def score_idea(idea: IdeaScore) -> IdeaScore:
    """Run the 5-dimension scoring."""
    console.print("\n[bold]Now scoring each dimension. Be honest. The rubric is the rubric.[/bold]\n")

    for dim in DIMENSIONS:
        score, justification = score_dimension(dim)
        idea.scores[dim["key"]] = score
        idea.justifications[dim["key"]] = justification

    console.print("\n[bold]Optional notes[/bold] (free-form context):")
    idea.notes = Prompt.ask(">", default="")

    return idea


def show_summary(idea: IdeaScore) -> None:
    """Display the scoring summary."""
    table = Table(title=f"Score Summary — {idea.name}", show_lines=False)
    table.add_column("Dimension", style="bold")
    table.add_column("Score", justify="right")
    table.add_column("Justification")

    for dim in DIMENSIONS:
        key = dim["key"]
        table.add_row(
            dim["name"],
            f"{idea.scores[key]}/10",
            idea.justifications[key],
        )
    table.add_row("[bold cyan]TOTAL[/bold cyan]", f"[bold cyan]{idea.total}/50[/bold cyan]", "")
    console.print()
    console.print(table)
    console.print()
    console.print(
        Panel(
            f"[bold]Decision:[/bold] {idea.decision}",
            border_style="green" if idea.total >= 30 else "yellow" if idea.total >= 15 else "red",
        )
    )


def render_backlog_entry(idea: IdeaScore) -> str:
    """Render the full markdown backlog entry."""
    today = dt.date.today().isoformat()
    holes_md = "\n".join(f"  {i}. {h}" for i, h in enumerate(idea.watering_holes, 1)) or "  _(none recorded)_"
    quotes_md = "\n".join(f"> *\"{q}\"*" for q in idea.quotes) or "_(no verbatim quotes recorded)_"
    notes_md = idea.notes or "_(no additional notes)_"

    return textwrap.dedent(f"""\

        ## {idea.name}

        **Date scored:** {today}
        **Source:** {idea.source}
        **Status:** {idea.status_bucket}

        **Scoring (out of 50):**
        - Massive Pain: {idea.scores['pain']}/10 — {idea.justifications['pain']}
        - Purchasing Power: {idea.scores['power']}/10 — {idea.justifications['power']}
        - Easy to Target: {idea.scores['target']}/10 — {idea.justifications['target']}
        - Growing Market: {idea.scores['growth']}/10 — {idea.justifications['growth']}
        - Personal Fit: {idea.scores['fit']}/10 — {idea.justifications['fit']}
        - **Total: {idea.total}/50**

        **One-sentence pitch:**
        > *{idea.pitch}*

        **Avatar:**
        {idea.avatar}

        **Initial format guess:** {idea.format_guess}

        **Initial price guess:** ${idea.price_guess}

        **Watering holes:**
        {holes_md}

        **Verbatim pain-point quotes:**
        {quotes_md}

        **Decision:** {idea.decision}

        **Notes:**
        {notes_md}
        """)


def append_to_backlog(entry: str) -> None:
    """Append the entry to the idea-backlog.md file."""
    if not BACKLOG_PATH.exists():
        console.print(f"[red]Error: backlog file not found at {BACKLOG_PATH}[/red]")
        return

    current = BACKLOG_PATH.read_text(encoding="utf-8")
    new_content = current.rstrip() + "\n" + entry + "\n"
    BACKLOG_PATH.write_text(new_content, encoding="utf-8")
    console.print(f"[green]✓ Appended to {BACKLOG_PATH.relative_to(REPO_ROOT)}[/green]")


def main() -> None:
    parser = argparse.ArgumentParser(description="Score a digital product idea against the 50-point rubric.")
    parser.add_argument("--idea", help="Pre-fill the idea name, skip first prompt.")
    parser.add_argument("--no-write", action="store_true", help="Don't write to backlog; print only.")
    args = parser.parse_args()

    idea = collect_idea_metadata()
    if args.idea and not idea.name:
        idea.name = args.idea

    idea = score_idea(idea)
    show_summary(idea)
    entry = render_backlog_entry(idea)

    console.print("\n[bold]Generated backlog entry:[/bold]")
    console.print(Panel(entry, border_style="dim", expand=False))

    if args.no_write:
        console.print("[yellow]--no-write set; skipping backlog write.[/yellow]")
        return

    if Confirm.ask("\nAppend to idea-backlog.md?", default=True):
        append_to_backlog(entry)
    else:
        console.print("[yellow]Skipped. Entry above can be pasted manually.[/yellow]")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[yellow]Cancelled.[/yellow]")
        sys.exit(0)
