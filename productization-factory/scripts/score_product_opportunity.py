#!/usr/bin/env python3
"""
score_product_opportunity.py - Score workflow product families and emit reports.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
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
CONFIG_PATH = FACTORY_ROOT / "config" / "product-families.yml"
REPORTS_ROOT = FACTORY_ROOT / "reports"
MARKDOWN_REPORT = REPORTS_ROOT / "revenue-priority-scoreboard.md"
JSON_REPORT = REPORTS_ROOT / "revenue-priority-scoreboard.json"

console = Console() if Console else None

RUBRIC = {
    "pain_urgency": 20,
    "purchasing_power": 15,
    "ease_of_targeting": 15,
    "tool_leverage": 10,
    "speed_to_ship": 10,
    "recurring_revenue_potential": 15,
    "proof_case_study_potential": 10,
    "strategic_fit": 5,
}

ACTIVE_SPRINT_OVERRIDE = "client-portal-service-delivery-os"
ACTIVE_SPRINT_PRODUCT = "The Good Parts of SuiteDash"


def log(message: str) -> None:
    if console:
        console.print(message)
    else:
        print(message)


def load_registry() -> dict:
    with CONFIG_PATH.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def validate_inputs(scoring_inputs: dict, family_slug: str) -> None:
    for key, max_score in RUBRIC.items():
        value = scoring_inputs.get(key)
        if value is None:
            raise ValueError(f"{family_slug} is missing scoring input: {key}")
        if not isinstance(value, int):
            raise ValueError(f"{family_slug} has non-integer score for {key}: {value!r}")
        if value < 0 or value > max_score:
            raise ValueError(f"{family_slug} score {key}={value} is outside 0-{max_score}")


def confidence_band(total: int) -> str:
    if total >= 90:
        return "Immediate priority"
    if total >= 80:
        return "Strong build candidate"
    if total >= 70:
        return "Viable once current sprint clears"
    return "Exploratory"


def score_families(config: dict) -> list[dict]:
    scored = []
    for family in config.get("families", []):
        inputs = family.get("scoring_inputs", {})
        validate_inputs(inputs, family["slug"])
        total = sum(inputs.values())
        scored.append(
            {
                "slug": family["slug"],
                "name": family["name"],
                "score": total,
                "confidence_band": confidence_band(total),
                "default_pricing_ladder": family.get("default_pricing_ladder", config.get("default_pricing_ladder")),
                "example_tools": family.get("example_tools", []),
                "low_ticket_products": family.get("low_ticket_products", []),
                "scoring_inputs": inputs,
            }
        )

    return sorted(scored, key=lambda item: (-item["score"], item["name"]))


def render_markdown(scored: list[dict]) -> str:
    lines = [
        "# Revenue Priority Scoreboard",
        "",
        f"Generated: {dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')}",
        "",
        "## Recommended now",
        "",
        f"- Execution-priority family: `{ACTIVE_SPRINT_OVERRIDE}`",
        f"- Active anchor product: `{ACTIVE_SPRINT_PRODUCT}`",
        "- Reason: the repo already has live sprint momentum, a partially complete launch surface, and the clearest path from trust tripwire into toolkit, setup sprint, and managed service.",
        "",
        "## Raw family scores",
        "",
        "| Rank | Family | Score | First low-ticket idea | Confidence band |",
        "|---|---|---:|---|---|",
    ]

    for index, family in enumerate(scored, start=1):
        first_low_ticket = family["low_ticket_products"][0] if family["low_ticket_products"] else "-"
        lines.append(
            f"| {index} | `{family['name']}` | {family['score']}/100 | {first_low_ticket} | {family['confidence_band']} |"
        )

    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "- Treat the table above as raw opportunity pressure, not an automatic sprint selector.",
            "- The active-sprint override stays with `Client Portal & Service Delivery OS` until `The Good Parts of SuiteDash` either ships or is formally deprioritized.",
            "- Use the next-ranked families to seed backlog and proof work, not to fragment the main sprint.",
            "",
            "## Rubric",
            "",
            "| Dimension | Max |",
            "|---|---:|",
        ]
    )

    for key, max_score in RUBRIC.items():
        lines.append(f"| `{key}` | {max_score} |")

    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Score workflow product families and emit reports.")
    parser.add_argument("--stdout", action="store_true", help="Print markdown report to stdout.")
    args = parser.parse_args()

    config = load_registry()
    scored = score_families(config)
    REPORTS_ROOT.mkdir(parents=True, exist_ok=True)

    markdown = render_markdown(scored)
    json_payload = {
        "generated_at": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "recommended_now": {
            "family_slug": ACTIVE_SPRINT_OVERRIDE,
            "anchor_product": ACTIVE_SPRINT_PRODUCT,
        },
        "rubric": RUBRIC,
        "families": scored,
    }

    MARKDOWN_REPORT.write_text(markdown, encoding="utf-8")
    JSON_REPORT.write_text(json.dumps(json_payload, indent=2), encoding="utf-8")

    if args.stdout:
        print(markdown)

    log(f"[green]Wrote[/green] {MARKDOWN_REPORT.relative_to(FACTORY_ROOT.parent)}" if console else f"Wrote {MARKDOWN_REPORT.relative_to(FACTORY_ROOT.parent)}")
    log(f"[green]Wrote[/green] {JSON_REPORT.relative_to(FACTORY_ROOT.parent)}" if console else f"Wrote {JSON_REPORT.relative_to(FACTORY_ROOT.parent)}")


if __name__ == "__main__":
    try:
        main()
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)
