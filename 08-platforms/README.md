# 08 - Platforms

Where the products are sold. Default = Gumroad. Graduate paths exist when scale demands them.

## Files in this folder

- [`vercel-sites/`](./vercel-sites/) - Isolated static landing pages and deployment-ready preview surfaces.
- [`gumroad-setup.md`](./gumroad-setup.md) - Configuring Gumroad for digital products, fees, pricing rules, payouts.
- [`gumroad-workflows.md`](./gumroad-workflows.md) - Setting up email automations natively in Gumroad.
- [`alternatives.md`](./alternatives.md) - Payhip, ThriveCart, Lemon Squeezy, and when to consider each.
- [`tech-stack.md`](./tech-stack.md) - The full Dynasty Empire stack reference for digital products.
- [`../00-foundation/operator-system/design-tool-routing.md`](../00-foundation/operator-system/design-tool-routing.md) - Preferred design, page-building, media, and conversion tool routing for Hermes and Paperclip.
- [`production-readiness-checklist.md`](./production-readiness-checklist.md) - Production storefront/platform readiness checklist for Gumroad, Vercel, Neon/n8n, `ikeohu.com` linkage, and launch measurement gates.
- [`suitedash-storefront-linkage-status.md`](./suitedash-storefront-linkage-status.md) - SuiteDash-specific storefront, sitemap, and `ikeohu.com` linkage handoff/status for DIG-24.

## Decision Rule

Use Gumroad until at least one of the following is true:

- Email list exceeds 5,000 active subscribers
- Total monthly revenue exceeds $5K and Gumroad's 10% fee starts to hurt
- You need advanced tax / VAT handling that Gumroad doesn't provide
- You need conditional email logic that Gumroad Workflows can't do

Then evaluate the graduate path: custom Vercel + Stripe, ThriveCart, or Lemon Squeezy as merchant of record.

## Production Gate

Before launch traffic starts, run [`production-readiness-checklist.md`](./production-readiness-checklist.md). A product is not platform-ready until a buyer can discover the offer, pay, receive the files, enter the follow-up workflow, and be measured through the 7-day, 30-day, and 90-day review cadence.

## Why Gumroad First

- Zero setup time; a product can be live in under 30 minutes
- Handles tax, VAT, refunds, and fraud
- Built-in workflows plus abandoned cart support
- Discoverability via the Gumroad audience
- The 10% fee is high, but the time saved is higher when you are early

## What Gumroad Does Not Do Well

- Complex conditional email logic
- Custom-domain checkout; the storefront can be branded, but checkout lives on `gumroad.com`
- Advanced segmentation
- High-volume B2B flows where invoices and purchase orders become standard
