# Procesio API viability follow-up

Related issue: DIG-60
Verification timestamp: 2026-05-08T09:40:12Z
Owner: Automation Engineer

## Scope and safety

This pass checked public Procesio documentation, Swagger/OpenAPI metadata, secure runtime-only env names, and data-minimized non-mutating HTTP reads only.

No Procesio process, webhook, credential, schedule, project, action, form, user, workspace, integration, or execution was created, updated, deleted, triggered, imported, assigned, or scheduled. No raw API key, AppSumo license code, cookie, workspace data, process payload, or private run output is stored in this repo.

## Official docs and current API shape

Public Procesio docs are hosted at `https://docs.procesio.com/`.

The relevant official pages are:

- `https://docs.procesio.com/api-keys` — Generate API Key for authorization.
- `https://docs.procesio.com/running-a-process-with-api-keys` — Running a process with API Keys.
- `https://docs.procesio.com/developers-guide/procesio-api-documentation` — Procesio API documentation.
- `https://webapi.procesio.app/swagger/index.html` — live Swagger UI.
- `https://webapi.procesio.app/swagger/v1.19/swagger.json` — current OpenAPI JSON observed in the Swagger UI.

The live OpenAPI document reports:

- OpenAPI: `3.0.1`
- Title/version: `Web API - v1.19`
- Base host used by docs/examples: `https://webapi.procesio.app`
- API-key security schemes:
  - `key` header: API key name
  - `value` header: API key value
- Bearer security also exists for JWT auth, but the API-key docs and run-process page explicitly use the separate `key` + `value` headers.

The docs' process-run example is intentionally a write/execute route and is out of scope for this issue:

- `POST /api/Projects/{id}/run`
- Required headers include `key`, `value`, and `workspace`
- Request body example includes `connectionId`

## Runtime credential inventory

Secure source inspection found:

- `/mnt/c/Users/ohu00/Documents/.env`: `PROCESIO_API_KEY` exists.
- `tools/.env`: no active Procesio key material found during this pass.
- No `PROCESIO_API_KEY_NAME`, Procesio workspace name, or Procesio workspace/tenant identifier was found in the inspected env names.

The raw key value was not printed or copied. The observed `PROCESIO_API_KEY` value appears to be a single opaque key value, not a combined `name:value` pair.

## Non-mutating validation performed

Safe unauthenticated/public checks:

- `GET https://procesio.com/` returned HTTP 200.
- `GET https://docs.procesio.com/` returned HTTP 200.
- `GET https://webapi.procesio.app/swagger/index.html` returned HTTP 200.
- `GET https://webapi.procesio.app/swagger/v1.19/swagger.json` returned HTTP 200 and exposed the official OpenAPI path list.

Safe credential-shape checks against low-risk GET endpoints were performed with no body persistence:

- `GET /api/Users/me`
- `GET /api/Workspaces`
- `GET /api/Projects/count`
- `GET /api/Projects`

Observed results:

| Auth shape attempted | Result | Interpretation |
|---|---|---|
| `Authorization: Bearer <PROCESIO_API_KEY>` | HTTP 407 `Unauthorized` on all checked GETs | The available API-key value is not accepted as a JWT bearer token. |
| `value: <PROCESIO_API_KEY>` only | HTTP 407 `Unauthorized` on all checked GETs | Key value alone is insufficient. |
| `key: PROCESIO_API_KEY` + `value: <PROCESIO_API_KEY>` | HTTP 401 `Unauthorized` on all checked GETs | The API recognizes the key/value auth shape but rejects the env var name as the API key name. |
| `X-API-Key: <PROCESIO_API_KEY>` | HTTP 407 `Unauthorized` on all checked GETs | Procesio does not use the generic `X-API-Key` shape for this Web API. |

No successful authenticated account/workspace read was established because the current runtime supplies only the API key value, while Procesio requires the API key name and value as separate headers.

## Smallest safe endpoint set after unblock

Once the operator supplies the missing API key name and workspace name/identifier, use only manual-first GET probes in this order:

1. `GET /api/Users/me` — confirm identity/permission shape; do not store private profile fields.
2. `GET /api/Workspaces` — confirm accessible workspace names/IDs; summarize only counts and non-sensitive field names.
3. `GET /api/Projects/count` with the approved `workspace` header if required — confirm read permission without listing process definitions.
4. `GET /api/Projects` with `--page-size 1 --summary-only --json` only after the count succeeds — summarize visible count/status fields, not full process metadata or payloads.

Avoid these until a separate write/execute contract exists:

- `POST /api/Projects/{id}/run`
- all process/action/credential/webhook/schedule/form/user/workspace create/update/delete routes
- API key creation/deletion
- credential test/create/update routes
- webhook assignment/listening actions
- run history/output exports unless specifically approved and redacted

## Tooling added

`tools/appsumo_readonly_probe.py` now includes a guarded `procesio` platform with GET-only resources:

```bash
cd /mnt/c/Users/ohu00/Desktop/digitalproducts/tools
source .venv/bin/activate

python appsumo_readonly_probe.py procesio --list-resources

# Requires both the API key value and the separate key name.
python appsumo_readonly_probe.py procesio users-me \
  --env-file /mnt/c/Users/ohu00/Documents/.env \
  --api-key-name <procesio_api_key_name> \
  --summary-only --json

# For workspace-scoped reads after identity succeeds.
python appsumo_readonly_probe.py procesio projects-count \
  --env-file /mnt/c/Users/ohu00/Documents/.env \
  --api-key-name <procesio_api_key_name> \
  --workspace <workspace_name> \
  --summary-only --json
```

The probe intentionally exits before making a request if `--api-key-name` is missing, because `PROCESIO_API_KEY` alone supplies only the `value` header and repeated key-value guesses are not useful.

## Classification

`api_base_verified_key_name_missing`

Procesio is not yet a viable read-only Hermes/Paperclip operator surface from the current runtime. The blocker is precise: the API base and OpenAPI contract are verified, and `PROCESIO_API_KEY` exists, but the required separate API key name and workspace context are missing.

## Operator ask

Provide, without exposing it in repo docs or issue comments:

1. The Procesio API key name that pairs with the existing `PROCESIO_API_KEY` value, preferably as `PROCESIO_API_KEY_NAME` or a dedicated `PROCESIO_API_KEY_NAME_AUTOMATION`.
2. The approved workspace header value for first reads, if the account has more than one workspace.
3. Confirmation that the key is allowed to perform only metadata reads for `Users/me`, `Workspaces`, and `Projects/count` before any process/project listing.
4. A dedicated automation-owned key pair if Procesio is later promoted into n8n.

After those are supplied, run only the guarded GET probes above, review summary-only output for data leakage, and then decide whether a disabled/manual-first n8n health check is warranted.
