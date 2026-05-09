#!/usr/bin/env python3
"""
validate_product_folder.py - Check whether a product has the required repo artifacts.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

try:
    from rich.console import Console
except ImportError:
    Console = None


SCRIPT_ROOT = Path(__file__).resolve().parent
FACTORY_ROOT = SCRIPT_ROOT.parent
REPO_ROOT = FACTORY_ROOT.parent

console = Console() if Console else None


def log(message: str) -> None:
    if console:
        console.print(message)
    else:
        print(message)


def has_nonhidden_files(directory: Path) -> bool:
    if not directory.exists() or not directory.is_dir():
        return False
    for entry in directory.iterdir():
        if entry.name.startswith("."):
            continue
        return True
    return False


def build_checks(slug: str) -> list[tuple[str, Path, str]]:
    return [
        ("validation worksheet", REPO_ROOT / "01-market-research" / "by-product" / slug / "validation.md", "file"),
        ("offer brief", REPO_ROOT / "02-offers" / "by-product" / f"{slug}.md", "file"),
        ("product README", REPO_ROOT / "03-products" / slug / "README.md", "file"),
        ("manuscript folder", REPO_ROOT / "03-products" / slug / "manuscript", "dir"),
        ("assets folder", REPO_ROOT / "03-products" / slug / "assets", "dir"),
        ("bonuses folder", REPO_ROOT / "03-products" / slug / "bonuses", "dir"),
        ("deliverables folder", REPO_ROOT / "03-products" / slug / "deliverables", "dir"),
        ("sales page", REPO_ROOT / "04-sales-pages" / "by-product" / f"{slug}.md", "file"),
        ("post-purchase email", REPO_ROOT / "05-email-workflows" / "by-product" / slug / "post-purchase-sequence.md", "file"),
        ("launch sequence email", REPO_ROOT / "05-email-workflows" / "by-product" / slug / "launch-sequence.md", "file"),
        ("abandoned-cart email", REPO_ROOT / "05-email-workflows" / "by-product" / slug / "abandoned-cart.md", "file"),
        ("launch playbook", REPO_ROOT / "06-launch-playbooks" / "by-product" / f"{slug}.md", "file"),
        ("iteration plan", REPO_ROOT / "09-iteration-and-scale" / "by-product" / f"{slug}.md", "file"),
        ("analytics sheet", REPO_ROOT / "analytics" / "by-product" / f"{slug}.md", "file"),
    ]


def evaluate_checks(checks: list[tuple[str, Path, str]]) -> tuple[list[dict], list[dict]]:
    passed = []
    missing = []

    for label, path, kind in checks:
        ok = path.exists() if kind == "file" else has_nonhidden_files(path)
        payload = {"label": label, "path": str(path), "kind": kind}
        if ok:
            passed.append(payload)
        else:
            missing.append(payload)

    return passed, missing


def render_markdown(slug: str, passed: list[dict], missing: list[dict]) -> str:
    status = "PASS" if not missing else "BLOCKED"
    lines = [
        f"# Sprint Readiness Report: {slug}",
        "",
        f"Status: **{status}**",
        "",
        f"- Passed checks: {len(passed)}",
        f"- Missing checks: {len(missing)}",
        "",
    ]

    if missing:
        lines.extend(["## Missing", ""])
        for item in missing:
            path = Path(item["path"]).relative_to(REPO_ROOT)
            lines.append(f"- `{item['label']}` -> `{path}`")
        lines.append("")

    lines.extend(["## Passed", ""])
    for item in passed:
        path = Path(item["path"]).relative_to(REPO_ROOT)
        lines.append(f"- `{item['label']}` -> `{path}`")

    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate whether a product has the required factory artifacts.")
    parser.add_argument("slug", help="Product slug, for example 01-suitedash-good-parts")
    parser.add_argument("--json", action="store_true", help="Print JSON instead of human-readable output.")
    parser.add_argument("--report", help="Optional markdown report output path.")
    args = parser.parse_args()

    checks = build_checks(args.slug)
    passed, missing = evaluate_checks(checks)
    result = {
        "slug": args.slug,
        "passed": passed,
        "missing": missing,
        "status": "pass" if not missing else "blocked",
    }

    if args.report:
        report_path = Path(args.report)
        if not report_path.is_absolute():
            report_path = REPO_ROOT / report_path
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(render_markdown(args.slug, passed, missing), encoding="utf-8")
        log(f"[green]Wrote[/green] {report_path.relative_to(REPO_ROOT)}" if console else f"Wrote {report_path.relative_to(REPO_ROOT)}")

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        log(f"[bold]{args.slug}[/bold]: {'PASS' if not missing else 'BLOCKED'}" if console else f"{args.slug}: {'PASS' if not missing else 'BLOCKED'}")
        for item in missing:
            path = Path(item["path"]).relative_to(REPO_ROOT)
            log(f"[red]- Missing[/red] {item['label']}: {path}" if console else f"- Missing {item['label']}: {path}")
        if not missing:
            log("[green]All required factory artifacts are present.[/green]" if console else "All required factory artifacts are present.")

    if missing:
        sys.exit(1)


if __name__ == "__main__":
    main()
