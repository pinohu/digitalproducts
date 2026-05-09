# Late / Zernio API Viability (DIG-66)

Verification date: 2026-05-08
Owner: Automation Engineer
Status: `api_verified_readonly`

## Scope

This pass verifies whether the AppSumo Late account can support a guarded, read-only operator surface. Late's public docs now present the service as Zernio, but the existing operator/AppSumo credential name remains `GETLATE_DEV_API_KEY`.

Safety rules applied:

- Used only public docs/OpenAPI and runtime-only secure credential sources.
- Performed only HTTP `GET` requests.
- Did not create, schedule, queue, edit, publish, delete, validate-send, or otherwise mutate posts.
- Did not connect/disconnect social accounts, send DMs, reply to comments, moderate inbox items, create webhooks, or alter account/API-key settings.
- Stored only endpoint/auth shape, HTTP status, top-level JSON keys, and visible counts; no raw account handles, profile URLs, post bodies, users, tokens, or API responses are committed.

## Docs and auth shape

- Public docs root: `https://docs.zernio.com/`.
- Legacy docs path `https://docs.getlate.dev/` redirects/rebrands to Zernio.
- Official OpenAPI endpoint: `https://docs.zernio.com/api/openapi`.
- OpenAPI title/version observed: `Zernio API`, API version `1.0.1`.
- Documented auth: `Authorization: Bearer <api-key>`.
- Documented base URL: `https://zernio.com/api`.
- Legacy/operator base verified live: `https://getlate.dev/api/v1`.
- Current repo default keeps the operator-facing service key as `late` with `GETLATE_DEV_API_KEY` and default base `https://getlate.dev/api/v1`; use `--base-url https://zernio.com/api/v1` if the legacy host is ever retired.

## Credential source

- `GETLATE_DEV_API_KEY` exists in the secure operator dotenv outside the repo (`/mnt/c/Users/ohu00/Documents/.env` in this WSL environment).
- `tools/.env` does not carry the key.
- The process environment value encountered during this pass was malformed and returned HTTP 401; explicitly loading the secure dotenv with `--env-file /mnt/c/Users/ohu00/Documents/.env` restored access.
- No raw key material was printed, copied, or committed.

## Verified read-only probes

All probes below used bearer auth and data-minimized output.

| Resource | Endpoint | Result | Safe signal |
|---|---|---|---|
| `profiles` | `GET /profiles` | HTTP 200 | Top-level `profiles`; visible count 1. |
| `accounts` | `GET /accounts` | HTTP 200 | Top-level `accounts`, `hasAnalyticsAccess`; visible count 8. |
| `account-health` | `GET /accounts/health` | HTTP 200 | Top-level `accounts`, `summary`; visible count 8. |
| `posts` | `GET /posts?limit=1` | HTTP 200 | Top-level `pagination`, `posts`; visible count 1. Keep sample/raw post data suppressed. |
| `usage-stats` | `GET /usage-stats` | HTTP 200 | Top-level billing/plan/usage summary keys; treat as account-sensitive and summary-only. |
| `users` | `GET /users` | HTTP 200 | Top-level `canDelete`, `currentUserId`, `users`; visible count 1. Keep user data suppressed. |

The same endpoint set also returned HTTP 200 against `https://zernio.com/api/v1/...` during runtime-only checks.

## Repo changes

- `tools/appsumo_readonly_probe.py` now includes a guarded `late` platform with these GET-only resources:
  - `profiles`
  - `accounts`
  - `account-health`
  - `posts`
  - `usage-stats`
  - `users`
- The probe redacts `url` and `username` fields in addition to existing PII/secret-shaped fields before emitting samples or aggregates.
- `tools/README.md`, `automation/README.md`, and `automation/appsumo-readonly-connector-spikes.md` document the verified auth shape, safe commands, and non-negotiable mutation exclusions.
- `automation/n8n-workflows/late-readonly-health-check.md` and `.draft.json` provide a disabled/manual-first n8n workflow pack. No live n8n workflow or credential record was created.

## Safe command examples

```bash
cd /mnt/c/Users/ohu00/Desktop/digitalproducts

# List supported Late/Zernio GET-only resources
tools/.venv/bin/python tools/appsumo_readonly_probe.py late --list-resources

# Data-minimized manual checks
tools/.venv/bin/python tools/appsumo_readonly_probe.py late profiles --env-file /mnt/c/Users/ohu00/Documents/.env --page-size 1 --summary-only --json
tools/.venv/bin/python tools/appsumo_readonly_probe.py late accounts --env-file /mnt/c/Users/ohu00/Documents/.env --page-size 1 --summary-only --json
tools/.venv/bin/python tools/appsumo_readonly_probe.py late account-health --env-file /mnt/c/Users/ohu00/Documents/.env --page-size 1 --summary-only --json
tools/.venv/bin/python tools/appsumo_readonly_probe.py late posts --env-file /mnt/c/Users/ohu00/Documents/.env --page-size 1 --summary-only --json
tools/.venv/bin/python tools/appsumo_readonly_probe.py late usage-stats --env-file /mnt/c/Users/ohu00/Documents/.env --summary-only --json
tools/.venv/bin/python tools/appsumo_readonly_probe.py late users --env-file /mnt/c/Users/ohu00/Documents/.env --page-size 1 --summary-only --json
```

## n8n promotion recommendation

Late/Zernio is viable for a disabled/manual-first health summary, not for autonomous posting.

First workflow scope:

1. Manual trigger only.
2. Execute the local Python probe with `--summary-only --json` for `profiles`, `accounts`, `account-health`, `posts`, `usage-stats`, and `users`.
3. Normalize to counts, HTTP status, top-level field names, and coarse health/usage indicators.
4. Notify/review only; do not post to Paperclip or enable Cron until the digest has been reviewed for PII leakage.
5. Scheduled use should use a dedicated automation-owned credential such as `GETLATE_DEV_API_KEY_AUTOMATION` or an n8n credential, not the operator-discovery key.

Out of scope for this workflow:

- Post create/update/delete/schedule/publish/queue operations.
- Validation sends, content generation, bulk imports, or social account connect/disconnect.
- DMs, comments, inbox, moderation, webhook creation/update/delete, API-key mutation, or account settings changes.
- Raw account handle/profile URL/post body/user export into repo, Paperclip, GitHub, Slack, email, or n8n execution logs.

## Remaining external actions

- Create a real n8n credential record for Late/Zernio before any n8n run.
- Prefer a rotated/dedicated automation key before enabling any schedule.
- Confirm whether future production should keep `https://getlate.dev/api/v1` or switch the n8n credential/base to `https://zernio.com/api/v1` if Late sunsets the legacy host.
