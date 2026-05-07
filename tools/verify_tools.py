#!/usr/bin/env python3
"""Offline readiness checks for the digitalproducts Python tools.

This script intentionally does not call external APIs. It verifies imports,
script syntax, config shape, expected repo paths, and which optional secrets are
present so local setup problems are caught before running Reddit/n8n/Gumroad/etc.
"""

from __future__ import annotations

import importlib
import os
import py_compile
import sys
from pathlib import Path

try:
    import yaml
    from dotenv import load_dotenv
    from rich.console import Console
    from rich.table import Table
except ImportError as exc:  # pragma: no cover - only hit before setup completes
    print(f"Missing dependency: {exc}. Run the setup commands in tools/README.md", file=sys.stderr)
    sys.exit(1)

TOOLS_ROOT = Path(__file__).resolve().parent
REPO_ROOT = TOOLS_ROOT.parent
CONFIG_PATH = TOOLS_ROOT / "config.yaml"
ENV_PATH = TOOLS_ROOT / ".env"

console = Console()

REQUIRED_IMPORTS = {
    "rich": "CLI rendering",
    "yaml": "config.yaml parsing",
    "dotenv": ".env loading",
    "praw": "reddit_miner.py Reddit API client",
    "anthropic": "reddit_miner.py Claude extraction",
    "pytrends": "trends_checker.py Google Trends client",
    "github": "future GitHub write automation",
    "requests": "future API integrations",
}

SCRIPTS = [
    "idea_scorer.py",
    "reddit_miner.py",
    "trends_checker.py",
    "product_bootstrapper.py",
    "verify_tools.py",
]

EXPECTED_PATHS = [
    "01-market-research/idea-discovery/idea-backlog.md",
    "01-market-research/idea-discovery/scoring-rubric.md",
    "01-market-research/idea-discovery/mining-prompts/reddit-mining.md",
    "01-market-research/niche-validation-template.md",
    "03-products",
    "automation/n8n-workflows",
]

SECRET_GROUPS = {
    "Reddit mining": ["REDDIT_CLIENT_ID", "REDDIT_CLIENT_SECRET", "REDDIT_USER_AGENT"],
    "Claude extraction": ["ANTHROPIC_API_KEY"],
    "GitHub write automation": ["GITHUB_TOKEN", "GITHUB_REPO"],
    "n8n workflow API": ["N8N_BASE_URL", "N8N_API_KEY"],
    "Gumroad automation": ["GUMROAD_ACCESS_TOKEN"],
    "Neon analytics": ["NEON_DATABASE_URL"],
    "Vercel deploy automation": ["VERCEL_TOKEN", "VERCEL_PROJECT_ID"],
}


def status(ok: bool) -> str:
    return "[green]PASS[/green]" if ok else "[red]FAIL[/red]"


def load_environment() -> None:
    if ENV_PATH.exists():
        load_dotenv(ENV_PATH)


def check_imports() -> bool:
    table = Table(title="Python dependency imports")
    table.add_column("Module")
    table.add_column("Purpose")
    table.add_column("Status")
    all_ok = True
    for module_name, purpose in REQUIRED_IMPORTS.items():
        try:
            importlib.import_module(module_name)
            ok = True
        except Exception:
            ok = False
            all_ok = False
        table.add_row(module_name, purpose, status(ok))
    console.print(table)
    return all_ok


def check_compile() -> bool:
    table = Table(title="Script compilation")
    table.add_column("Script")
    table.add_column("Status")
    all_ok = True
    for script in SCRIPTS:
        try:
            py_compile.compile(str(TOOLS_ROOT / script), doraise=True)
            ok = True
        except Exception as exc:
            ok = False
            all_ok = False
            console.print(f"[red]{script}: {exc}[/red]")
        table.add_row(script, status(ok))
    console.print(table)
    return all_ok


def check_config() -> bool:
    ok = CONFIG_PATH.exists()
    data = {}
    if ok:
        try:
            data = yaml.safe_load(CONFIG_PATH.read_text(encoding="utf-8")) or {}
        except Exception as exc:
            console.print(f"[red]config.yaml parse error: {exc}[/red]")
            ok = False
    required_sections = ["repo", "reddit", "claude", "scoring", "trends", "product_bootstrap"]
    missing = [section for section in required_sections if section not in data]
    if missing:
        ok = False
    console.print(f"config.yaml: {status(ok)}" + (f" (missing: {', '.join(missing)})" if missing else ""))
    return ok


def check_paths() -> bool:
    table = Table(title="Expected repo paths")
    table.add_column("Path")
    table.add_column("Status")
    all_ok = True
    for rel_path in EXPECTED_PATHS:
        ok = (REPO_ROOT / rel_path).exists()
        all_ok = all_ok and ok
        table.add_row(rel_path, status(ok))
    console.print(table)
    return all_ok


def check_secrets() -> None:
    table = Table(title="External credential readiness (informational)")
    table.add_column("System")
    table.add_column("Variables")
    table.add_column("Status")
    for system, variables in SECRET_GROUPS.items():
        present = [name for name in variables if os.getenv(name)]
        if len(present) == len(variables):
            readiness = "[green]ready[/green]"
        elif present:
            readiness = f"[yellow]partial ({len(present)}/{len(variables)})[/yellow]"
        else:
            readiness = "[yellow]missing[/yellow]"
        table.add_row(system, ", ".join(variables), readiness)
    console.print(table)
    console.print(
        "[dim]Missing external credentials do not fail offline verification; they block only real API-backed runs.[/dim]"
    )


def main() -> int:
    load_environment()
    checks = [check_imports(), check_compile(), check_config(), check_paths()]
    check_secrets()
    if all(checks):
        console.print("\n[bold green]Offline tools verification passed.[/bold green]")
        return 0
    console.print("\n[bold red]Offline tools verification failed.[/bold red]")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
