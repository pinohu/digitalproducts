# Storefront, Sitemap, and ikeohu.com Linkage Status — The Good Parts of SuiteDash

Owner: Growth Analyst
Related issues: DIG-24, DIG-31
Operating date: 2026-05-08 sprint day / 2026-05-07 local system date
Status: blocked on live checkout/storefront and owned-site write access; exact repo-side linkage plan is ready and the DIG-31 post-unblock attempt has been recorded truthfully.

## Executive status

DIG-24 cannot truthfully complete the ROADMAP.md storefront, sitemap, or `ikeohu.com` linkage Definition-of-Done items yet because the required live checkout/storefront URL does not exist in repo-visible state and this agent has no Gumroad admin access or `ikeohu.com` site-repo/CMS write access.

What does exist:

- Vercel staging offer surface: `https://suitedash-good-parts-preview.vercel.app`
- Live `www.ikeohu.com` site and sitemap are reachable publicly.
- Current sitemap: `https://www.ikeohu.com/sitemap.xml`
- Current relevant/nearby essay candidates in the sitemap:
  - `https://www.ikeohu.com/insights/the-adoption-gap`
  - `https://www.ikeohu.com/insights/the-may-31-cliff`
- Gumroad activation blocker/status file: `06-launch-playbooks/by-product/01-suitedash-good-parts-gumroad-activation-status.md`

The staging page must not be treated as the production checkout path. It is noindex/no-follow and its CTA is intentionally disabled until Gumroad is live.

## URL registry

| Asset | Current value | Production status | Required next action |
|---|---|---|---|
| Gumroad product URL | `[BLOCKED: needs Gumroad admin access/product creation]` | Not live | DIG-22/operator creates product, uploads files, records URL. |
| Gumroad checkout/direct buy URL | `[BLOCKED: needs Gumroad admin access/checkout activation]` | Not live | DIG-22/operator records direct buy or product checkout URL after discount/test purchase setup. |
| Founding discount URL | `[BLOCKED: needs Gumroad discount creation]` | Not live | Create `SUITEDASHFOUNDING29` and record the discounted URL. |
| Gumroad creator storefront URL | `[BLOCKED: needs Gumroad creator profile/storefront access]` | Not live | Record the public creator storefront once the product appears there. |
| Vercel staging landing page | `https://suitedash-good-parts-preview.vercel.app` | Staging only | Replace disabled CTA with Gumroad URL only after checkout + proof + workflow readiness. |
| Canonical production sales page | `[TBD after Gumroad URL exists]` | Not selected | Default to Gumroad product URL unless Vercel is promoted to a production sales page. |
| ikeohu.com selected link path | `[BLOCKED: needs site-repo/CMS write access + canonical product URL]` | Not live | Add a natural CTA to a relevant existing essay or publish the proposed new essay below. |
| Sitemap/product index entry | `[BLOCKED: needs site-repo/CMS write access + deployment]` | Not live | Add the chosen product/essay URL to the site route list/sitemap source and deploy. |

## Recommended owned-site linkage

Preferred path: publish a new focused essay because the current public `ikeohu.com` sitemap does not show an obviously SuiteDash/client-portal-specific page.

- Proposed essay URL: `https://www.ikeohu.com/insights/the-good-parts-of-suitedash`
- Proposed essay title: `The Good Parts of SuiteDash: what operators should borrow before building custom client portals`
- Natural CTA copy:
  > If you want the checklist version, get The Good Parts of SuiteDash here: [CANONICAL_PRODUCT_URL]?utm_source=ikeohu&utm_medium=essay&utm_campaign=suitedash_good_parts_launch
- Measurement tag: `utm_source=ikeohu&utm_medium=essay&utm_campaign=suitedash_good_parts_launch`

Fallback path if publishing a new essay is too slow: add a short, clearly related implementation note near the end of `https://www.ikeohu.com/insights/the-adoption-gap`, because it already discusses enterprise software adoption and implementation friction. Do not add the link to an unrelated page just to satisfy the checkbox.

## Storefront and sitemap operator checklist

Complete only after DIG-22 produces a live Gumroad product/checkout URL:

1. Decide canonical product target:
   - Use Gumroad product URL for Sprint 1 by default.
   - Use Vercel only if the production Vercel page has a working Gumroad CTA, analytics, and launch-proof section.
2. Confirm Gumroad creator profile/storefront is public and product is visible.
3. Record exact Gumroad product, checkout, founding discount, and storefront URLs in:
   - `06-launch-playbooks/by-product/01-suitedash-good-parts-activation-checklist.md`
   - `06-launch-playbooks/by-product/01-suitedash-good-parts-gumroad-activation-status.md`
   - `analytics/by-product/01-suitedash-good-parts.md`
   - this file
4. Add the owned-site CTA to either:
   - new essay `https://www.ikeohu.com/insights/the-good-parts-of-suitedash`, or
   - existing essay `https://www.ikeohu.com/insights/the-adoption-gap` only if the note is contextually natural.
5. Add or verify sitemap/product-index inclusion after deployment:
   - `https://www.ikeohu.com/sitemap.xml`
   - any site-level product/publications/catalog index if one exists in the site repo.
6. Re-crawl the chosen essay URL and sitemap URL after deploy; record HTTP 200 evidence and final URLs here.
7. Update `ROADMAP.md` only after the live storefront/sitemap and `ikeohu.com` link are verified.

## Exact external blockers

1. No Gumroad admin/session is available to create or read the live product, checkout, discount, or storefront URLs.
2. No live Gumroad checkout URL is recorded in the repo, so there is no safe canonical destination for public owned-site traffic.
3. No `ikeohu.com` source repository, CMS session, or deployment permission is available in this environment.
4. The public apex domain `https://ikeohu.com` redirects to `https://www.ikeohu.com/`; the bare apex also presents a certificate hostname mismatch in Python's default SSL verification. Use `https://www.ikeohu.com/...` as the canonical link base until DNS/certificate settings are intentionally changed.
5. The Vercel preview page is noindex staging with checkout disabled; wiring it as production before Gumroad/proof/workflows would violate the ROADMAP.md Definition of Done.
6. Permissioned testimonials/paid beta proof are still tracked separately by DIG-25 and should not be faked for the owned-site CTA.

## DIG-31 post-unblock execution attempt — 2026-05-08

DIG-31 was selected as the highest-priority assigned Growth Analyst issue. It remains externally blocked by its stated dependencies: DIG-28 is still `blocked`, DIG-29 has not produced a repo-visible live Gumroad product/checkout/storefront URL, and this runtime has no `ikeohu.com` CMS/site-repo/deploy access.

Fresh public URL verification from this run:

| Check | Result | Evidence |
|---|---|---|
| Vercel staging page | Reachable, staging only | `https://suitedash-good-parts-preview.vercel.app` returned HTTP 200. Checkout remains intentionally disabled until Gumroad is live. |
| Sitemap | Reachable, but no SuiteDash entry | `https://www.ikeohu.com/sitemap.xml` returned HTTP 200; it contains `the-adoption-gap` and `the-may-31-cliff`, but not `suitedash` or `the-good-parts-of-suitedash`. |
| Proposed SuiteDash essay | Not live | `https://www.ikeohu.com/insights/the-good-parts-of-suitedash` returned HTTP 404. |
| Fallback essay | Reachable candidate only | `https://www.ikeohu.com/insights/the-adoption-gap` returned HTTP 200, but no write access exists to add a contextual CTA. |

DIG-31 acceptance remains incomplete. Do not close DIG-31, update ROADMAP shipped status, or call the product listed on the storefront/sitemap until exact live Gumroad and owned-site URLs are recorded here after operator access/deploy.

## Definition of Done guardrail

This file is a linkage handoff, not a shipped-status claim. The product remains unshipped until ROADMAP.md Definition of Done is satisfied, including live Gumroad upload/checkout, post-purchase workflow, abandoned cart, 3 permissioned testimonials, storefront/sitemap listing, `ikeohu.com` link, first sale, and shipped catalog entry.

Current DIG-24/DIG-31 outcome: exact URLs that exist were recorded, exact missing URLs are marked blocked, and the operator-owned storefront/sitemap/`ikeohu.com` linkage sequence is ready to execute after live checkout exists.
