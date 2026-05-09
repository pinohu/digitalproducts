# Emailit Read-Only Health Check Workflow

Status: repo-side implementation pack; no live n8n workflow created in this run.
Related issues: DIG-40, DIG-39
Implementation target: `n8n.audreysplace.place`
Safety class: read-only, data-minimized, manual-first

## Purpose

Promote the verified DIG-39 Emailit API v2 read-only surface into a concrete n8n health workflow pack. The workflow is intended to answer: "Can the Emailit workspace still be reached, and do the key operational surfaces look present enough for future email infrastructure work?"

It is not a sending workflow. It must not send emails, create contacts, alter domains or DNS verification, edit templates, create webhooks, update suppressions, rotate API keys, or activate any live email automation.

## Truthful live-build status

No live n8n draft workflow was created or activated by this pass. The artifacts added here are:

- this node-by-node workflow spec;
- `emailit-readonly-health-check.draft.json`, an import/reference draft with `active: false` and placeholder/no-op notification;
- a manual verification path using `tools/appsumo_readonly_probe.py emailit ... --summary-only --json`.

Before any live run, an operator still must provide n8n editor access plus a dedicated automation-owned Emailit API key credential. The keys discovered during DIG-39 are acceptable for discovery only and should not become permanent scheduler credentials by accident.

## Non-negotiable safety rules

1. Only Emailit API v2 HTTP `GET` requests or `tools/appsumo_readonly_probe.py emailit` GET-only commands are allowed.
2. Keep the workflow disabled until a manual execution is reviewed for PII/secret leakage.
3. Do not add Emailit send, create, update, delete, DNS/domain verification, contact import, suppression update, template mutation, webhook mutation, or API-key mutation nodes.
4. Emit counts, status buckets, content types, and allowed field-name lists only. Do not emit message bodies, recipient addresses, contact records, API key material, webhook secrets, template bodies, or raw domain/account records.
5. Do not store raw secrets in n8n workflow JSON, repo files, logs, or Paperclip comments.
6. If posting back to Paperclip in a later issue, every API request must use `Authorization: Bearer $PAPERCLIP_API_KEY`; comments/issue updates must also include `X-Paperclip-Run-Id: $PAPERCLIP_RUN_ID`. Do not use board/browser/local-board writes.
7. Keep Cron, GitHub writeback, and Paperclip writeback disabled until a notification-only run has been reviewed.

## Credential-source contract

| Secret / credential | Source of truth | Used by | Notes |
|---|---|---|---|
| `EMAILIT_API_KEY_AUTOMATION` | Preferred n8n credential/env record created specifically for this workflow | Emailit domains/events/templates/webhooks GETs | Create a dedicated read-capable automation key if Emailit supports scope separation. Rotate and label owner/date in n8n. |
| `EMAILIT_API_KEY` | Temporary fallback secure runtime env only | Manual discovery runs | DIG-39 verified this works from the secure operator dotenv; do not rely on it for scheduled production. |
| `EMAILIT_API_KEY_1` / `EMAILIT_API_KEY_2` / `EMAILIT_API_KEY_FOR_AILUROPHOBIA` | Secure operator dotenv only | Emergency comparison during troubleshooting | All returned HTTP 200 for `GET /domains?limit=1` in DIG-39, but their workspace/account purpose is not documented enough for scheduler ownership. |
| Notification credential | n8n credential | Operator success/failure digest | Required before enabling Cron. Email/Slack/Discord is fine if it does not expose raw records. |
| `PAPERCLIP_API_KEY` / `PAPERCLIP_RUN_ID` | n8n env only, future optional writeback | Optional Paperclip comments/issue updates | Not enabled in this draft. Must follow authenticated curl/run-id mutation rules. |
| GitHub PAT | n8n credential only, future optional writeback | Optional repo digest commits | Not enabled in this draft. Fine-grained contents write only; never commit raw Emailit records. |

## Recommended schedule

- Start with Manual Trigger only.
- After one reviewed notification-only run: weekly Monday 09:15 America/New_York.
- If a launch-critical Emailit dependency is later approved, consider daily checks during launch week only, then return to weekly.
- Do not run more than daily without an explicit rate-limit and data-retention review.

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
  "emailit_base_url": "https://api.emailit.com/v2",
  "preferred_secret_name": "EMAILIT_API_KEY_AUTOMATION",
  "fallback_secret_name": "EMAILIT_API_KEY",
  "paperclip_issue_id": "714683bd-df7c-4709-945c-f46c8eb7698f"
}
```

### 3. Domains Health Summary

Preferred implementation: Execute Command node using the repo utility:

```bash
cd /mnt/c/Users/ohu00/Desktop/digitalproducts/tools
./.venv/bin/python appsumo_readonly_probe.py emailit domains \
  --secret-name EMAILIT_API_KEY_AUTOMATION \
  --page-size 25 \
  --summary-only \
  --json
```

Fallback for manual local review only:

```bash
./.venv/bin/python appsumo_readonly_probe.py emailit domains \
  --env-file /mnt/c/Users/ohu00/Documents/.env \
  --secret-name EMAILIT_API_KEY \
  --page-size 1 \
  --summary-only \
  --json
```

Allowed output: HTTP status, visible count, content type, and non-secret field names/status buckets. Do not emit domain names, DNS values, SPF/DKIM tokens, or verification secrets into Paperclip/GitHub.

### 4. Events Health Summary

```bash
cd /mnt/c/Users/ohu00/Desktop/digitalproducts/tools
./.venv/bin/python appsumo_readonly_probe.py emailit events \
  --secret-name EMAILIT_API_KEY_AUTOMATION \
  --page-size 25 \
  --summary-only \
  --json
```

Allowed output: aggregate event status/type buckets and record counts. Do not emit recipient addresses, subjects, message bodies, raw event IDs, or provider payloads.

### 5. Templates Health Summary

```bash
cd /mnt/c/Users/ohu00/Desktop/digitalproducts/tools
./.venv/bin/python appsumo_readonly_probe.py emailit templates \
  --secret-name EMAILIT_API_KEY_AUTOMATION \
  --page-size 25 \
  --summary-only \
  --json
```

Allowed output: template count and safe field-name/schema presence. Do not emit template HTML/text/body, preview URLs, or customer-specific content.

### 6. Optional Webhooks Status Summary

Keep enabled only as a metadata/status check:

```bash
cd /mnt/c/Users/ohu00/Desktop/digitalproducts/tools
./.venv/bin/python appsumo_readonly_probe.py emailit webhooks \
  --secret-name EMAILIT_API_KEY_AUTOMATION \
  --page-size 25 \
  --summary-only \
  --json
```

Allowed output: count and status buckets. Do not emit webhook URLs, signing secrets, or payload samples. Do not create or update webhooks.

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
  - `summary_time_utc`
- Drop `sample`, raw response body, URLs with query strings, IDs, emails, names, domain names, template bodies, event payloads, webhook URLs, and API key fields.
- Set `raw_records_emitted=false` explicitly.

### 8. Build Digest

The digest should look like:

```markdown
# Emailit read-only health summary

Generated: 2026-05-08T00:00:00.000Z
Safety: Emailit API v2 GET-only; raw records omitted; no sends/mutations attempted.

- domains: HTTP 200; visible count 1.
- events: HTTP 200; visible count 25; status buckets: delivered 20 / opened 5.
- templates: HTTP 200; visible count 0.
- webhooks: HTTP 200; visible count 0.

No raw Emailit records, message bodies, recipient addresses, template bodies, webhook URLs, DNS secrets, or API key material emitted.
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
| 401/403 | Stop immediately and notify credential owner. Verify the n8n credential name/source before changing API base. Do not fall back to random `EMAILIT_API_KEY_*` variables in scheduled runs without operator approval. |
| 404 endpoint | Mark the resource unsupported and continue other resources. Confirm API v2 docs before changing route shape. Do not test write routes. |
| 429/rate limit | Retry twice with exponential backoff: 5 minutes, then 30 minutes. If still failing, stop and notify; do not tighten the schedule. |
| 5xx/network timeout | Retry once after 5 minutes, then stop and notify with resource name and status only. Do not dump raw stdout/stderr if it may contain records. |
| Parse/schema error | Stop digest build, notify that normalization failed, and include only node/resource/status metadata. |
| Paperclip/GitHub writeback failure | Future-only: keep notification digest as source of truth, retry writeback once, then leave manual fallback instructions. |

## Manual verification checklist

1. Run `tools/.venv/bin/python tools/verify_tools.py` from repo root.
2. Confirm n8n has a dedicated Emailit credential/env value such as `EMAILIT_API_KEY_AUTOMATION` before any scheduled run.
3. Run these commands in a controlled manual environment:

```bash
cd /mnt/c/Users/ohu00/Desktop/digitalproducts

tools/.venv/bin/python tools/appsumo_readonly_probe.py emailit domains \
  --env-file /mnt/c/Users/ohu00/Documents/.env \
  --page-size 1 \
  --summary-only \
  --json

tools/.venv/bin/python tools/appsumo_readonly_probe.py emailit events \
  --env-file /mnt/c/Users/ohu00/Documents/.env \
  --page-size 5 \
  --summary-only \
  --json

tools/.venv/bin/python tools/appsumo_readonly_probe.py emailit templates \
  --env-file /mnt/c/Users/ohu00/Documents/.env \
  --page-size 5 \
  --summary-only \
  --json
```

4. Confirm outputs contain no raw API keys, customer emails, message bodies, contact records, DNS token values, webhook URLs, or template bodies.
5. Import `emailit-readonly-health-check.draft.json` into n8n, keep it disabled, and run manually against the dedicated credential.
6. Review notification output before enabling Cron.

## External systems still requiring real credentials

- n8n: editor access, import permission, and credential record creation are required; no live n8n draft was created here.
- Emailit: a dedicated automation-owned key is required before production scheduling. DIG-39 discovery keys prove API viability but are not a durable scheduler contract.
- Paperclip: only needed if a future issue enables summary comments; use authenticated API requests and run IDs for mutations.
- GitHub: only needed if future digest commits are enabled.
- Gumroad, Neon, and Vercel: not used by this Emailit health check, but remain required elsewhere in the production stack.
