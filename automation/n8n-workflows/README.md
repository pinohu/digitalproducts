# n8n Workflows

Specifications for the n8n workflows that automate scheduled and event-driven parts of the digital product pipeline. Implementation target: `n8n.audreysplace.place`.

## Available Workflow Specs

| Workflow | Trigger | What It Does |
|---|---|---|
| [`idea-discovery-pipeline.md`](./idea-discovery-pipeline.md) | Cron (weekly) | Mines Reddit, runs Claude analysis, appends candidates to idea-backlog.md |
| [`launch-automation.md`](./launch-automation.md) | Manual + scheduled | Sends the 7-email launch sequence with social posts |
| [`post-purchase-automation.md`](./post-purchase-automation.md) | Webhook (Gumroad purchase) | Triggers post-purchase email sequence + analytics logging |
| [`analytics-aggregation.md`](./analytics-aggregation.md) | Cron (weekly) | Pulls Gumroad data, updates analytics/revenue-tracker.md |

## Format

Each spec describes:
- **Trigger node** (cron schedule, webhook URL, manual)
- **Step-by-step nodes** with input/output schemas
- **Required credentials** (API keys, OAuth)
- **Error handling** strategy
- **Rate limit considerations**

The specs are NOT importable n8n JSON — they're build instructions. n8n's JSON format requires actual node UUIDs and is brittle to share. The instructions are designed to be implemented in n8n's visual editor in 30-60 minutes per workflow.

## Build Order

If you're starting from scratch:

1. **First: `post-purchase-automation.md`** — Lowest complexity, fires on existing customer events. Wins immediately by automating what's currently manual.
2. **Second: `idea-discovery-pipeline.md`** — Highest leverage. Once running, ideas accumulate automatically.
3. **Third: `analytics-aggregation.md`** — Eliminates the weekly Gumroad-dashboard tax.
4. **Last: `launch-automation.md`** — Most complex. Build only when you've launched 2-3 products manually and know the workflow shape.

## Credentials Setup

Before any workflow runs, configure these credentials in n8n:

| Credential | Used By | Where to Get |
|---|---|---|
| Gumroad API key | post-purchase, analytics | gumroad.com/settings/advanced |
| Anthropic API key | idea-discovery, launch | console.anthropic.com |
| Reddit API (PRAW) credentials | idea-discovery | reddit.com/prefs/apps |
| GitHub PAT (write to this repo) | idea-discovery | use existing token from Dynasty memory (gitignored in `tools/.env`) |
| Beehiiv / ConvertKit API key | launch (when graduated) | platform settings |
| LinkedIn API or Taplio | launch (social posts) | Taplio settings or LinkedIn dev portal |

## Convention: Source-of-Truth in Git

All workflow outputs that represent durable state (idea-backlog entries, analytics rows, review documents) write to this Git repo via the GitHub API rather than storing in n8n's database. This makes the repo the canonical source — n8n is just the runtime.

## Rate Limits

- **Anthropic API:** Per-minute and per-day limits depending on tier. Idea discovery should batch into chunks small enough to stay under per-call token limits.
- **Reddit API:** 60 requests / minute per OAuth app. PRAW handles this transparently.
- **Gumroad API:** Documented limits at gumroad.com docs. Generally not a constraint at our volume.
- **GitHub API:** 5,000/hour with PAT. Idea-backlog updates are well within limits.
