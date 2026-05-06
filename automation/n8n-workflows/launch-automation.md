# Workflow: Launch Automation

Orchestrates the 7-email launch sequence + 6 scheduled social posts over 7 days. Triggered manually at the start of a launch with the product's slug, then runs autonomously.

## Trigger

- Type: Manual / Webhook
- Input parameters:
  - `product_slug` (e.g., "01-suitedash-good-parts")
  - `launch_datetime` (ISO 8601, e.g., "2026-05-20T09:00:00-04:00")
  - `founding_price_expires` (ISO 8601, typically launch_datetime + 144 hours)

## Architecture

This workflow uses n8n's **Wait** nodes to schedule events across 7 days. The workflow stays "live" for the duration of the launch.

```
Trigger (manual)
    ↓
Load product context from repo
    ↓
[Day 0, 09:00] Send Email 1 (The Reveal) → Post on LinkedIn (Live announcement)
    ↓ (Wait 7 hours)
[Day 0, 16:00] Send Email 2 (What's Inside)
    ↓ (Wait 17 hours)
[Day 1, 09:00] Send Email 3 (First Reactions) → Post on LinkedIn (testimonial)
    ↓ (Wait 24 hours)
[Day 2, 09:00] Send Email 4 (Use Case)
    ↓ (Wait 48 hours)
[Day 4, 09:00] Send Email 5 (Objection Handling)
    ↓ (Wait 24 hours)
[Day 5, 09:00] Send Email 6 (Cost of Inaction)
    ↓ (Wait 24 hours)
[Day 6, 09:00] Send Email 7 (Last Call AM) → Post on LinkedIn (final reminder)
    ↓ (Wait 11 hours)
[Day 6, 20:00] Send Email 8 (Last Call - 4 hours left)
    ↓ (Wait 4 hours)
[Day 6, 23:59] Disable founding-price discount in Gumroad
    ↓
[Day 7, 09:00] Update sales page to full price + send post-launch thank-you
```

## Node-by-Node Build (Key Nodes)

### Node 1: Webhook Trigger
- Type: Webhook
- HTTP method: POST
- Path: `/launch/start`
- Authentication: Header (Bearer token)
- Required body fields: `product_slug`, `launch_datetime`, `founding_price_expires`

### Node 2: Load Product Context
- Type: HTTP Request (multiple, parallel)
- Pulls from GitHub:
  - `02-offers/by-product/{slug}.md` (offer brief)
  - `04-sales-pages/by-product/{slug}.md` (sales page)
  - `05-email-workflows/by-product/{slug}/launch-sequence.md` (customized launch emails)

### Node 3: Validate Prerequisites
- Type: IF node
- Conditions:
  - Offer brief exists
  - Sales page exists
  - All 7 launch emails are drafted (not template placeholders)
  - Email tool credentials are valid
- On fail: Send error notification, abort

### Node 4: Wait Until Launch Time
- Type: Wait (Until DateTime)
- DateTime: `launch_datetime`

### Node 5-N: Email Send Nodes (×8)
- Type: HTTP Request to email platform
  - Gumroad Workflows: trigger via Gumroad API (if using Gumroad-native)
  - Beehiiv/ConvertKit: API calls per platform
- One node per email in the sequence
- Each email body pulled from the loaded launch sequence content

### Node 6-M: Social Post Nodes (×3-6)
- Type: HTTP Request to Taplio API or LinkedIn API
- Posts the Day 0 announcement, Day 2 testimonial post, Day 6 last-call

### Node Z: Disable Founding Price (Day 6 23:59)
- Type: HTTP Request to Gumroad API
- Endpoint: PATCH discount code expiration → past
- Or: PATCH product price → full post-founding price

### Node Z+1: Final Cleanup (Day 7)
- Update sales page (commit changes to GitHub repo)
- Send notification: "Launch complete. {{total_sales}} sales. {{total_revenue}} revenue."

## Error Handling

- **Email send failure:** Retry once after 5 min. If still fails, send Slack/email alert with the failed email content for manual send.
- **Wait node interruption (n8n restart):** n8n persists Wait state, so workflow resumes automatically.
- **Missing prerequisite:** Abort with clear error, don't partially launch.

## Variations

### For Re-Launches
Same workflow, with reduced cadence (3-4 emails instead of 7) and shorter founding-price window (24 hours vs. 48). Trigger with parameter `mode=relaunch`.

### For Bundle Launches
Adds a Day 0 email targeting existing single-product buyers with a bundle-upgrade offer.

## Manual Override Points

The workflow should include manual approval gates at:
- Before sending Email 1 (final go/no-go)
- Before sending Email 7 (last-call confirmation)

These prevent autonomous catastrophes like "we launched and the sales page was broken."

## Testing

Before using on a real launch:

1. Build the workflow with all dates/times shifted forward by 1 day in a test environment
2. Use Gumroad test mode (100% discount code) to validate email triggers
3. Send test emails to a personal address, not the real list
4. Validate social posts go to a test/private LinkedIn account
5. Run end-to-end once before the first real launch

## Pre-Launch Checklist Inside the Workflow

The workflow's first action after manual trigger should be running through `06-launch-playbooks/pre-launch-checklist.md` items via API calls to verify the product is launch-ready. If any fail, abort and report.
