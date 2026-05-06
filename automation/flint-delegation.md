# Flint Delegation

How to delegate background work to the Flint VM (`pinohu@172.20.192.46`) for jobs that shouldn't tie up Claude's interactive context.

## When to Use Flint vs. Claude vs. Python Locally

| Job Type | Best Runtime | Why |
|---|---|---|
| Conversational reasoning, judgment calls, content drafting | **Claude (this app)** | Strong at synthesis, needs human in loop |
| Scheduled mining (weekly/daily) | **n8n** at `n8n.audreysplace.place` | Persistent cron, error retry, multi-step |
| Long-running data jobs (full-week Reddit pulls, large analytics) | **Flint VM** | Background-friendly, persistent state, won't time out |
| One-off scripted ops (bootstrap a product folder, score a single idea) | **Local Python** in `tools/` | Fast iteration, no infrastructure overhead |
| Cross-tool API orchestration with retries | **n8n** | Built for this |

## The Bridge

The bridge is already operational:

- **Inbox (Claude → Flint):** `POST https://claude-inbox.audreysplace.place/message`
  - Body: `{"content": "task description"}`
  - Auth: `Authorization: Bearer 1ed943c21ef9e2f60fe1189241a286d769e4191051ad2c0c035282722cb4b030`
- **Outbox (Flint → Claude):** `GET https://claude-outbox.audreysplace.place/messages`
- **Flint VM details:** SSH `pinohu@172.20.192.46`, key `~/.ssh/id_ed25519`, bridge files `~/clawd/claude-bridge/`

## Delegation Patterns for the Digital Products Pipeline

### Pattern 1: Background Reddit Mining

**When:** You want a deep mining sweep across 20+ subreddits without tying up Claude.

**How:**

1. Claude posts a task to Flint inbox:
   ```
   {
     "content": "Run full Reddit mining sweep:
     - Subreddits: [list of 20+]
     - Lookback: 14 days
     - Top 30 threads per sub
     - Apply reddit-mining.md prompt to each batch
     - Commit candidates to digitalproducts/01-market-research/idea-discovery/idea-backlog.md
     - Notify when complete"
   }
   ```
2. Flint runs `tools/reddit_miner.py` with the params, processes via Claude API, commits to repo.
3. Claude polls outbox; receives "Complete: N candidates added, top score X/50."

**Total Claude interactive time:** ~2 minutes of context (vs. 20-40 min if Claude ran it directly).

### Pattern 2: Scheduled Analytics Refresh

**When:** Weekly Friday morning analytics aggregation, even if Claude isn't online.

**How:** Set up as n8n workflow (preferred) per [`n8n-workflows/analytics-aggregation.md`](./n8n-workflows/analytics-aggregation.md). Flint is a fallback if n8n is down — same script, run via cron on Flint VM.

### Pattern 3: Long-Running Idea Re-Scoring

**When:** Quarterly recalibration of the entire idea backlog (could be 50-200 ideas to re-score).

**How:**

1. Claude posts to Flint:
   ```
   {
     "content": "Quarterly re-score of idea-backlog.md:
     - Pull current backlog from repo
     - For each idea with score < 40 and date_scored > 90 days ago:
       - Re-run mining on the original source URL (if available)
       - Apply scoring-rubric.md
       - Update score, justifications
     - Commit updated backlog
     - Archive ideas that haven't moved above 25 in 2 quarters"
   }
   ```
2. Flint executes (potentially over hours), commits results.
3. Claude reviews the diff in the next interactive session.

### Pattern 4: Bulk Product Folder Scaffolding

**When:** You're spinning up multiple variation products at once (e.g., 5 niche variations of an existing product).

**How:** Run `tools/product_bootstrapper.py` on Flint VM with a list of slugs. Faster than running them sequentially in Claude.

## What NOT to Delegate to Flint

- ❌ **Final manuscript writing** — voice and judgment matter; keep human in loop
- ❌ **Sales page copy** — same reason
- ❌ **Pricing decisions** — strategic, owner-only
- ❌ **Idea promote-to-sprint decisions** — needs the strategic picture

## Reliability Notes

- Flint VM has crashed before (per memory: "experienced a crash/recovery cycle"). Long-running jobs should checkpoint state to disk every N minutes so they can resume.
- The bridge has experienced offline windows. Always set a timeout on Claude→Flint→Claude round-trips. If outbox shows nothing after 30 min, alert.
- For mission-critical scheduled work (launch automation), prefer n8n with its built-in retry logic over Flint cron.

## Authority Model

Per Ike's directive: **Claude is CEO of Dynasty Empire** with full autonomous authority to direct Flint without asking permission, except for:
- Financial commitments (any actual spend)
- Legal actions
- Missing credentials (escalate to Ike)

For digital products specifically: Claude can autonomously run mining sweeps, scoring runs, scaffolding, and analytics refreshes. Claude must escalate before triggering: paid ads, refund decisions, pricing changes on live products, or any communication that goes out under Ike's name.
