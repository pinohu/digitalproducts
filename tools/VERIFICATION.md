# Tools Verification Notes

Last verification pass: 2026-05-07
Owner: Automation Engineer
Issue: DIG-8 — Make the idea-discovery and bootstrap tools runnable and documented

## Local environment result

The WSL host has Python 3.12.3, but `python3 -m venv` failed because the OS package `python3.12-venv` / `python3-venv` is not installed and sudo requires a password.

Fallback used successfully during initial triage:

```bash
cd tools
uv venv .uv-venv
source .uv-venv/bin/activate
uv pip install -r requirements.txt
```

After adding the setup script, the repeatable command was verified successfully:

```bash
cd tools
UV_LINK_MODE=copy bash setup.sh
source .venv/bin/activate
python verify_tools.py
```

`tools/setup.sh` now automates this path: it tries standard `python -m venv` first, then falls back to `uv` when available, and prints the required `sudo apt-get install python3-venv` remediation when neither route works.

## Commands verified

Run from repo root:

```bash
cd tools
source .uv-venv/bin/activate
python -m py_compile idea_scorer.py reddit_miner.py trends_checker.py product_bootstrapper.py
python idea_scorer.py --help
python reddit_miner.py --help
python trends_checker.py --help
python product_bootstrapper.py --help
python product_bootstrapper.py --slug 99-test-product --title "Test Product" --dry-run --yes
```

Result: PASS for compile, help output, and product bootstrap dry-run.

## Script-by-script notes

| Script | Verification status | Requires real credentials? | Notes |
|---|---:|---:|---|
| `idea_scorer.py` | PASS: compiles and `--help` runs | No | `--idea` now pre-fills the idea name instead of prompting for it first. It is still intentionally interactive for scoring evidence. |
| `reddit_miner.py` | PASS: compiles and `--help` runs | Yes | Requires Reddit app credentials for PRAW. `--dry-run` skips Claude analysis but still needs Reddit credentials because it fetches real Reddit threads. |
| `trends_checker.py` | PASS: compiles and `--help` runs | No API key, but uses external Google Trends | `pytrends` can be intermittently blocked/rate-limited by Google. Treat failures as external-system flakiness unless compile/help checks fail. |
| `product_bootstrapper.py` | PASS: compiles, `--help` runs, dry-run works | No | `--dry-run --yes` is safe for repeatable verification; it writes no files. |

## Required secrets inventory

Copy `tools/.env.example` to `tools/.env` and fill only real values. `tools/.env` is gitignored.

| Variable | Used by | Required for local verification? | Required for production use? | Source |
|---|---|---:|---:|---|
| `REDDIT_CLIENT_ID` | `reddit_miner.py` | No for help/compile; yes for real/dry-run mining | Yes | Reddit script app at https://www.reddit.com/prefs/apps |
| `REDDIT_CLIENT_SECRET` | `reddit_miner.py` | No for help/compile; yes for real/dry-run mining | Yes | Reddit script app |
| `REDDIT_USER_AGENT` | `reddit_miner.py` | No | Yes | Descriptive app user agent, e.g. `digitalproducts-mining/1.0 by u/<username>` |
| `ANTHROPIC_API_KEY` | `reddit_miner.py` candidate extraction | No if using `--dry-run` | Yes for Claude/Anthropic extraction | Anthropic Console |
| `GITHUB_TOKEN` | Future commit/push automation | No | Yes if tools/n8n push repo changes | Fine-grained GitHub PAT with contents write on this repo |
| `GITHUB_REPO` | Future commit/push automation | No | Yes if tools/n8n push repo changes | Defaults to `pinohu/digitalproducts` |
| `N8N_BASE_URL` / `N8N_API_KEY` | n8n implementation work | No | Yes for n8n import/activation automation | n8n instance/API settings |
| `GUMROAD_ACCESS_TOKEN` | Gumroad product/sales/email automation | No | Yes before storefront/product workflow writes | Gumroad application/API access |
| `NEON_DATABASE_URL` | Analytics/event storage | No | Yes before Neon-backed analytics | Neon project connection string |
| `VERCEL_TOKEN` / `VERCEL_PROJECT_ID` | Landing-page deployment automation | No | Yes before Vercel deployment automation | Vercel account/project settings |

## External blockers still requiring real access

- Reddit: real script app credentials are required before `reddit_miner.py` can fetch threads.
- Anthropic: real API key is required before Reddit mining can produce Claude-assisted candidate extraction.
- Google Trends: no credential is required, but Google can rate-limit pytrends; retry later before treating it as a code failure.
- n8n: workflow specs exist, but importing/activating workflows still requires n8n credentials and instance access.
- Gumroad: product upload, workflow activation, abandoned cart settings, and storefront status still require real Gumroad access.
- Neon: analytics automation cannot persist launch metrics until a real Neon project and connection string exist.
- Vercel: landing page deployment and ikeohu.com linkage require real Vercel project credentials and DNS/project access.
