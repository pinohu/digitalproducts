# Emailit Read-Only Endpoint Follow-Up

Related issue: DIG-39
Verification date: 2026-05-08
Owner: Automation Engineer

## Scope and safety rules

- Only public documentation lookup and authenticated HTTP `GET` probes were performed.
- No email sends, template creation, domain verification, DNS changes, subscriber/contact writes, webhook creation, suppression writes, API-key writes, or other mutations were attempted.
- No raw API keys, bearer tokens, email addresses, domain names, contact records, message bodies, cookies, or credential-file contents are stored in this document.
- Runtime credentials were loaded from the secure operator dotenv at `/mnt/c/Users/ohu00/Documents/.env`; repo files only name environment variables.

## Documentation findings

Emailit docs currently identify API v2 as the active API:

- Docs base: `https://emailit.com/docs/`
- API reference: `https://emailit.com/docs/api-reference/`
- REST base URL: `https://api.emailit.com/v2`
- Auth shape: `Authorization: Bearer <api_key>`
- API v1 status: deprecated and scheduled for removal at the end of February 2026.

The earlier `/v1/templates`, `/v1/emails`, `/v1/users/me`, and `/domains` guesses were using the wrong generation/route shape. The current read-only routes are under `/v2`.

## Credential signals checked

Secure dotenv variable names present at runtime:

- `EMAILIT_API_KEY`
- `EMAILIT_API_KEY_1`
- `EMAILIT_API_KEY_2`
- `EMAILIT_API_KEY_FOR_AILUROPHOBIA`

All four keys returned HTTP 200 for `GET https://api.emailit.com/v2/domains?limit=1` with bearer auth. This suggests the keys are valid for the same currently reachable workspace surface rather than stale or wrong-environment tokens.

## Read-only endpoint verification

Default key used for endpoint breadth check: `EMAILIT_API_KEY` from the secure operator dotenv.

Command pattern:

```bash
cd /mnt/c/Users/ohu00/Desktop/digitalproducts
source tools/.venv/bin/activate
python tools/appsumo_readonly_probe.py emailit <resource> \
  --env-file /mnt/c/Users/ohu00/Documents/.env \
  --page-size 1 \
  --summary-only \
  --json
```

| Resource | Endpoint | Result | Data-minimized signal |
|---|---|---:|---|
| Templates | `GET /v2/templates` | HTTP 200 | 0 visible records |
| Domains | `GET /v2/domains` | HTTP 200 | 1 visible record |
| Emails | `GET /v2/emails` | HTTP 200 | 1 visible record |
| Contacts | `GET /v2/contacts` | HTTP 200 | 1 visible record |
| Audiences | `GET /v2/audiences` | HTTP 200 | 1 visible record |
| Suppressions | `GET /v2/suppressions` | HTTP 200 | 1 visible record |
| Webhooks | `GET /v2/webhooks` | HTTP 200 | 0 visible records |
| API keys | `GET /v2/api-keys` | HTTP 200 | 1 visible record |
| Events | `GET /v2/events` | HTTP 200 | 1 visible record |

No raw samples were committed. The probe's `--summary-only --json` mode reports counts, status buckets, and non-secret field names only.

## Verdict

Emailit should be upgraded from `api_reachable_permission_unverified` to `api_verified_readonly`.

The blocker was endpoint generation/route shape, not an invalid key or missing permission for basic read-only resources. The correct API base and auth shape are now confirmed:

```text
Base URL: https://api.emailit.com/v2
Auth: Authorization: Bearer $EMAILIT_API_KEY
```

## Smallest safe connector spike to add next

Use the repo utility now extended with `emailit` support:

```bash
python tools/appsumo_readonly_probe.py emailit domains \
  --env-file /mnt/c/Users/ohu00/Documents/.env \
  --page-size 1 \
  --summary-only \
  --json

python tools/appsumo_readonly_probe.py emailit events \
  --env-file /mnt/c/Users/ohu00/Documents/.env \
  --page-size 5 \
  --summary-only \
  --json
```

Recommended n8n promotion order, still manual-first and disabled by default:

1. Domains health check: confirm at least one sending domain exists and summarize verification-status fields only.
2. Events health check: summarize delivery-event status/type counts without message bodies or recipient addresses.
3. Templates health check: confirm whether reusable templates exist; do not create/publish templates from automation yet.
4. Only after an explicit write contract: consider a transactional email send spike against a test-only recipient/domain with idempotency, allowlisted `from`, and a rollback/audit plan.

## External systems and credentials still required

- Real Emailit workspace access is still required for dashboard-level checks, domain policy decisions, and any future sends.
- A dedicated automation-owned Emailit API key should be created before n8n production use; the current secure operator keys are enough for discovery but should not become permanent scheduler credentials by accident.
- n8n still requires a real Emailit credential record and a disabled/manual workflow review before any Cron or Paperclip/GitHub writeback.
- No live product launch email workflow should depend on Emailit until sender domain, reply-to, suppression handling, unsubscribe/compliance requirements, and test-recipient policy are approved.
