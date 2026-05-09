# AppSumo Read-Only Connector Spikes — Agiled, AgenticFlow, AITable.ai, Emailit, Boost.space, Flowlu, Certopus, WbizTool, CallScaler, Dadan, Late/Zernio, Formaloo, Flotiq, and Procesio

Related issues: DIG-27, DIG-35, DIG-39, DIG-42, DIG-45, DIG-52, DIG-56, DIG-58, DIG-60, DIG-64, DIG-66, DIG-67, DIG-68
Source access ledger: `01-market-research/appsumo/2026-05-08-priority-access-ledger.md`
Verification date: 2026-05-08
Owner: Automation Engineer

## Scope and safety rules

- Only read-only HTTP `GET` probes were added and run.
- No destructive writes, creates, updates, deletes, imports, syncs, or webhook activations were performed.
- No raw API keys, bearer tokens, cookies, passwords, or credential file contents are stored here.
- Runtime credentials should live in `tools/.env`, shell environment, or a secure dotenv passed with `--env-file`.
- The reusable utility is `tools/appsumo_readonly_probe.py`.
- Emailit details and endpoint evidence live in `automation/emailit-readonly-endpoint-followup.md`.
- Boost.space and Flowlu viability details live in `automation/boost-flowlu-api-viability.md`; both require verified tenant bases before live connector promotion.
- Certopus endpoint/auth details live in `automation/certopus-readonly-endpoint-followup.md`; it is verified for metadata/count-only GET summaries via `X-API-KEY`, not for certificate issuance, sends, downloads, or recipient mutations.
- WbizTool endpoint/auth details live in `automation/wbiztool-api-viability.md`; its API base/docs are clarified, but the current secure runtime source has only `WBIZTOOL_COM_API_KEY` and lacks the required WbizTool `client_id` and `whatsapp_client` values.
- CallScaler endpoint details live in `automation/callscaler-api-viability.md`; secure CallScaler key names are present, but both current values returned HTTP 401 against the expected `https://callscaler.com/api/v1` bearer surface, so it remains manual-first until the operator supplies a fresh key or exact base/auth shape.
- Dadan endpoint/auth details live in `automation/dadan-api-viability.md`; it is verified only for limited `GET /requestrecording/{RequestCode}` checks on `https://app.dadan.io/api/v1/usedadan` with `X-Dadan-API-Key`, not for recording-request creation, uploads, sharing, or account/developer mutations.
- AgenticFlow endpoint/auth details live in `automation/agenticflow-api-viability.md`; the current key authenticates through the official CLI and the CLI can expose workspace/project context, but the documented `GET /v1/agents/` REST read currently returns HTTP 403 `API key does not have access to this project`, so promotion is blocked until the operator supplies/rotates a project-scoped key or confirms the correct project context.
- Procesio endpoint/auth details live in `automation/procesio-api-viability.md`; the Web API base is `https://webapi.procesio.app` and API-key auth requires separate `key` + `value` headers. Current runtime has `PROCESIO_API_KEY` value only, so first reads are blocked until the operator supplies the matching API key name and approved workspace header/context.
- Late/Zernio endpoint/auth details live in `automation/late-zernio-api-viability.md`; Late's docs have rebranded to Zernio, bearer auth with `GETLATE_DEV_API_KEY` is verified for summary-only GETs, and posting/social-account/inbox/comment/webhook/user/API-key mutations remain out of scope.
- Formaloo endpoint/auth details live in `automation/formaloo-api-viability.md`; the official v3 API uses `FORMALOO_API_KEY` plus `FORMALOO_API_SECRET` to mint a short-lived JWT, then `x-api-key` + `Authorization: JWT` for summary-only forms/profile GETs. Form submissions, response exports, schema/webhook/team mutations, raw owner/respondent PII, and scheduled n8n activation remain out of scope without a separate contract and dedicated automation credential.
- Flotiq endpoint/auth details live in `automation/flotiq-api-viability.md`; the official API uses `X-AUTH-TOKEN` against `https://api.flotiq.com`, and the current key is verified only for summary-only content-type definition counts and media counts. Content/object/media mutations, raw CMS exports, arbitrary content model listing, webhooks, API keys, users, environments, and scheduled n8n activation remain out of scope without a separate contract and dedicated automation credential.
- CallScaler endpoint/auth details live in `automation/callscaler-access-surface.md`; the API base is `https://callscaler.com/api/v1/` with bearer auth, and DIG-64 confirmed secure dotenv key names exist but both available keys returned HTTP 401 on minimal safe GET probes. Do not add CallScaler to n8n until the operator verifies/rotates an API key or supplies an approved browser session.

## Utility usage

```bash
cd /mnt/c/Users/ohu00/Desktop/digitalproducts/tools
source .venv/bin/activate

# List supported resources
python appsumo_readonly_probe.py agiled --list-resources
python appsumo_readonly_probe.py aitable --list-resources

# Agiled read-only examples
python appsumo_readonly_probe.py agiled users --page-size 3
python appsumo_readonly_probe.py agiled projects --page-size 3

# If credentials are kept in a secure external dotenv, pass it explicitly
python appsumo_readonly_probe.py agiled users --env-file /path/to/secure.env --page-size 3

# AITable.ai read-only examples
python appsumo_readonly_probe.py aitable spaces --page-size 3
python appsumo_readonly_probe.py aitable nodes --space-id spc_xxx --page-size 3
python appsumo_readonly_probe.py aitable records --datasheet-id dst_xxx --page-size 3

# Data-minimized output for n8n/Paperclip-safe summaries (omits raw samples)
python appsumo_readonly_probe.py agiled projects --page-size 25 --summary-only --json
python appsumo_readonly_probe.py aitable spaces --env-file /path/to/secure.env --page-size 25 --summary-only --json

# Emailit read-only health examples (API v2; no sends/mutations)
python appsumo_readonly_probe.py emailit domains --env-file /path/to/secure.env --page-size 1 --summary-only --json
python appsumo_readonly_probe.py emailit events --env-file /path/to/secure.env --page-size 5 --summary-only --json
python appsumo_readonly_probe.py emailit templates --env-file /path/to/secure.env --page-size 5 --summary-only --json

# Certopus read-only health examples (uses X-API-KEY; no certificate issuance/sends/exports)
python appsumo_readonly_probe.py certopus templates --env-file /path/to/secure.env --page-size 5 --summary-only --json
python appsumo_readonly_probe.py certopus organisations --env-file /path/to/secure.env --page-size 5 --summary-only --json
python appsumo_readonly_probe.py certopus wallet --env-file /path/to/secure.env --page-size 5 --summary-only --json

# CallScaler guarded metadata-first checks; DIG-64 current secure keys return HTTP 401, so do not promote until key/base/auth is fixed
python appsumo_readonly_probe.py callscaler dashboard-stats --env-file /path/to/secure.env --summary-only --json
python appsumo_readonly_probe.py callscaler calls --env-file /path/to/secure.env --page-size 1 --summary-only --json
python appsumo_readonly_probe.py callscaler numbers --secret-name CALLSCALER_API_KEY_1 --env-file /path/to/secure.env --page-size 1 --summary-only --json

# Dadan limited read-only detail check; requires an operator-approved request code created by the same key
python appsumo_readonly_probe.py dadan recording-request --env-file /path/to/secure.env --request-code <request-code> --summary-only --json

# Late/Zernio verified read-only health examples; no posting/social-account mutations
python appsumo_readonly_probe.py late profiles --env-file /path/to/secure.env --page-size 1 --summary-only --json
python appsumo_readonly_probe.py late accounts --env-file /path/to/secure.env --page-size 1 --summary-only --json
python appsumo_readonly_probe.py late account-health --env-file /path/to/secure.env --page-size 1 --summary-only --json
python appsumo_readonly_probe.py late posts --env-file /path/to/secure.env --page-size 1 --summary-only --json
python appsumo_readonly_probe.py late usage-stats --env-file /path/to/secure.env --summary-only --json
python appsumo_readonly_probe.py late users --env-file /path/to/secure.env --page-size 1 --summary-only --json

# Flotiq verified read-only CMS health examples; no content/model/media mutations or raw CMS exports
python appsumo_readonly_probe.py flotiq content-types --env-file /path/to/secure.env --page-size 1 --summary-only --json
python appsumo_readonly_probe.py flotiq media --env-file /path/to/secure.env --page-size 1 --summary-only --json

# Formaloo verified read-only health examples; token minting POST only, then forms/profile GETs
python appsumo_readonly_probe.py formaloo forms --env-file /path/to/secure.env --page-size 1 --summary-only --json
python appsumo_readonly_probe.py formaloo profile --env-file /path/to/secure.env --summary-only --json

# AgenticFlow guarded read-only first check; requires operator-supplied workspace/project IDs
python appsumo_readonly_probe.py agenticflow agents --secret-name AGENTICFLOW_AI_KEY --env-file /path/to/secure.env --workspace-id <workspace_uuid> --project-id <project_uuid> --page-size 1 --summary-only --json

# Procesio guarded read-only first checks; requires the API key name paired with PROCESIO_API_KEY
python appsumo_readonly_probe.py procesio users-me --env-file /path/to/secure.env --api-key-name <procesio_api_key_name> --summary-only --json
python appsumo_readonly_probe.py procesio projects-count --env-file /path/to/secure.env --api-key-name <procesio_api_key_name> --workspace <workspace_name> --summary-only --json

# Boost.space and Flowlu are tenant-shaped; these intentionally require verified --base-url values
python appsumo_readonly_probe.py boostspace address-countries --env-file /path/to/secure.env --base-url https://<verified-system>.boost.space/api --page-size 1 --summary-only --json
python appsumo_readonly_probe.py flowlu crm-accounts --env-file /path/to/secure.env --base-url https://<verified-company>.flowlu.com/api/v1/module --page-size 1 --summary-only --json
```

The utility exits `0` on 2xx responses and `2` on HTTP/request failures, so it can be used in n8n Execute Command nodes or CI smoke checks without parsing the body first.

## Agiled spike

### Auth shape

- Base URL: `https://app.agiled.app/api/v1`
- Header: `Authorization: Bearer $AGILED_API_KEY`
- Credential source used for live smoke check: secure operator dotenv outside the repo.

### Verified read-only pulls

| Resource | Endpoint | Result | Useful signal |
|---|---|---|---|
| Users | `GET /users` | HTTP 200 | Returned active user records with IDs, names, email fields, company IDs, status, avatar/profile metadata, and brand IDs. This can support people/owner mapping for an operating ledger. |
| Projects | `GET /projects` | HTTP 200 | Returned project records with IDs, names, summaries, status, dates, budget/time fields, and visibility flags. This can support project/status reporting into Paperclip or a repo-generated ops dashboard. |

### Narrowed gaps

- `GET /companies` returned 404 (`route api/v1/companies could not be found`), so Agiled company/client data likely uses a different endpoint name or permission shape.
- `clients` and `tasks` are included in the utility as plausible read-only resources, but they still need endpoint-by-endpoint verification before production use.
- Records include potentially personal/customer data. Future automation should summarize counts/statuses by default and avoid committing raw CRM exports.
- Repeated smoke checks can trigger Agiled HTTP 429 rate limiting. Treat connector probes as verification steps, not polling loops; n8n schedules should start at weekly/daily cadence with backoff.

### Recommendation

Agiled is the stronger immediate API-backed operating surface of the two tested tools. It has enough authenticated read access to support a weekly read-only sync of users and projects into an internal status report. Do not promote it to a write-capable workflow until the exact project/task/client endpoint map and data-minimization rules are documented.

## AITable.ai spike

### Auth shape attempted

- Base URL from DIG-26 ledger: `https://aitable.ai/fusion/v1`
- Header: `Authorization: Bearer ***`
- Primary endpoint: `GET /spaces`

### Current verification result

DIG-35 reconciled the earlier 401/200 mismatch. With the current secure operator dotenv explicitly loaded via `--env-file /mnt/c/Users/ohu00/Documents/.env`, AITable read-only access is working.

Observed 2026-05-08T03:12:56Z:

| Probe | Result | Notes |
|---|---|---|
| `GET /spaces` on `https://aitable.ai/fusion/v1` | HTTP 200 | Returned two admin spaces: `nawa automation space` and `Hoang's Space`. |
| `GET /spaces` on `https://api.aitable.ai/fusion/v1` | HTTP 200 | Same space set; host alias works. |
| `GET /spaces` on `https://apitable.com/fusion/v1` | HTTP 200 | Same space set; host alias works. |
| `GET /spaces` on `https://api.apitable.com/fusion/v1` | HTTP 200 | Same space set; host alias works. |
| `GET /spaces/spcjbFvCoF57M/nodes` | HTTP 200 | Returned multiple folders/datasheets, including trading, legal, AppSumo, and test automation nodes. |
| `GET /spaces/spcg79VTfrMgs/nodes` | HTTP 200 | Returned one datasheet node. |
| `GET /datasheets/dstHEhlAmeChAWQ5En/records` | HTTP 200 | Returned one visible test/empty-fields record. |
| `GET /datasheets/dstlPn0Bty73sfLjJJ/records` | HTTP 200 | Returned one AppSumo inventory-style record. |

Root cause assessment: the default host/base in `tools/appsumo_readonly_probe.py` is not the problem. The earlier 401 was most likely caused by token or environment-source drift: `tools/.env` does not contain `AITABLE_API_KEY`, while `/mnt/c/Users/ohu00/Documents/.env` does. Explicit `--env-file` loading overrides stale shell/tool values and restores access.

### Current recommendation

AITable is verified as a read-only candidate again, provided runs load the current secure operator dotenv or an equivalent rotated key. It is safe to keep in the n8n promotion queue for data-minimized read-only summaries. Do not enable writes, imports, webhooks, or row updates without a separate issue that defines field-level contracts, rollback behavior, and automation-owned credentials.

### What the utility supports

| Resource | Endpoint | Required flags | Purpose |
|---|---|---|---|
| Spaces | `GET /spaces` | none | Discover accessible workspaces/spaces. |
| Nodes | `GET /spaces/{space_id}/nodes` | `--space-id` | Discover datasheets/views under a known space. |
| Records | `GET /datasheets/{datasheet_id}/records` | `--datasheet-id` | Pull rows from a selected operating ledger/datasheet. |

### Recommendation

AITable is now a verified read-only candidate again when the current secure dotenv is loaded explicitly. Promote it only for low-frequency, data-minimized summaries: first discover spaces, then select specific datasheets by ID, then summarize record counts/status fields. Do not commit raw datasheet exports, and do not add write-capable AITable workflows without a dedicated contract and rollback issue.

## Emailit spike

Detailed evidence lives at `automation/emailit-readonly-endpoint-followup.md`.

### Auth shape

- Base URL: `https://api.emailit.com/v2`
- Header: `Authorization: Bearer ***`
- Credential source used for live smoke check: secure operator dotenv outside the repo.
- API v1 is deprecated; earlier `/v1` failures were endpoint-generation/route-shape failures, not proof that the current keys were invalid.

### Verified read-only pulls

DIG-39 verified the default `EMAILIT_API_KEY` with `--summary-only --json` against:

| Resource | Endpoint | Result | Notes |
|---|---|---|---|
| Templates | `GET /templates` | HTTP 200 | 0 visible records in the checked workspace. |
| Domains | `GET /domains` | HTTP 200 | Domain metadata exists; do not mutate DNS/verification from automation. |
| Emails | `GET /emails` | HTTP 200 | Email records exist; keep summaries data-minimized and avoid message bodies/addresses. |
| Contacts | `GET /contacts` | HTTP 200 | Contact data exists; do not commit raw contact exports. |
| Audiences | `GET /audiences` | HTTP 200 | Audience metadata exists. |
| Suppressions | `GET /suppressions` | HTTP 200 | Suppression data exists; do not create/update/delete suppressions without a write contract. |
| Webhooks | `GET /webhooks` | HTTP 200 | 0 visible records in the checked workspace. |
| API keys | `GET /api-keys` | HTTP 200 | API-key metadata exists; raw key material must never be printed or committed. |
| Events | `GET /events` | HTTP 200 | Event metadata exists; summarize type/status counts only. |

All four secure-runtime key names (`EMAILIT_API_KEY`, `EMAILIT_API_KEY_1`, `EMAILIT_API_KEY_2`, `EMAILIT_API_KEY_FOR_AILUROPHOBIA`) returned HTTP 200 for `GET /domains?limit=1`.

### Recommendation

Emailit is now `api_verified_readonly`. The smallest safe next connector is a disabled/manual-first health check over domains/events/templates that emits only counts and field names. Do not add email sends, contact writes, domain verification/DNS mutations, template publish/update, webhook creation, suppression updates, or API-key writes until a separate issue defines an explicit write contract, test-recipient policy, idempotency, and rollback/audit evidence.

## Certopus spike

Detailed evidence lives at `automation/certopus-readonly-endpoint-followup.md`.

### Auth shape

- Base URL: `https://api.certopus.com`
- Header: `X-API-KEY: ***`
- Credential source used for live smoke check: secure operator dotenv outside the repo.
- Official Swagger UI at `https://api.certopus.com/` embeds the Certopus API spec and documents the `apiKeyAuth` header name as `X-API-KEY`.

### Verified read-only pulls

DIG-45 verified the current `CERTOPUS_API_KEY` with summary-only safe GET checks:

| Resource | Endpoint | Result | Notes |
|---|---|---|---|
| Templates | `GET /v1/templates` | HTTP 200 | Returned grouped template categories and counts. Raw template/background/email data should not be stored. |
| Organisations | `GET /v1/organisations` | HTTP 200 | Returned two organisation records. Summaries should avoid names and branding payloads unless explicitly approved. |
| Wallet | `GET /v1/wallet` | HTTP 200 | Returned zero visible certificate records in the smoke check. Keep as count-only. |
| SMTP | `GET /v1/smtp` | HTTP 200 | Returned `empty`. Do not expose or mutate SMTP configuration. |

### Recommendation

Certopus is `api_verified_readonly` for disabled/manual-first metadata health checks. The smallest safe connector summarizes template category counts, organisation count/integration flag, wallet certificate count, and SMTP presence only. Do not issue certificates, send emails, download/export PDFs or spreadsheets, import/delete recipients, mutate SMTP/domain/white-label settings, or activate live n8n scheduling without a separate write contract and automation-owned credential.

## WbizTool API viability follow-up

Detailed evidence lives at `automation/wbiztool-api-viability.md`.

### Auth and endpoint shape

- Official docs root: `https://wbiztool.com/docs/`.
- Official API base: `https://wbiztool.com/api/v1/`.
- Auth is not bearer/header based; documented calls put `client_id` and `api_key` in the request body.
- WhatsApp-specific report/send surfaces also require `whatsapp_client` from the WbizTool WhatsApp Setting page.
- WbizTool uses `POST` even for read-like routes such as WhatsApp client list and message report/history, so it does not fit the current GET-only `tools/appsumo_readonly_probe.py` safety contract.

### Current verification result

The secure operator dotenv currently contains `WBIZTOOL_COM_API_KEY`, but no WbizTool-specific client ID or WhatsApp client ID env name was found. A data-minimized credential-shape probe to `POST /api/v1/whatsapp-client/list/` with only the available API key returned JSON status `0` / message `Auth Error` and no client list. This narrows the blocker to missing required credential pairing rather than unknown API base.

### Recommendation

Classify WbizTool as `credential_pair_incomplete`. Do not create an n8n workflow or add it to the GET-only probe yet. The next operator ask is `WBIZTOOL_CLIENT_ID` and, for any report/history work, `WBIZTOOL_WHATSAPP_CLIENT_ID`. Once supplied, the first safe check should be a manual-only, summary/redacted `whatsapp-client/list` status count; message sends, scheduling, cancellation, phone verification, media handling, group sends, and message-history exports remain unauthorized without a separate write contract.

## CallScaler API viability follow-up

Detailed evidence lives at `automation/callscaler-api-viability.md`.

### Auth and endpoint shape tested

- Prior public API shape from DIG-64: `https://callscaler.com/api/v1/`.
- Auth attempted: `Authorization: Bearer ***`.
- Secure runtime key names present: `CALLSCALER_API_KEY` and `CALLSCALER_API_KEY_1` in `/mnt/c/Users/ohu00/Documents/.env`; neither is present in `tools/.env`.

### Current verification result

Both secure key names returned HTTP 401 for metadata-first GET probes to `/calls?limit=1`, `/dashboard/stats`, `/numbers?limit=1`, and `/analytics/summary`. Shallow identity guesses `/user`, `/account`, and `/me` also returned HTTP 401. Only HTTP status, JSON type, and top-level `error` key presence were recorded; no call, number, caller, recording, transcript, billing, or key material was stored.

### Recommendation

Classify CallScaler as `api_key_present_but_unauthenticated`, not access-verified. Keep the guarded `callscaler` resources in `tools/appsumo_readonly_probe.py` for repeatable manual retries after the operator supplies a fresh read-only key or confirms the current base/auth/account context. Do not create a live n8n workflow or export raw call/number data until a successful summary-only read is reviewed.

## Dadan API viability follow-up

Detailed evidence lives at `automation/dadan-api-viability.md`.

### Auth and endpoint shape

- Active API base for the documented integration path: `https://app.dadan.io/api/v1/usedadan`.
- Header auth: `X-Dadan-API-Key: ***`.
- App-embedded developer docs expose `POST /requestrecording` for creating recording request links and `GET /requestrecording/{RequestCode}` for retrieving one request's details.
- The prior guessed `https://api.dadan.io` host still returns Cloudflare HTTP 525 and should not be used for connector work.

### Current verification result

The secure operator dotenv contains `DADAN_API_KEY`, while `tools/.env` does not. Missing-key and invalid-key probes return distinct 401 messages, and the runtime key returns the distinct valid-key/wrong-request-code 401 (`Request not found or not created by API key`) when checking a zero UUID request code. This validates the base/auth shape without exposing real recording/video data.

### Recommendation

Classify Dadan as `api_verified_limited_readonly`. Keep only the guarded `dadan recording-request` GET resource in `tools/appsumo_readonly_probe.py`; it requires `--request-code` and should be used only with an operator-approved, non-sensitive request code created by the same key. Do not create a live n8n workflow yet. Dadan request creation, uploads, video sharing, webhook/account/developer setting changes, and raw submission/video exports require a separate write contract and field-level privacy approval.

## Procesio API viability follow-up

Detailed evidence lives at `automation/procesio-api-viability.md`.

### Auth and endpoint shape

- Official docs root: `https://docs.procesio.com/`.
- Live Swagger/OpenAPI: `https://webapi.procesio.app/swagger/index.html` and `https://webapi.procesio.app/swagger/v1.19/swagger.json`.
- Current API base: `https://webapi.procesio.app`.
- API-key auth uses separate request headers: `key: <api_key_name>` and `value: <api_key_value>`.
- Workspace-scoped routes may also require `workspace: <workspace_name_or_id>`.

### Current verification result

The secure operator dotenv contains `PROCESIO_API_KEY`, but no matching `PROCESIO_API_KEY_NAME` or approved workspace header value was found. Safe non-mutating auth-shape probes against `/api/Users/me`, `/api/Workspaces`, `/api/Projects/count`, and `/api/Projects` narrowed the blocker: bearer auth and value-only auth return HTTP 407, while `key` + `value` with the env-var name as a guessed key name returns HTTP 401. This confirms the Web API shape but not successful account access.

### Recommendation

Classify Procesio as `api_base_verified_key_name_missing`. Keep the guarded `procesio` resources in `tools/appsumo_readonly_probe.py`, but do not run repeated guesses or create a live n8n workflow. The next operator ask is the exact API key name paired with the existing `PROCESIO_API_KEY` value, plus approved workspace context and confirmation that only metadata reads (`users-me`, `workspaces`, `projects-count`, then optionally one summary-only project page) are authorized. Do not run `POST /api/Projects/{id}/run`, create processes/actions/webhooks/schedules/credentials, export run history, or mutate workspace/user/project settings without a separate write/execute contract.

## Boost.space and Flowlu tenant-shaped follow-up

Detailed evidence lives at `automation/boost-flowlu-api-viability.md`.

### Boost.space

- Official OpenAPI schemas: `https://apidoc.boost.space/5.2.3.json` and `https://apidoc.boost.space/develop.json`.
- Official server shape: `https://{system}.boost.space/api`.
- Auth shape: `Authorization: Bearer ***`.
- Current secure source state: `BOOST_SPACE_API_KEY` and Make/Boost.space integrator variables are present, but no verified `{system}.boost.space` tenant hostname was found.
- Generic probes against `https://api.boost.space/`, `/v1/modules`, and `/api/modules` returned HTTP 404; `https://developers.boost.space/api/user` returned HTTP 401 with the available key.
- Classification: `tenant_base_missing`, not key-invalid.

### Flowlu

- Official OpenAPI schema: `https://www.flowlu.com/api/json/openapien.json`.
- Official server shape: `https://{company}.flowlu.com/api/v1/module`.
- Auth shape: query parameter `api_key=***`.
- Current secure source state: `FLOWLU_API_KEY` is present, but no verified `{company}.flowlu.com` workspace subdomain was found.
- Generic probes against `https://www.flowlu.com/api/v1/module` and `/crm/account/list` returned HTTP 404 even with the key as `api_key`.
- Classification: `tenant_subdomain_missing`, not key-invalid.

### What the utility supports

`tools/appsumo_readonly_probe.py` now includes guarded configs for future unblocked runs:

| Platform | Resource | Endpoint path | Required flag | Purpose |
|---|---|---|---|---|
| `boostspace` | `address-countries` | `/address/country` | `--base-url https://<verified-system>.boost.space/api` | Low-sensitivity first API smoke check. |
| `boostspace` | `activities` | `/activities` | `--base-url https://<verified-system>.boost.space/api` | Later summary-only operational activity check; may contain sensitive records. |
| `flowlu` | `crm-accounts` | `/crm/account/list` | `--base-url https://<verified-company>.flowlu.com/api/v1/module` | CRM account smoke check; summary-only only. |
| `flowlu` | `agile-projects` | `/agile/projects/list` | same | Project inventory summary. |
| `flowlu` | `tasks` | `/task/tasks/list` | same | Task status summary. |
| `flowlu` | `invoices` | `/fin/invoice/list` | same | Finance-sensitive; avoid unless explicitly approved. |

The script exits before making a request if `boostspace` or `flowlu` is run without a verified `--base-url`. This is deliberate: do not guess tenant/system subdomains.

### Recommendation

Do not promote either tool into n8n yet. The next useful action is an operator access-completion packet: exact Boost.space system URL, exact Flowlu company URL, confirmation that the existing API keys belong to those tenants, and approval for the first summary-only read. Once supplied, run one `--page-size 1 --summary-only --json` probe before writing any n8n workflow spec.

## AgenticFlow API viability follow-up

Detailed evidence lives at `automation/agenticflow-api-viability.md`.

### Auth and endpoint shape

- Current REST base: `https://api.agenticflow.ai/`.
- Header auth: `Authorization: Bearer ***`
- Current secure source contains AgenticFlow API-key material; the official CLI expects `AGENTICFLOW_API_KEY`, so use `--secret-name AGENTICFLOW_AI_KEY` with the repo probe only when that alternate runtime name is needed.
- Lowest-risk documented REST read: `GET /v1/agents/?workspace_id={workspace_id}[&project_id={project_id}&limit=...]`.
- Official docs do not document a REST endpoint to list workspaces or projects for an API key. Use the AgenticFlow UI or `af whoami/bootstrap` after proper auth setup to obtain IDs.

### Current verification result

Runtime-only checks confirmed the key is accepted by the official CLI (`npx --yes @pixelml/agenticflow-cli whoami --json` reported key-present behavior and exposed workspace/project context). Direct REST checks without context returned HTTP 400 `Project ID must be provided for project-scoped resource access`; the guarded `GET /v1/agents/` probe with CLI-returned workspace/project context returned HTTP 403 `API key does not have access to this project`. Guessed `/v1/workspaces`, `/v1/projects`, `/v1/me`, and `/v1/auth/me` routes are not documented and should not be used.

### What the utility supports

| Platform | Resource | Endpoint path | Required flags | Purpose |
|---|---|---|---|---|
| `agenticflow` | `agents` | `/v1/agents/` | `--workspace-id`; provide `--project-id` for current key behavior | Summary-only first check of visible agent metadata/counts. |

### Recommendation

Classify AgenticFlow as `api_auth_verified_project_scope_mismatch`. Do not promote it into n8n yet. The next operator ask is the correct project-scoped API key/context, ideally as a dedicated automation-owned `AGENTICFLOW_API_KEY_AUTOMATION`. The first approved probe should be manual, page-size 1, summary-only JSON after REST returns HTTP 200. Do not create/run agents, stream messages, publish, trigger webhooks, create workflows/workforces, configure MCP, or mutate platform objects without a separate write contract.

## CallScaler API viability follow-up

Detailed evidence lives at `automation/callscaler-access-surface.md`.

### Auth and endpoint shape

- Public API base: `https://callscaler.com/api/v1/`.
- Header auth: `Authorization: Bearer ***`.
- Browser/API-key management path from docs: `https://v3.callscaler.com/app/settings?tab=api-keys`.
- Lowest-risk read-only probes remain `GET /calls?limit=1`, `GET /dashboard/stats`, `GET /numbers?limit=1`, and later aggregate-only analytics/call-flow checks.

### Current verification result

DIG-64 found `CALLSCALER_API_KEY` and `CALLSCALER_API_KEY_1` in the secure operator dotenv while `tools/.env` has no CallScaler key names. Both secure keys are non-placeholder shaped, but both returned HTTP 401 JSON `unauthorized` for `GET /calls?limit=1`, `GET /dashboard/stats`, and `GET /numbers?limit=1`. The default key also returned HTTP 401 for `GET /analytics/calls` and `GET /call-flows`. No raw call records, phone numbers, caller identities, recordings, transcripts, billing details, or key values were printed or stored.

### Recommendation

Classify CallScaler as `api_base_verified_credentials_invalid_or_unscoped`. Do not add it to `tools/appsumo_readonly_probe.py`, n8n, or scheduled health checks yet. The next operator ask is to verify or rotate a real API key from the CallScaler settings page, confirm which account/tenant the two secure dotenv keys belong to, and approve one first read-only resource. Until then, avoid recordings/transcripts, exports, phone-number inventory dumps, webhook/integration changes, number provisioning, call-flow edits, and billing changes.

## Late / Zernio API viability follow-up

Detailed evidence lives at `automation/late-zernio-api-viability.md`.

### Auth and endpoint shape

- Public docs have rebranded from Late to Zernio: `https://docs.getlate.dev/` redirects to `https://docs.zernio.com/`.
- Official OpenAPI is reachable at `https://docs.zernio.com/api/openapi` and documents bearer auth.
- Documented Zernio base is `https://zernio.com/api`; legacy/operator base `https://getlate.dev/api/v1` was also verified and remains the default in `tools/appsumo_readonly_probe.py` to preserve AppSumo/operator naming.
- Secure runtime has `GETLATE_DEV_API_KEY`; `tools/.env` does not include the key.

### Current verification result

Using the secure operator dotenv explicitly, both `https://getlate.dev/api/v1` and `https://zernio.com/api/v1` returned HTTP 200 for `profiles`, `accounts`, `accounts/health`, `posts?limit=1`, `usage-stats`, and `users`. Only status, top-level keys, and visible counts were recorded. No raw account handles, profile URLs, users, post bodies, media URLs, tokens, or account records were stored.

One process-environment `GETLATE_DEV_API_KEY` value encountered during the pass was malformed and returned HTTP 401, so repeatable runs should pass `--env-file /mnt/c/Users/ohu00/Documents/.env` or use a clean automation-owned n8n credential/env value.

### What the utility supports

| Platform | Resource | Endpoint path | Required flags | Purpose |
|---|---|---|---|---|
| `late` | `profiles` | `/profiles` | none | Profile/account readiness count. |
| `late` | `accounts` | `/accounts` | none | Connected-account inventory count; suppress handles/URLs. |
| `late` | `account-health` | `/accounts/health` | none | Coarse account health summary. |
| `late` | `posts` | `/posts` | none; use `--page-size 1` | Queue/post visibility smoke check; suppress raw post content. |
| `late` | `usage-stats` | `/usage-stats` | none | Coarse plan/usage signal; treat billing fields as sensitive. |
| `late` | `users` | `/users` | none | User count/access smoke check; suppress raw user details. |

### Recommendation

Classify Late/Zernio as `api_verified_readonly`. Promote only as a disabled/manual-first health workflow using summary-only data over profiles/accounts/account-health/posts/usage/users. Do not create/schedule/publish/edit/delete/queue posts, send validations, connect/disconnect social accounts, handle DMs/comments/inbox items, mutate webhooks/users/API keys/settings, or export raw account/profile/post/user data without a separate write contract and dedicated automation credential.

## Flotiq API viability follow-up

Detailed evidence lives at `automation/flotiq-api-viability.md`.

### Auth and endpoint shape

- Official docs: `https://flotiq.com/docs/API/`.
- API base: `https://api.flotiq.com`.
- Header auth: `X-AUTH-TOKEN: ***`.
- Secure runtime has `FLOTIQ_API_KEY`; `tools/.env` should not store the broad discovery key.

### Current verification result

Using the secure operator dotenv explicitly, `GET /api/v1/internal/contenttype?limit=1&pageSize=1` returned HTTP 200 with 11 total content type definitions, and `GET /api/v1/content/_media?limit=1&pageSize=1` returned HTTP 200 with 0 visible media records in the smoke check. Only status, counts, request metadata, and non-secret field names were recorded. No raw CMS entry payloads, media URLs, author/user emails, full schema definitions, tokens, API keys, webhooks, or environment settings were stored.

### What the utility supports

| Platform | Resource | Endpoint path | Required flags | Purpose |
|---|---|---|---|---|
| `flotiq` | `content-types` | `/api/v1/internal/contenttype` | none; use `--page-size 1 --summary-only --json` | Count visible content type definitions and verify CMS model-surface access. |
| `flotiq` | `media` | `/api/v1/content/_media` | none; use `--page-size 1 --summary-only --json` | Media-library count smoke check without storing media records or URLs. |

### Recommendation

Classify Flotiq as `api_verified_readonly`. Promote only as a disabled/manual-first health workflow using summary-only data over content-type/media counts, and use a dedicated `FLOTIQ_API_KEY_AUTOMATION` or n8n credential before any schedule. Do not create/update/delete/import/publish content types or content objects, upload/export media, list arbitrary content-object models, mutate API keys/webhooks/users/environments/GraphQL/schema settings, or expose raw CMS content/media/schema data without a separate write/export contract and field-level privacy approval.

## Formaloo API viability follow-up

Detailed evidence lives at `automation/formaloo-api-viability.md`.

### Auth and endpoint shape

- Official developer/help docs: `https://help.formaloo.com/en/collections/3330828-for-developers` and `https://docs.formaloo.com/#/`.
- Current API base used by repo tooling: `https://api.formaloo.me/v3.0`.
- Token mint route: `POST /oauth2/authorization-token/` with `x-api-key: ***`, `Authorization: Basic ***`, and `grant_type=client_credentials`.
- Read routes then use `x-api-key: ***` plus `Authorization: JWT <short-lived-token>`.
- Secure runtime has `FORMALOO_API_KEY` and `FORMALOO_API_SECRET`; `tools/.env` should not store raw discovery secrets.

### Current verification result

Using the secure operator dotenv explicitly, the v3 token route returned HTTP 200 and the guarded probe returned HTTP 200 for `forms` and `profile` in `--summary-only --json` mode. `forms` reported a visible page count plus account total count, and `profile` reported only coarse readiness fields. No API key, secret, JWT, raw form URL/title/body, owner email/name/phone, respondent data, submission row, export file, webhook URL, or team setting value was copied into the repo.

### What the utility supports

| Platform | Resource | Endpoint path | Required flags | Purpose |
|---|---|---|---|---|
| `formaloo` | `forms` | `/forms/` | none; use `--page-size 1 --summary-only --json` | Count visible forms and safe metadata field names. |
| `formaloo` | `profile` | `/profile/` | none; use `--summary-only --json` | Coarse profile/account readiness summary without owner PII. |

### Recommendation

Classify Formaloo as `api_verified_readonly`. Promote only as a disabled/manual-first health workflow using summary-only data over forms/profile metadata, and use a dedicated `FORMALOO_API_KEY_AUTOMATION` + `FORMALOO_API_SECRET_AUTOMATION` or n8n credential before any schedule. Do not submit forms, create/update/delete forms/apps/projects/dashboards/portals/fields, export rows/submissions/responses, create/change webhooks/custom domains/team settings, or expose raw owner/respondent/form data without a separate write/export contract and field-level privacy approval.

## n8n promotion path

DIG-36 added a concrete repo-side n8n implementation pack at `automation/n8n-workflows/appsumo-readonly-summary.md` plus disabled/manual-only draft JSON at `automation/n8n-workflows/appsumo-readonly-summary.draft.json`. DIG-40 added the Emailit-specific disabled/manual-first health pack at `automation/n8n-workflows/emailit-readonly-health-check.md` plus `automation/n8n-workflows/emailit-readonly-health-check.draft.json`. DIG-47 added the Certopus-specific disabled/manual-first health pack at `automation/n8n-workflows/certopus-readonly-health-check.md` plus `automation/n8n-workflows/certopus-readonly-health-check.draft.json`. DIG-66 added the Late/Zernio disabled/manual-first health pack at `automation/n8n-workflows/late-readonly-health-check.md` plus `automation/n8n-workflows/late-readonly-health-check.draft.json`. DIG-67 added the Formaloo disabled/manual-first health pack at `automation/n8n-workflows/formaloo-readonly-health-check.md` plus `automation/n8n-workflows/formaloo-readonly-health-check.draft.json`. DIG-68 added the Flotiq disabled/manual-first health pack at `automation/n8n-workflows/flotiq-readonly-health-check.md` plus `automation/n8n-workflows/flotiq-readonly-health-check.draft.json`. No live n8n workflow was created or activated by these repo-side passes.

1. Keep `tools/appsumo_readonly_probe.py` as the local smoke-test and debug harness.
2. Configure credentials in n8n, not in workflow JSON or repo files.
3. For Paperclip-safe summaries, run the probe with `--summary-only --json` so raw record samples are omitted before any notification/comment/writeback node.
4. Start with a scheduled weekly Agiled read-only workflow:
   - Execute Command or HTTP Request node for `/users` and `/projects`.
   - Function node to reduce raw records to counts/status summaries.
   - GitHub/Paperclip handoff only after summaries are reviewed for PII leakage.
5. Add AITable read-only summaries now that DIG-35 verified `GET /spaces`, `GET /nodes`, and one `GET /records` path with the current secure dotenv. Use low-frequency schedules and summarize counts/status fields before emitting to Paperclip/GitHub.
6. Emailit now has a dedicated disabled/manual-first n8n health pack (`emailit-readonly-health-check.md` + `.draft.json`) for domains/events/templates/optional webhooks summaries. Scheduled use requires an automation-owned `EMAILIT_API_KEY_AUTOMATION` credential and reviewed notification digest first; sends and contact/domain/template/webhook mutations remain out of scope.
7. Certopus has a dedicated disabled/manual-first n8n health pack (`certopus-readonly-health-check.md` + `.draft.json`) for templates, organisations, wallet count, and SMTP presence summaries. Scheduled use requires an automation-owned `CERTOPUS_API_KEY_AUTOMATION` credential and reviewed notification digest first; certificate issuance, sends, downloads/exports, recipient mutations, SMTP/domain/white-label changes, and wallet mutations remain out of scope.
8. Late/Zernio has a dedicated disabled/manual-first n8n health pack (`late-readonly-health-check.md` + `.draft.json`) for profiles/accounts/account-health/posts/usage/users summaries. Scheduled use requires an automation-owned `GETLATE_DEV_API_KEY_AUTOMATION` or n8n credential and reviewed notification digest first; posting, scheduling, publishing, social-account changes, inbox/comment/DM handling, webhooks, users, API keys, and account settings mutations remain out of scope.
9. Formaloo has a dedicated disabled/manual-first n8n health pack (`formaloo-readonly-health-check.md` + `.draft.json`) for forms/profile summaries. Scheduled use requires a dedicated `FORMALOO_API_KEY_AUTOMATION` + `FORMALOO_API_SECRET_AUTOMATION` pair or n8n credential and reviewed notification digest first; form submissions, schema/app/project/webhook/team mutations, exports, and raw owner/respondent/form data remain out of scope.
10. Flotiq has a dedicated disabled/manual-first n8n health pack (`flotiq-readonly-health-check.md` + `.draft.json`) for content-type/media count summaries. Scheduled use requires an automation-owned `FLOTIQ_API_KEY_AUTOMATION` or n8n credential and reviewed notification digest first; content/model/media/API-key/webhook/user/environment mutations and raw CMS exports remain out of scope.
11. Do not enable write/update nodes for any platform without a separate issue, explicit field-level contract, rollback plan, and credentials dedicated to automation.

## External blockers requiring real credentials or operator access

- Agiled: exact client/company/task endpoint map and permission scope for the existing API key.
- AITable.ai: access works with the current secure operator dotenv; future production runs still need an explicit n8n credential record or rotated automation-owned key. If a run returns 401, first verify the dotenv/credential source before changing API hosts.
- Emailit: read-only API v2 health checks are verified with the current secure operator dotenv. Production n8n use still needs a dedicated automation-owned Emailit key and operator approval; no sends or contact/domain/template/webhook mutations are authorized.
- Certopus: read-only metadata/count checks are verified with the current secure operator dotenv using `X-API-KEY`. Production n8n use still needs a dedicated credential record or rotated automation-owned key and operator review; no certificate issuance, sends, recipient mutations, downloads/exports, SMTP/domain/white-label changes, or wallet mutations are authorized.
- Late/Zernio: read-only profiles/accounts/account-health/posts/usage/users checks are verified with the current secure operator dotenv using bearer auth. Production n8n use still needs a dedicated credential record or rotated `GETLATE_DEV_API_KEY_AUTOMATION`, manual digest review, and a decision on legacy `getlate.dev` versus current `zernio.com` base. No posting/scheduling/publishing, social-account changes, inbox/comment/DM handling, webhook/user/API-key/account mutations, or raw profile/account/post/user exports are authorized.
- Formaloo: read-only forms/profile checks are verified with the current secure operator dotenv using the official short-lived JWT flow. Production n8n use still needs a dedicated credential record or rotated `FORMALOO_API_KEY_AUTOMATION` + `FORMALOO_API_SECRET_AUTOMATION`, manual digest review, and Cron approval. No form submissions, response exports, schema/app/project/webhook/team/custom-domain mutations, or raw owner/respondent/form payload exports are authorized.
- Flotiq: read-only content-type/media count checks are verified with the current secure operator dotenv using `X-AUTH-TOKEN`. Production n8n use still needs a dedicated credential record or rotated `FLOTIQ_API_KEY_AUTOMATION`, manual digest review, and Cron approval. No content type/object/media/API-key/webhook/user/environment/GraphQL/schema mutations, arbitrary content-object listing, media URL export, or raw CMS payload export is authorized.
- AgenticFlow: the current key authenticates through the official CLI, but REST/n8n connector work is project-scope blocked: `GET /v1/agents/` with CLI-returned workspace/project context returned HTTP 403 `API key does not have access to this project`. Need the correct project-scoped key/context, preferably as `AGENTICFLOW_API_KEY_AUTOMATION`. First successful read should be only `agenticflow agents --page-size 1 --summary-only --json`; no agent/workflow/workforce/MCP runs or mutations are authorized.
- Procesio: official Web API base/auth are verified (`https://webapi.procesio.app`, separate `key` + `value` headers), but the current secure source has only the `PROCESIO_API_KEY` value. Need the exact API key name plus approved workspace header/context before retrying guarded GET-only probes. First successful reads should be `procesio users-me`, `workspaces`, and `projects-count` in summary-only mode; no project runs, process/workflow/webhook/credential/schedule changes, run-output exports, or workspace/user/project mutations are authorized.
- CallScaler: API base/auth shape are verified (`https://callscaler.com/api/v1/`, bearer auth), and secure dotenv keys exist, but both available keys returned HTTP 401 on `calls`, `dashboard/stats`, and `numbers` first reads. Need a verified/rotated API key from CallScaler settings or an approved browser session before any connector or n8n work; no raw call data, recordings, transcripts, phone numbers, exports, webhooks, numbers, call flows, or billing changes are authorized.
- Flowlu: exact tenant/company subdomain (`https://<company>.flowlu.com/`) and approval for the first summary-only read-only resource; the current API key cannot be validated without that tenant base.
- Boost.space: exact system URL (`https://<system>.boost.space/`) and confirmation that the current API key is a profile bearer token for that system; generic `api.boost.space` probes are known-wrong.
- n8n: deployed n8n API access and credential records for Agiled/AITable/Emailit before scheduled automation can run.
- Paperclip/GitHub writes: if connector summaries are posted back automatically, those writes must use the approved authenticated API/CLI paths and must avoid raw customer data.
