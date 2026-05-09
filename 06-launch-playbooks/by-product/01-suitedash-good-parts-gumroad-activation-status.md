# Gumroad Activation Status — The Good Parts of SuiteDash

Owner: Funnel and Launch Ops
Related issues: DIG-22, DIG-29
Operating date: 2026-05-08 sprint day
Status: blocked on external Gumroad operator access; repo package is ready for upload.

## Executive status

DIG-22 cannot be completed as a live platform activation from this environment because no Gumroad admin credential, business account session, payout/tax access, or support inbox credential is available to the agent. No live Gumroad product, checkout URL, founding discount URL, or test purchase can be truthfully recorded yet.

Repo-side activation readiness is complete: the upload package, product copy sources, pricing, guarantee, hero assets, and test-purchase checklist are all present and tied back to the offer brief and ROADMAP.md Definition of Done.

## Offer brief alignment

Source offer: `02-offers/by-product/01-suitedash-good-parts.md`

Use these exact launch facts in Gumroad:

- Product title: `The Good Parts of SuiteDash`
- Product slug target: `the-good-parts-of-suitedash` or the closest available Gumroad slug
- Public price: USD 49
- Founding price: USD 29
- Founding discount code: `SUITEDASHFOUNDING29`
- Founding window: 48 hours after launch start
- Currency: USD
- Allow customers to pay more: ON
- Guarantee: 30-day money-back guarantee
- Core promise: the 90-minute operator path through the 20% of SuiteDash that creates 80% of client-ops value
- Bonus stack: 90-Minute Lock-In Protocol, 7 SuiteDash Automation Recipes, SuiteDash Kill List

## Files ready for Gumroad upload

Upload from `03-products/01-suitedash-good-parts/deliverables/`:

- `The-Good-Parts-of-SuiteDash.pdf` — core download
- `90-Minute-SuiteDash-Lock-In-Protocol.pdf` — bonus 1
- `7-SuiteDash-Automation-Recipes.pdf` — bonus 2
- `SuiteDash-Kill-List.pdf` — bonus 3
- `START-HERE.md` — buyer entrypoint
- `The-Good-Parts-of-SuiteDash-Bonus-Pack.zip` — optional convenience bonus ZIP
- `The-Good-Parts-of-SuiteDash-Gumroad-Package.zip` — full upload handoff package
- `suitedash-good-parts-gumroad-hero.png` — Gumroad hero image
- `suitedash-good-parts-cover.png` — cover art
- `suitedash-good-parts-square-thumbnail.png` — optional Gumroad thumbnail

Verification note: all files above exist in the repo as of this DIG-22 pass. Do not claim upload until a Gumroad operator confirms the product page has the files attached.

Additional credential/package check from this run:

- `GUMROAD_*` environment variables: none present in the agent runtime.
- Full handoff package local size: `The-Good-Parts-of-SuiteDash-Gumroad-Package.zip` = 327,453 bytes.
- Core PDF local size: `The-Good-Parts-of-SuiteDash.pdf` = 52,627 bytes.
- Bonus pack local size: `The-Good-Parts-of-SuiteDash-Bonus-Pack.zip` = 85,732 bytes.

## Gumroad fields to create

Record these URLs here after platform creation:

| Field | Value |
|---|---|
| Gumroad product URL | `[BLOCKED: needs Gumroad admin access]` |
| Gumroad checkout URL | `[BLOCKED: needs Gumroad admin access]` |
| Founding discount URL | `[BLOCKED: needs Gumroad admin access]` |
| Creator storefront URL | `[BLOCKED: needs Gumroad admin access]` |
| Test purchase receipt/order ID | `[BLOCKED: needs Gumroad admin access + operator test purchase]` |
| Support/reply-to inbox | `[BLOCKED: needs monitored support inbox credential/decision]` |

## Exact external blockers

1. Gumroad admin login/session for the correct business or creator account.
2. Business email identity and public creator profile details.
3. Payout method and tax profile completion.
4. Permission to create a live paid product, upload ZIP/PDF assets, and publish or preview the product page.
5. A monitored support/reply-to inbox to use in product settings and post-purchase workflow copy.
6. Permission to create and test a 100% discount code or run an operator-funded test purchase.
7. Permissioned testimonials or paid beta/pre-order proof from DIG-25 before the social-proof section is embedded.
8. Final launch date/timezone for the 48-hour founding discount expiration.
9. Optional Vercel production/domain access if the staging CTA should be wired before Gumroad is canonical.

## Operator execution checklist

Once access exists, complete these steps in order:

1. Log into Gumroad using the business/brand account.
2. Confirm payout/tax profile is complete before accepting paid traffic.
3. Create a digital product titled `The Good Parts of SuiteDash`.
4. Set public price to USD 49 and enable pay-what-you-want above the minimum if available.
5. Upload `The-Good-Parts-of-SuiteDash-Gumroad-Package.zip` or the individual PDF/ZIP files listed above.
6. Add `suitedash-good-parts-gumroad-hero.png` as the product hero.
7. Paste product description from `04-sales-pages/by-product/01-suitedash-good-parts.md`, keeping social proof honest if testimonials are still missing.
8. Add the 30-day money-back guarantee wording from the offer brief/sales page.
9. Create discount code `SUITEDASHFOUNDING29` to reduce checkout to USD 29 and set expiration 48 hours after launch start.
10. Enable reviews.
11. Enable abandoned cart recovery.
12. Create or publish the product and copy product, checkout, discount, and storefront URLs back into this file and the activation checklist.
13. Run a 100% discount-code test purchase or operator-funded test purchase.
14. Confirm download links work and the welcome email arrives within 5 minutes.
15. Only after DIG-23 workflows are live, record workflow evidence in `05-email-workflows/by-product/01-suitedash-good-parts/` and `analytics/by-product/01-suitedash-good-parts.md`.

## DIG-29 post-unblock execution attempt — 2026-05-08

DIG-29 was selected as the highest-priority Funnel and Launch Ops issue after the heartbeat found no separate newly assigned open issue. It remains externally blocked by DIG-28: this runtime has no Gumroad admin/session credential and no `GUMROAD_*` environment variables, so no live product can be created, published, uploaded to, or test-purchased truthfully from here.

Upload-critical package evidence re-verified locally:

| File | Size | SHA-256 |
|---|---:|---|
| `The-Good-Parts-of-SuiteDash-Gumroad-Package.zip` | 327,453 bytes | `5b034468269c3c3481186b6a66120db2dc5214c4ae9b4cb2b8b771464b7407a3` |
| `The-Good-Parts-of-SuiteDash.pdf` | 52,627 bytes | `df88e346163061ab47465e44eac9b98dea5385f5acceec4f2ca5a1e97cc554b6` |
| `The-Good-Parts-of-SuiteDash-Bonus-Pack.zip` | 85,732 bytes | `2b5124ef3948c89cee0afadd44c4caf98d1ef4ee2df95fb9adfecd9698491a91` |

DIG-29 acceptance remains incomplete until an operator supplies Gumroad access/evidence and records all of the following in this file and the activation checklist: live Gumroad product URL, checkout URL, founding discount URL, creator storefront URL, uploaded package confirmation, support/reply-to setting, test purchase receipt/order ID, and confirmation that downloads work from the receipt.

## Definition of Done guardrail

This file does not make the product shipped. ROADMAP.md requires all Definition of Done items before the shipped catalog can change, including Gumroad upload, live sales page, bonuses, guarantee, live post-purchase workflow, 3 testimonials, abandoned cart, storefront/sitemap listing, ikeohu.com link, first sale, and shipped catalog entry.

Current DIG-22/DIG-29 outcome: repo-side package verified and exact operator blocker documented; live Gumroad activation, upload, checkout URL, and test purchase remain externally blocked.
