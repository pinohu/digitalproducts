# Flotiq Read-Only Health Check (Disabled / Manual-First)

Related issue: DIG-68
Source viability note: `automation/flotiq-api-viability.md`
Draft workflow JSON: `automation/n8n-workflows/flotiq-readonly-health-check.draft.json`

## Purpose

Run a data-minimized Flotiq CMS readiness digest without exporting content entries, media URLs, schema bodies, users, API keys, webhooks, or environment settings.

## Safety contract

- Import the draft JSON disabled/manual-first only.
- Use a dedicated n8n credential or automation-owned environment value, not the broad discovery key, before scheduling.
- Required secret: `FLOTIQ_API_KEY` or preferably `FLOTIQ_API_KEY_AUTOMATION` in n8n/runtime secret storage.
- The Execute Command nodes must run only `tools/appsumo_readonly_probe.py flotiq ... --summary-only --json`.
- Do not call arbitrary `/api/v1/content/{content_type}` routes unless a future issue approves the exact content type name and output fields.
- Do not create, update, delete, import, publish, unpublish, upload, export, or mutate content types, content objects, media, webhooks, API keys, users, environments, GraphQL/schema settings, or permissions.
- Do not include raw content titles/bodies/slugs, media URLs, author/user emails, full schema definitions, webhook URLs, tokens, API keys, or private CMS payloads in notifications.

## Manual runbook

From the repo root on a trusted runner:

```bash
cd /mnt/c/Users/ohu00/Desktop/digitalproducts
source tools/.venv/bin/activate

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

Expected safe output shape:

- `content-types`: HTTP status, page count, total content-type definition count, and non-secret field names only.
- `media`: HTTP status, page count, total media count, and no raw media records or URLs.

## n8n node outline

1. Manual Trigger (Cron disabled until reviewed).
2. Execute Command: Flotiq content-type summary.
3. Execute Command: Flotiq media summary.
4. Code node: parse JSON and reject payloads containing banned data fragments such as `email`, `token`, `secret`, `api_key`, `url`, `body`, `content`, `schemaDefinition`, `webhook`, or non-summary `sample` data.
5. Notification node: send only the approved digest to the operator review channel.

## Promotion gate

Do not enable Cron until all are true:

- Dedicated Flotiq automation credential exists in n8n or secure runner env.
- Manual output has been reviewed and contains no raw content/media/user/schema data.
- Operator approves cadence and recipient.
- A separate issue defines any desired content-object, write, export, or CMS mutation behavior. DIG-68 does not authorize writes.
