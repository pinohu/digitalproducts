# Roadmap

The single source of truth for what's being worked on, what's queued, and what's already shipped.

---

## Active Sprint

| Product | Slug | Price | Status | Sprint Dates |
|---|---|---|---|---|
| The Good Parts of SuiteDash | `01-suitedash-good-parts` | $49 | **Content complete — Day 11 of 14, pre-launch window** | 2026-05-06 → 2026-05-20 |

**Live document:** [`10-execution-sprints/current-sprint.md`](./10-execution-sprints/current-sprint.md)

---

## Idea Backlog

The list of validated and partially-validated ideas waiting for a sprint slot. Sourced from automated mining, audience replies, competitor gaps, and lateral expansion of existing products.

**Populated by:** [`01-market-research/idea-discovery/idea-backlog.md`](./01-market-research/idea-discovery/idea-backlog.md)

| Slot | Status | Notes |
|---|---|---|
| Active Sprint | Filled | The Good Parts of SuiteDash |
| Next sprint candidate | TBD | Selected from backlog after current sprint ships + 7-day review |
| Backlog | Open | Pending first idea mining pass |

The backlog is intentionally living. New ideas enter via `tools/idea_scorer.py` and the mining prompts in `01-market-research/idea-discovery/mining-prompts/`. Ideas exit when they get promoted to a sprint, get killed (with reason logged), or sit at <25/50 score for 90+ days (auto-archived).

---

## Shipped Catalog

| # | Product | Slug | Launch Date | Price | Total Sales | Status |
|---|---|---|---|---|---|---|
| _none yet_ | | | | | | |

When the first product ships, this table becomes the canonical view of the catalog. Bundle entries appear here too once 3+ products are live.

---

## Catalog Strategy (12-Month View)

```
Months 1-3:    1-2 products live (validate avatar, price point, funnel)
Months 4-6:    3-5 products live + first bundle
Months 7-9:    Variations of best-performing products
Months 10-12:  Premium tier ($297+) + DWY service ($997+)
```

This is the realistic pace for a solo creator. See [`09-iteration-and-scale/catalog-roadmap.md`](./09-iteration-and-scale/catalog-roadmap.md) for the full plan.

---

## Definition of Done (Per Product)

A product is not "shipped" until **all** of these are true:

- [ ] PDF / deliverable finalized and uploaded to Gumroad
- [ ] Sales page published with all 12 sections
- [ ] At least one bonus stacked into the offer
- [ ] Money-back guarantee stated
- [ ] Post-purchase email workflow live (0hr / day 1 / day 3 / day 7 / day 14 / day 30)
- [ ] At least 3 testimonials from beta readers embedded
- [ ] Abandoned cart workflow enabled
- [ ] Listed on the storefront and in the sitemap
- [ ] Linked from at least one ikeohu.com essay
- [ ] First sale recorded
- [ ] Entry added to the Shipped Catalog table above

---

## Status Updates

| Date | Update |
|---|---|
| 2026-05-06 | Repo scaffolded with full framework + automation layer. Sprint 1 initiated for SuiteDash Good Parts. Idea discovery system designed; first mining pass pending. |
| 2026-05-06 | Sprint 1 content pass complete: validation, offer, manuscript (4,250 words / 8 chapters), 3 bonuses, 12-section sales page, 6-email post-purchase sequence, 14-day launch playbook, KPI tracker. Tools hardened (54 tests passing, unified `dpops.py` CLI). All 4 n8n workflows exported as importable JSON. Remaining: cover art, PDF export, beta testimonials, Gumroad upload, launch. |
