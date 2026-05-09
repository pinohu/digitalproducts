# Automation

The cross-cutting automation layer. Where the framework's templates and stages get connected into a running pipeline that minimizes manual work.

## Files in this folder

- [`pipeline.md`](./pipeline.md) — The end-to-end automation pipeline, stage by stage.
- [`flint-delegation.md`](./flint-delegation.md) — How to delegate background work to the Flint VM.
- [`prompt-library.md`](./prompt-library.md) — Index of all Claude / LLM prompts used across the system.
- [`claude-skills/`](./claude-skills/) — Claude skill specs that can be installed at `/mnt/skills/user/<skill-name>/SKILL.md`.
- [`n8n-workflows/`](./n8n-workflows/) — n8n workflow specifications (markdown describing nodes, triggers, data flow) plus disabled/manual-first JSON drafts where useful.
- [`appsumo-readonly-connector-spikes.md`](./appsumo-readonly-connector-spikes.md) — DIG-27/DIG-35/DIG-39/DIG-42/DIG-45/DIG-56/DIG-64/DIG-66/DIG-67/DIG-68 Agiled/AITable/Emailit/Boost.space/Flowlu/Certopus/Dadan/CallScaler/Late-Zernio/Formaloo/Flotiq read-only connector findings and promotion path.
- [`flotiq-api-viability.md`](./flotiq-api-viability.md) — DIG-68 Flotiq `X-AUTH-TOKEN` verification, guarded content-type/media summary surface, and disabled/manual-first n8n promotion contract.
- [`formaloo-api-viability.md`](./formaloo-api-viability.md) — DIG-67 Formaloo auth-flow verification, guarded forms/profile summary surface, and disabled/manual-first n8n promotion contract.
- [`late-zernio-api-viability.md`](./late-zernio-api-viability.md) — DIG-66 Late/Zernio docs/auth verification, safe GET-only endpoint set, and disabled/manual-first n8n promotion contract.
- [`callscaler-api-viability.md`](./callscaler-api-viability.md) — DIG-64 CallScaler secure-env recheck, bearer-auth 401 result, and safe retry contract.
- [`agenticflow-api-viability.md`](./agenticflow-api-viability.md) — DIG-58 AgenticFlow CLI auth, REST base/auth shape, and project-scope blocker for future read-only health checks.
- [`procesio-api-viability.md`](./procesio-api-viability.md) — DIG-60 Procesio Web API base/auth shape and current API-key-name/workspace blocker.
- [`dadan-api-viability.md`](./dadan-api-viability.md) — DIG-56 Dadan API base/auth verification and limited recording-request detail safety contract.
- [`emailit-readonly-endpoint-followup.md`](./emailit-readonly-endpoint-followup.md) — DIG-39 Emailit API v2 auth/endpoint verification and safest next connector spike.
- [`certopus-readonly-endpoint-followup.md`](./certopus-readonly-endpoint-followup.md) — DIG-45 Certopus `X-API-KEY` auth/endpoint verification and metadata-only health-check contract.
- [`boost-flowlu-api-viability.md`](./boost-flowlu-api-viability.md) — DIG-42 Boost.space and Flowlu tenant-shaped API classification, blockers, and guarded retry commands.

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
| n8n workflow specs | ✅ Drafted + AppSumo, Emailit, Certopus, Late/Zernio, Formaloo, and Flotiq read-only packs added | Implementation still requires building in n8n.audreysplace.place; `automation/n8n-workflows/appsumo-readonly-summary.draft.json`, `automation/n8n-workflows/emailit-readonly-health-check.draft.json`, `automation/n8n-workflows/certopus-readonly-health-check.draft.json`, `automation/n8n-workflows/late-readonly-health-check.draft.json`, `automation/n8n-workflows/formaloo-readonly-health-check.draft.json`, and `automation/n8n-workflows/flotiq-readonly-health-check.draft.json` are disabled/manual-only and contain no credentials; Emailit health checks are read-only domains/events/templates/optional webhooks only, Certopus health checks are templates/organisations/wallet/SMTP metadata only, Late/Zernio health checks are profiles/accounts/account-health/posts/usage/users summaries only, Formaloo health checks are forms/profile count/readiness summaries only, and Flotiq health checks are content-type/media count summaries only, not sends/certificate operations/posting/social-account/form/schema/submission/content/media/CMS mutations |
| Python tools | ✅ Runnable local stack documented + AppSumo read-only probe added | `tools/setup.sh` installs deps; `tools/verify_tools.py` checks imports/config/secrets offline; `tools/appsumo_readonly_probe.py` can perform GET-only Agiled/AITable/Emailit/Certopus/CallScaler/Dadan/Late-Zernio/Formaloo/Flotiq checks, includes guarded AgenticFlow `agents` metadata checks that require workspace/project context and a project-scoped key, includes guarded Procesio metadata checks that require the separate API key name plus optional workspace header, and includes guarded Boost.space/Flowlu tenant-shaped probes that require operator-verified `--base-url`; Late/Zernio is verified read-only via `GETLATE_DEV_API_KEY` for profiles/accounts/account-health/posts/usage/users summaries; Formaloo is verified read-only via `FORMALOO_API_KEY` + `FORMALOO_API_SECRET` token minting for forms/profile summaries; Flotiq is verified read-only via `FLOTIQ_API_KEY` and `X-AUTH-TOKEN` for content-type/media count summaries; CallScaler currently returns HTTP 401 for both secure key names and needs a fresh key/base/auth confirmation before promotion; Dadan requires an operator-approved recording request code and uses only the detail `GET`; Procesio is blocked until the operator supplies the key name paired to the existing key value; use `--summary-only --json` for data-minimized n8n/Paperclip-safe reporting; live Reddit/Trends/AppSumo runs still need credentials/network |
| Flint delegation patterns | ✅ Drafted | See `flint-delegation.md` |

## What's Pending (User Action)

- [ ] Install Claude skills to user skill directory (see each skill's installation note)
- [ ] Build n8n workflows from specs (each spec includes node-by-node instructions); for AppSumo, Emailit, Certopus, Late/Zernio, and Formaloo read-only packs, import the JSON only as disabled/manual-first and review notification output before enabling Cron or writeback
- [ ] Set up Python virtualenv + real API keys per `tools/README.md`; run `python tools/verify_tools.py` from an activated environment
- [ ] Wire Flint VM to handle the Reddit miner cron schedule
- [ ] Add real external credentials before production writes: Reddit app, Anthropic API key, n8n credentials, Gumroad access, Neon database URL if used, and Vercel project/token if deploying landing pages
- [ ] Create real n8n credential records for Agiled, AITable, Emailit, Certopus, Late/Zernio, Formaloo, and Flotiq before running AppSumo, email-health, certificate-health, social-publishing-health, form-health, or CMS-health summary workflows; AITable must use the current secure credential source/rotated automation-owned key, Emailit should use a dedicated automation-owned key before any scheduled health check, Certopus should use a dedicated credential before any n8n run, Late/Zernio should use a dedicated `GETLATE_DEV_API_KEY_AUTOMATION` or n8n credential before scheduling, Formaloo should use a dedicated `FORMALOO_API_KEY_AUTOMATION` + `FORMALOO_API_SECRET_AUTOMATION` pair or n8n credential before scheduling, and Flotiq should use a dedicated `FLOTIQ_API_KEY_AUTOMATION` or n8n credential before scheduling. Import `emailit-readonly-health-check.draft.json`, `late-readonly-health-check.draft.json`, `formaloo-readonly-health-check.draft.json`, and `flotiq-readonly-health-check.draft.json` disabled/manual-first only, review notification digests, and do not enable Emailit sends/mutations, Certopus certificate/recipient/SMTP/domain/wallet mutations, Late/Zernio posting/social-account/inbox/comment/webhook/user/API-key mutations, Formaloo form submissions/schema/webhook/team/export mutations, or Flotiq content/model/media/API-key/webhook/user/environment mutations without separate write contracts.
- [ ] Confirm AgenticFlow project scoping before promoting it: the secure runtime key authenticates through the official CLI and the current REST base is `https://api.agenticflow.ai/`, but `GET /v1/agents/` with CLI-returned workspace/project context currently returns 403 `API key does not have access to this project`; provide the correct project-scoped key/context or a dedicated `AGENTICFLOW_API_KEY_AUTOMATION` before any disabled/manual-first health workflow.
- [ ] Provide the Procesio API key name and approved workspace context before retrying Procesio: DIG-60 verified `https://webapi.procesio.app` and the separate `key` + `value` header shape, but the current secure runtime has only `PROCESIO_API_KEY` as the value. First reads must stay manual, GET-only, and summary-only (`users-me`, `workspaces`, `projects-count` before any project listing); no project runs or workflow/webhook/credential/schedule mutations are authorized.
- [ ] Provide exact tenant bases before retrying Boost.space or Flowlu: Boost.space needs `https://<system>.boost.space/`; Flowlu needs `https://<company>.flowlu.com/`. The current repo has keys but cannot validate either tool without those URLs.
- [ ] Provide a fresh CallScaler read-only API key or exact current base/auth shape before promoting CallScaler: DIG-64 loaded `CALLSCALER_API_KEY` and `CALLSCALER_API_KEY_1` from the secure operator dotenv and both returned HTTP 401 for metadata-first bearer reads against `https://callscaler.com/api/v1`. First successful retry must stay manual, GET-only, and summary-only; no call records, phone numbers, caller identities, recordings, transcripts, or billing data may be exported.
- [ ] Provide a dedicated automation-owned `DADAN_API_KEY`, one approved non-sensitive Dadan recording request code created by that key, and field-level approval before promoting the Dadan recording-request detail check to any n8n workflow. Do not automate Dadan request creation or video/share workflows without a separate write contract.
