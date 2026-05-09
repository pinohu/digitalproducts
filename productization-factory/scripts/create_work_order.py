#!/usr/bin/env python3
"""
create_work_order.py - Generate a Productization Factory work order.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError as exc:
    print(f"Missing dependency: {exc}. Install PyYAML in the repo tool environment.", file=sys.stderr)
    sys.exit(1)

try:
    from rich.console import Console
except ImportError:
    Console = None


SCRIPT_ROOT = Path(__file__).resolve().parent
FACTORY_ROOT = SCRIPT_ROOT.parent
REPO_ROOT = FACTORY_ROOT.parent
FAMILY_CONFIG = FACTORY_ROOT / "config" / "product-families.yml"
WORK_ORDER_ROOT = FACTORY_ROOT / "work-orders"

console = Console() if Console else None


def log(message: str) -> None:
    if console:
        console.print(message)
    else:
        print(message)


def load_family_registry() -> dict:
    with FAMILY_CONFIG.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def slugify(value: str) -> str:
    cleaned = re.sub(r"[^a-z0-9]+", "-", value.strip().lower())
    return cleaned.strip("-") or "work-order"


def find_family(config: dict, slug: str) -> dict:
    for family in config.get("families", []):
        if family["slug"] == slug:
            return family
    raise KeyError(f"Unknown family slug: {slug}")


def next_work_order_id() -> str:
    today = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%d")
    max_counter = 0

    for path in WORK_ORDER_ROOT.rglob("*.yml"):
        parts = path.stem.split("-")
        if len(parts) < 3:
            continue
        if parts[0] != "WF" or parts[1] != today:
            continue
        if not parts[2].isdigit():
            continue
        max_counter = max(max_counter, int(parts[2]))

    return f"WF-{today}-{max_counter + 1:03d}"


def default_acceptance(stage: str) -> list[str]:
    stage_map = {
        "market-research": [
            "Validation artifact exists and names a specific buyer, pain, and proof path",
            "Repo truth reflects current demand assumptions and blockers",
        ],
        "offer-engineering": [
            "Offer brief is updated",
            "Pricing ladder is explicit",
            "Bonus stack or risk-reversal logic is explicit",
        ],
        "product-build": [
            "Core deliverable exists",
            "At least one bonus or supporting asset exists",
            "Implementation SOP or delivery path is documented",
        ],
        "sales-page": [
            "Sales page draft exists",
            "Primary CTA and FAQ are explicit",
            "Proof or proof-gap language is truthful",
        ],
        "email-workflow": [
            "Post-purchase sequence exists",
            "Launch or follow-up sequence exists",
            "Upsell or next-step path is explicit",
        ],
        "launch-plan": [
            "Launch checklist exists",
            "External blockers are named truthfully",
            "Operator handoff is clear",
        ],
        "iteration-and-scale": [
            "Next-rung offer ladder is explicit",
            "Metrics or review path are documented",
            "Managed-service follow-on is named",
        ],
    }
    return stage_map.get(
        stage,
        [
            "Stage artifact exists",
            "Repo truth is aligned with the current sprint",
        ],
    )


def default_review_checklist() -> list[str]:
    return [
        "One buyer",
        "One pain",
        "One promise",
        "Upsell path exists",
        "Repo truth aligned with current sprint",
    ]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Create a Productization Factory work order.")
    parser.add_argument("--family", required=True, help="Product family slug.")
    parser.add_argument("--stage", required=True, help="Factory stage, e.g. offer-engineering or launch-plan.")
    parser.add_argument("--target-product", required=True, help="Target product name.")
    parser.add_argument("--buyer", help="Specific buyer. Defaults to the first buyer type in the family.")
    parser.add_argument("--pain", help="Primary painful problem. Defaults to the first family problem.")
    parser.add_argument("--outcome", help="Promised outcome. Defaults to the first family outcome.")
    parser.add_argument("--owner-agent", default="Chief of Staff", help="Owning agent label.")
    parser.add_argument("--implementation-agent", default="Codex", help="Implementation agent label.")
    parser.add_argument(
        "--bucket",
        choices=["backlog", "active", "review", "completed"],
        default="backlog",
        help="Work-order bucket.",
    )
    parser.add_argument("--repo-path", action="append", default=[], help="Repo path to associate with the work order.")
    parser.add_argument("--dependency", action="append", default=[], help="Dependency issue or work-order ID.")
    parser.add_argument("--acceptance", action="append", default=[], help="Acceptance criterion.")
    parser.add_argument("--review-item", action="append", default=[], help="Review checklist item.")
    parser.add_argument("--prompt", default="", help="Suggested next Codex prompt.")
    parser.add_argument("--dry-run", action="store_true", help="Print the YAML without writing a file.")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    config = load_family_registry()
    family = find_family(config, args.family)
    using_family_defaults = not args.buyer or not args.pain or not args.outcome

    work_order_id = next_work_order_id()
    stage_slug = slugify(args.stage)
    bucket_path = WORK_ORDER_ROOT / args.bucket
    bucket_path.mkdir(parents=True, exist_ok=True)

    payload = {
        "id": work_order_id,
        "created_at": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "status": args.bucket,
        "product_family": family["slug"],
        "target_product": args.target_product,
        "buyer": args.buyer or family["buyer_types"][0],
        "pain": args.pain or family["painful_problems"][0],
        "promised_outcome": args.outcome or family["promised_outcomes"][0],
        "stage": args.stage,
        "owner_agent": args.owner_agent,
        "implementation_agent": args.implementation_agent,
        "repo_paths": args.repo_path,
        "dependencies": args.dependency,
        "acceptance_criteria": args.acceptance or default_acceptance(stage_slug),
        "review_checklist": args.review_item or default_review_checklist(),
        "next_codex_prompt": args.prompt or "Update the repo artifacts for this stage and keep repo truth aligned with the active sprint.",
    }

    yaml_text = yaml.safe_dump(payload, sort_keys=False, allow_unicode=False)
    filename = f"{work_order_id}-{family['slug']}-{stage_slug}.yml"
    destination = bucket_path / filename

    if args.dry_run:
        if using_family_defaults:
            log(
                "[yellow]Using family defaults for buyer, pain, or outcome. "
                "Pass --buyer/--pain/--outcome for product-specific work orders.[/yellow]"
                if console
                else "Using family defaults for buyer, pain, or outcome. Pass --buyer/--pain/--outcome for product-specific work orders."
            )
        log(f"[bold]Dry run:[/bold] {destination.relative_to(REPO_ROOT)}" if console else f"Dry run: {destination.relative_to(REPO_ROOT)}")
        print(yaml_text)
        return

    destination.write_text(yaml_text, encoding="utf-8")
    if using_family_defaults:
        log(
            "[yellow]Created with family-default buyer, pain, or outcome. "
            "Tighten those fields if this work order is product-specific.[/yellow]"
            if console
            else "Created with family-default buyer, pain, or outcome. Tighten those fields if this work order is product-specific."
        )
    log(f"[green]Created[/green] {destination.relative_to(REPO_ROOT)}" if console else f"Created {destination.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    try:
        main()
    except KeyError as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)
