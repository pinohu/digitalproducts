# Paperclip Company

This repo now has a dedicated Paperclip company and Hermes agent roster for driving the `digitalproducts` operating system to production.

## Company

- Name: `Digital Products Operating System`
- Company ID: `4b02078e-90d2-42ed-95d5-c5a54b7d3a16`
- Issue prefix: `DIG`
- Workspace: `C:\Users\ohu00\Desktop\digitalproducts`
- Paperclip API: `http://127.0.0.1:3100/api`

## Managed Agents

| Agent | ID | Responsibility |
|---|---|---|
| Chief of Staff | `95c21e7a-7117-4b68-b73c-54666e9091ad` | Owns roadmap decomposition, sprint coordination, and cross-agent delivery |
| Market Research Lead | `a3969520-53ff-40e2-b37e-c7f26ee51118` | Stage 1 research, validation, buyer/avatar evidence |
| Offer Engineer | `44b9e7c1-f999-4a14-8570-20bf33f1371a` | Pricing, bonuses, guarantees, offer briefs |
| Product Builder | `393e6eb4-69e6-4e07-b2b6-7a4e21ab2d6f` | Product manuscripts, deliverables, bonus assets |
| Funnel and Launch Ops | `183b8891-275c-4205-9f84-c163da871411` | Sales pages, launch emails, pre-launch and launch assets |
| Automation Engineer | `2a96ba46-e48e-42c9-a6a7-dacabd994d88` | Python tools, n8n workflow plans, env/setup hardening |
| Growth Analyst | `4edee279-605d-4a92-b992-beeceb880c5c` | Traffic strategy, platform readiness, analytics, review cadence |
| Quality Gatekeeper | `e91b4fd4-6223-4513-a8ff-f0d002445830` | CI quality, release evidence, Playwright/Storybook/Lighthouse/Pa11y governance |
| Accessibility Auditor | `4b57693f-bf62-42d0-8da1-471ed47ab747` | WCAG 2.2 AA, keyboard flows, focus states, usability and mobile review |
| Release Governor | `02a79e25-e730-4917-80f3-568f7458b2ea` | Release-state policy, shipped-gate truth, and manual-approval governance |

Additional operator role after bootstrap:

- `Browser Operations Lead` for browser-first SaaS execution, QA, and workflow completion where APIs are absent or incomplete

## Seeded Board

### Program Layer

- `DIG-1` Program: Drive digitalproducts repo to production
- `DIG-2` Sprint 1: Ship The Good Parts of SuiteDash to first 5 customers
- `DIG-7` Program: Stand up automation and platform foundation

### SuiteDash Sprint Work

- `DIG-3` Validate SuiteDash opportunity, avatar, and proof points
- `DIG-4` Engineer the SuiteDash offer brief, pricing, bonuses, and guarantee
- `DIG-5` Build the SuiteDash product scaffold, manuscript plan, and bonus deliverables
- `DIG-6` Draft the SuiteDash sales page, email workflows, and launch assets

### Foundation Work

- `DIG-8` Make the idea-discovery and bootstrap tools runnable and documented
- `DIG-9` Define the production storefront and platform readiness checklist
- `DIG-10` Define launch metrics, analytics baselines, and review cadence
- `DIG-11` Create the first-pass n8n and automation implementation plan

## How To Run

Start Paperclip from this repo:

```powershell
cd "C:\Users\ohu00\Desktop\digitalproducts"
.\ops\paperclip\start-paperclip.ps1
```

Stop it:

```powershell
.\ops\paperclip\stop-paperclip.ps1
```

Open the UI:

- [Paperclip UI](http://127.0.0.1:3100)

## Operator Bootstrap

Reapply the full operator setup from the repo:

```powershell
cd "C:\Users\ohu00\Desktop\digitalproducts"
.\ops\paperclip\enable-operator-mode.ps1 -EnableStrictMode
```

This bootstrap:

- syncs curated credentials from `C:\Users\ohu00\Documents\.env` into Paperclip `local_encrypted` secrets
- upgrades all managed agents to include `browser`, `mcp-chromeops`, and `mcp-local-deep-research`
- enables secret-backed runtime env bindings for the agent fleet
- enables heartbeats on managed agents
- grants the `Chief of Staff` controlled agent-creation permissions
- creates the `Browser Operations Lead` if missing

Add the governance-specific agent trio when needed:

```powershell
cd "C:\Users\ohu00\Desktop\digitalproducts"
.\ops\paperclip\add-governance-agents.ps1
```

## Credential Wiring

- `tools/.env` is now hydrated from `C:\Users\ohu00\Documents\.env` with the repo-relevant subset for Anthropic, GitHub, n8n, Vercel, and Postgres-backed analytics.
- `~/.agent-secrets.env` is sourced by WSL shells through `~/.bashrc` and `~/.profile` so Hermes/tool shells can see shared platform and LLM credentials without storing them in the repo.
- Paperclip now has a repo-native bootstrap script for syncing the broader operator credential set into encrypted local secret storage and attaching it to managed agents as `secret_ref` bindings.
- Verified live:
  - GitHub token reaches `pinohu/digitalproducts`
  - `N8N_API_KEY` works against `https://n8n.audreysplace.place`
  - Vercel token is valid and a team is available

Browser operations model:

- Hermes runs inside WSL
- browser-first SaaS work uses a Windows-side `chrome-devtools-mcp` bridge exposed as `mcp-chromeops`
- the dedicated browser profile and launch helpers live under `ops/browser/`
- decision record: `00-foundation/operator-system/adr-001-browser-and-secret-ops.md`

Current remaining gaps:

- Reddit app credentials are still missing, so live Reddit mining is not ready yet.
- Gumroad access token is still missing, so publish/storefront/workflow writes remain blocked.
- `VERCEL_PROJECT_ID` is intentionally unset until the exact deployment target is chosen.
- The repo now has a usable Postgres connection string for automation experiments, but it came from a generic `DATABASE_URL`; if a Neon-specific runtime target is required later, that should replace it explicitly.

## Operating Rules

- The repo is the source of truth. Agents should update files, not only issue comments.
- `FRAMEWORK.md`, `ROADMAP.md`, `automation/pipeline.md`, and `10-execution-sprints/current-sprint.md` are canonical operating documents.
- `00-foundation/operator-system/governance-stack.md`, `mobile-control-center.md`, and `manual-actions-ledger.md` are now canonical for quality, mobile continuation, and operator-only work.
- Product work is not complete until the `ROADMAP.md` Definition of Done is satisfied.
- External blockers should be recorded explicitly in issues instead of being silently worked around.

## Expected External Dependencies

These still require real account access, credentials, or operator decisions before true production launch:

- Gumroad product/storefront configuration
- Vercel deployment target selection (`VERCEL_PROJECT_ID`) and any project-specific environment variables
- Final decision on whether the production analytics datastore is Neon-specific or the currently available generic Postgres target
- n8n workflow deployment and credential records inside the n8n instance
- Domain and content linkage for `ikeohu.com`
- Any launch-specific testimonials, buyer feedback, or payment-processing access
