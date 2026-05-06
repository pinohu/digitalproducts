# Digital Products Empire

The home base for every digital product shipped under the Dynasty Empire portfolio. Structured around a single 10-stage framework that runs from market validation through catalog expansion.

> **Operator:** Ike Ohu · **Holding:** PNR Holdings LLC · **Brand:** Dynasty Empire
> **Primary platform:** Gumroad · **Stack:** Vercel + Neon · **Default price tripwire:** $49

---

## What Lives Where

| Folder | Purpose |
|---|---|
| [`00-foundation/`](./00-foundation/) | Brand positioning, value ladder, audience profile, pricing philosophy. The strategic spine. |
| [`01-market-research/`](./01-market-research/) | Niche validation, starving-crowd checks, competitor analysis. Per-product research lives in `by-product/`. |
| [`02-offers/`](./02-offers/) | Grand Slam Offer templates, value equation worksheets, bonus stacks, guarantee language. |
| [`03-products/`](./03-products/) | The actual product builds. One folder per product. `01-suitedash-good-parts/` is the priority ship. |
| [`04-sales-pages/`](./04-sales-pages/) | The 12-section sales page structure, headline formulas, proven templates, per-product sales copy. |
| [`05-email-workflows/`](./05-email-workflows/) | Post-purchase sequences, waitlist sequences, launch sequences, abandoned cart, nurture flows. |
| [`06-launch-playbooks/`](./06-launch-playbooks/) | The 14-day launch template, pre-launch / launch-day / post-launch checklists. |
| [`07-traffic-engine/`](./07-traffic-engine/) | Content calendars, platform strategy, lead magnets, newsletter structure, LinkedIn playbook. |
| [`08-platforms/`](./08-platforms/) | Gumroad setup, Gumroad Workflows, Payhip / ThriveCart / Lemon Squeezy alternatives, full tech stack. |
| [`09-iteration-and-scale/`](./09-iteration-and-scale/) | Bundles, variations, catalog roadmap, affiliate program, 90-day post-launch reviews. |
| [`10-execution-sprints/`](./10-execution-sprints/) | The 14-day sprint template, the current active sprint, archive of completed sprints. |
| [`shared-assets/`](./shared-assets/) | Reusable swipe files, testimonial bank, headlines, stock bonuses, brand elements. |
| [`analytics/`](./analytics/) | Revenue and conversion tracking, per-product performance. |

## Start Here

1. Read [`FRAMEWORK.md`](./FRAMEWORK.md) — the 10-stage operating system this entire repo is organized around.
2. Read [`ROADMAP.md`](./ROADMAP.md) — the 7-PDF queue, current status of each, what ships first.
3. Open [`10-execution-sprints/current-sprint.md`](./10-execution-sprints/current-sprint.md) — the live 14-day sprint for the SuiteDash PDF.

## Operating Principles

- **Ship over polish.** 14-day timebox per product. v1.0 ugly beats v2.0 unreleased.
- **Audience first.** Every product is sold to the email list before strangers.
- **Price for value, not effort.** $49 trust tripwire, ladder up from there.
- **Risk reversal always.** Money-back guarantee on every product. Refund rate is almost always 2–5%; the conversion lift is 3–5x.
- **One outcome per product.** Hormozi's rule: one problem, one promise.
- **Bundle early.** Three PDFs at $49 each = $147 unbundled / $97 bundled. AOV always wins.
- **Workflow on day zero.** Every product ships with the post-purchase email sequence already live.

## Tech Stack (Default)

- **Storefront:** Gumroad (primary), Vercel + Stripe (graduate path)
- **Email:** Gumroad Workflows → ConvertKit/Beehiiv as the list scales
- **Authority site:** ikeohu.com (six-lane authority strategy)
- **Backend / data:** Neon Postgres
- **Automation:** n8n at `n8n.audreysplace.place`
- **Auth / membership (graduate):** SuiteDash

## Conventions

- **Numbered folders for ordering.** `00-` through `10-` reflect the framework stage order. Don't renumber.
- **Per-product folders use ordinal-prefix-slug.** `01-suitedash-good-parts/`, `02-...`, etc.
- **README.md in every folder** explains what goes there. If a folder feels empty, the README points at the templates that fill it.
- **Templates live at the folder root. Per-product instances live in `by-product/<slug>/`.**

## Status

| | |
|---|---|
| Repo created | 2026-05-06 |
| Framework version | v1.0 |
| Active sprint | SuiteDash Good Parts (Day 1 of 14) |
| Products live | 0 |
| Products in queue | 7 |
