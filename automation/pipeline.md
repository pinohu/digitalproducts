# Pipeline

The end-to-end automation pipeline. From "we don't have an idea" to "first sale recorded" — and what's automated at each step.

## The Full Pipeline

```
┌────────────────────────────────────────────────────────────────────┐
│  STAGE 1 — IDEA DISCOVERY                                          │
│  Cadence: Daily/weekly mining                                      │
│  Trigger: Cron (n8n) or manual (Python)                            │
│                                                                    │
│  Inputs: Reddit, X, LinkedIn, audience replies, Gumroad,           │
│          Google Trends                                             │
│                                                                    │
│  Tools:                                                            │
│  - tools/reddit_miner.py (PRAW-based subreddit scan)               │
│  - tools/trends_checker.py (pytrends-based)                        │
│  - automation/n8n-workflows/idea-discovery-pipeline.md             │
│  - automation/claude-skills/idea-validator.md                      │
│  - 01-market-research/idea-discovery/mining-prompts/*.md           │
│                                                                    │
│  Output: New entries in 01-market-research/idea-discovery/         │
│          idea-backlog.md, scored against the 50-point rubric       │
└────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌────────────────────────────────────────────────────────────────────┐
│  STAGE 2 — VALIDATION (when sprint slot opens)                     │
│  Cadence: Once per sprint kickoff (~ every 14 days)                │
│  Trigger: Manual (operator picks top backlog idea)                 │
│                                                                    │
│  Tools:                                                            │
│  - 01-market-research/niche-validation-template.md                 │
│  - 01-market-research/competitor-analysis-template.md              │
│  - automation/claude-skills/idea-validator.md                      │
│  - tools/product_bootstrapper.py (creates folder skeleton)         │
│                                                                    │
│  Output:                                                           │
│  - 01-market-research/by-product/<slug>/validation.md (filled in)  │
│  - 03-products/<NN>-<slug>/ (folder scaffold)                      │
│  - Pre-sale landing page on Vercel (if validation passes)          │
└────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌────────────────────────────────────────────────────────────────────┐
│  STAGE 3 — OFFER ENGINEERING                                       │
│  Cadence: Days 1-3 of sprint                                       │
│  Trigger: Manual                                                   │
│                                                                    │
│  Tools:                                                            │
│  - automation/claude-skills/offer-engineer.md                      │
│  - 02-offers/grand-slam-offer-template.md                          │
│  - 02-offers/value-equation-worksheet.md                           │
│  - 02-offers/bonus-stack-template.md                               │
│  - 02-offers/guarantee-templates.md                                │
│                                                                    │
│  Output: 02-offers/by-product/<slug>.md with full offer brief      │
└────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌────────────────────────────────────────────────────────────────────┐
│  STAGE 4 — PRODUCT BUILD                                           │
│  Cadence: Days 4-9 of sprint                                       │
│  Trigger: Manual + Claude-assisted                                 │
│                                                                    │
│  Tools:                                                            │
│  - 03-products/<slug>/manuscript/ (drafting)                       │
│  - 03-products/<slug>/bonuses/ (bonus production)                  │
│  - Claude-assisted writing (no formal skill — direct prompting)    │
│  - Canva / design tools for cover art                              │
│                                                                    │
│  Output: Final PDF + bonuses in 03-products/<slug>/deliverables/   │
└────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌────────────────────────────────────────────────────────────────────┐
│  STAGE 5 — SALES PAGE                                              │
│  Cadence: Day 10 of sprint                                         │
│  Trigger: Manual + Claude-assisted                                 │
│                                                                    │
│  Tools:                                                            │
│  - automation/claude-skills/sales-page-writer.md                   │
│  - 04-sales-pages/sales-page-structure.md (12-section)             │
│  - 04-sales-pages/headline-formulas.md                             │
│  - shared-assets/testimonial-bank/ (pull testimonials)             │
│                                                                    │
│  Output:                                                           │
│  - 04-sales-pages/by-product/<slug>.md (draft)                     │
│  - Live page deployed to Vercel or Gumroad product description     │
└────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌────────────────────────────────────────────────────────────────────┐
│  STAGE 6 — EMAIL WORKFLOWS                                         │
│  Cadence: Day 11 of sprint                                         │
│  Trigger: Manual setup, then automatic on customer events          │
│                                                                    │
│  Tools:                                                            │
│  - 05-email-workflows/post-purchase-sequence.md (template)         │
│  - 05-email-workflows/launch-sequence.md (template)                │
│  - 05-email-workflows/abandoned-cart.md (template)                 │
│  - automation/n8n-workflows/post-purchase-automation.md            │
│    (alternative: native Gumroad Workflows)                         │
│                                                                    │
│  Output: 6-email post-purchase workflow live in Gumroad,           │
│          7-email launch workflow queued                            │
└────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌────────────────────────────────────────────────────────────────────┐
│  STAGE 7 — LAUNCH                                                  │
│  Cadence: Days 12-14 of sprint                                     │
│  Trigger: Day 14 launch event                                      │
│                                                                    │
│  Tools:                                                            │
│  - 06-launch-playbooks/14-day-launch-template.md                   │
│  - 06-launch-playbooks/launch-day-checklist.md                     │
│  - automation/n8n-workflows/launch-automation.md                   │
│    (scheduled email + social posting)                              │
│  - automation/claude-skills/launch-manager.md                      │
│                                                                    │
│  Output: Product live, founding-price window active,               │
│          first-day sales recorded                                  │
└────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌────────────────────────────────────────────────────────────────────┐
│  STAGE 8 — POST-LAUNCH ITERATION                                   │
│  Cadence: Day 7, Day 30, Day 90 after launch                       │
│  Trigger: Calendar reminder (n8n)                                  │
│                                                                    │
│  Tools:                                                            │
│  - 06-launch-playbooks/post-launch-iteration.md                    │
│  - 09-iteration-and-scale/90-day-review-template.md                │
│  - automation/n8n-workflows/analytics-aggregation.md               │
│  - automation/claude-skills/launch-manager.md                      │
│                                                                    │
│  Output:                                                           │
│  - Reviews saved to 10-execution-sprints/completed-sprints/        │
│  - Updated entries in analytics/                                   │
│  - New idea seeds appended to idea-backlog.md (closes the loop)    │
└────────────────────────────────────────────────────────────────────┘
                                │
                                └─────► (Loops back to Stage 1)
```

## Paperclip Operating Cadence

Paperclip is the coordination layer for executing this pipeline without relying on ad hoc memory.

| Cadence | Owner | Required action |
|---|---|---|
| Daily heartbeat | Chief of Staff | List assigned issues, pick the highest-priority actionable item, and update repo docs when product status changes. |
| Sprint dependency gate | Chief of Staff + specialist owners | Confirm upstream artifacts exist before downstream work hardens: validation → offer → product → funnel → launch. |
| Handoff completion | Specialist owner | Leave the deliverable in the repo path named in the issue, note blockers explicitly, and do not mark production work complete unless ROADMAP.md DoD allows it. |
| Foundation review | Chief of Staff | Keep DIG-7/DIG-8/DIG-9/DIG-10/DIG-11 aligned so automation, storefront, analytics, and n8n plans support the active sprint and the next one. |

Current Sprint 1 gates are tracked in `10-execution-sprints/current-sprint.md`; canonical production status remains in `ROADMAP.md`. DIG-59 resolved the DIG-53/DIG-54 productivity reviews as expected parent-orchestration activity: DIG-1 and DIG-2 stay in progress while the live launch is blocked, and they should not be closed or reframed as shipped until evidence satisfies the full Definition of Done. DIG-33's final shipped-gate DoD ledger is recorded at `06-launch-playbooks/by-product/01-suitedash-good-parts-dig33-shipped-gate.md` and currently blocks shipped/catalog closure until live Gumroad, workflow, storefront/linkage, proof, and first-sale evidence exist. DIG-61's AppSumo operator-input bundle is now the concise operator-return checklist at `01-market-research/appsumo/2026-05-08-operator-input-bundle.md`; DIG-65 reconciled its SuiteDash section with the safe portal-host evidence in `suitedash-access-completion-packet.md`, so operators should use the eight confirmed live SuiteDash portal auth hosts and treat Coadjutant/Dome Law/NAWA as repair or clean-network recheck items before supplying secure session or Public ID + Secret Key pairing. DIG-64 clarified CallScaler: secure dotenv key names exist, but both current keys return HTTP 401 on minimal safe reads, so CallScaler remains blocked pending verified/rotated API key or approved browser session and must not be promoted to n8n or scheduled probes. DIG-67 verified Formaloo as a guarded read-only forms/profile health surface with token minting plus GET-only summaries; scheduled n8n use still requires dedicated Formaloo automation credentials and operator review.

## Time Investment

For a single product, fully running this pipeline:

| Stage | Manual Time (hours) | With Automation (hours) | Savings |
|---|---|---|---|
| Idea discovery (per cycle) | 5–10 | 0.5 | 90%+ |
| Validation | 3 | 1.5 | 50% |
| Offer engineering | 4 | 1.5 | 60% |
| Product build | 30–80 | 25–60 | 20-25% (mostly creative work) |
| Sales page | 4–8 | 1–2 | 70-80% |
| Email workflows | 4 | 0.5 | 85% |
| Launch | 6 (over 14 days) | 2 (over 14 days) | 65% |
| Post-launch iteration | 3 | 0.5 | 80%+ |
| **Total per product** | **60–115 hours** | **32–69 hours** | **~45%** |

The big wins are upstream (idea discovery) and downstream (analytics + iteration). The middle (product build) is creative work that automation can assist but not replace.

## Paperclip Operating Tracks

Current production execution is managed through Paperclip issues, with Chief of Staff owning cross-track sequencing rather than doing every specialist task directly.

| Track | Paperclip issue(s) | Primary output | Gate / Production Requirement |
|---|---|---|---|
| Program orchestration | DIG-1, DIG-2, DIG-7, DIG-16, DIG-28, DIG-33 | Roadmap/sprint truth, dependency gates, handoffs, operator unblock packet, launch-readiness and shipped-gate closure | Always active; canonical docs must stay truthful; DIG-33 cannot close until full ROADMAP DoD + first sale evidence exist |
| SuiteDash validation | DIG-3 | Buyer/avatar, proof points, go/no-go recommendation | Gate A, Day 3; feeds offer and sales-page claims |
| Offer engineering | DIG-4 | Offer brief, pricing, bonus stack, guarantee | Gate A, Day 3; locks bonus and guarantee language |
| Product build | DIG-5, DIG-12, DIG-13, DIG-17 | Manuscript plan, full manuscript, bonus deliverables, exported PDFs, lightweight launch assets | Gate B, Day 8; source package can inform funnel work, but Gumroad upload stays blocked until DIG-17 output exists |
| Funnel and launch | DIG-6, DIG-15, DIG-22, DIG-23, DIG-29, DIG-30 | Sales page, email workflows, launch checklist, Gumroad/Vercel activation steps, live checkout, test purchase, enabled workflows | Gate C/D; DIG-22/DIG-23 are repo-side blocker handoffs; DIG-29/DIG-30 are blocked live-execution issues pending DIG-28 operator access/evidence and live product/download URL |
| Beta proof / testimonials | DIG-14, DIG-25, DIG-32 | Named proof, paid beta/pre-order signal, testimonial snippets | Gate C, Day 11-13; DIG-25 is repo-side outreach handoff; DIG-32 is blocked live outreach/proof execution and blocks ROADMAP testimonial DoD until real permissioned proof exists |
| Python tooling | DIG-8 | Runnable setup docs, env inventory, verification notes | Requires local dependency verification before scheduled automation is trusted |
| Storefront/platform readiness | DIG-9, DIG-24, DIG-31 | Gumroad, Vercel, Neon/n8n, `ikeohu.com`, and sitemap readiness checklist plus live storefront/linkage updates | DIG-24 is repo-side linkage handoff; DIG-31 is blocked live storefront/sitemap/owned-site execution requiring real external account access and live product URL |
| Analytics/review cadence | DIG-10 | First-launch KPIs, baseline tracking, and 7/30/90-day review locations | Requires live traffic/sales data before post-launch metrics are complete |
| n8n implementation planning | DIG-11 | `automation/n8n-workflows/implementation-plan.md` plus ordered idea-discovery, launch, post-purchase, and analytics workflow specs | Requires deployed n8n credentials and connected third-party accounts |
| AppSumo operator-input bundle | DIG-61, DIG-65 | `01-market-research/appsumo/2026-05-08-operator-input-bundle.md` | Operator must provide exact tenant URLs/sessions/context/client IDs/Public ID pairings/request codes through secure channels before further read-only checks; SuiteDash section must stay aligned to verified safe portal-host evidence; no writes authorized |

For sprint work, do not mark a stage complete just because an issue exists. A stage advances only when its repo-visible deliverable exists and the downstream gate can consume it. The MVP launch path still favors native Gumroad setup for Day 14; n8n becomes production-critical after the manual workflow has been proven once.

Sprint 1 current gate truth: SuiteDash is package-ready in the repo and has a live Vercel staging page, but it is not launched. The DIG-7 automation/platform foundation is repo-complete: local tools pass offline verification from `tools/.venv`, production readiness/storefront status docs exist, analytics baseline exists, and the n8n implementation plan is written. DIG-22/DIG-23/DIG-24/DIG-25 closed as truthful repo-side blocker handoffs, not live launch completion. DIG-28 was rechecked on 2026-05-08T02:15:49Z and remains unresolved: no Gumroad admin/session or live URLs, payout/tax/profile confirmation, support inbox, test-purchase method, final launch deadline, owned-site write/deploy access, approved outreach channel, permissioned proof, or first-sale evidence is available. The production-critical chain therefore stays blocked behind DIG-28, then DIG-29 live Gumroad/test purchase, DIG-30 live workflows/abandoned cart, DIG-31 live storefront/sitemap/`ikeohu.com` linkage, DIG-32 proof/testimonials, and DIG-33 first-sale/full-DoD closure.

## Setup Order (For Maximum Leverage Fastest)

If you're setting this up from scratch, prioritize in this order:

1. **Day 1: Python tools.** Create the `tools/.venv`, install `tools/requirements.txt`, run `python tools/verify_tools.py`, then smoke-test `tools/idea_scorer.py` and `tools/product_bootstrapper.py --dry-run`. Live Reddit/Trends checks require real Reddit credentials and network access.
2. **Day 2: Claude skills.** Install the offer-engineer and sales-page-writer skills. These get used on every product.
3. **Day 3: Gumroad Workflows.** Set up the post-purchase email workflow (native Gumroad, no n8n required for MVP).
4. **Week 2: First n8n workflow.** Build the idea-discovery scheduled mining flow. Routes Reddit scrape outputs into Claude → idea-backlog.md.
5. **Week 2.5: AppSumo read-only summary pack.** Import `appsumo-readonly-summary.draft.json` only as a disabled/manual draft, configure n8n credential records for Agiled/AITable/notifications, run `appsumo-readonly-summary.md` manually with `--summary-only`, review for PII leakage, then enable weekly Cron if safe.
6. **Week 3: Read-only ops connector.** Use `tools/appsumo_readonly_probe.py` and `automation/appsumo-readonly-connector-spikes.md` to promote verified Agiled and AITable GET pulls into n8n; load current secure credentials explicitly, keep summaries data-minimized, and treat any AITable 401 as credential-source drift until proven otherwise.
7. **Week 4: Launch automation n8n workflow.** Build the multi-email scheduled launch sequence.
8. **Week 5: Emailit read-only health check.** Use DIG-39's verified `emailit` probe resources for disabled/manual-first domains/events/templates summaries only; require a dedicated automation-owned Emailit credential before n8n scheduling, and do not add sends or contact/domain/template/webhook writes without a separate write contract.
9. **Week 5: Certopus read-only health check.** Use DIG-45/DIG-47's verified `certopus` probe resources and disabled/manual-first n8n pack for templates/organisations/wallet/SMTP metadata summaries only; require `CERTOPUS_API_KEY_AUTOMATION` before scheduling, and do not add certificate issuance, sends, downloads/exports, recipient, SMTP/domain/white-label, or wallet mutations without a separate write contract.
10. **Week 5+: Dadan limited recording-request detail check.** Use DIG-56's `dadan recording-request` probe only with an operator-approved request code created by the same `DADAN_API_KEY`; keep it manual-first and summary-only, and do not automate request creation, uploads, video sharing, webhooks, or raw submission/video exports without a separate write contract.
11. **Week 5+: Refine.** Build out the analytics aggregation and any other workflows as you find friction.

## What's Manual on Purpose

These steps stay manual because human judgment + creativity dominate the value:

- **Final scoring decisions** on edge-case ideas
- **Final product manuscript writing** (Claude can draft; human owns voice)
- **Final sales page polish** (especially headline + opening)
- **Founding-price launch announcement post** on social
- **Replies to customer questions** during launch
- **Choosing which idea to sprint next** from the backlog

Automating these would lower quality. Don't.
