# Tools

Python scripts that automate the highest-leverage parts of the digital products pipeline. Run from a terminal; output goes into the repo.

## What's Here

| Script | What It Does | Cadence |
|---|---|---|
| [`idea_scorer.py`](./idea_scorer.py) | Interactive CLI to score an idea against the 50-point rubric | Per idea |
| [`reddit_miner.py`](./reddit_miner.py) | Mine pain points from configured subreddits using PRAW | Weekly |
| [`trends_checker.py`](./trends_checker.py) | Check Google Trends trajectory for candidate keywords | Per idea (validation phase) |
| [`product_bootstrapper.py`](./product_bootstrapper.py) | Scaffold a new product folder with the standard structure | Per new product |
| [`dpops.py`](./dpops.py) | Unified `dpops <subcommand>` wrapper around all four scripts | As needed |

## Setup

### 1. Python environment

Requires Python 3.10+. From the repo root:

```bash
cd tools/
python -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 2. API credentials

Some scripts need API keys. Create `tools/.env` (gitignored):

```bash
# Reddit (https://www.reddit.com/prefs/apps — create a "script" app)
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USER_AGENT=dynasty-empire-mining/1.0 by u/yourusername

# Anthropic (https://console.anthropic.com)
ANTHROPIC_API_KEY=sk-ant-...

# GitHub (use a fine-grained PAT with contents:write on pinohu/digitalproducts)
GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
GITHUB_REPO=pinohu/digitalproducts
```

### 3. Configuration

Each script reads from `tools/config.yaml` for non-secret settings (subreddits to mine, scoring thresholds, etc.). A starter config is included.

## Usage

### Score an idea interactively

```bash
python idea_scorer.py
```

Walks you through the 5 dimensions, asks for justifications, computes the total, generates the backlog entry, and (with confirmation) appends to `01-market-research/idea-discovery/idea-backlog.md`.

### Mine Reddit for new candidates

```bash
python reddit_miner.py --subreddits SaaS,Solopreneur --lookback 7
```

Pulls top threads from configured subreddits, extracts pain-point patterns, sends to Claude API for analysis, and outputs candidate ideas in the standard format.

By default the markdown output lands at `01-market-research/idea-discovery/candidate-ideas/YYYY-MM-DD.md`, with a companion `.json` file at the same path. Override with `--output <path>` and `--json-output <path>`.

Use `--dry-run` to skip the Claude API call and save the raw matched threads only. With `--dry-run`, no `ANTHROPIC_API_KEY` is required.

### Check trends for a candidate

```bash
python trends_checker.py "your candidate keyword"
```

Returns 24-month trend data from Google Trends. Output includes growth rate, confidence level, and a recommendation that maps to Dimension 4 of the scoring rubric.

The script handles Google Trends rate-limiting (HTTP 429) with exponential-backoff retries (5s, 10s, 20s, 40s by default). If pytrends still fails after `--max-retries`, the script exits with code 2 and prints `Trend data unavailable: …` so the caller can distinguish rate-limit failures from other errors.

### Bootstrap a new product folder

```bash
python product_bootstrapper.py --slug 02-newsletter-monetization --title "Newsletter Monetization Playbook"
```

Creates the standard product folder structure under `03-products/` with all the right subfolders, README, and stub files for offer/sales-page/email-workflow. Slug must follow `NN-kebab-case-slug` format.

The exact set of files/folders created is driven by `tools/config.yaml -> product_bootstrap.per_product_files`. Re-running against an existing slug is **idempotent**: existing files are left untouched (no clobbering), and only missing pieces are created. Use `--dry-run` to preview without writing and `--yes` to skip the confirmation prompt.

### Unified CLI: `dpops.py`

Instead of remembering each script's filename, you can run everything through a single entrypoint:

```bash
python tools/dpops.py score                                                  # idea_scorer.py
python tools/dpops.py mine --subreddits SaaS,Solopreneur --dry-run           # reddit_miner.py
python tools/dpops.py trends "newsletter monetization"                       # trends_checker.py
python tools/dpops.py bootstrap --slug 02-newsletter-monetization \           # product_bootstrapper.py
    --title "Newsletter Monetization Playbook"
```

All flags after the subcommand are passed through unchanged, so per-script docs still apply. `python tools/dpops.py --help` lists subcommands.

### Idea scorer batch mode

`idea_scorer.py --batch ideas.txt` (one idea name per line; `#` comments allowed) produces a stub backlog entry per idea — useful for quickly seeding the backlog from a brainstorm dump. Combine with `--dry-run` to preview entries without appending. The original interactive flow is unchanged.

## Tests

```bash
pip install -r requirements.txt   # pytest is now in requirements
pytest tools/tests/
```

Tests cover:

- `IdeaScore.total / decision / status_bucket` and `render_backlog_entry` (no API calls — pure data).
- `product_bootstrapper` against a `tmp_path` fake repo (verifies every per-product file/folder is created and that re-runs are idempotent).
- `trends_checker.fetch_trends` growth-rate computation and 429 retry/backoff logic via mocked pytrends.

Tests do not require any API keys or network access.

## Output Conventions

All scripts write to the repo (this directory's parent) when committing changes. They never write to other paths. They never delete files unless explicitly run with `--delete` flags.

Every script that writes to the repo:
1. Pulls latest before any change
2. Stages the changes locally
3. Shows a diff and asks for confirmation (unless `--auto-commit` is set)
4. Commits with a structured message: `"feat(scope): <change>"` or `"chore(automation): <change>"`
5. Pushes if `--push` is set; otherwise leaves the commit local for review

## Failure Modes

| Failure | Cause | Fix |
|---|---|---|
| `ImportError: praw` | Virtualenv not activated | `source .venv/bin/activate` then re-run |
| `401 Unauthorized` (Reddit) | Bad credentials | Verify `.env` matches Reddit app credentials |
| `429 Rate Limit` (Anthropic) | Too many requests | Lower batch size in config.yaml |
| `Permission denied` (GitHub push) | Token expired | Refresh GitHub PAT, update `.env` |
| `Trend data unavailable` (pytrends) | Google Trends temporarily blocking after retries | Wait 1 hour, retry; pytrends has known intermittent issues. Exit code 2 indicates rate-limit exhaustion specifically. |
| `Missing required env vars: ANTHROPIC_API_KEY` (reddit_miner) | `.env` missing keys for non-dry-run mining | Add key to `tools/.env` or rerun with `--dry-run` |

## Running From Flint VM

If you want to run these long-running scripts on Flint instead of locally:

```bash
ssh pinohu@172.20.192.46
cd ~/digitalproducts/tools  # repo cloned there
source .venv/bin/activate
nohup python reddit_miner.py --subreddits SaaS,Solopreneur,Entrepreneur --lookback 30 > miner.log 2>&1 &
```

The script runs in background; check `miner.log` for progress.

## Promoting a Script to n8n

When a script is running reliably weekly+ and you want it to run autonomously without you, port it to n8n:

1. Read the equivalent n8n workflow spec in [`/automation/n8n-workflows/`](../automation/n8n-workflows/)
2. Build the n8n workflow following the spec
3. Disable the local cron (if any)
4. Local script becomes a debugging/dev tool; n8n runs production

This separation keeps local scripts fast to iterate (Python in a virtualenv) while production work runs in the orchestrated environment.
