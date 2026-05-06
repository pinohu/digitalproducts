# Workflow: Analytics Aggregation

Pulls Gumroad sales data weekly, computes per-product and aggregate metrics, updates `analytics/revenue-tracker.md` and `analytics/conversion-tracker.md` via Git commit.

## Schedule

Cron: `0 7 * * FRI` (every Friday at 7 AM EST — before the weekly newsletter writing session)

## Node-by-Node Build

### Node 1: Cron Trigger
- Schedule: `0 7 * * FRI`

### Node 2: Gumroad API — Pull Sales Data
- Type: HTTP Request
- Method: GET
- URL: `https://api.gumroad.com/v2/sales?after={{previous_friday}}&before={{this_friday}}`
- Authentication: Gumroad API key
- Returns: List of sales with product, amount, refund status, etc.

### Node 3: Aggregate by Product
- Type: Code
- Logic:
  - Group sales by product
  - Sum revenue per product
  - Count refunds per product
  - Compute net revenue (gross - refunds - 10% Gumroad fee)

### Node 4: Pull Page View Data
- Type: HTTP Request to Plausible/Vercel Analytics API
- Returns: Page views per sales page URL for the week

### Node 5: Compute Conversion Rates
- Type: Code
- Logic: Conversion rate = sales / page views per product

### Node 6: Read Current revenue-tracker.md
- Type: HTTP Request to GitHub API (GET file content)

### Node 7: Update Revenue Tracker
- Type: Code
- Logic:
  - Parse markdown table
  - Append new row for this week (or update current month's row)
  - Re-render full markdown

### Node 8: Update Conversion Tracker
- Same as Node 6-7 but for `conversion-tracker.md`

### Node 9: Commit to GitHub
- Type: HTTP Request to GitHub API
- Commits both updated files in single commit
- Message: `"chore: weekly analytics update {{week_ending}}"`

### Node 10: Generate Weekly Summary
- Type: Code
- Format:
  ```
  Week ending {{date}}:
  - Total revenue: $XXX
  - Total sales: XX
  - Top product: {{product}} ({{sales}} sales)
  - Refunds: X (rate: X%)
  - WoW revenue change: +/- X%
  ```

### Node 11: Send Summary Notification
- Type: Email or Slack
- Body: The weekly summary

## Variations

### Monthly Aggregation (Add)
- Same workflow, cron `0 8 1 * *` (1st of month at 8 AM)
- Aggregates the full month, generates a more comprehensive report
- Updates the per-month rows in revenue-tracker.md
- Includes per-channel breakdown (email vs. social vs. organic)

### Quarterly Strategic Review Generator
- Cron `0 9 1 1,4,7,10 *` (1st of Jan/Apr/Jul/Oct)
- Pulls 90 days of data
- Runs Claude API to generate strategic synthesis
- Outputs to `analytics/quarterly-reviews/Q{N}-{YYYY}.md`

## What Gets Tracked Automatically

| Metric | Frequency | Source |
|---|---|---|
| Total revenue | Weekly | Gumroad |
| Per-product revenue | Weekly | Gumroad |
| Per-product sales count | Weekly | Gumroad |
| Refund rate | Weekly | Gumroad |
| Sales page conversion rate | Weekly | Gumroad + Plausible |
| Email open/click rate | Per launch | Email platform |
| Bundle attach rate | Weekly | Gumroad |

## What Stays Manual

- **Buyer cohort LTV** — requires longitudinal tracking, easier to update quarterly by hand
- **Affiliate-driven %** — Gumroad reports it but interpretation is qualitative
- **Channel attribution** — UTMs help but final attribution is manual
- **Refund reasons** — qualitative, captured in separate refund-feedback file
- **Launch retrospectives** — narrative, written by hand using `06-launch-playbooks/post-launch-iteration.md`

## Error Handling

- **Gumroad API timeout:** Retry 3x. If still fails, skip this week's update and notify admin.
- **GitHub commit conflict:** Pull latest, retry once. If still conflicts, append to a buffer file for next week's run.
- **Page view API down:** Use cached value from previous week, flag in summary.

## Why This Matters

Without this workflow, weekly analytics is a 30-minute manual task that slips into hour-long deep-dives, gets skipped some weeks, and eventually creates blind spots. With this workflow, the weekly tax goes to ~5 minutes (review the summary, note any anomalies). The compounding effect is that strategic decisions get made on actual recent data, not stale memory of last quarter.
