# Workflow: Post-Purchase Automation

Triggered on Gumroad purchase webhook. Logs the sale, fires the post-purchase email sequence (or augments Gumroad's native workflow), and updates analytics.

> **Note:** Gumroad has native Workflows for post-purchase email automation. This n8n workflow is for **augmenting** Gumroad's native flow with cross-tool actions (analytics logging, Slack notifications, lead-magnet upsells, etc.) — not replacing it.

## Trigger

- Type: Webhook
- HTTP method: POST
- Path: `/gumroad/purchase`
- Authentication: Gumroad webhook signature verification
- Configure in Gumroad: Settings → Advanced → Ping URL

## Webhook Payload (From Gumroad)

```json
{
  "seller_id": "...",
  "product_id": "prod_...",
  "product_name": "The Good Parts of SuiteDash",
  "product_permalink": "https://gumroad.com/l/...",
  "permalink": "...",
  "price": 4900,
  "currency": "USD",
  "email": "buyer@example.com",
  "full_name": "Buyer Name",
  "purchase_id": "...",
  "purchaser_id": "...",
  "discount_code": "LAUNCH50",
  "test": false,
  "timestamp": "2026-05-20T10:22:14Z"
}
```

## Node-by-Node Build

### Node 1: Webhook Trigger
- Receives Gumroad ping
- Validates signature

### Node 2: Filter Test Purchases
- Type: IF
- Condition: `test == false`
- On test purchase: Skip downstream nodes, log only

### Node 3: Log Sale to Repo Analytics
- Type: HTTP Request to GitHub API
- Updates `analytics/by-product/<slug>.md` with the sale row
- Updates `analytics/revenue-tracker.md` monthly totals

### Node 4: Send Slack/Email Notification
- "🎉 New sale: {{full_name}} bought {{product_name}} for ${{price/100}}."

### Node 5: Tag in Email Platform
- Type: HTTP Request
- Adds buyer to "buyers-{slug}" tag in ConvertKit/Beehiiv (when graduated)
- For Gumroad-native phase: skip this node, native workflow handles tagging

### Node 6: Cross-Sell Trigger
- Type: IF
- Condition: Buyer has previously purchased product N-1 in the catalog
- On match: Add to "high-LTV cohort" segment for next bundle pitch

### Node 7: Update Active Sprint Status (If Launch Day)
- Type: IF + HTTP Request
- Condition: Today is Day 0 of an active launch
- On match: Increment launch-day counter in `10-execution-sprints/current-sprint.md`

### Node 8: Refund Webhook Handler (Separate Workflow)
- Type: Webhook (separate from main flow, but triggered by Gumroad refund pings)
- Updates analytics with refund
- Removes buyer from "active customer" tags
- Logs refund reason if provided

## Error Handling

- **GitHub API failure:** Retry 3x with backoff. If still fails, send admin alert with the sale data so it can be logged manually.
- **Email tagging failure:** Don't block the workflow. Log error, continue.

## Why Augment Instead of Replace

Gumroad's native Workflows do email automation well. They handle:
- Welcome / download email (instant)
- Time-delayed follow-ups
- Abandoned cart (24-hour automated)

What Gumroad doesn't do:
- Cross-tool sync (Slack notifications, analytics logging)
- Conditional logic ("if this is buyer's 2nd purchase, do X")
- Cross-product cohort management

That's what this n8n workflow handles. Best of both worlds.

## Testing

1. Make a $0 test purchase with a 100% discount code
2. Verify the test=true path runs (logs only, no real actions)
3. Make a small ($1) real purchase
4. Verify all nodes fire correctly
5. Refund the test purchase
6. Verify the refund webhook handler runs

## Performance

Per-purchase webhook processing time: <2 seconds (well within Gumroad's 5-second webhook timeout). If processing exceeds 5 seconds, Gumroad retries — be careful with synchronous third-party API calls.
