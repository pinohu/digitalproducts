# Certopus Read-Only Health Check Workflow

Status: repo-side implementation pack; no live n8n workflow created in this run.
Related issues: DIG-47, DIG-45
Implementation target: `n8n.audreysplace.place`
Safety class: read-only, data-minimized, manual-first

## Purpose

Promote the verified DIG-45 Certopus API surface into a concrete n8n health workflow pack. The workflow is intended to answer: "Can the Certopus workspace still be reached, and do the lowest-risk metadata surfaces still look healthy enough for future training/completion workflow design?"

It is not a certificate operations workflow. It must not issue certificates, create or delete recipients, send mail, download/export certificate or recipient data, mutate wallet state, or change SMTP/domain/white-label settings.

## Truthful live-build status

No live n8n draft workflow was created or activated by this pass. The artifacts added here are:

- this node-by-node workflow spec;
- `certopus-readonly-health-check.draft.json`, an import/reference draft with `active: false` and placeholder/no-op notification;
- a manual verification path using `tools/appsumo_readonly_probe.py certopus ... --summary-only --json`.

Before any live run, an operator still must provide n8n editor access plus a dedicated automation-owned Certopus API key credential. The `CERTOPUS_API_KEY` discovered during DIG-45 is acceptable for discovery/manual verification only and should not become the permanent scheduler credential by accident.

## Non-negotiable safety rules

1. Only Certopus HTTP `GET` requests or `tools/appsumo_readonly_probe.py certopus` GET-only commands are allowed.
2. Keep the workflow disabled until a manual execution is reviewed for recipient data, branding payload, template body, SMTP, wallet, and secret leakage.
3. Do not add Certopus certificate issuance, recipient create/delete/import, send-mail, download/export, SMTP mutation, domain/white-label mutation, webhook, or wallet mutation nodes.
4. Emit counts, category names, status/presence flags, and reviewed non-secret field-name lists only.
5. Do not emit recipient names/emails, certificate IDs tied to people, rendered certificate content, template/background bodies, organisation names, brand images/signatures, SMTP host/user/password values, wallet addresses/transaction details, API keys, or raw response bodies.
6. Do not store raw secrets in n8n workflow JSON, repo files, logs, or Paperclip comments.
7. If posting back to Paperclip in a later issue, every API request must use `Authorization: Bearer $PAPERCLIP_API_KEY`; comments/issue updates must also include `X-Paperclip-Run-Id: $PAPERCLIP_RUN_ID`. Do not use board/browser/local-board writes.
8. Keep Cron, GitHub writeback, and Paperclip writeback disabled until a notification-only run has been reviewed.

## Credential-source contract

| Secret / credential | Source of truth | Used by | Notes |
|---|---|---|---|
| `CERTOPUS_API_KEY_AUTOMATION` | Preferred n8n credential/env record created specifically for this workflow | Certopus templates/organisations/wallet/SMTP GETs | Create or rotate a dedicated automation-owned key if Certopus supports scoped/owned keys. Label owner/date/purpose in n8n. |
| `CERTOPUS_API_KEY` | Temporary fallback secure runtime env only | Manual discovery and local verification runs | DIG-45 verified this works from the secure operator dotenv. Do not rely on it for scheduled production unless the operator explicitly approves that ownership model. |
| Notification credential | n8n credential | Operator success/failure digest | Required before enabling Cron. Email/Slack/Discord is fine if it does not expose raw records. |
| `PAPERCLIP_API_KEY` / `PAPERCLIP_RUN_ID` | n8n env only, future optional writeback | Optional Paperclip comments/issue updates | Not enabled in this draft. Must follow authenticated API and run-id mutation rules. |
| GitHub PAT | n8n credential only, future optional writeback | Optional repo digest commits | Not enabled in this draft. Fine-grained contents write only; never commit raw Certopus records. |

## Recommended schedule

- Start with Manual Trigger only.
- After one reviewed notification-only run: weekly Monday 09:25 America/New_York.
- If a productized training/completion workflow later depends on Certopus, consider a short daily check during the launch week only, then return to weekly.
- Do not run more than daily without an explicit rate-limit, data-retention, and payload-leakage review.

## Node plan

### 1. Manual Trigger

Use Manual Trigger for the initial import. Do not add Cron until review passes.

### 2. Set Runtime Config

Set fields:

```json
{
  "run_mode": "manual_review",
  "max_page_size": 25,
  "emit_raw_records": false,
  "certopus_base_url": "https://api.certopus.com",
  "preferred_secret_name": "CERTOPUS_API_KEY_AUTOMATION",
  "fallback_secret_name": "CERTOPUS_API_KEY",
  "paperclip_issue_id": "a9a52fb6-4009-4d21-8a0b-bd4cbf426f62"
}
```

### 3. Templates Health Summary

Preferred implementation: Execute Command node using the repo utility:

```bash
cd /mnt/c/Users/ohu00/Desktop/digitalproducts/tools
./.venv/bin/python appsumo_readonly_probe.py certopus templates \
  --secret-name CERTOPUS_API_KEY_AUTOMATION \
  --page-size 25 \
  --summary-only \
  --json
```

Fallback for manual local review only:

```bash
./.venv/bin/python appsumo_readonly_probe.py certopus templates \
  --env-file /mnt/c/Users/ohu00/Documents/.env \
  --secret-name CERTOPUS_API_KEY \
  --page-size 5 \
  --summary-only \
  --json
```

Allowed output: HTTP status, category names/counts, visible count, content type, and non-secret field names. Do not emit template bodies, background image payloads, certificate artwork, email-template bodies, template IDs tied to real campaigns, or raw records.

### 4. Organisations Health Summary

```bash
cd /mnt/c/Users/ohu00/Desktop/digitalproducts/tools
./.venv/bin/python appsumo_readonly_probe.py certopus organisations \
  --secret-name CERTOPUS_API_KEY_AUTOMATION \
  --page-size 25 \
  --summary-only \
  --json
```

Allowed output: organisation count and aggregate `integrationAllowed` presence/count if available. Do not emit organisation names, image URLs, brand images, brand signatures, admin/user details, or raw payloads.

### 5. Wallet Count Summary

```bash
cd /mnt/c/Users/ohu00/Desktop/digitalproducts/tools
./.venv/bin/python appsumo_readonly_probe.py certopus wallet \
  --secret-name CERTOPUS_API_KEY_AUTOMATION \
  --page-size 25 \
  --summary-only \
  --json
```

Allowed output: visible wallet/certificate count and HTTP status only. Do not emit recipient-linked certificate IDs, wallet addresses, transaction details, credential IDs, or certificate records.

### 6. SMTP Presence Summary

```bash
cd /mnt/c/Users/ohu00/Desktop/digitalproducts/tools
./.venv/bin/python appsumo_readonly_probe.py certopus smtp \
  --secret-name CERTOPUS_API_KEY_AUTOMATION \
  --page-size 5 \
  --summary-only \
  --json
```

Allowed output: presence/empty status only. Do not emit SMTP hostnames, usernames, passwords, ports, sender identities, DKIM/SPF details, or raw configuration.

### 7. Normalize Connector Results

Code node rules:

- Parse JSON from each Execute Command stdout.
- Keep only:
  - `platform`
  - `resource`
  - `status_code`
  - `content_type`
  - `record_count_visible`
  - `status_counts`
  - `visible_field_names` after reviewing that the field names are not secrets
  - `category_counts` if the utility emits it for template groups
  - `summary_time_utc`
- Drop `sample`, raw response body, URLs with query strings, IDs, emails, names, organisation labels, image URLs, template bodies, SMTP settings, wallet details, and API key fields.
- Set `raw_records_emitted=false`, `certopus_writes_attempted=false`, and `certificate_operations_attempted=false` explicitly.

### 8. Build Digest

The digest should look like:

```markdown
# Certopus read-only health summary

Generated: 2026-05-08T00:00:00.000Z
Safety: Certopus GET-only via X-API-KEY; raw records omitted; no certificate operations/sends/mutations attempted.

- templates: HTTP 200; visible count 88; category counts present.
- organisations: HTTP 200; visible count 2; integrationAllowed summary present.
- wallet: HTTP 200; visible count 0.
- smtp: HTTP 200; presence empty.

No raw Certopus records, recipient data, certificate payloads, organisation names/branding assets, SMTP settings, wallet details, or API key material emitted.
```

### 9. Notify Operator

Replace the placeholder/no-op node in the draft JSON with an approved notification channel. Review this notification output before enabling any schedule or writeback.

### 10. Optional Paperclip/GitHub Writeback

Not enabled in this draft. If a future issue authorizes writeback:

- Keep notification-only success as the upstream gate.
- Paperclip comments must be posted with authenticated terminal/curl or n8n HTTP Request using both `Authorization: Bearer $PAPERCLIP_API_KEY` and `X-Paperclip-Run-Id: $PAPERCLIP_RUN_ID` for the mutation.
- GitHub commits must include only the data-minimized digest, not raw records.

## Retry and failure handling

| Failure | Handling |
|---|---|
| 401/403 | Stop immediately and notify credential owner. Verify the n8n credential name/source and `X-API-KEY` header before changing API base. Do not fall back to random discovery keys in scheduled runs without operator approval. |
| 404 endpoint | Mark the resource unsupported and continue other resources. Confirm Swagger route shape before changing route. Do not test write routes. |
| 429/rate limit | Retry twice with exponential backoff: 5 minutes, then 30 minutes. If still failing, stop and notify; do not tighten the schedule. |
| 5xx/network timeout | Retry once after 5 minutes, then stop and notify with resource name and status only. Do not dump raw stdout/stderr if it may contain records. |
| Parse/schema error | Stop digest build, notify that normalization failed, and include only node/resource/status metadata. |
| Unexpected non-empty wallet count | Keep count-only, mark for operator review, and do not inspect/download linked certificate records without a separate issue. |
| Non-empty SMTP config | Emit presence only, mark for operator review, and do not display SMTP details. |
| Paperclip/GitHub writeback failure | Future-only: keep notification digest as source of truth, retry writeback once, then leave manual fallback instructions. |

## Manual verification checklist

1. Run `tools/.venv/bin/python tools/verify_tools.py` from repo root.
2. Confirm n8n has a dedicated Certopus credential/env value such as `CERTOPUS_API_KEY_AUTOMATION` before any scheduled run.
3. Run these commands in a controlled manual environment:

```bash
cd /mnt/c/Users/ohu00/Desktop/digitalproducts

tools/.venv/bin/python tools/appsumo_readonly_probe.py certopus templates \
  --env-file /mnt/c/Users/ohu00/Documents/.env \
  --page-size 5 \
  --summary-only \
  --json

tools/.venv/bin/python tools/appsumo_readonly_probe.py certopus organisations \
  --env-file /mnt/c/Users/ohu00/Documents/.env \
  --page-size 5 \
  --summary-only \
  --json

tools/.venv/bin/python tools/appsumo_readonly_probe.py certopus wallet \
  --env-file /mnt/c/Users/ohu00/Documents/.env \
  --page-size 5 \
  --summary-only \
  --json

tools/.venv/bin/python tools/appsumo_readonly_probe.py certopus smtp \
  --env-file /mnt/c/Users/ohu00/Documents/.env \
  --page-size 5 \
  --summary-only \
  --json
```

4. Inspect the digest before notification/writeback. Confirm it contains only status/count/presence/category/field-name information.
5. Import `certopus-readonly-health-check.draft.json` into n8n only as inactive/manual. Configure the notification node and credential references in n8n, not in the repo.
6. Execute manually once, review output, then document the review before enabling any weekly Cron in a separate authorized issue.

## External systems still requiring real credentials

- n8n: editor/API access and a real credential/env record for `CERTOPUS_API_KEY_AUTOMATION`.
- Certopus: a dedicated automation-owned API key or explicit approval to use the existing key for scheduled read-only health checks.
- Notification channel: Email/Slack/Discord credential for operator digest delivery.
- Paperclip/GitHub writeback: future-only; requires explicit issue authorization and safe writeback implementation.
