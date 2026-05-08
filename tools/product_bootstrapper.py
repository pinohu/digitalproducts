#!/usr/bin/env python3
"""
product_bootstrapper.py — Scaffold a new product folder following the
                          standard repo structure.

Creates:
  03-products/<slug>/{manuscript,assets,bonuses,deliverables}/
  03-products/<slug>/README.md
  01-market-research/by-product/<slug>/validation.md (stub)
  02-offers/by-product/<slug>.md (stub)
  04-sales-pages/by-product/<slug>.md (stub)
  05-email-workflows/by-product/<slug>/ (stub README)
  06-launch-playbooks/by-product/<slug>.md (stub)
  analytics/by-product/<slug>.md (stub)

Usage:
    python product_bootstrapper.py --slug 02-newsletter-monetization \\
        --title "Newsletter Monetization Playbook" \\
        --price 49 \\
        --avatar "Solo creators with 1K-10K newsletter subscribers"
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

import yaml

try:  # pragma: no cover
    from rich.console import Console
    from rich.prompt import Confirm
except ImportError:  # pragma: no cover
    class Console:  # type: ignore
        def print(self, *args, **kwargs):
            print(*args)

    class Confirm:  # type: ignore
        @staticmethod
        def ask(*a, **k):
            return True


REPO_ROOT = Path(__file__).resolve().parent.parent
TOOLS_ROOT = Path(__file__).resolve().parent
CONFIG_PATH = TOOLS_ROOT / "config.yaml"

console = Console()


SLUG_RE = re.compile(r"^\d{2}-[a-z0-9]+(?:-[a-z0-9]+)*$")


def validate_slug(slug: str) -> bool:
    return bool(SLUG_RE.match(slug))


def load_config() -> dict:
    if not CONFIG_PATH.exists():
        return {
            "product_bootstrap": {
                "product_subfolders": ["manuscript", "assets", "bonuses", "deliverables"],
                "per_product_files": [
                    "01-market-research/by-product/{slug}/validation.md",
                    "02-offers/by-product/{slug}.md",
                    "04-sales-pages/by-product/{slug}.md",
                    "05-email-workflows/by-product/{slug}/",
                    "06-launch-playbooks/by-product/{slug}.md",
                    "analytics/by-product/{slug}.md",
                ],
            }
        }
    with CONFIG_PATH.open() as f:
        return yaml.safe_load(f)


def render_product_readme(slug: str, title: str, price: int, avatar: str) -> str:
    today = dt.date.today().isoformat()
    return f"""# Product — {title}

> *Status:* **Reserved** — sprint not yet started
> *Slug:* `{slug}`
> *Price:* ${price} (default trust tripwire)
> *Created:* {today}

## One-Sentence Pitch

> *I help [{avatar}] solve [problem] without [common objection].*
> _(refine after running validation worksheet)_

## The Avatar

{avatar}

## Why This Product

_(Fill in once validation worksheet is complete)_

## File Structure

| Folder | What Goes Here |
|---|---|
| `manuscript/` | Outline, drafts, final manuscript. |
| `assets/` | Cover art (1280x720), hero, social card. |
| `bonuses/` | Bonus deliverables. |
| `deliverables/` | Final files ready for Gumroad upload. |

## Definition of Done Checklist

- [ ] Validation worksheet complete (`/01-market-research/by-product/{slug}/validation.md`)
- [ ] Offer brief complete (`/02-offers/by-product/{slug}.md`)
- [ ] Manuscript final, proofread
- [ ] Cover art designed
- [ ] All bonuses created and packaged
- [ ] Sales page live (`/04-sales-pages/by-product/{slug}.md`)
- [ ] Money-back guarantee on sales page
- [ ] Post-purchase email workflow live in Gumroad
- [ ] At least 3 testimonials from beta readers
- [ ] Abandoned cart workflow enabled
- [ ] Linked from at least one ikeohu.com essay
- [ ] First sale recorded
- [ ] Entry added to ROADMAP.md Shipped Catalog

## Related Files

- Validation: `/01-market-research/by-product/{slug}/validation.md`
- Offer: `/02-offers/by-product/{slug}.md`
- Sales page: `/04-sales-pages/by-product/{slug}.md`
- Email workflow: `/05-email-workflows/by-product/{slug}/`
- Launch playbook: `/06-launch-playbooks/by-product/{slug}.md`
- Analytics: `/analytics/by-product/{slug}.md`
"""


def render_validation_stub(slug: str, title: str, avatar: str) -> str:
    return f"""# Validation — {title}

> *Status:* **In progress**
> *Started:* {dt.date.today().isoformat()}

## Product Working Title
{title}

## Product Slug
{slug}

## One-Sentence Pitch
> *I help {avatar} solve [problem] without [objection].*

## The Avatar

| Attribute | Detail |
|---|---|
| Job title or role | {avatar} |
| Annual revenue / income range | _TBD_ |
| Years of experience | _TBD_ |
| Tools they already use | _TBD_ |
| #1 frustration in this domain | _TBD_ |
| #2 frustration | _TBD_ |
| #3 frustration | _TBD_ |

## The Problem

**Painful version (their words):**
> _TBD_

**Structural version:**
> _TBD_

**What they've tried:**
1.
2.
3.

## The Outcome

**30 days after they finish:**
> _TBD_

**Quantifiable improvement:**
> _TBD_

## Starving Crowd Check

| Criterion | Pass / Fail | Evidence |
|---|---|---|
| Massive pain | | |
| Purchasing power | | |
| Easy to target | | |
| Growing market | | |

## Pre-Sale Validation Plan

- [ ] Audience post / poll
- [ ] Email to existing list
- [ ] Landing page with notify-me / pre-order button
- [ ] Direct outreach to 20 ideal-fit prospects
- [ ] Beta cohort offer (50% off in exchange for testimonial)

## Decision

- [ ] Proceed to offer construction
- [ ] Refine and re-validate
- [ ] Kill — reason:

---
_Use the full template at `/01-market-research/niche-validation-template.md` for guidance._
"""


def render_offer_stub(slug: str, title: str, price: int) -> str:
    return f"""# Offer Brief — {title}

> *Status:* **Pending**
> *Slug:* {slug}
> *Target price:* ${price}

## The Core
_TBD_

## The Avatar
_(pull from validation worksheet)_

## The Promise
> *_TBD_*

## The Pricing
- Founding price: ${price}
- Public price: $TBD
- Why this price: _TBD_

## The Value Equation
- Dream Outcome: ?/10
- Perceived Likelihood: ?/10
- Time Delay (lower = better): ?/10
- Effort (lower = better): ?/10

## The Bonus Stack
| # | Bonus | Objection Addressed | Standalone Value | Deliverable |
|---|---|---|---|---|
| 1 | | | $ | |
| 2 | | | $ | |
| 3 | | | $ | |

**Stack value:** $TBD
**Stack-to-price ratio:** TBDx (target: 10x+)

## The Guarantee
_(pull from `/02-offers/guarantee-templates.md`)_

## The Urgency
_TBD_

## The Final Offer Statement
_TBD_

---
_Use the full template at `/02-offers/grand-slam-offer-template.md`. Use `dynasty-offer-engineer` Claude skill to draft._
"""


def render_sales_page_stub(slug: str, title: str) -> str:
    return f"""# Sales Page — {title}

> *Status:* **Pending**
> *Slug:* {slug}

<!-- Section 1: Headline -->
# [Headline TBD]

<!-- Section 2: Sub-Headline -->
> *[Sub-headline TBD]*

<!-- Section 3: Pain Agitation -->
[TBD]

<!-- Section 4: Promise / Transformation -->
[TBD]

<!-- Section 5: Authority / Credibility -->
[TBD]

<!-- Section 6: What's Inside -->
[TBD]

<!-- Section 7: Bonus Stack -->
[TBD]

<!-- Section 8: Risk Reversal / Guarantee -->
> [Guarantee TBD]

<!-- Section 9: Social Proof -->
[Pending — collect from beta readers]

<!-- Section 10: Pricing -->
[TBD]

<!-- Section 11: FAQ -->
[TBD]

<!-- Section 12: Final CTA + Urgency -->
[TBD]

---
_Use full structure at `/04-sales-pages/sales-page-structure.md`. Use `dynasty-sales-page-writer` Claude skill to draft from offer brief._
"""


def render_email_workflow_stub(slug: str, title: str) -> str:
    return f"""# Email Workflows — {title}

> *Status:* **Pending**
> *Slug:* {slug}

## Required Workflows

- [ ] Post-purchase sequence (6 emails: 0hr, day 1, 3, 7, 14, 30)
- [ ] Launch sequence (7-8 emails over the launch window)
- [ ] Abandoned cart (Gumroad native)
- [ ] Waitlist sequence (if pre-launch)

## Drafting

For each workflow, customize the templates from:
- `/05-email-workflows/post-purchase-sequence.md`
- `/05-email-workflows/launch-sequence.md`
- `/05-email-workflows/waitlist-sequence.md`
- `/05-email-workflows/abandoned-cart.md`

Save customized versions in this folder as separate files:
- `post-purchase-sequence.md`
- `launch-sequence.md`
- `waitlist-sequence.md`
- `abandoned-cart.md`

Then implement in Gumroad Workflows (or graduate platform).
"""


def render_launch_stub(slug: str, title: str) -> str:
    return f"""# Launch Playbook — {title}

> *Status:* **Pending**
> *Slug:* {slug}

## Launch Dates (TBD)

- Day -7 (tease starts): _TBD_
- Day 0 (launch): _TBD_, 9:00 AM EST
- Day 6 (last call): _TBD_, midnight EST

## Customizations from Default Template

_(Use `/06-launch-playbooks/14-day-launch-template.md` as base. Note any product-specific deviations here.)_

## Beta Tester Recruitment

- [ ] List of 10-20 ideal beta candidates identified
- [ ] Outreach sent
- [ ] First 3 commitments received

## Launch Day Notes

_(Filled in on Day 0)_
"""


def render_analytics_stub(slug: str, title: str) -> str:
    return f"""# Analytics — {title}

> *Status:* **Pending — populate after launch**
> *Slug:* {slug}

## Cumulative Metrics

| Metric | Day 7 | Day 30 | Day 90 | Cumulative |
|---|---|---|---|---|
| Total sales | | | | |
| Total revenue | | | | |
| Refunds | | | | |
| Net revenue | | | | |
| Sales page conversion | | | | |
| AOV | | | | |

## Channel Breakdown

| Channel | Sales | Revenue |
|---|---|---|
| Email list (launch) | | |
| Social (LinkedIn) | | |
| Social (X) | | |
| Affiliate | | |
| Organic search | | |
| Direct | | |

## Reviews

- 7-day review: `/10-execution-sprints/completed-sprints/[date]-{slug}-7day-review.md`
- 30-day review: `/10-execution-sprints/completed-sprints/[date]-{slug}-30day-review.md`
- 90-day review: `/10-execution-sprints/completed-sprints/[date]-{slug}-90day-review.md`
"""


def create_file_safe(path: Path, content: str, dry_run: bool) -> bool:
    """Create a file. Returns True if created, False if it already existed."""
    if path.exists():
        return False
    if dry_run:
        console.print(f"  [dim](would create) {path.relative_to(REPO_ROOT)}[/dim]")
        return True
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    console.print(f"  [green]✓[/green] {path.relative_to(REPO_ROOT)}")
    return True


def create_dir_safe(path: Path, dry_run: bool) -> None:
    if path.exists():
        return
    if dry_run:
        console.print(f"  [dim](would mkdir) {path.relative_to(REPO_ROOT)}/[/dim]")
        return
    path.mkdir(parents=True, exist_ok=True)
    (path / ".gitkeep").write_text("", encoding="utf-8")
    console.print(f"  [green]✓[/green] {path.relative_to(REPO_ROOT)}/")


def main() -> None:
    parser = argparse.ArgumentParser(description="Bootstrap a new product folder.")
    parser.add_argument("--slug", required=True, help="NN-kebab-case-slug (e.g. 02-newsletter-monetization)")
    parser.add_argument("--title", required=True, help="Display title for the product")
    parser.add_argument("--price", type=int, default=49, help="Default price (USD)")
    parser.add_argument("--avatar", default="[avatar TBD]", help="One-line avatar description")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be created without writing")
    parser.add_argument("--yes", action="store_true", help="Skip confirmation")
    args = parser.parse_args()

    if not validate_slug(args.slug):
        console.print(
            f"[red]Invalid slug: '{args.slug}'[/red]\n"
            "Must match pattern NN-kebab-case (e.g. '02-newsletter-monetization')"
        )
        sys.exit(1)

    config = load_config()
    pb = config["product_bootstrap"]

    console.print(f"\n[bold]Bootstrapping product:[/bold] {args.title}")
    console.print(f"[bold]Slug:[/bold] {args.slug}")
    console.print(f"[bold]Price:[/bold] ${args.price}")
    console.print(f"[bold]Avatar:[/bold] {args.avatar}\n")

    if not args.yes and not args.dry_run:
        if not Confirm.ask("Proceed with creating files?", default=True):
            console.print("[yellow]Cancelled.[/yellow]")
            return

    # Product folder
    product_root = REPO_ROOT / "03-products" / args.slug
    create_dir_safe(product_root, args.dry_run)
    for sub in pb["product_subfolders"]:
        create_dir_safe(product_root / sub, args.dry_run)
    create_file_safe(
        product_root / "README.md",
        render_product_readme(args.slug, args.title, args.price, args.avatar),
        args.dry_run,
    )

    # Per-product files in other stage folders
    file_renderers = {
        f"01-market-research/by-product/{args.slug}/validation.md": render_validation_stub(
            args.slug, args.title, args.avatar
        ),
        f"02-offers/by-product/{args.slug}.md": render_offer_stub(
            args.slug, args.title, args.price
        ),
        f"04-sales-pages/by-product/{args.slug}.md": render_sales_page_stub(
            args.slug, args.title
        ),
        f"05-email-workflows/by-product/{args.slug}/README.md": render_email_workflow_stub(
            args.slug, args.title
        ),
        f"06-launch-playbooks/by-product/{args.slug}.md": render_launch_stub(
            args.slug, args.title
        ),
        f"analytics/by-product/{args.slug}.md": render_analytics_stub(
            args.slug, args.title
        ),
    }

    for rel_path, content in file_renderers.items():
        full_path = REPO_ROOT / rel_path
        create_file_safe(full_path, content, args.dry_run)

    # Reconcile against config['product_bootstrap']['per_product_files'] so that
    # any path declared in config but missed above still gets created (with a
    # generic stub for files, or as a directory with .gitkeep for trailing-/).
    expected = pb.get("per_product_files", [])
    rendered_paths = {p.format(slug=args.slug) for p in expected}
    rendered_paths_resolved = set(file_renderers.keys())
    for tmpl in expected:
        rel = tmpl.format(slug=args.slug)
        if rel.endswith("/"):
            create_dir_safe(REPO_ROOT / rel.rstrip("/"), args.dry_run)
            continue
        if rel in rendered_paths_resolved:
            continue
        # Unknown file path declared in config — generate a generic stub.
        create_file_safe(
            REPO_ROOT / rel,
            f"# {args.title}\n\n> *Stub generated by product_bootstrapper.py*\n",
            args.dry_run,
        )

    console.print(
        "\n[bold green]Bootstrap complete.[/bold green]\n"
        f"\nNext steps:\n"
        f"  1. Open `01-market-research/by-product/{args.slug}/validation.md` and complete the worksheet.\n"
        f"  2. Once validation passes, use `dynasty-offer-engineer` Claude skill to draft the offer brief.\n"
        f"  3. Update `ROADMAP.md` with this product in the appropriate slot.\n"
        f"  4. When sprint slot opens, copy the 14-day sprint template to `current-sprint.md`.\n"
    )


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[yellow]Cancelled.[/yellow]")
        sys.exit(0)
