# Analytics

Performance tracking. Where the numbers live. The single source of truth for "how is the catalog actually doing?"

## Files in this folder

- [`revenue-tracker.md`](./revenue-tracker.md) — Monthly and per-product revenue tracking.
- [`conversion-tracker.md`](./conversion-tracker.md) — Sales page conversion, email conversion, bundle conversion across products.
- `by-product/<slug>.md` — Detailed per-product metrics, cumulative.

## What to Track (and What Not To)

**Track:**
- Total revenue (monthly)
- Per-product revenue
- Sales page conversion rate (per product)
- Email open rate / click rate (per launch)
- Refund rate (per product, cumulative)
- AOV (per product, per bundle)
- LTV by buyer cohort (Year 1, Year 2)
- Affiliate-driven revenue %

**Don't track obsessively:**
- Daily revenue (creates anxiety, doesn't drive decisions)
- Vanity metrics (followers, likes) without conversion data
- Anything that changes hourly (real-time dashboards = procrastination)

## Cadence

- **Weekly:** Glance at total revenue + new sales (5 min, Friday)
- **Monthly:** Full review + update trackers (30 min, last Friday of month)
- **Quarterly:** Strategic review + decisions about pricing, products, channels (2 hours)
- **Annually:** Year-in-review + next-year planning (half day)

## Where the Data Comes From

- **Sales / revenue:** Gumroad dashboard
- **Conversion rate:** Vercel Analytics + Plausible (page visits) ÷ Gumroad sales
- **Email metrics:** Gumroad Workflows or Beehiiv dashboard
- **Refunds:** Gumroad
- **Affiliate %:** Gumroad affiliate dashboard

Don't rely on memory. The trackers in this folder are the canonical record.
