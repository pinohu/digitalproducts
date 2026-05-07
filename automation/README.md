# Automation

The cross-cutting automation layer. Where the framework's templates and stages get connected into a running pipeline that minimizes manual work.

## Files in this folder

- [`pipeline.md`](./pipeline.md) — The end-to-end automation pipeline, stage by stage.
- [`flint-delegation.md`](./flint-delegation.md) — How to delegate background work to the Flint VM.
- [`prompt-library.md`](./prompt-library.md) — Index of all Claude / LLM prompts used across the system.
- [`claude-skills/`](./claude-skills/) — Claude skill specs that can be installed at `/mnt/skills/user/<skill-name>/SKILL.md`.
- [`n8n-workflows/`](./n8n-workflows/) — n8n workflow specifications (markdown describing nodes, triggers, data flow).

## Three Layers of Automation

The repo separates automation into three layers, each with different infrastructure:

### Layer 1: Claude Skills (Conversational, On-Demand)

Skills are markdown files that load specific instructions and templates into Claude's context when triggered by user intent. They're great for:
- Tasks that need judgment + structured output (offer engineering, sales page writing)
- Tasks that happen episodically (once per product launch, not every day)
- Tasks where the human stays in the loop

See [`claude-skills/`](./claude-skills/).

### Layer 2: n8n Workflows (Scheduled, Headless)

n8n at `n8n.audreysplace.place` runs workflows on schedules or webhook triggers. Used for:
- Daily/weekly mining of data sources
- Email automation sequences
- Webhook-driven post-purchase actions
- Periodic analytics pulls
- Cross-tool sync

See [`n8n-workflows/`](./n8n-workflows/).

### Layer 3: Python Tools (Local, Manual or CLI)

Scripts in [`/tools/`](../tools/) are run from a terminal. Best for:
- Heavy data processing (Reddit scrapes, trend analysis)
- One-off operations (bootstrapping a new product folder)
- Local experimentation before promoting to n8n
- Anything that needs a Python ecosystem (PRAW, pytrends, pandas)

## How These Layers Talk to Each Other

```
                  ┌──────────────────────────┐
                  │   GitHub repo (this)     │
                  │   git as state store     │
                  └─────────────┬────────────┘
                                │
              ┌─────────────────┼─────────────────┐
              │                 │                 │
              ▼                 ▼                 ▼
      ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
      │   Claude     │  │   n8n        │  │   Python     │
      │   (this app) │  │  workflows   │  │   tools/     │
      └──────┬───────┘  └──────┬───────┘  └──────┬───────┘
             │                 │                 │
             │                 │                 │
             ▼                 ▼                 ▼
      Conversational      Scheduled /       Local/manual
      reasoning,          webhook-driven    data work,
      judgment calls,     headless tasks    bootstrapping,
      content drafting    (mining, emails,  one-off ops
                          analytics sync)
```

The repo itself is the shared state. Claude updates `idea-backlog.md`, n8n watches the file via Git webhook + commits new candidates from scheduled mining, Python tools generate new product folder scaffolds.

## What's Currently Live

| Component | Status | Notes |
|---|---|---|
| Claude skills (specs) | ✅ Drafted | Installation requires copying to user skills folder |
| n8n workflow specs | ✅ Drafted | Implementation requires building in n8n.audreysplace.place |
| Python tools | ✅ Runnable local stack documented | `tools/setup.sh` installs deps; `tools/verify_tools.py` checks imports/config/secrets offline; live Reddit/Trends runs still need credentials/network |
| Flint delegation patterns | ✅ Drafted | See `flint-delegation.md` |

## What's Pending (User Action)

- [ ] Install Claude skills to user skill directory (see each skill's installation note)
- [ ] Build n8n workflows from specs (each spec includes node-by-node instructions)
- [ ] Set up Python virtualenv + real API keys per `tools/README.md`; run `python tools/verify_tools.py` from an activated environment
- [ ] Wire Flint VM to handle the Reddit miner cron schedule
- [ ] Add real external credentials before production writes: Reddit app, Anthropic API key, n8n credentials, Gumroad access, Neon database URL if used, and Vercel project/token if deploying landing pages
