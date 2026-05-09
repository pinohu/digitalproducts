# n8n Implementation Plan

Status: first-pass build sequence; not yet executed in a live n8n instance.
Related issue: DIG-11
Implementation target: `n8n.audreysplace.place`

This plan converts the workflow specs in this folder into an executable build order. It intentionally keeps Sprint 1 launch-critical work on native Gumroad until the manual path is proven once.

## Guiding decisions

1. Native Gumroad Workflows are the Sprint 1 default for post-purchase and abandoned-cart email. n8n augments logging, notifications, and later cross-tool automation.
2. Git remains the durable source of truth. n8n may update repo files through GitHub API commits, but the repo owns backlog, analytics, sprint reviews, and launch records.
3. Build low-risk event automation before complex scheduled launch orchestration.
4. Do not treat any workflow as production until credentials, a test payload, error handling, and rollback/manual fallback are verified.

## Phase 0 — Environment and credential gate

Target timing: before any workflow build.

Deliverables:
- Confirm n8n instance access at `n8n.audreysplace.place`.
- Create a dedicated n8n credential inventory.
- Create a test notification destination for workflow failures.
- Confirm GitHub write path to `pinohu/digitalproducts`.

Required credentials:

| Credential | Needed for | Required before phase |
|---|---|---|
| n8n admin/editor access | all workflows | Phase 0 |
| GitHub PAT with contents write access to `pinohu/digitalproducts` | idea discovery, analytics, launch status commits | Phase 0 |
| Gumroad API key | post-purchase, analytics, discount/product operations | Phase 1 |
| Gumroad webhook secret/signature setup | post-purchase/refund events | Phase 1 |
| Notification channel credential (email/Slack/Discord) | all workflow failure alerts | Phase 0 |
| Reddit OAuth/PRAW app | idea discovery | Phase 2 |
| Anthropic API key | idea discovery, optional launch copy checks | Phase 2 |
| Plausible/Vercel Analytics API token | analytics aggregation | Phase 3 |
| Email platform API key, if not native Gumroad | launch automation | Phase 4 |
| LinkedIn/Taplio/X credentials | launch social automation | Phase 4 |

## Phase 1 — Post-purchase and refund augmentation

Spec: `post-purchase-automation.md`

Why first:
- Lowest complexity.
- Runs only after a real customer event.
- Gives immediate value by recording first-sale evidence and keeping analytics current.

Build order:
1. Create `/gumroad/purchase` webhook trigger.
2. Add Gumroad signature validation.
3. Add test-purchase branch: log test events without counting revenue.
4. Add sale logging to `analytics/by-product/<slug>.md` and `analytics/revenue-tracker.md` through GitHub API.
5. Add notification node for new sale.
6. Add refund webhook as a separate workflow or sibling branch.
7. Test with a 100% discount code purchase and then a small real purchase.

Production gate:
- Test purchase appears in logs but not revenue totals.
- Real purchase records product, price, discount code, purchase ID, and timestamp.
- Refund path reverses or annotates the sale.
- GitHub commit conflict retry is verified or manually documented.

Manual fallback:
- Record sale/refund manually in analytics files if webhook processing fails.

## Phase 2 — Idea discovery pipeline

Spec: `idea-discovery-pipeline.md`

Why second:
- Highest compounding leverage after Sprint 1.
- Does not block the current SuiteDash launch.
- Creates future sprint candidates automatically.

Build order:
1. Create a manually triggered test version before enabling cron.
2. Configure subreddit list and lookback variables.
3. Pull Reddit top/week payloads for one subreddit.
4. Normalize thread payloads.
5. Send batched payload to Anthropic using the repo mining prompt.
6. Parse candidate ideas and filter score >= 25.
7. Append entries to `01-market-research/idea-discovery/idea-backlog.md` through GitHub API.
8. Send summary notification.
9. Enable weekly Monday cron only after one successful manual run.

Production gate:
- One manual run against a known subreddit creates either a valid backlog commit or a clear no-candidates notification.
- Duplicate prevention is handled by URL/title matching before commit.
- Anthropic and Reddit rate-limit retries are configured.

Manual fallback:
- Run `tools/reddit_miner.py` and `tools/idea_scorer.py` locally, then manually append backlog entries.

## Phase 3 — Analytics aggregation

Spec: `analytics-aggregation.md`

Why third:
- Requires real Gumroad sales and analytics URLs.
- Useful after the first launch starts generating data.

Build order:
1. Pull Gumroad sales for the weekly window.
2. Group by product and refund status.
3. Pull page-view data from the selected analytics source.
4. Compute conversion rates.
5. Update `analytics/revenue-tracker.md` and `analytics/conversion-tracker.md` in one GitHub commit.
6. Send weekly summary notification.

Production gate:
- Handles zero-sales week without failing.
- Handles missing analytics token by using `N/A` and notifying operator.
- Weekly summary reconciles with the Gumroad dashboard for one known period.

Manual fallback:
- Update analytics markdown files manually from Gumroad dashboard once per week.

## Phase 4 — Launch automation

Spec: `launch-automation.md`

Why last:
- Highest blast radius.
- Depends on knowing the real launch cadence after 1-2 manual launches.
- Email and social accounts require careful approval gates.

Build order:
1. Start with a dry-run workflow that loads product context and validates prerequisites only.
2. Add manual approval before Email 1.
3. Add wait-node schedule for launch emails.
4. Add manual approval before final last-call emails.
5. Add optional social posting only after email-only automation is stable.
6. Add founding-discount expiration update only after Gumroad API writes are tested on a sandbox or low-risk product.

Production gate:
- Dry run confirms sales page, offer brief, launch sequence, product URL, and checkout URL exist.
- Test launch uses shifted dates and a private/test recipient list.
- Manual fallback copy is included in every failure alert.

Manual fallback:
- Send launch emails manually from the source files in `05-email-workflows/by-product/<slug>/`.
- Update discount code and sales page manually in Gumroad/repo.

## Cross-workflow dependencies

| Dependency | Blocks | Notes |
|---|---|---|
| Gumroad product URL and checkout URL | Phase 1, Phase 3, Phase 4 | Sprint 1 still needs operator activation before automation can bind to real IDs. |
| First test purchase | Phase 1 production, analytics validation | Required before first-sale DoD can be automated. |
| GitHub PAT | Phase 1-3 durable updates | Use least privilege; store only in n8n credentials. |
| Notification channel | All phases | Required so failures do not silently disappear. |
| Reddit + Anthropic credentials | Phase 2 | Not needed for Sprint 1 launch. |
| Analytics token | Phase 3 | Can start with manual/N/A traffic counts until installed. |
| Email/social API access | Phase 4 | Defer until native/manual launch path proves cadence. |

## Sprint 1 recommendation

For The Good Parts of SuiteDash:
- Use native Gumroad setup for Day 14 launch operations.
- Build Phase 1 only after Gumroad product and webhook settings exist.
- Defer Phase 2-4 until the first product is live or the operator explicitly prioritizes automation over launch execution.
- Do not let n8n availability block Gumroad upload, proof collection, or first sale.
