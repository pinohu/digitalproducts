# Digital Products Operating System

> The end-to-end machinery for taking a digital product from *"there might be an idea here"* to *"$X in revenue and a buyer cohort I can sell to again."* Framework + templates + automation.

This repo is the operating system for **any digital product**, not just one. It's the home base for:

- **Idea discovery** — automated mining of pain points, trends, and gaps to surface validated niches
- **Validation** — pre-sale, waitlist, beta cohort patterns that filter ideas before any build
- **Offer engineering** — Hormozi Grand Slam Offer construction, Value Equation math, bonus stacks
- **Product builds** — per-product folders with manuscript, assets, bonuses, deliverables
- **Sales pages** — the 12-section structure that converts on every product
- **Email workflows** — post-purchase, launch, waitlist, abandoned cart, nurture sequences
- **Launch playbooks** — 14-day launch sequences, pre/launch-day/post checklists
- **Traffic** — content calendars, platform strategy, lead magnets
- **Iteration & scale** — bundles, variations, catalog roadmap, affiliate programs
- **Automation** — Claude skills, n8n workflows, Python tools, Flint VM delegation
- **Analytics** — revenue, conversion, per-product performance

The framework is documented in [`FRAMEWORK.md`](./FRAMEWORK.md) — start there.

> **Primary deployment:** Dynasty Empire portfolio (PNR Holdings LLC). The system is portable, but Dynasty Empire is its first user. Active sprint: **The Good Parts of SuiteDash** ($49 trust tripwire, target ship 2026-05-20).

---

## What Lives Where

| Folder | Stage | Purpose |
|---|---|---|
| [`00-foundation/`](./00-foundation/) | Pre-stage | Brand positioning, audience profile, value ladder, pricing philosophy |
| [`01-market-research/`](./01-market-research/) | **Stage 1** | **Idea discovery + market validation.** Includes the [`idea-discovery/`](./01-market-research/idea-discovery/) automation layer |
| [`02-offers/`](./02-offers/) | Stage 2 | Grand Slam Offer construction, Value Equation, bonus stacks, guarantees |
| [`03-products/`](./03-products/) | Stage 3 | Actual product builds. One folder per product |
| [`04-sales-pages/`](./04-sales-pages/) | Stage 8 | The 12-section sales page structure + headline formulas |
| [`05-email-workflows/`](./05-email-workflows/) | Stage 9 | Post-purchase, waitlist, launch, abandoned cart, nurture sequences |
| [`06-launch-playbooks/`](./06-launch-playbooks/) | Stage 9 | 14-day launch template + checklists |
| [`07-traffic-engine/`](./07-traffic-engine/) | Stage 7 | Platform strategy, content calendar, lead magnets, newsletter, LinkedIn |
| [`08-platforms/`](./08-platforms/) | Stage 6 | Gumroad setup, alternatives, full tech stack reference |
| [`09-iteration-and-scale/`](./09-iteration-and-scale/) | Stage 10 | Bundles, variations, catalog roadmap, affiliate program, 90-day reviews |
| [`10-execution-sprints/`](./10-execution-sprints/) | Operations | 14-day sprint template + active sprint document |
| [`automation/`](./automation/) | **Cross-cutting** | **Claude skills, n8n workflows, Flint delegation, prompt library** |
| [`tools/`](./tools/) | **Cross-cutting** | **Python scripts: idea scorer, Reddit miner, trends checker, product bootstrapper** |
| [`shared-assets/`](./shared-assets/) | Cross-cutting | Swipe files, testimonial bank, headlines, stock bonuses, brand elements |
| [`analytics/`](./analytics/) | Cross-cutting | Revenue and conversion tracking |

(Folder numbers reflect ordering for navigation, not 1-to-1 with the framework's stage numbers — the framework has 10 stages, this repo has 11 numbered folders to match how work actually flows.)

## Start Here

1. **Read [`FRAMEWORK.md`](./FRAMEWORK.md)** — the canonical 10-stage operating system.
2. **Read [`ROADMAP.md`](./ROADMAP.md)** — the idea backlog, active sprint, shipped catalog.
3. **Read [`automation/pipeline.md`](./automation/pipeline.md)** — how the automation stack ties stages together.
4. **Open [`10-execution-sprints/current-sprint.md`](./10-execution-sprints/current-sprint.md)** — the live sprint document.

## The Automation Stack

The repo is structured so that any stage can be run **manually** (using templates as worksheets) **or via automation** (Claude skills, n8n workflows, Python tools).

```
Idea Discovery (automated)
  ├── Reddit / X / forum mining via tools/reddit_miner.py
  ├── Google Trends via tools/trends_checker.py
  ├── Scoring via tools/idea_scorer.py + scoring-rubric.md
  └── Output: idea backlog (01-market-research/idea-discovery/idea-backlog.md)
        ↓
Validation (semi-automated)
  ├── Validation worksheet (filled in by Claude or operator)
  ├── Pre-sale landing page (deployed via Vercel)
  └── Waitlist capture via Gumroad subscribe form
        ↓
Offer Engineering (Claude-assisted)
  ├── automation/claude-skills/offer-engineer.md
  ├── 02-offers/grand-slam-offer-template.md
  └── Output: per-product offer brief
        ↓
Product Build (manual + scaffolding)
  ├── tools/product_bootstrapper.py creates folder structure
  ├── 03-products/<slug>/manuscript/ filled in
  └── Bonuses produced
        ↓
Sales Page (Claude-assisted)
  ├── automation/claude-skills/sales-page-writer.md
  └── 04-sales-pages/by-product/<slug>.md
        ↓
Launch (n8n-orchestrated)
  ├── automation/n8n-workflows/launch-automation.md
  ├── 06-launch-playbooks/14-day-launch-template.md
  └── Email sequences fire from Gumroad Workflows
        ↓
Iteration (Claude-assisted)
  ├── automation/claude-skills/launch-manager.md
  ├── 09-iteration-and-scale/90-day-review-template.md
  └── Buyer feedback → next product idea (loops to top)
```

## Operating Principles

- **Ship over polish.** 14-day timebox per product. v1.0 ugly beats v2.0 unreleased.
- **Audience first.** Every product is sold to the email list before strangers.
- **Price for value, not effort.** $49 trust tripwire default; ladder up.
- **Risk reversal always.** Money-back guarantee on every product.
- **One outcome per product.** Hormozi's rule: one problem, one promise.
- **Automation everywhere it pays for itself.** Manual when it's faster; scripted when it repeats.
- **Workflow on day zero.** Every product ships with the post-purchase email sequence already live.

## Tech Stack (Default)

- **Storefront:** Gumroad (primary), Vercel + Stripe (graduate path)
- **Email:** Gumroad Workflows → Beehiiv as the list scales
- **Authority site:** ikeohu.com (six-lane authority strategy)
- **Backend / data:** Neon Postgres
- **Automation:** n8n at `n8n.audreysplace.place`
- **AI agents:** Claude (this) + Flint VM bridge (`claude-inbox/outbox.audreysplace.place`)
- **Auth / membership (graduate):** SuiteDash

## Conventions

- **Numbered folders for ordering.** `00-` through `10-` reflect work sequence. Don't renumber.
- **Per-product folders use ordinal-prefix-slug.** `01-suitedash-good-parts/`, `02-...`, etc.
- **README.md in every folder** explains what goes there.
- **Templates live at the folder root. Per-product instances live in `by-product/<slug>/`.**
- **Automation scripts in `tools/`. Workflow specs in `automation/n8n-workflows/`. Claude skills in `automation/claude-skills/`.**

## Status

| | |
|---|---|
| Repo created | 2026-05-06 |
| Framework version | v1.0 |
| Active sprint | The Good Parts of SuiteDash (content complete; pre-launch packaging + distribution setup in progress) |
| Last update | 2026-05-08 — channel-mix audit completed; LinkedIn demoted from primary to secondary for this product (see [`/01-market-research/by-product/01-suitedash-good-parts/distribution-findings.md`](./01-market-research/by-product/01-suitedash-good-parts/distribution-findings.md)). 7 new files added: distribution findings, watering-holes addendum, YouTube comments playbook, G2/Capterra Q&A playbook, YouTube comment scaffolds, comparison-content affiliate pitch, Upwork productized listing. |
| Idea backlog size | TBD — first mining pass pending |
| Products live | 0 |
| Products shipped (cumulative) | 0 |
