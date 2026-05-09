# AppSumo Read-Only Summary Workflow — Agiled + AITable

Status: repo-side implementation pack; no live n8n workflow created in this run.
Related issues: DIG-36, DIG-27, DIG-35
Implementation target: `n8n.audreysplace.place`
Safety class: read-only, data-minimized, manual-first

## Purpose

Promote the verified Agiled and AITable read-only connector spikes into a concrete n8n build plan for low-frequency operating summaries. The workflow reports counts, status buckets, and connector health only. It must not export raw CRM records, datasheet rows, bearer tokens, customer emails, or full project/client tables into Paperclip, GitHub, or issue comments.

## Truthful live-build status

No live n8n draft workflow was created or activated by this repo-side pass. The artifacts added here are:

- this node-by-node workflow spec;
- `appsumo-readonly-summary.draft.json`, an import/reference draft with disabled/manual-only settings and placeholder credentials;
- the `tools/appsumo_readonly_probe.py --summary-only` option for data-minimized command output.

Before any live run, an operator still must provide real n8n editor access plus credential records for Agiled, AITable, notifications, and any repo/Paperclip write path.

## Non-negotiable safety rules

1. Only HTTP `GET` requests or `tools/appsumo_readonly_probe.py` GET-only commands are allowed.
2. Do not add create/update/delete/import/webhook-write nodes for Agiled or AITable in this workflow.
3. Keep the workflow disabled until one manual execution has been reviewed for PII leakage.
4. Summaries must prefer counts/status buckets over row-level exports.
5. Do not store raw secrets in n8n workflow JSON, repo files, logs, or Paperclip comments.
6. If posting back to Paperclip, every API request must use `Authorization: Bearer $PAPERCLIP_API_KEY`; comments/issue updates must also include `X-Paperclip-Run-Id: $PAPERCLIP_RUN_ID`.
7. If a connector returns 401, first check credential-source drift before changing API hosts. DIG-35 verified AITable works when the current secure operator dotenv is explicitly loaded.

## Credential-source contract

| Secret / credential | Source of truth | Used by | Notes |
|---|---|---|---|
| `AGILED_API_KEY` | n8n credential record or secure runtime env | Agiled users/projects reads | Existing local spike verified users/projects reads; repeated checks can hit 429. |
| `AITABLE_API_KEY` | n8n credential record or secure runtime env loaded from current secure dotenv | AITable spaces/nodes/records reads | DIG-35 lesson: `tools/.env` may be stale/missing; `/mnt/c/Users/ohu00/Documents/.env` had the working key in WSL. In n8n, create one explicit credential record and label its rotation date. |
| `PAPERCLIP_API_KEY` | n8n credential/env only, if Paperclip comment/update is enabled | Optional Paperclip summary comments | Never use browser/local-board writes. Include run ID for comments/updates. |
| `PAPERCLIP_RUN_ID` | n8n env/run variable, if Paperclip comment/update is enabled | Optional Paperclip summary comments | Required for all Paperclip mutations. |
| GitHub PAT | n8n credential only, if committing summary markdown | Optional repo summary commits | Fine-grained contents write only; do not commit raw records. |
| Notification credential | n8n credential | Failure/success alerts | Email/Slack/Discord destination for connector failures and weekly digest. |

## Recommended schedule

- Start with manual trigger only.
- After review: weekly Monday 09:00 America/New_York.
- Do not run more than daily without a separate rate-limit review.
- Agiled has shown HTTP 429 risk during repeated smoke checks; use low-frequency schedules and backoff.

## Node plan

### 1. Manual Trigger

Use Manual Trigger for the first imported draft. Do not add Cron until review passes.

Output: empty item.

### 2. Set Runtime Config

Set fields:

```json
{
  "run_mode": "manual_review",
  "max_page_size": 25,
  "emit_raw_records": false,
  "paperclip_issue_id": "7d50a585-41ce-467f-a6ba-98afb3dc65cc"
}
```

### 3. Agiled Users Summary

Preferred implementation: Execute Command node using the repo utility:

```bash
cd /mnt/c/Users/ohu00/Desktop/digitalproducts/tools
./.venv/bin/python appsumo_readonly_probe.py agiled users --page-size 25 --summary-only --json
```

Alternative: HTTP Request node:

- Method: GET
- URL: `https://app.agiled.app/api/v1/users`
- Headers: `Accept: application/json`, `Authorization: Bearer {{$credentials.agiledApiKey}}`
- Query: `limit=25`, `pageSize=25`

### 4. Agiled Projects Summary

Execute Command:

```bash
cd /mnt/c/Users/ohu00/Desktop/digitalproducts/tools
./.venv/bin/python appsumo_readonly_probe.py agiled projects --page-size 25 --summary-only --json
```

### 5. AITable Spaces Summary

Execute Command:

```bash
cd /mnt/c/Users/ohu00/Desktop/digitalproducts/tools
./.venv/bin/python appsumo_readonly_probe.py aitable spaces --page-size 25 --summary-only --json
```

If using a secure external dotenv in a local runner, add `--env-file /path/to/current-secure.env`. In n8n production, prefer a dedicated credential/env record over mounting an operator's personal dotenv.

### 6. Optional AITable Nodes/Records Summary

Only enable after an operator selects exact safe IDs. Keep these disabled in the initial draft:

```bash
./.venv/bin/python appsumo_readonly_probe.py aitable nodes --space-id <approved_space_id> --page-size 25 --summary-only --json
./.venv/bin/python appsumo_readonly_probe.py aitable records --datasheet-id <approved_datasheet_id> --page-size 25 --summary-only --json
```

Do not run broad records pulls across all datasheets. Pick only approved datasheets whose fields are safe to aggregate.

### 7. Normalize Connector Results

Function node rules:

- Parse JSON from each command/HTTP node.
- Keep only:
  - `platform`
  - `resource`
  - `status_code`
  - `record_count_visible`
  - `status_counts`
  - `visible_field_names` only if needed for schema review
  - timestamp
- Drop `sample`, raw response body, request URL query strings, emails, names, descriptions, notes, comments, and IDs unless explicitly needed for connector health.

Example output item:

```json
{
  "platform": "agiled",
  "resource": "projects",
  "status_code": 200,
  "record_count_visible": 12,
  "status_counts": {"active": 7, "completed": 5},
  "summary_time_utc": "{{$now}}"
}
```

### 8. Build Digest

Function node creates a short markdown digest:

```markdown
# AppSumo read-only weekly summary

- Agiled users: HTTP 200, 3 visible records.
- Agiled projects: HTTP 200, 12 visible records, status buckets: active 7 / completed 5.
- AITable spaces: HTTP 200, 2 visible spaces.

No raw CRM records or datasheet rows emitted. Workflow is read-only.
```

### 9. Notify Operator

Send the digest to the configured notification channel. This is required before enabling any repo or Paperclip writeback.

### 10. Optional Paperclip/GitHub Writeback

Keep disabled until the notification-only run is reviewed.

Paperclip comment write, if enabled later:

```bash
curl -fsS -X POST \
  -H "Authorization: Bearer $PAPERCLIP_API_KEY" \
  -H "X-Paperclip-Run-Id: $PAPERCLIP_RUN_ID" \
  -H "Content-Type: application/json" \
  --data "$(python -c 'import json,sys; print(json.dumps({"body": sys.stdin.read()}))')" \
  "http://127.0.0.1:3100/api/issues/7d50a585-41ce-467f-a6ba-98afb3dc65cc/comments"
```

Do not use browser/local-board writes for Paperclip.

## Retry and failure handling

| Failure | Handling |
|---|---|
| Agiled 429 | Retry twice with exponential backoff: 5 minutes, then 30 minutes. If still failing, stop and notify; do not tighten schedule. |
| 401/403 | Stop immediately and notify credential owner. For AITable, verify credential-source drift before host changes. |
| 404 endpoint | Mark resource unsupported and continue other resources; do not infer write permissions. |
| n8n command timeout | Stop workflow and notify with command/resource name only. Do not dump raw stdout/stderr if it may contain records. |
| Paperclip/GitHub writeback failure | Preserve notification digest; retry writeback once; otherwise leave manual fallback instructions. |

## Manual verification checklist

1. Run `tools/.venv/bin/python tools/verify_tools.py` from repo root.
2. Run `tools/.venv/bin/python tools/appsumo_readonly_probe.py agiled users --summary-only --json --page-size 3` with real credentials.
3. Run `tools/.venv/bin/python tools/appsumo_readonly_probe.py agiled projects --summary-only --json --page-size 3` with real credentials.
4. Run `tools/.venv/bin/python tools/appsumo_readonly_probe.py aitable spaces --summary-only --json --page-size 3` with the current n8n/secure credential source.
5. Confirm no output contains raw API keys, customer emails, notes, descriptions, full CRM rows, or datasheet rows.
6. Import `appsumo-readonly-summary.draft.json` into n8n, keep it disabled, and run manually against test credentials.
7. Review notification digest before enabling Cron or writeback.

## External systems still requiring real credentials

- n8n: editor access and credential records must be created by an operator.
- Agiled: API key and exact endpoint permissions for users/projects and any future clients/tasks checks.
- AITable: production n8n credential or rotated automation-owned key; do not rely on stale `tools/.env`.
- Paperclip: only if summary comments are enabled; use authenticated curl with run ID for mutations.
- GitHub: only if digest commits are enabled.
- Gumroad, Neon, Vercel: not used by this workflow, but still required elsewhere in the production stack.
