# Platform Alternatives

When to consider each platform beyond Gumroad. Most creators stay on Gumroad longer than they need to. A few graduate too early.

## Payhip

**Best for:** Lower fees, simple needs, EU-based creators.

**Pros:**
- Lower fees than Gumroad (5% on free plan vs. 10%)
- Built-in EU VAT handling
- Cleaner default storefront design

**Cons:**
- Smaller ecosystem (fewer affiliates, fewer discoverability paths)
- Workflow / email automation is weaker than Gumroad
- Less brand recognition with buyers

**When to switch:** If volume is high enough that the 5% vs. 10% fee differential covers a couple weeks of revenue per year. Generally: $30K+ ARR.

---

## ThriveCart

**Best for:** Course creators, multi-product creators, advanced funnel needs.

**Pros:**
- One-time payment ($495 lifetime, no monthly fees) — fee math wins at scale
- Robust upsell / downsell / order bump features
- Multi-currency, advanced tax handling
- Built-in affiliate management

**Cons:**
- $495 upfront is real money
- More configuration overhead than Gumroad
- You're still using Stripe / PayPal underneath, so you handle VAT yourself unless you bolt on Quaderno or similar

**When to switch:** When monthly Gumroad fees exceed ~$200 (i.e., $2K monthly revenue). At that point, ThriveCart pays for itself in ~2.5 months.

---

## Lemon Squeezy

**Best for:** SaaS / digital product creators who want EU-VAT handled and clean developer ergonomics.

**Pros:**
- Merchant of record (handles all tax / VAT for you)
- Clean API and webhook support
- Modern UI, built for SaaS-like products
- Strong subscription / license handling

**Cons:**
- 5% + 50¢ per transaction (similar effective rate to Gumroad)
- Smaller customer base than Gumroad
- Newer platform, fewer integrations

**When to switch:** If you have international customers and want fully-handled tax compliance (similar to Gumroad's MoR model), AND you want a more modern API for advanced integrations.

---

## Custom Stack (Vercel + Stripe + Email Tool)

**Best for:** When the product becomes the business and infrastructure overhead is justified.

**Pros:**
- Full control of UX, brand, checkout
- Lowest possible fees (~3% Stripe only)
- Custom logic, segmentation, integrations

**Cons:**
- You handle: VAT (via Quaderno, ~$30/mo), refunds, fraud, dunning
- Setup time: 20–80 hours
- Maintenance time: ongoing
- The savings only matter at $50K+ ARR

**When to switch:** Generally not before $5K MRR consistently. The 13% Gumroad fee on $5K/mo = $650/mo. The custom stack saves ~$500/mo of that, after subtracting Stripe + tools. The 80-hour setup pays back in ~6 months. Below this threshold, it's a waste of build time.

---

## Decision Matrix

| Creator Stage | Recommended Platform |
|---|---|
| First product, <$1K total revenue | **Gumroad** |
| 2–3 products, <$2K/mo | **Gumroad** |
| Multiple products, $2–5K/mo | **Gumroad** or **ThriveCart** (if upsells matter) |
| $5K+/mo, multi-product, complex flows | **ThriveCart** or **Custom (Vercel + Stripe + Beehiiv)** |
| EU-heavy customer base, MoR matters | **Gumroad** or **Lemon Squeezy** |

## Stay on Gumroad Until Forced Off

The decision to migrate is almost always made too early. Every hour spent on platform migration is an hour not spent making the next product. The math hardly ever favors switching before $50K+ ARR.
