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

## Setup Order (For Maximum Leverage Fastest)

If you're setting this up from scratch, prioritize in this order:

1. **Day 1: Python tools.** Get `tools/idea_scorer.py` and `tools/reddit_miner.py` running. This unlocks the highest-leverage automation (idea discovery) immediately.
2. **Day 2: Claude skills.** Install the offer-engineer and sales-page-writer skills. These get used on every product.
3. **Day 3: Gumroad Workflows.** Set up the post-purchase email workflow (native Gumroad, no n8n required for MVP).
4. **Week 2: First n8n workflow.** Build the idea-discovery scheduled mining flow. Routes Reddit scrape outputs into Claude → idea-backlog.md.
5. **Week 3: Launch automation n8n workflow.** Build the multi-email scheduled launch sequence.
6. **Week 4+: Refine.** Build out the analytics aggregation and any other workflows as you find friction.

## What's Manual on Purpose

These steps stay manual because human judgment + creativity dominate the value:

- **Final scoring decisions** on edge-case ideas
- **Final product manuscript writing** (Claude can draft; human owns voice)
- **Final sales page polish** (especially headline + opening)
- **Founding-price launch announcement post** on social
- **Replies to customer questions** during launch
- **Choosing which idea to sprint next** from the backlog

Automating these would lower quality. Don't.
