# Activation Checklist - The Good Parts of SuiteDash

Owner: Funnel and Launch Ops
Related issues: DIG-15, DIG-22, DIG-23, DIG-29
Status: repo-side activation sheet ready; Vercel preview is live; DIG-22/DIG-29 verified the Gumroad upload package and documented the exact external access blocker in `01-suitedash-good-parts-gumroad-activation-status.md`. External Gumroad/proof access is still required for execution.

## Product facts

- Product name: The Good Parts of SuiteDash
- Slug: `01-suitedash-good-parts`
- Core promise: the 90-minute operator path through the 20% of SuiteDash that creates 80% of the client-ops value
- Founding price: USD 29
- Public price: USD 49
- Guarantee: 30-day money-back guarantee
- Checkout platform: Gumroad
- Standalone landing page: https://suitedash-good-parts-preview.vercel.app (staging copy; checkout not wired yet)

## Source of truth

Use these repo files when entering platform data:

- Sales page: `04-sales-pages/by-product/01-suitedash-good-parts.md`
- Launch emails: `05-email-workflows/by-product/01-suitedash-good-parts/launch-sequence.md`
- Post-purchase emails: `05-email-workflows/by-product/01-suitedash-good-parts/post-purchase-sequence.md`
- Abandoned cart email: `05-email-workflows/by-product/01-suitedash-good-parts/abandoned-cart.md`
- Manuscript: `03-products/01-suitedash-good-parts/manuscript/02-v1-manuscript.md`
- Bonus files: `03-products/01-suitedash-good-parts/bonuses/`
- Package entrypoint: `03-products/01-suitedash-good-parts/deliverables/START-HERE.md`
- Packaging truth: `03-products/01-suitedash-good-parts/deliverables/packaging-checklist.md`
- Asset brief: `03-products/01-suitedash-good-parts/assets/asset-brief.md`
- Proof bank: `shared-assets/testimonial-bank/01-suitedash-good-parts.md`

## Gumroad product setup

### Product type

- Product format: digital product
- Delivery mode: file download
- Optional bundle later: ZIP containing all PDFs plus `START-HERE.md`

### Product title and pricing

Enter exactly:

- Title: `The Good Parts of SuiteDash`
- Public price: `49`
- Founding discount target price: `29`
- Currency: `USD`
- Allow customers to pay more: `ON`

Recommended discount code:

- Code: `SUITEDASHFOUNDING29`
- Discount behavior: reduces price to USD 29
- Expiration: 48 hours after launch start

### Gumroad URL placeholders to record

Fill these into the repo once created (DIG-24 linkage handoff: `08-platforms/suitedash-storefront-linkage-status.md`):

- Gumroad product URL: `[GUMROAD_PRODUCT_URL]`
- Gumroad checkout URL: `[GUMROAD_CHECKOUT_URL]`
- Founding discount URL: `[GUMROAD_FOUNDING_URL]`
- Creator storefront URL: `[GUMROAD_STOREFRONT_URL]`

Update these files after URLs are real:

- `04-sales-pages/by-product/01-suitedash-good-parts.md`
- `05-email-workflows/by-product/01-suitedash-good-parts/launch-sequence.md`
- `05-email-workflows/by-product/01-suitedash-good-parts/post-purchase-sequence.md`
- `05-email-workflows/by-product/01-suitedash-good-parts/abandoned-cart.md`
- `08-platforms/production-readiness-checklist.md`
- `analytics/by-product/01-suitedash-good-parts.md`

### File upload order

Export these source files to PDFs before upload:

1. `The-Good-Parts-of-SuiteDash.pdf`
   Source: `03-products/01-suitedash-good-parts/manuscript/02-v1-manuscript.md`
2. `90-Minute-SuiteDash-Lock-In-Protocol.pdf`
   Source: `03-products/01-suitedash-good-parts/bonuses/01-90-minute-lock-in-protocol.md`
3. `7-SuiteDash-Automation-Recipes.pdf`
   Source: `03-products/01-suitedash-good-parts/bonuses/02-automation-recipes.md`
4. `SuiteDash-Kill-List.pdf`
   Source: `03-products/01-suitedash-good-parts/bonuses/03-kill-list.md`
5. `START-HERE.pdf` or `START-HERE.md`
   Source: `03-products/01-suitedash-good-parts/deliverables/START-HERE.md`

Optional:

- `The-Good-Parts-of-SuiteDash-Bonus-Pack.zip`

### Cover and product media

Use the brief in `03-products/01-suitedash-good-parts/assets/asset-brief.md`.

Required assets:

- Gumroad hero image: 1280 x 720
- PDF cover page
- Social card: 1200 x 630

Do not use official SuiteDash logos or screenshots unless permission is confirmed.

### Description blocks to enter

Whether Gumroad hosts the full page or a short version, keep these elements aligned:

1. Headline
2. Sub-headline
3. Pain/problem
4. Promise/transformation
5. What is inside
6. Bonus stack
7. Guarantee
8. Proof/testimonials
9. Pricing
10. FAQ
11. Final CTA
12. Launch urgency

If Gumroad page length becomes unwieldy, host the full sales page elsewhere and keep Gumroad focused on:

- headline,
- short promise,
- what is included,
- guarantee,
- testimonials,
- pricing,
- CTA.

### Gumroad settings

Set these during activation:

- Reviews: `ON`
- Abandoned cart: `ON`
- Recommended products: `OFF` for Sprint 1 unless another relevant product exists
- Affiliates: `OFF` until the first proof cycle is complete, unless a warm launch partner is already lined up
- Reply-to inbox: monitored and recorded
- Refund policy text: must match the 30-day guarantee wording in the offer brief and sales page

## Gumroad workflow mapping

### Post-purchase workflow

Trigger: customer purchases this product

Map the sequence exactly:

- 0 hours -> welcome + download
- 1 day -> quick win
- 3 days -> common mistakes
- 7 days -> use case or early proof
- 14 days -> next step
- 30 days -> testimonial request

Source file:

- `05-email-workflows/by-product/01-suitedash-good-parts/post-purchase-sequence.md`

### Abandoned cart workflow

Trigger: Gumroad abandoned cart

Source file:

- `05-email-workflows/by-product/01-suitedash-good-parts/abandoned-cart.md`

Reminder:

- Gumroad uses a 24-hour timer by default
- remove founding-price language once the discount window closes

### Launch email sequence

This is not a Gumroad native product workflow. Queue it in the email platform or send manually from the product launch owner using:

- `05-email-workflows/by-product/01-suitedash-good-parts/launch-sequence.md`

## Vercel decision

Current state: a reviewable Vercel page now exists at `https://suitedash-good-parts-preview.vercel.app`, but it is still staging because the Gumroad checkout path and live proof are not attached.

Keep the Vercel page in the launch path only if one of these is true:

- Gumroad page cannot hold the required sales narrative cleanly
- launch traffic needs a branded page before checkout
- `ikeohu.com` essay traffic requires a standalone canonical page

Before treating the Vercel page as canonical, require:

- project selection or creation in the correct team
- production URL
- CTA to Gumroad checkout
- analytics enabled
- mobile review complete

## Operator execution order

1. Proofread and export the manuscript and bonus PDFs
2. Generate cover/hero/social assets from the asset brief
3. Create Gumroad product and upload files
4. Configure founding discount
5. Paste the product description and proof
6. Insert real URLs into sales page and email sources
7. Configure post-purchase workflow
8. Configure abandoned cart email
9. Run a 100 percent discount-code test purchase
10. Record final URLs and test results back in the repo

## Test-purchase checklist

- Product page loads
- Founding discount applies correctly
- Download links work
- Welcome email arrives within 5 minutes
- Reply-to inbox is monitored
- Abandoned cart email copy is saved and enabled
- Sales page and Gumroad page use the same promise, price, guarantee, and bonus stack

## External blockers

- Gumroad admin access
- real support inbox
- exported PDF files
- generated visual assets
- at least 3 real testimonials
- final launch date and timezone
- optional Vercel CTA/domain refinement if Gumroad is not the only page
