# 08 · Platforms

Where the products are sold. Default = Gumroad. Graduate paths exist when scale demands them.

## Files in this folder

- [`gumroad-setup.md`](./gumroad-setup.md) — Configuring Gumroad for digital products, fees, pricing rules, payouts.
- [`gumroad-workflows.md`](./gumroad-workflows.md) — Setting up email automations natively in Gumroad.
- [`alternatives.md`](./alternatives.md) — Payhip, ThriveCart, Lemon Squeezy, and when to consider each.
- [`tech-stack.md`](./tech-stack.md) — The full Dynasty Empire stack reference for digital products.

## Decision Rule

Use Gumroad until at least one of the following is true:
- Email list exceeds 5,000 active subscribers
- Total monthly revenue exceeds $5K and Gumroad's 10% fee starts to hurt
- You need advanced tax / VAT handling that Gumroad doesn't provide
- You need conditional email logic that Gumroad Workflows can't do

Then evaluate the graduate path (custom Vercel + Stripe, or ThriveCart, or Lemon Squeezy as merchant of record).

## Why Gumroad First

- Zero setup time (a product can be live in under 30 min)
- Handles tax, VAT, refunds, fraud
- Built-in workflows + abandoned cart
- Discoverability via the Gumroad audience
- 10% fee is high, but the time saved is higher when you're early

## What Gumroad Doesn't Do Well

- Complex conditional email logic
- Custom domain checkout (you can do storefront, but checkout is on gumroad.com)
- Advanced segmentation
- High-volume B2B (where invoices and POs become standard)
