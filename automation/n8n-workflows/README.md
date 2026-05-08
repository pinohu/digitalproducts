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

The specs are the canonical reference. Alongside each spec there is now an importable n8n JSON file (same basename) generated from the spec — see [Importing the Workflows](#importing-the-workflows) below. The specs remain the source of truth; if you change a workflow's behavior, update the spec and re-export the JSON.

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

## Importing the Workflows

Each spec has a sibling `.json` file ready to import into n8n:

| Workflow file | Spec |
|---|---|
| `idea-discovery-pipeline.json` | `idea-discovery-pipeline.md` |
| `launch-automation.json` | `launch-automation.md` |
| `post-purchase-automation.json` | `post-purchase-automation.md` |
| `analytics-aggregation.json` | `analytics-aggregation.md` |

### Steps

1. Download the desired `.json` file from this directory (or clone the repo).
2. In your n8n instance (e.g. `n8n.audreysplace.place`), go to **Workflows** in the left sidebar.
3. Click **Add workflow → Import from File** (or the three-dot menu → **Import from File**).
4. Select the downloaded `.json`. The workflow loads in the editor with `active: false`.
5. For every node that shows a red credential warning, open it and pick the matching credential from your n8n credential store (or create one). The exported JSON ships with placeholder `{ "id": "REPLACE_ME", ... }` references — no secrets are embedded.
6. For `launch-automation.json`, also replace `REPLACE_ME_SUBWORKFLOW_ID_EMAIL_SENDER` in the three Execute Workflow nodes with the ID of your own email-sender sub-workflow (the parent workflow is split this way to stay under 25 nodes).
7. Save, then run once manually with safe inputs before flipping the **Active** toggle on.

### Credentials Each Workflow Expects

| Workflow | Credentials referenced (by placeholder name) |
|---|---|
| `idea-discovery-pipeline.json` | Reddit OAuth2, Anthropic API (x-api-key), GitHub PAT (Bearer), Slack API |
| `launch-automation.json` | Launch Webhook Bearer Token, GitHub PAT (Bearer), Slack API, Taplio / LinkedIn API, Gumroad API Key |
| `post-purchase-automation.json` | Gumroad Webhook Signing Secret, GitHub PAT (Bearer), Slack API, ConvertKit/Beehiiv API, Gumroad API Key |
| `analytics-aggregation.json` | Gumroad API Key, Plausible API, GitHub PAT (Bearer), Slack API |

Credential placeholders all use `id: "REPLACE_ME"` so n8n will surface the missing reference clearly in the editor — there is no chance of an exported credential leaking through.

## Rate Limits

- **Anthropic API:** Per-minute and per-day limits depending on tier. Idea discovery should batch into chunks small enough to stay under per-call token limits.
- **Reddit API:** 60 requests / minute per OAuth app. PRAW handles this transparently.
- **Gumroad API:** Documented limits at gumroad.com docs. Generally not a constraint at our volume.
- **GitHub API:** 5,000/hour with PAT. Idea-backlog updates are well within limits.
