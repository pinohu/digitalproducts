# CallScaler API Viability

Related issue: DIG-64
Verification timestamp: 2026-05-08T10:12:01Z
Owner: Automation Engineer

## Scope and safety rules

This pass was read-only and credential-safe.

- Credential names were inspected only to confirm whether CallScaler key material exists; no raw API keys were printed, copied, or committed.
- Runtime key loading used the secure operator dotenv at `/mnt/c/Users/ohu00/Documents/.env` explicitly, not a browser-agent environment assumption.
- Probes used `GET` only against the prior public/official API shape: `https://callscaler.com/api/v1/` with `Authorization: Bearer`.
- No phone numbers, caller identities, recordings, transcripts, raw call records, billing details, or API keys were stored.
- Output was reduced to HTTP status, JSON type, and top-level response keys only.

## Secure runtime inventory

The secure operator dotenv contains these CallScaler-shaped key names:

- `CALLSCALER_API_KEY`
- `CALLSCALER_API_KEY_1`

`tools/.env` does not contain CallScaler credentials. That means repeatable checks must use `--env-file /mnt/c/Users/ohu00/Documents/.env` or an equivalent secure credential source; do not copy key values into repo files.

## Probe matrix

Both available key names were tested with bearer auth against metadata-minimized GET requests.

| Resource | Endpoint | Result for `CALLSCALER_API_KEY` | Result for `CALLSCALER_API_KEY_1` | Stored data |
|---|---|---:|---:|---|
| Calls first page | `GET /calls?limit=1` | HTTP 401 | HTTP 401 | Status + top-level key `error` only |
| Dashboard stats | `GET /dashboard/stats` | HTTP 401 | HTTP 401 | Status + top-level key `error` only |
| Numbers first page | `GET /numbers?limit=1` | HTTP 401 | HTTP 401 | Status + top-level key `error` only |
| Analytics summary | `GET /analytics/summary` | HTTP 401 | HTTP 401 | Status + top-level key `error` only |
| User guess | `GET /user` | HTTP 401 | HTTP 401 | Status + top-level key `error` only |
| Account guess | `GET /account` | HTTP 401 | HTTP 401 | Status + top-level key `error` only |
| Me guess | `GET /me` | HTTP 401 | HTTP 401 | Status + top-level key `error` only |

The first four routes match the DIG-64 requested safe-read examples. The last three were shallow identity-read guesses used only to distinguish endpoint mismatch from blanket auth failure; they also returned 401.

## Classification

`api_key_present_but_unauthenticated`

CallScaler should not move to `api_verified_readonly` yet. The secure source does include CallScaler-shaped key material, but neither key authenticated against the expected bearer API surface. This is no longer merely an agent-env binding gap: the keys were loaded from the secure dotenv at runtime and still returned 401.

Most likely blockers:

1. the stored CallScaler values are expired, revoked, environment-specific, or not REST API bearer tokens;
2. the account requires a different API base, tenant/account context, or auth header shape than the prior public shape;
3. the key must be reissued from the CallScaler admin/API settings page with read-only scope.

## Guarded tooling added

`tools/appsumo_readonly_probe.py` now includes a guarded `callscaler` platform with these GET-only resources:

- `calls`
- `dashboard-stats`
- `numbers`
- `analytics-summary`
- `user`
- `account`
- `me`

Example verification commands:

```bash
cd /mnt/c/Users/ohu00/Desktop/digitalproducts/tools
source .venv/bin/activate
python appsumo_readonly_probe.py callscaler dashboard-stats --env-file /mnt/c/Users/ohu00/Documents/.env --summary-only --json
python appsumo_readonly_probe.py callscaler calls --env-file /mnt/c/Users/ohu00/Documents/.env --page-size 1 --summary-only --json
python appsumo_readonly_probe.py callscaler numbers --env-file /mnt/c/Users/ohu00/Documents/.env --page-size 1 --summary-only --json
```

Use `--secret-name CALLSCALER_API_KEY_1` to test the alternate key name without printing its value.

## Next operator ask

Please provide one of the following through the approved secure credential channel:

- a fresh CallScaler read-only API key confirmed for `https://callscaler.com/api/v1/` bearer auth;
- the exact current CallScaler API docs/base/auth shape if different from the prior public shape;
- a human-approved browser session path to the CallScaler admin/API settings page so the API issuing context can be verified without exposing call/customer data.

First successful retry should stay metadata-first: `dashboard-stats`, then `numbers --page-size 1 --summary-only`, then `calls --page-size 1 --summary-only` only if the operator approves the call-record field summary. Do not export raw calls, phone numbers, recordings, transcripts, billing records, or caller/customer identifiers.

## Unauthorized work

No live n8n workflow, schedule, webhook, phone/call export, call recording/transcript pull, billing inspection, number provisioning, call-routing change, or write/mutation was created or attempted.
