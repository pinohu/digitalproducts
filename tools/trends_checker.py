#!/usr/bin/env python3
"""
trends_checker.py — Pull 24-month Google Trends data for a candidate
                    keyword and map results to the Growth dimension of
                    the 50-point scoring rubric.

Usage:
    python trends_checker.py "newsletter monetization"
    python trends_checker.py "suitedash automation" --geo US
    python trends_checker.py "kw1" "kw2" "kw3"   # multi-keyword comparison
"""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

import yaml

# Lazy imports — rich/pytrends are only required for actual CLI runs, not for
# unit tests that mock the trends backend. We surface clean errors when a
# function that needs them is invoked without the dep installed.
try:  # pragma: no cover
    from pytrends.request import TrendReq  # type: ignore
except ImportError:  # pragma: no cover
    TrendReq = None  # type: ignore

try:  # pragma: no cover
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
except ImportError:  # pragma: no cover
    # Minimal stand-ins so tests can still import the module.
    class Console:  # type: ignore
        def print(self, *args, **kwargs):
            print(*args)

    def Panel(*args, **kwargs):  # type: ignore
        return args[0] if args else ""

    class Table:  # type: ignore
        def __init__(self, *args, **kwargs):
            self.rows = []

        def add_column(self, *args, **kwargs):
            pass

        def add_row(self, *args, **kwargs):
            self.rows.append(args)


REPO_ROOT = Path(__file__).resolve().parent.parent
TOOLS_ROOT = Path(__file__).resolve().parent
CONFIG_PATH = TOOLS_ROOT / "config.yaml"

console = Console()


def load_config() -> dict:
    if not CONFIG_PATH.exists():
        return {
            "trends": {
                "default_lookback_months": 24,
                "growth_thresholds": {
                    "high": 30,
                    "moderate": 10,
                    "flat": -5,
                    "declining": -15,
                },
            }
        }
    with CONFIG_PATH.open() as f:
        return yaml.safe_load(f)


class TrendsUnavailableError(RuntimeError):
    """Raised when Google Trends data cannot be fetched after retries."""


def _is_rate_limit(exc: Exception) -> bool:
    """Detect pytrends/requests 429-style failures across SDK versions."""
    msg = str(exc).lower()
    if "429" in msg or "too many requests" in msg or "rate limit" in msg:
        return True
    response = getattr(exc, "response", None)
    if response is not None and getattr(response, "status_code", None) == 429:
        return True
    return False


def fetch_trends(
    keywords: list[str],
    lookback_months: int,
    geo: str = "",
    *,
    max_retries: int = 4,
    initial_backoff_seconds: float = 5.0,
    sleep_fn=time.sleep,
    trend_req_factory=None,
) -> dict:
    """Fetch Google Trends interest-over-time for given keywords.

    Retries with exponential backoff on rate-limit (429) responses. Raises
    `TrendsUnavailableError` if pytrends keeps failing after the retry budget.
    """
    factory = trend_req_factory or (lambda: TrendReq(hl="en-US", tz=360))
    timeframe = f"today {lookback_months}-m"

    console.print(
        f"[cyan]Pulling Google Trends data for {keywords} "
        f"({timeframe}, geo={geo or 'global'})...[/cyan]"
    )

    backoff = initial_backoff_seconds
    last_exc: Exception | None = None
    for attempt in range(1, max_retries + 1):
        try:
            pytrends = factory()
            pytrends.build_payload(keywords, timeframe=timeframe, geo=geo)
            interest = pytrends.interest_over_time()
            break
        except Exception as e:  # pragma: no cover - exercised via test mocks
            last_exc = e
            if not _is_rate_limit(e) or attempt == max_retries:
                # Non-retryable, or out of retries.
                raise TrendsUnavailableError(
                    f"Google Trends unavailable after {attempt} attempt(s): {e}"
                ) from e
            console.print(
                f"[yellow]Rate-limited by Google Trends "
                f"(attempt {attempt}/{max_retries}); sleeping {backoff:.1f}s...[/yellow]"
            )
            sleep_fn(backoff)
            backoff *= 2
    else:  # pragma: no cover - loop exits via break/raise
        raise TrendsUnavailableError(
            f"Google Trends unavailable: {last_exc}"
        ) from last_exc

    if interest.empty:
        return {kw: None for kw in keywords}

    # Drop the 'isPartial' column if present
    if "isPartial" in interest.columns:
        interest = interest.drop(columns=["isPartial"])

    results = {}
    for kw in keywords:
        if kw not in interest.columns:
            results[kw] = None
            continue
        series = interest[kw]
        # First and last quarter averages — more stable than first/last point
        q1_avg = series.iloc[: len(series) // 4].mean() if len(series) > 4 else series.iloc[0]
        q4_avg = (
            series.iloc[-len(series) // 4 :].mean() if len(series) > 4 else series.iloc[-1]
        )
        max_val = series.max()
        min_val = series.min()

        if q1_avg == 0:
            growth_pct = float("inf") if q4_avg > 0 else 0
        else:
            growth_pct = ((q4_avg - q1_avg) / q1_avg) * 100

        results[kw] = {
            "q1_avg": float(q1_avg),
            "q4_avg": float(q4_avg),
            "max": float(max_val),
            "min": float(min_val),
            "growth_pct": growth_pct,
            "data_points": len(series),
        }

    return results


def map_growth_to_rubric_score(growth_pct: float, thresholds: dict) -> tuple[int, str]:
    """Map percentage growth to the 0-10 Growth dimension score."""
    if growth_pct == float("inf"):
        return 10, "Started from 0 baseline; brand-new search interest. Very high potential."

    if growth_pct >= thresholds["high"]:
        return 9, f"Up {growth_pct:.1f}% — strong growth, accelerating market."
    if growth_pct >= 20:
        return 8, f"Up {growth_pct:.1f}% — clear upward trajectory."
    if growth_pct >= thresholds["moderate"]:
        return 7, f"Up {growth_pct:.1f}% — moderate, steady growth."
    if growth_pct >= 0:
        return 6, f"Up {growth_pct:.1f}% — slight positive trend; stable+."
    if growth_pct >= thresholds["flat"]:
        return 5, f"Down {abs(growth_pct):.1f}% — essentially flat."
    if growth_pct >= thresholds["declining"]:
        return 3, f"Down {abs(growth_pct):.1f}% — meaningful decline."
    return 1, f"Down {abs(growth_pct):.1f}% — significant decline. Avoid."


def render_results(results: dict, thresholds: dict) -> None:
    """Display results in a formatted table + recommendations."""
    table = Table(title="Google Trends — Growth Dimension Analysis", show_lines=True)
    table.add_column("Keyword", style="bold cyan")
    table.add_column("Avg Q1", justify="right")
    table.add_column("Avg Q4", justify="right")
    table.add_column("Growth %", justify="right")
    table.add_column("Score", justify="right", style="bold")
    table.add_column("Verdict")

    for kw, data in results.items():
        if data is None:
            table.add_row(kw, "—", "—", "—", "—", "[red]No data[/red]")
            continue

        score, verdict = map_growth_to_rubric_score(data["growth_pct"], thresholds)
        growth_str = (
            f"+{data['growth_pct']:.1f}%"
            if data["growth_pct"] >= 0
            else f"{data['growth_pct']:.1f}%"
        )
        score_color = "green" if score >= 7 else "yellow" if score >= 5 else "red"

        table.add_row(
            kw,
            f"{data['q1_avg']:.1f}",
            f"{data['q4_avg']:.1f}",
            growth_str,
            f"[{score_color}]{score}/10[/{score_color}]",
            verdict,
        )

    console.print(table)

    # Confidence + recommendation panel
    valid_results = [r for r in results.values() if r is not None]
    if not valid_results:
        console.print("[red]No usable data returned.[/red]")
        return

    if len(valid_results) == 1:
        confidence = "MEDIUM (single keyword)"
    else:
        scores = [
            map_growth_to_rubric_score(r["growth_pct"], thresholds)[0] for r in valid_results
        ]
        spread = max(scores) - min(scores)
        confidence = "HIGH (consistent)" if spread <= 2 else "MEDIUM (mixed signals)"

    avg_score = sum(
        map_growth_to_rubric_score(r["growth_pct"], thresholds)[0] for r in valid_results
    ) / len(valid_results)

    if avg_score >= 8:
        rec = "[bold green]BUILD[/bold green] — Growth dimension scores 8+. Move idea forward to validation."
    elif avg_score >= 6:
        rec = "[yellow]VALIDATE FURTHER[/yellow] — Growth score 6-7. Pre-sale or waitlist before sprinting."
    elif avg_score >= 4:
        rec = "[yellow]PARK[/yellow] — Growth score 4-5. Backlog; re-score in 90 days."
    else:
        rec = "[red]KILL[/red] — Growth score <4. Document reason, archive."

    console.print(
        Panel(
            f"[bold]Confidence:[/bold] {confidence}\n"
            f"[bold]Average growth score:[/bold] {avg_score:.1f}/10\n"
            f"[bold]Recommendation:[/bold] {rec}",
            title="Verdict",
            border_style="cyan",
        )
    )

    console.print(
        "\n[dim]Note: Google Trends data is normalized (0-100). "
        "Absolute search volume requires Keyword Planner or SEMrush. "
        "Use this score as one of multiple growth signals — corroborate with "
        "community size growth, AppSumo trending, and industry reports.[/dim]"
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Pull Google Trends data and score the Growth dimension of an idea."
    )
    parser.add_argument(
        "keywords",
        nargs="+",
        help="One or more keywords to analyze (max 5 per Google Trends limit).",
    )
    parser.add_argument(
        "--lookback",
        type=int,
        default=None,
        help="Lookback months (default from config: 24).",
    )
    parser.add_argument(
        "--geo",
        default="",
        help="Geographic restriction (e.g., 'US', 'GB'). Default: global.",
    )
    parser.add_argument(
        "--max-retries",
        type=int,
        default=4,
        help="Max retries on Google Trends rate-limit (429). Default: 4.",
    )
    parser.add_argument(
        "--initial-backoff",
        type=float,
        default=5.0,
        help="Initial backoff seconds between retries (doubles each attempt). Default: 5.0.",
    )
    args = parser.parse_args()

    if len(args.keywords) > 5:
        console.print(
            "[red]Google Trends limits comparisons to 5 keywords. Reducing to first 5.[/red]"
        )
        args.keywords = args.keywords[:5]

    config = load_config()
    lookback = args.lookback or config["trends"]["default_lookback_months"]
    thresholds = config["trends"]["growth_thresholds"]

    try:
        results = fetch_trends(
            args.keywords,
            lookback,
            args.geo,
            max_retries=args.max_retries,
            initial_backoff_seconds=args.initial_backoff,
        )
    except TrendsUnavailableError as e:
        console.print(f"[red]Trend data unavailable: {e}[/red]")
        console.print(
            "[yellow]Google Trends has known intermittent issues. "
            "Wait 1 hour and retry, or check that pytrends is up to date.[/yellow]"
        )
        sys.exit(2)
    except Exception as e:
        console.print(f"[red]Error fetching trends: {e}[/red]")
        sys.exit(1)

    render_results(results, thresholds)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[yellow]Cancelled.[/yellow]")
        sys.exit(0)
