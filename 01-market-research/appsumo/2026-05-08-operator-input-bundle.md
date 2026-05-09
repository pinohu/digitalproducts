# AppSumo Operator Input Bundle

Created: 2026-05-08T09:37:16Z
Owner: Chief of Staff
Related issues: DIG-61, DIG-65
Primary sources:
- `01-market-research/appsumo/2026-05-08-priority-access-ledger.md`
- `01-market-research/appsumo/suitedash-access-completion-packet.md`
- `automation/boost-flowlu-api-viability.md`
- `automation/agenticflow-api-viability.md`
- `automation/procesio-api-viability.md`
- `automation/wbiztool-api-viability.md`
- `00-foundation/operator-system/browser-runbooks/smsit-access-classification.md`

## Purpose

This is the short operator-return checklist for the highest-value blocked AppSumo surfaces. It deliberately avoids raw secrets, full ledger repetition, and speculative tenant guesses.

Use this when the operator is back at the keyboard: provide the missing non-secret labels/URLs/scope notes through repo docs where safe, and provide credentials, API keys, sessions, cookies, license codes, Public IDs, client IDs, or OTP/MFA material only through the approved secure credential/session channel.

## Universal rules

- Do not paste secret values into Git, Paperclip comments, screenshots, chat, or terminal output.
- Provide exact URLs and labels; do not ask agents to infer tenant subdomains from product names or env var names.
- Prefer a dedicated automation-owned credential for anything that may later be scheduled.
- First verification after any unblock must be read-only, data-minimized, and manually reviewed.
- No writes, sends, imports, exports, workflow activations, key rotations, settings changes, billing changes, or customer-data dumps are authorized by this bundle.

## Highest-value asks

| Priority | Tool | Current classification | Operator input needed | Where it likely lives | First read-only verification after input |
|---:|---|---|---|---|---|
| 1 | SuiteDash | `tenant_urls_verified_public_auth_mixed_credentials_insufficient` | Use one of the eight live exact portal auth hosts already recorded in `suitedash-access-completion-packet.md`; approved browser session or human-assisted login path; MFA/session note; one `X-Public-ID` to existing `X-Secret-Key` mapping; tenant/key labels; scope note; approved first-read target. Confirm/repair Coadjutant, Dome Law, and NAWA before use. | SuiteDash tenant admin, especially Integrations / Secure API; existing secure dotenv has secret-key-shaped `SUITEDASH_*` values but lacks Public IDs and credential/session material. | Browser: authenticated tenant page title + top-level navigation labels only. API: documented metadata GET such as `/contact/meta`, then one `limit=1` approved endpoint if safe. |
| 2 | KonnectzIT | `browser_url_verified_credentials_invalid` | Human-approved KonnectzIT browser credential/session, or exact account credential mapping; confirm if MFA/CAPTCHA/session approval is required. | KonnectzIT account at `https://app.konnectzit.com/`; credential manager or operator browser profile. | Login to dashboard read-only; summarize workflow/app/webhook inventory counts and surface names only. No workflow edits or runs. |
| 3 | Boost.space | `tenant_base_missing` | Exact Boost.space system URL, for example `https://<system>.boost.space/`; confirm the available key belongs to that system; approve first resource. | Boost.space user profile/account URL; browser address bar after login; API token page. | `tools/appsumo_readonly_probe.py boostspace address-countries --base-url https://<system>.boost.space/api --page-size 1 --summary-only --json`. If 200, optionally inspect `activities` summary only. |
| 4 | Flowlu | `tenant_subdomain_missing` | Exact Flowlu workspace URL, for example `https://<company>.flowlu.com/`; confirm `FLOWLU_API_KEY` belongs to that workspace; approve first resource. | Flowlu browser workspace URL and API settings. | `tools/appsumo_readonly_probe.py flowlu crm-accounts --base-url https://<company>.flowlu.com/api/v1/module --page-size 1 --summary-only --json`; use `agile-projects` or `tasks` instead if CRM is too sensitive. |
| 5 | AgenticFlow | `api_auth_verified_project_scope_mismatch` | Correct workspace URL/UUID; project UUID that the current key can access, or a new dedicated project-scoped automation key; approve one-agent metadata read. | AgenticFlow web app URL `https://agenticflow.ai/app/workspaces/<workspace_uuid>/...` and workspace settings / API keys. | `tools/appsumo_readonly_probe.py agenticflow agents --secret-name AGENTICFLOW_AI_KEY --workspace-id <workspace_uuid> --project-id <project_uuid> --page-size 1 --summary-only --json`. Expected unblock is HTTP 200; 403 means key/project mismatch remains. |
| 6 | WbizTool | `credential_pair_incomplete` | `WBIZTOOL_CLIENT_ID`; confirm current API key or provide dedicated `WBIZTOOL_API_KEY_AUTOMATION`; `WBIZTOOL_WHATSAPP_CLIENT_ID` only if report/history checks are approved; scope note and first-read target. | WbizTool API Keys page and WhatsApp Setting page. | Manual-only redacted `POST /api/v1/whatsapp-client/list/` with client ID + API key. Summarize counts/status fields only; do not add to GET-only probe until a read-like-POST guard exists. |
| 7 | SMS-iT CRM | `api_docs_and_login_verified_credentials_invalid_or_unmapped` | Human-approved browser credential/session for `https://aicpanel.smsit.ai/login`, or the exact issuing context for `SMS_IT_API_KEY*`: base URL, auth shape, workspace/account ID if required, and one safe read-only endpoint. | SMS-iT/AICPanel account, Stoplight/API docs, API-key/settings page. | Browser: account readiness and dashboard/plan surface summary only. API: one confirmed account-read endpoint only, summarized without contacts/messages. |
| 8 | Procesio | `api_base_verified_key_name_missing` | Exact Procesio API key name paired with the existing `PROCESIO_API_KEY` value; approved workspace header/context if required; confirmation that first checks may read only metadata. | Procesio account/API settings; API-key detail page; workspace settings. | `tools/appsumo_readonly_probe.py procesio users-me --api-key-name <procesio_api_key_name> --summary-only --json`, then `workspaces` and `projects-count` with `--workspace` only after identity succeeds. No project runs or workflow/webhook/credential/schedule mutations. |
| 9 | CallScaler | `api_base_verified_credentials_invalid_or_unscoped` | Fresh/rotated read-only CallScaler API key, or exact current base/auth/account context; approve one metadata-first read. | CallScaler v3 app settings/API keys page; secure credential channel. | `tools/appsumo_readonly_probe.py callscaler dashboard-stats --env-file /mnt/c/Users/ohu00/Documents/.env --summary-only --json`, then `numbers`/`calls` with `--page-size 1` only after privacy approval. No call exports/recordings/transcripts/phone data. |
| 10 | Dadan | `api_verified_limited_readonly` | One operator-approved non-sensitive recording request code created by the same key, plus approval for what fields may be summarized. | Dadan `https://app.dadan.io` recording request/admin area. | `tools/appsumo_readonly_probe.py dadan recording-request --request-code <request-code> --summary-only --json`; no request creation, upload, sharing, or raw submission/video export. |

## Ready-to-copy operator asks

### SuiteDash

Please choose one of the eight live SuiteDash portal labels recorded in `suitedash-access-completion-packet.md` (ClickOnPage, Desk Village, instaxis, Naija Clan, notroom, relguard, SitBid, or Your Deputy) and provide, through the approved secure channel:
- chosen live portal label/URL, or a replacement/current URL for Coadjutant, Dome Law, or NAWA if one of those is the intended tenant;
- browser session path or plan for human-assisted login;
- MFA/session prerequisites;
- one `X-Public-ID` paired to the matching existing `SUITEDASH_*` secret key name;
- tenant/key scope note, such as internal demo, client portal, or inactive test tenant;
- approved first-read target.

Non-secret info such as tenant label and first-read target can be recorded in the repo. Public IDs and secret keys must stay in the secure credential store.

### KonnectzIT

Please provide either a human-approved logged-in session for `https://app.konnectzit.com/` or the correct account credential path. The first read will only confirm dashboard access and summarize visible workflow/app/webhook surfaces; no workflows, app connections, webhook settings, or runs will be changed.

### Boost.space and Flowlu

Please provide the exact tenant URLs:
- Boost.space: `https://<system>.boost.space/`
- Flowlu: `https://<company>.flowlu.com/`

Also confirm that the existing secure keys belong to those tenants. First checks will use `--page-size 1 --summary-only --json` and will not export records.

### AgenticFlow

Please confirm the workspace UUID and project UUID that the API key is scoped to, or provide a dedicated automation-owned key. The first read will be a one-agent metadata/count check only. No agents, workflows, workforces, prompts, MCP connections, runs, or webhooks will be created or triggered.

### WbizTool

Please provide `WBIZTOOL_CLIENT_ID` and, only if report/history inspection is desired, `WBIZTOOL_WHATSAPP_CLIENT_ID`. First check should be `whatsapp-client/list` with status/count-only output. No messages, schedules, cancellations, media actions, phone verification, group sends, or history exports are authorized.

### SMS-iT CRM

Please provide a verified browser session/credential for `https://aicpanel.smsit.ai/login`, or confirm the exact API base/auth shape/account ID for the current `SMS_IT_API_KEY*` values. First verification will summarize account/workspace readiness only and will not touch contacts, messages, campaigns, or automations.

### Procesio

Please provide the Procesio API key name that pairs with the existing secure `PROCESIO_API_KEY` value, plus the approved workspace header/context for first reads if the account is workspace-scoped. First verification will be GET-only and metadata-first (`users-me`, `workspaces`, then `projects-count`), emitted as summary-only JSON. No process/project runs, workflow edits, webhook/schedule/credential changes, run-output exports, user/workspace settings changes, or live n8n activation are authorized.

### CallScaler

Please verify or rotate a read-only CallScaler API key from the CallScaler v3 settings/API-key page, or provide the exact current API base/auth/account context if it differs from `https://callscaler.com/api/v1` bearer auth. The current secure key names exist but return HTTP 401. First retry will be `dashboard-stats` summary-only, then `numbers`/`calls` with `--page-size 1` only after privacy approval. No call exports, phone numbers, caller identities, recordings, transcripts, call-flow payloads, webhook details, or billing data are authorized.

## Sequencing recommendation

1. Resolve SuiteDash first because it directly supports the active product domain and can improve evidence for the SuiteDash product line without implying the live Gumroad launch is shipped.
2. Resolve KonnectzIT next because it is the highest-value integration/workflow layer currently blocked by credentials/session rather than unknown product fit.
3. Resolve Boost.space and Flowlu as a paired tenant-base pass; both are blocked by exact URLs, not by proven-invalid keys.
4. Resolve AgenticFlow only after project-scoped API context is clear.
5. Resolve Procesio after the key-name/workspace blocker is cleared; it can stay manual-first because the first useful checks are metadata-only and not launch-critical.
6. Resolve WbizTool and SMS-iT CRM last unless messaging/CRM becomes a near-term product or launch dependency; both carry higher privacy/send-risk and need stricter manual review.

## Definition of done for DIG-61

- One concise operator-input bundle exists at this path.
- Each top blocker names the exact missing input, likely source, and first read-only verification.
- The bundle contains no secret values and authorizes no writes.
- `ROADMAP.md`, `automation/pipeline.md`, and `10-execution-sprints/current-sprint.md` link or summarize the bundle so repo operations stay current.
