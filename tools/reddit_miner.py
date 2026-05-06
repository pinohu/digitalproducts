#!/usr/bin/env python3
"""
reddit_miner.py — Mine pain points from configured subreddits.

Pulls top threads, applies the signal-pattern filter, optionally sends
matched threads to Claude with the reddit-mining.md prompt for structured
candidate extraction, and outputs candidates ready for scoring.

Usage:
    python reddit_miner.py
    python reddit_miner.py --subreddits SaaS,Solopreneur --lookback 14
    python reddit_miner.py --dry-run   # skip Claude API call, raw threads only
    python reddit_miner.py --output candidates.md

Environment (in tools/.env):
    REDDIT_CLIENT_ID
    REDDIT_CLIENT_SECRET
    REDDIT_USER_AGENT
    ANTHROPIC_API_KEY
"""

from __future__ import annotations

import argparse
import datetime as dt
import os
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

import yaml

try:
    import praw
    from anthropic import Anthropic
    from dotenv import load_dotenv
    from rich.console import Console
    from rich.progress import Progress, SpinnerColumn, TextColumn
except ImportError as e:
    print(f"Missing dependency: {e}. Run: pip install -r requirements.txt", file=sys.stderr)
    sys.exit(1)


REPO_ROOT = Path(__file__).resolve().parent.parent
TOOLS_ROOT = Path(__file__).resolve().parent
CONFIG_PATH = TOOLS_ROOT / "config.yaml"
ENV_PATH = TOOLS_ROOT / ".env"
PROMPT_PATH = (
    REPO_ROOT
    / "01-market-research"
    / "idea-discovery"
    / "mining-prompts"
    / "reddit-mining.md"
)

console = Console()


@dataclass
class Thread:
    title: str
    selftext: str
    url: str
    subreddit: str
    score: int
    num_comments: int
    created_utc: float
    matched_patterns: list[str] = field(default_factory=list)

    @property
    def age_days(self) -> float:
        return (dt.datetime.utcnow().timestamp() - self.created_utc) / 86400

    def excerpt(self, max_len: int = 800) -> str:
        body = (self.selftext or "")[:max_len].strip()
        return f"[r/{self.subreddit}] {self.title}\n{body}\nURL: {self.url}\n"


def load_config() -> dict:
    if not CONFIG_PATH.exists():
        console.print(f"[red]config.yaml not found at {CONFIG_PATH}[/red]")
        sys.exit(1)
    with CONFIG_PATH.open() as f:
        return yaml.safe_load(f)


def load_env() -> None:
    if ENV_PATH.exists():
        load_dotenv(ENV_PATH)
    else:
        console.print(
            f"[yellow]Warning: {ENV_PATH} not found. "
            f"Assuming env vars are set in shell.[/yellow]"
        )


def get_reddit_client() -> praw.Reddit:
    client_id = os.getenv("REDDIT_CLIENT_ID")
    client_secret = os.getenv("REDDIT_CLIENT_SECRET")
    user_agent = os.getenv("REDDIT_USER_AGENT", "dynasty-empire-mining/1.0")

    if not (client_id and client_secret):
        console.print(
            "[red]Missing REDDIT_CLIENT_ID or REDDIT_CLIENT_SECRET in env.[/red]\n"
            "Create a 'script' app at https://www.reddit.com/prefs/apps and add to tools/.env"
        )
        sys.exit(1)

    return praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent,
    )


def fetch_threads(
    reddit: praw.Reddit,
    subreddits: list[str],
    lookback_days: int,
    threads_per_sub: int,
    min_score: int,
    min_comments: int,
) -> list[Thread]:
    threads: list[Thread] = []
    cutoff = dt.datetime.utcnow().timestamp() - lookback_days * 86400

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        for sub_name in subreddits:
            task = progress.add_task(f"Pulling r/{sub_name}...", total=None)
            try:
                sub = reddit.subreddit(sub_name)
                # Use 'top' with time filter; week/month covers most lookback windows
                time_filter = "week" if lookback_days <= 7 else "month"
                count = 0
                for post in sub.top(time_filter=time_filter, limit=threads_per_sub * 3):
                    if count >= threads_per_sub:
                        break
                    if post.created_utc < cutoff:
                        continue
                    if post.score < min_score:
                        continue
                    if post.num_comments < min_comments:
                        continue
                    threads.append(
                        Thread(
                            title=post.title,
                            selftext=post.selftext or "",
                            url=f"https://reddit.com{post.permalink}",
                            subreddit=sub_name,
                            score=post.score,
                            num_comments=post.num_comments,
                            created_utc=post.created_utc,
                        )
                    )
                    count += 1
            except Exception as e:
                console.print(f"[red]Error fetching r/{sub_name}: {e}[/red]")
            progress.remove_task(task)
            console.print(f"[green]✓[/green] r/{sub_name}: {count} threads")

    return threads


def pattern_filter(threads: list[Thread], patterns: list[str]) -> list[Thread]:
    """Tag threads matching signal patterns. Keep all; tag is informational."""
    compiled = [re.compile(re.escape(p), re.IGNORECASE) for p in patterns]
    pattern_strs = patterns

    for t in threads:
        text = f"{t.title} {t.selftext}".lower()
        for pat_re, pat_str in zip(compiled, pattern_strs):
            if pat_re.search(text):
                t.matched_patterns.append(pat_str)

    return threads


def load_mining_prompt() -> str:
    if not PROMPT_PATH.exists():
        console.print(f"[yellow]Warning: prompt file not found at {PROMPT_PATH}[/yellow]")
        return _DEFAULT_PROMPT

    text = PROMPT_PATH.read_text(encoding="utf-8")
    # Extract the prompt body (between the first ``` and the next ```)
    match = re.search(r"```\s*\n(.*?)\n```", text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return text


_DEFAULT_PROMPT = """\
You are mining Reddit threads for digital product opportunities.
For each candidate idea, output a record in the standard format with:
Source URL, Pattern matched, Verbatim quote, One-sentence pitch,
Pre-score (Pain/Power/Target/Growth/Fit), Format guess, Price guess,
Watering holes, Notes. Limit to top 5 candidates. If none, say so.

Now process:
"""


def call_claude(prompt: str, threads_text: str, model: str, max_tokens: int) -> str:
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        console.print(
            "[red]Missing ANTHROPIC_API_KEY in env. "
            "Skipping Claude analysis (use --dry-run to suppress this).[/red]"
        )
        return ""

    client = Anthropic(api_key=api_key)
    full_prompt = prompt + "\n\n" + threads_text

    console.print(
        f"[cyan]Calling Claude ({model}) with {len(threads_text)} chars of thread data...[/cyan]"
    )
    response = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        messages=[{"role": "user", "content": full_prompt}],
    )
    return response.content[0].text if response.content else ""


def write_output(content: str, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content, encoding="utf-8")
    console.print(f"[green]✓ Output written to {output_path}[/green]")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Mine Reddit pain points and extract digital product candidates."
    )
    parser.add_argument(
        "--subreddits",
        help="Comma-separated subreddit names (overrides config default).",
    )
    parser.add_argument("--lookback", type=int, help="Lookback days (overrides config).")
    parser.add_argument(
        "--threads-per-sub", type=int, help="Threads per subreddit (overrides config)."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Skip Claude API call; output raw matched threads only.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=TOOLS_ROOT / "output" / f"mining-{dt.date.today().isoformat()}.md",
        help="Output file path.",
    )
    args = parser.parse_args()

    load_env()
    config = load_config()

    subreddits = (
        args.subreddits.split(",")
        if args.subreddits
        else config["reddit"]["default_subreddits"]
    )
    lookback = args.lookback or config["reddit"]["default_lookback_days"]
    threads_per_sub = args.threads_per_sub or config["reddit"]["threads_per_subreddit"]
    min_score = config["reddit"]["min_thread_score"]
    min_comments = config["reddit"]["min_thread_comments"]
    patterns = config["reddit"]["signal_patterns"]

    console.print(
        f"\n[bold]Mining {len(subreddits)} subreddits, lookback {lookback} days, "
        f"top {threads_per_sub} per sub.[/bold]\n"
    )

    reddit = get_reddit_client()
    threads = fetch_threads(
        reddit, subreddits, lookback, threads_per_sub, min_score, min_comments
    )
    threads = pattern_filter(threads, patterns)

    matched = [t for t in threads if t.matched_patterns]
    console.print(
        f"\n[bold]Pulled {len(threads)} threads, "
        f"{len(matched)} matched signal patterns.[/bold]\n"
    )

    # Build threads text for Claude
    threads_text = "\n\n---\n\n".join(t.excerpt() for t in matched)

    output_lines = [
        f"# Reddit Mining Output — {dt.date.today().isoformat()}",
        "",
        f"**Subreddits:** {', '.join(subreddits)}",
        f"**Lookback:** {lookback} days",
        f"**Threads pulled:** {len(threads)}",
        f"**Threads matching signal patterns:** {len(matched)}",
        "",
        "---",
        "",
    ]

    if args.dry_run or not matched:
        output_lines += ["## Raw Matched Threads", ""]
        for t in matched:
            output_lines += [
                f"### {t.title}",
                f"- **r/{t.subreddit}**, {t.score} upvotes, {t.num_comments} comments, "
                f"{t.age_days:.1f} days old",
                f"- **Patterns matched:** {', '.join(t.matched_patterns)}",
                f"- **URL:** {t.url}",
                "",
                t.selftext[:1000] if t.selftext else "_(no body — link post)_",
                "",
            ]
    else:
        prompt = load_mining_prompt()
        analysis = call_claude(
            prompt,
            threads_text,
            config["claude"]["model"],
            config["claude"]["max_tokens_per_request"],
        )
        output_lines += [
            "## Claude Analysis (Candidate Extraction)",
            "",
            analysis or "_(no output from Claude)_",
            "",
            "---",
            "",
            "## Raw Matched Threads",
            "",
        ]
        for t in matched:
            output_lines += [
                f"- [{t.title}]({t.url}) — r/{t.subreddit}, {t.score}↑, "
                f"{t.num_comments}💬, patterns: {', '.join(t.matched_patterns)}",
            ]

    write_output("\n".join(output_lines), args.output)

    console.print(
        "\n[bold green]Done.[/bold green] Review the output, then for each strong candidate run:\n"
        "  python idea_scorer.py\n"
        "to add it to the idea backlog with full scoring.\n"
    )


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[yellow]Cancelled.[/yellow]")
        sys.exit(0)
