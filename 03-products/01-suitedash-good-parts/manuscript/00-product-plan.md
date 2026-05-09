# The Good Parts of SuiteDash — Product Plan

## Product status

- Product: The Good Parts of SuiteDash
- Slug: `01-suitedash-good-parts`
- Current sprint stage: Product build scaffold / manuscript planning
- Target format: PDF-first trust tripwire with 3 practical bonuses
- Founding/public price alignment: offer brief currently uses $29 founding / $49 public; roadmap still lists $49 active sprint price.
- Source base: existing SuiteDash implementation material in `/mnt/c/Users/ohu00/Downloads/SuiteDash/` plus validation and offer files in this repo.

## Version 1 shipping principle

This is not a complete SuiteDash course and should not become one. V1 wins by helping a capable operator answer three questions fast:

1. What should I configure first?
2. What should I ignore until later?
3. What client workflow proves the platform is worth keeping?

If a section does not support one of those questions, cut it or move it to a future SuiteDash Operator Pack.

## Core promise

Within 90 minutes, a SuiteDash owner should know which modules to configure, which features to skip, and what order to follow so their client portal stops being a half-built tool graveyard.

## Reader profile

The reader is not a beginner and does not want generic no-code encouragement. They are a technical operator, consultant, freelancer, or small agency owner who already owns or is actively evaluating SuiteDash and needs a compressed implementation path.

## Manuscript architecture

Target length: 25-35 PDF pages.

| Part | Working title | Job to be done | Target pages |
|---|---|---|---:|
| Front matter | Start here | Position the product, promise the 90-minute path, set expectations | 1-2 |
| 1 | Why SuiteDash Feels Hard | Explain the platform breadth problem and the cost of wandering | 3-4 |
| 2 | The 7 Modules That Matter First | Define the v1 keep list and what each module is for | 6-8 |
| 3 | The 90-Minute Configuration Order | Give the setup sequence that prevents rebuild loops | 5-7 |
| 4 | Two Automation Patterns Worth Shipping | Show the first automations that create visible ROI | 4-5 |
| 5 | The Kill List | Teach what to defer and why | 4-5 |
| 6 | SuiteDash vs. Purpose-Built Tools | Help readers decide when not to force SuiteDash | 3-4 |
| Back matter | Next steps | Implementation checklist, refund guarantee reminder, testimonial ask, next-rung tease | 1-2 |

## V1 module keep list

1. CRM contacts and companies — the system of record for the client relationship.
2. Custom fields — the decision layer that makes records useful.
3. Forms/intake — the cleanest entry point for client data.
4. Client portal + white label basics — the trust surface buyers actually see.
5. Projects/tasks/templates — the delivery operating system.
6. Files/documents/proposals/invoices — the transaction and evidence layer.
7. Automations/notifications — the leverage layer, but only after the manual workflow is clear.

## First workflow to teach

Use one client-facing flow as the spine of the guide:

Lead / client record → intake form → portal access → project template → file/document request → invoice/payment → status/update notification → follow-up/testimonial request.

This flow is simple enough for v1, broad enough to demonstrate SuiteDash’s core value, and concrete enough to keep the PDF from turning into a feature encyclopedia.

## Source material to mine

| Source | Use in product |
|---|---|
| `SUITEDASH DETAILS/suitedash_features_capabilities.md` | Keep/skip module taxonomy and limitations |
| `detailed_suitedash_implementation_steps6.md` | Exact field and configuration examples |
| `suitedash_complete_implementation_guide1.md` | Workflow examples and CLOSER/custom-field examples |
| `SuiteDash_BOS_Data_Dictionary_and_Implementation_Guide.md` | Naming conventions, workflow schemas, evidence logs, RACI/SLA ideas |
| `suiteDash-templates/*.csv` | Future importable template pack candidates |
| `automation-recipes/*/*.json` | Bonus automation recipe source material |

## Bonus deliverable mapping

| Bonus | File | Status | Notes |
|---|---|---|---|
| 90-Minute SuiteDash Lock-In Protocol | `bonuses/01-90-minute-lock-in-protocol.md` | Scaffold complete | Printable implementation checklist |
| 7 SuiteDash Automation Recipes | `bonuses/02-automation-recipes.md` | Scaffold complete | Recipe-level templates; not yet import-tested |
| The Kill List | `bonuses/03-kill-list.md` | Scaffold complete | 12 defer-until-trigger decisions |

## Production sequence

1. Draft the full manuscript from `manuscript/01-outline.md`.
2. Reconcile pricing references across ROADMAP, offer brief, sales page, and product README.
3. Convert bonus scaffolds into final printable/downloadable assets.
4. Produce cover/hero/social art from `assets/asset-brief.md`.
5. Package final PDF + bonuses into `deliverables/`.
6. Hand off to launch/funnel owners for Gumroad upload, sales page finalization, and email workflow activation.

## Definition of done gates still open

- Manuscript final/proofread.
- Cover art designed.
- Bonuses finalized and packaged.
- Gumroad product/upload/workflows live.
- At least 3 beta-reader testimonials embedded.
- Abandoned cart workflow enabled.
- Storefront/sitemap/ikeohu.com linkage.
- First sale recorded.

## Scope guardrails

Do not add video, cohort, community, complete import templates, or done-for-you implementation to the $49 product unless explicitly promoted into the next-rung offer. Those belong in the $297+ SuiteDash Operator Pack.