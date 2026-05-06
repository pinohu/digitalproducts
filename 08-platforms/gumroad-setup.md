# Gumroad Setup

Configuring Gumroad for digital products. Default platform until graduation criteria are met.

## Account Setup

- [ ] Account created with business email (not personal)
- [ ] Profile photo set (real face, not logo — converts better)
- [ ] Bio reflects the brand positioning (one sentence, outcome-focused)
- [ ] Custom URL claimed (`gumroad.com/<handle>`)
- [ ] Payout method connected and verified
- [ ] Tax forms completed (W-9 for US)

## Product Configuration

For every product:
- [ ] Title matches the sales page H1
- [ ] Description includes all 12 sections of the sales page (or links to the standalone sales page)
- [ ] Cover image: 1280×720, eye-catching, readable on mobile
- [ ] Files uploaded: core PDF + bonuses (3–5 files max)
- [ ] Pricing: founding price + post-founding price configured
- [ ] Variants if needed (e.g., PDF only vs. PDF + video)
- [ ] License key generation enabled if relevant
- [ ] "Allow customers to pay more" toggle: ON (occasional buyer pays $97 instead of $49)

## Pricing & Discounts

- **Default product price:** Set to post-founding price ($Y).
- **Discount code for founding price:** Create a code like `LAUNCH50` with the founding price ($X) and an expiration date.
- **Bundle discount codes:** When products are bundled, create a code that applies the bundle pricing.
- **Avoid:** Permanent discount codes — they poison the price perception.

## Fees (As of 2026)

Gumroad charges **10% per transaction** for new accounts. Plus payment processing (~3% + $0.30). Total effective fee: ~13%.

For a $49 sale: ~$42.30 net to you.

This is high, but it's the price of zero infrastructure overhead.

## Refunds

- Refunds processed in <60 seconds via the Gumroad dashboard
- Refunded amount returns to the original payment method in 3–5 business days
- Gumroad does not charge a fee on refunds
- Save the refund email response template (`/02-offers/guarantee-templates.md`) for fast handling

## Tax & VAT

Gumroad acts as **merchant of record** in the EU and UK, meaning Gumroad collects and remits VAT on your behalf. This is a significant advantage vs. running checkout yourself with Stripe (where you'd handle VAT manually or via a tool like Quaderno).

For US customers, you remain responsible for income tax on Gumroad earnings. Gumroad issues a 1099-K above the federal threshold.

## Storefront vs. Standalone Sales Page

- **Storefront:** `gumroad.com/<handle>` — a list of all your products. Good for buyers who want to browse.
- **Standalone product page:** Each product has its own URL. Use this for direct sales page traffic.
- **Custom domain:** Connect `shop.<yourdomain>.com` to Gumroad for branded URLs.

## Day-One Settings That Matter

- [ ] **Affiliate program:** Enable, set commission to 30%, recruit 5–10 affiliates from your network within first 30 days.
- [ ] **Reviews:** Enabled by default, but check the toggle.
- [ ] **Recommended products:** Add cross-sells (e.g., recommend Product 2 to buyers of Product 1).
- [ ] **License keys:** Enable for any product where buyer access management matters.
- [ ] **Workflows:** See `gumroad-workflows.md`.
