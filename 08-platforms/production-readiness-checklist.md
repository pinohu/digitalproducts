# Production Storefront and Platform Readiness Checklist

Owner: Growth Analyst
Scope: acquisition, conversion, delivery, measurement, and iteration readiness for the first product launch.
Initial product: `01-suitedash-good-parts` / The Good Parts of SuiteDash.
Canonical cadence: launch day, 7-day review, 30-day review, 90-day review.

## Production Readiness Definition

The platform is production-ready when a buyer can discover the offer, understand it, purchase it, receive the product, get follow-up support, and leave enough measurable signal for the next product/channel decision.

Production readiness is not just "page is live." It requires all of these gates:

1. Acquisition gate: at least one owned traffic path points to the offer.
2. Conversion gate: the sales page and checkout carry the same promise, price, guarantee, and bonus stack.
3. Delivery gate: Gumroad delivers the PDF/bonuses and starts the post-purchase workflow without manual intervention.
4. Trust gate: refund policy, support path, testimonials/proof placeholders, and buyer expectations are explicit.
5. Measurement gate: page visits, checkout/sales, email workflow metrics, refunds, and source/channel tags can be reviewed at 7, 30, and 90 days.
6. Iteration gate: review files exist in the repo and turn sales data into next-product and next-channel decisions.

## Gate 1 — Gumroad Product and Storefront

Default platform: Gumroad, per `08-platforms/README.md` and `FRAMEWORK.md` Stage 6.

Must be complete before launch:

- [ ] Gumroad account exists under the business/brand email.
- [ ] Public creator profile has real photo, outcome-focused bio, and branded handle.
- [ ] Payout method is connected and verified.
- [ ] Tax forms are complete.
- [ ] Product title exactly matches the sales page H1.
- [ ] Product URL/slug is recorded in this repo once created.
- [ ] Core PDF is uploaded.
- [ ] Bonus files are uploaded or clearly marked as delivered inside the main product.
- [ ] Cover image is 1280x720 and readable on mobile.
- [ ] Public price is configured at $49 after the founding window.
- [ ] Founding discount is configured to create the $29 launch price and has an expiration date.
- [ ] "Allow customers to pay more" is enabled.
- [ ] Money-back guarantee appears on the product page and matches `02-offers/guarantee-templates.md` / offer brief language.
- [ ] Abandoned cart recovery is enabled.
- [ ] Reviews are enabled.
- [ ] Affiliate program is enabled or explicitly deferred until after first 5 customers.
- [ ] Post-purchase workflow is live: 0hr, day 1, day 3, day 7, day 14, day 30.
- [ ] Storefront lists the product after launch.
- [ ] First sale is recorded in `analytics/revenue-tracker.md` and `ROADMAP.md` before the product is marked shipped.

Readiness evidence to save in repo:

- Gumroad product URL.
- Screenshot or text note confirming price/discount configuration.
- Workflow activation note in the by-product analytics file.
- Refund/support owner and support inbox.

External blockers:

- Gumroad login/access.
- Business email identity.
- Payout verification.
- Tax profile completion.
- Final PDF/bonus files from product build owner.
- Final sales copy from launch/funnel owner.
- Testimonials/proof from beta readers.

## Gate 2 — Vercel Landing Page / Deployment

Default pattern: standalone landing page on Vercel can be used for richer sales-page control, while Gumroad remains checkout/delivery.

Current SuiteDash asset: `https://suitedash-good-parts-preview.vercel.app` exists as a live staging page with checkout intentionally disabled until Gumroad URLs and proof are ready.

Must be complete before routing cold or owned traffic to Vercel:

- [ ] Landing page repo/project exists in the correct Vercel team.
- [ ] Production domain or subdomain is assigned.
- [ ] Page has the same H1, offer promise, price, bonus stack, guarantee, and FAQ as Gumroad.
- [ ] Primary CTA links to the Gumroad checkout/product URL.
- [ ] Mobile layout is reviewed.
- [ ] Page load and basic accessibility are acceptable for a one-page sales asset.
- [ ] Vercel Analytics is enabled.
- [ ] Plausible or equivalent privacy-friendly analytics is enabled if available.
- [ ] UTM parameters are preserved on CTA links where possible.
- [ ] 404 and canonical metadata do not create duplicate/confusing pages.
- [ ] The product is discoverable from the storefront/catalog path or intentionally hidden until launch.

Vercel can be deferred for Sprint 1 if the Gumroad product page includes all 12 required sales-page sections and analytics are still captured from Gumroad plus launch-source tracking. If deferred, record that decision in the 7-day review.

External blockers:

- Vercel account/team access.
- Domain/DNS access.
- Final Gumroad URL.
- Final sales page copy and hero/cover asset.
- Analytics provider credentials.

## Gate 3 — Neon and n8n Dependencies

Sprint 1 does not require custom checkout or a custom database. Neon and n8n become production dependencies only when automations cross tool boundaries or analytics need a consolidated data store.

MVP launch requirements:

- [ ] Gumroad native workflows cover post-purchase emails.
- [ ] Manual tracker updates are acceptable through the first 5 customers.
- [ ] No custom buyer database is required to accept payment.
- [ ] No n8n workflow is required for purchase delivery.

Production automation readiness before relying on n8n:

- [ ] n8n instance access confirmed.
- [ ] Credential storage policy defined for Gumroad, email/newsletter, Vercel/Plausible, and repo access.
- [ ] Workflow owner and alert path defined.
- [ ] Failed-run alerting configured.
- [ ] Analytics aggregation workflow maps to `analytics/` tracker fields.
- [ ] Workflow writes are tested in a sandbox or non-production target before live use.

Production data readiness before relying on Neon:

- [ ] Neon project/database selected.
- [ ] Schema for sales, traffic, email events, refunds, and products is defined.
- [ ] Read/write credentials are stored outside the repo.
- [ ] Backfill plan exists from Gumroad exports.
- [ ] Repo tracker remains the canonical summary even if Neon becomes the raw event store.

External blockers:

- n8n login and credential-store access.
- Gumroad API or export access.
- Neon project access and database credentials.
- Agreement on whether the first launch needs automation beyond native Gumroad.

## Gate 4 — ikeohu.com Linkage and Sitemap Requirements

Owned authority site role: drive qualified trust traffic to the offer without making social platforms the only acquisition path.

Must be complete before declaring the product shipped:

- [ ] At least one relevant ikeohu.com essay links to the product, matching ROADMAP Definition of Done.
- [ ] Link uses a natural editorial CTA, not a hard-sell banner only.
- [ ] Product page/storefront is included in the site sitemap or the relevant product/catalog index.
- [ ] Link target is the canonical sales page or Gumroad page.
- [ ] UTM/source tag distinguishes ikeohu.com traffic from LinkedIn, X, email, and direct.
- [ ] The essay CTA matches the product promise and does not overstate the offer.
- [ ] If the page is not ready, a waitlist/early-access CTA exists instead of a broken product link.

Suggested initial essay angle for SuiteDash:

- "The Good Parts of SuiteDash: what operators should borrow before building custom client portals"
- CTA: "If you want the checklist version, get The Good Parts of SuiteDash here."

External blockers:

- ikeohu.com CMS/repo access.
- Sitemap generation/deployment access.
- Final canonical product URL.
- Analytics tagging support on outbound links.

## Gate 5 — Analytics Baseline and Review Cadence

The launch is measurable when these fields are captured at minimum:

Traffic/acquisition:

- Source/channel: LinkedIn, X, ikeohu.com, email, direct, referral, Gumroad Discover.
- Sessions/visits to the sales page or Gumroad product page.
- Email subscribers or waitlist replies generated by launch content.
- Content/post URL for each launch push.

Conversion:

- Gumroad product page views if available.
- Checkout starts if available.
- Sales count.
- Gross revenue.
- Net revenue after Gumroad/payment fees.
- Conversion rate: sales / landing-page visits.
- Customer questions and objections.

Quality/retention:

- Refund count and refund rate.
- Review/testimonial count.
- Day 7 implementation replies.
- Day 30 testimonial request replies.
- Support issues.

Iteration:

- Most common buyer segment.
- Most common objection.
- Highest-converting channel.
- Lowest-friction content angle.
- Next-product recommendation.
- Next-channel recommendation.

Review files and cadence:

- Launch baseline: `analytics/by-product/01-suitedash-good-parts.md` before launch.
- 7-day review: same by-product file plus sprint notes in `10-execution-sprints/current-sprint.md` or completed sprint archive.
- 30-day review: update `analytics/revenue-tracker.md`, `analytics/conversion-tracker.md`, and by-product file.
- 90-day review: use `09-iteration-and-scale/90-day-review-template.md` and update `09-iteration-and-scale/catalog-roadmap.md` / idea backlog with the next product decision.

## Launch Decision Rules

Use these rules to turn production data into action:

- If sales-page conversion is below 1% after 200+ qualified visits, revise positioning/headline/offer clarity before sending more traffic.
- If conversion is 1–3%, keep the offer live and test proof, bonus framing, and channel-specific CTAs.
- If conversion is above 3%, prioritize more traffic from the highest-intent channel and consider raising the post-founding price.
- If refund rate exceeds 5%, inspect expectation mismatch before adding new bonuses or upsells.
- If day-7 replies show implementation friction, create the next bonus or product around that friction.
- If one channel produces at least 2x the conversion rate of another, double the next 14 days of content volume there and reduce the lower-performing channel.
- If buyers ask for the same adjacent workflow 3+ times, add it to the idea backlog as the next sprint candidate.

## SuiteDash Sprint 1 Readiness Summary

Current status: a live Vercel staging page exists, but Gumroad activation, proof, owned-traffic linkage, and workflow wiring are still blockers. SuiteDash-specific storefront/sitemap/`ikeohu.com` linkage status and operator handoff now lives at `08-platforms/suitedash-storefront-linkage-status.md`; exact public URLs remain blocked until a live Gumroad checkout/storefront exists and `ikeohu.com` write/deploy access is available.

Can launch when these minimums are true:

- [ ] Final PDF and at least one bonus are ready.
- [ ] Gumroad product is created with $29 founding price and $49 post-founding price logic.
- [ ] Gumroad page or Vercel page contains the 12-section sales page.
- [ ] Post-purchase workflow is live.
- [ ] Abandoned cart is enabled.
- [ ] At least one ikeohu.com link or planned launch post has a working product/waitlist CTA.
- [ ] Analytics baseline exists in `analytics/by-product/01-suitedash-good-parts.md`.
- [ ] First sale can be recorded in the repo trackers.

Do not mark shipped until every ROADMAP Definition of Done item is complete, including first sale recorded, storefront/sitemap listing, and ikeohu.com link.
