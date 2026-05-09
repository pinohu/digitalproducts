# Flotiq API Viability

Verification timestamp: 2026-05-08T11:28:00Z
Owner: Automation Engineer
Related issue: DIG-68

## Verdict

Flotiq is `api_verified_readonly` for disabled/manual-first CMS metadata health checks.

The secure operator dotenv at `/mnt/c/Users/ohu00/Documents/.env` contains `FLOTIQ_API_KEY`. No raw API key, content entry payload, media URL, user/author email, token, webhook, environment setting, or exported CMS data was copied into the repo.

## Official sources used

- Flotiq API docs: `https://flotiq.com/docs/API/`
- API base used by repo tooling: `https://api.flotiq.com`
- Auth header documented and verified: `X-AUTH-TOKEN: ***`

## Runtime checks performed

All checks used runtime-only secret loading from `/mnt/c/Users/ohu00/Documents/.env`.

| Probe | Result | Safe signal |
|---|---|---|
| `GET https://api.flotiq.com/api/v1/internal/contenttype?limit=1&pageSize=1` | HTTP 200 | Key can list content type definitions. Summary-only probe reported 11 total content type definitions and only non-secret top-level field names; schema/meta definition field names and payload values are omitted from automation summaries. |
| `GET https://api.flotiq.com/api/v1/content/_media?limit=1&pageSize=1` | HTTP 200 | Media content-object route is reachable and currently returned 0 visible records in the smoke check. No media URLs or asset payloads were stored. |
| unauthenticated `GET /api/v1/internal/contenttype` | HTTP 401 | Confirms the authenticated header is required; no fallback anonymous reads are assumed. |

## Tooling added

`tools/appsumo_readonly_probe.py` now supports:

```bash
python tools/appsumo_readonly_probe.py flotiq --list-resources
python tools/appsumo_readonly_probe.py flotiq content-types \
  --env-file /mnt/c/Users/ohu00/Documents/.env \
  --page-size 1 \
  --summary-only \
  --json
python tools/appsumo_readonly_probe.py flotiq media \
  --env-file /mnt/c/Users/ohu00/Documents/.env \
  --page-size 1 \
  --summary-only \
  --json
```

The helper uses `X-AUTH-TOKEN`, performs GET-only requests, redacts secret/PII-shaped fields, and in summary-only mode omits raw record samples. It does not create, update, delete, import, publish, or export CMS content.

## Safe operator surface

Allowed under this read-only classification:

- Count content type definitions.
- Verify that the API key can reach the content-model surface.
- Check media-library count/status without storing media records or URLs.
- Run disabled/manual-first n8n health checks after an operator reviews summary output.

Out of scope without a separate write/export contract:

- Creating, updating, deleting, importing, or publishing content types or content objects.
- Uploading, modifying, deleting, or exporting media.
- Listing arbitrary content-object models beyond explicitly approved content type names.
- Mutating API keys, users, webhooks, environments, GraphQL/schema settings, workflows, or permissions.
- Exporting raw content entries, author/user emails, media URLs, private payload bodies, draft content, or full schema definitions into repo, Paperclip, GitHub, n8n notifications, or logs.

## n8n promotion recommendation

A disabled/manual-first health pack now exists at:

- `automation/n8n-workflows/flotiq-readonly-health-check.md`
- `automation/n8n-workflows/flotiq-readonly-health-check.draft.json`

Before importing or scheduling it in real n8n:

1. Create a dedicated Flotiq automation credential or environment variable such as `FLOTIQ_API_KEY_AUTOMATION`.
2. Run manually with `--summary-only --json`.
3. Review the notification payload for accidental CMS content, media URL, author/user, or schema leakage.
4. Keep Cron disabled until an operator approves cadence and data minimization.

## Classification

`api_verified_readonly`

Flotiq is viable for guarded content-type/media count health checks and operator readiness summaries. It is not approved for content/model/media/API-key/webhook/user/environment mutations, raw content export, or live scheduled automation writes.
