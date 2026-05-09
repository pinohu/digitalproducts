# Analytics

Performance tracking. Where the numbers live. The single source of truth for "how is the catalog actually doing?"

## Files in this folder

- [`revenue-tracker.md`](./revenue-tracker.md) — Monthly and per-product revenue tracking.
- [`conversion-tracker.md`](./conversion-tracker.md) — Sales page conversion, email conversion, bundle conversion across products.
- `by-product/<slug>.md` — Detailed per-product metrics, launch baselines, and 7-day / 30-day / 90-day review notes.

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

- **7 days after launch:** Check traffic quality, conversion, support replies, refund signals, and the first concrete sales-page/channel changes.
- **30 days after launch:** Update revenue/conversion trackers, decide pricing/tier/affiliate/next-channel actions, and capture testimonial outcomes.
- **90 days after launch:** Run the strategic product review: optimize, bundle, create a variation, or promote the next product from the backlog.
- **Monthly outside launch windows:** Full review + update trackers (30 min, last Friday of month).
- **Annually:** Year-in-review + next-year planning (half day).

## Where the Data Comes From

- **Sales / revenue:** Gumroad dashboard
- **Conversion rate:** Vercel Analytics + Plausible (page visits) ÷ Gumroad sales
- **Email metrics:** Gumroad Workflows or Beehiiv dashboard
- **Refunds:** Gumroad
- **Affiliate %:** Gumroad affiliate dashboard

Don't rely on memory. The trackers in this folder are the canonical record.
