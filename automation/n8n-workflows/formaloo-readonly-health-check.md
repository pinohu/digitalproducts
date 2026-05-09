# Formaloo Read-Only Health Check (Disabled / Manual-First)

Related issue: DIG-67
Source viability note: `automation/formaloo-api-viability.md`
Draft workflow JSON: `automation/n8n-workflows/formaloo-readonly-health-check.draft.json`

## Purpose

Run a data-minimized Formaloo account-readiness digest without submitting forms, exporting responses, mutating schemas, or exposing respondent/profile PII.

## Safety contract

- Import the draft JSON disabled/manual-first only.
- Use a dedicated n8n credential or automation-owned environment pair, not the broad discovery key, before scheduling.
- Required secrets: `FORMALOO_API_KEY` and `FORMALOO_API_SECRET` (or dedicated automation equivalents mapped in n8n).
- The Execute Command node must run only `tools/appsumo_readonly_probe.py formaloo ... --summary-only --json`.
- Do not call Formaloo rows/submissions/export endpoints.
- Do not create, submit, update, delete, publish, unpublish, or change forms/apps/projects/dashboards/portals/webhooks/team settings.
- Do not include raw form titles, URLs, owner names, owner emails, respondent data, custom domains, webhook URLs, JWTs, API keys, or secrets in notifications.

## Manual runbook

From the repo root on a trusted runner:

```bash
cd /mnt/c/Users/ohu00/Desktop/digitalproducts
source tools/.venv/bin/activate

python tools/appsumo_readonly_probe.py formaloo forms \
  --env-file /mnt/c/Users/ohu00/Documents/.env \
  --page-size 1 \
  --summary-only \
  --json

python tools/appsumo_readonly_probe.py formaloo profile \
  --env-file /mnt/c/Users/ohu00/Documents/.env \
  --summary-only \
  --json
```

Expected safe output shape:

- `forms`: HTTP status, visible page count, total form count, status/type counts if present, and non-secret field names only.
- `profile`: HTTP status, coarse readiness fields such as verified-email boolean, score/balance/credit booleans/numbers, trial flag, HubSpot connected flag, and team field-name visibility only.

## n8n node outline

1. Manual Trigger (Cron disabled until reviewed).
2. Execute Command: Formaloo forms summary.
3. Execute Command: Formaloo profile summary.
4. Code node: parse JSON, reject payloads containing banned key fragments (`email`, `token`, `secret`, `api_key`, `url`, `address`, `phone`, `name`) except approved summary field names.
5. Notification node: send only the approved digest to the operator review channel.

## Promotion gate

Do not enable Cron until all are true:

- Dedicated Formaloo automation credential exists in n8n or secure runner env.
- Manual output has been reviewed and contains no raw form/profile/respondent data.
- Operator approves cadence and recipient.
- A separate issue defines any desired write/export behavior. DIG-67 does not authorize writes.
