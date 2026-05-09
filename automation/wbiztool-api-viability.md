# WbizTool API Viability and Read-Only Integration Handoff

Related issue: DIG-52
Verification timestamp: 2026-05-08T08:02:42Z
Owner: Automation Engineer

## Verdict

WbizTool is not yet a viable repo-run read-only API operator surface.

Current classification: `credential_pair_incomplete`

The blocker is precise: the secure runtime source currently exposes `WBIZTOOL_COM_API_KEY`, but WbizTool's documented API requires at least `client_id` plus `api_key` for account/client reads, and requires `whatsapp_client` for message-history reads. No WbizTool-specific `client_id` or `whatsapp_client` value was found in the checked runtime env names.

No raw API key, client ID, WhatsApp client ID, contact number, message body, token, or private WhatsApp data is stored in this repo.

## Official API facts confirmed

Source docs checked:

- `https://wbiztool.com/docs/`
- `https://wbiztool.com/docs/whatsapp-client-list-api/`
- `https://wbiztool.com/docs/history-messages-api/`
- `https://wbiztool.com/docs/send-message/`
- `https://wbiztool.com/docs/cancel-message-api/`

Observed contract:

| Area | Official shape | Safety classification |
|---|---|---|
| Base URL | `https://wbiztool.com/api/v1/` | Verified docs/base shape |
| Auth fields | Request-body `client_id` and `api_key` | Requires paired values; API key alone is insufficient |
| WhatsApp client field | Request-body `whatsapp_client` | Required for message send/history surfaces |
| WhatsApp client list | `POST /api/v1/whatsapp-client/list/` with `client_id` + `api_key` | Read-like but may expose connected WhatsApp client numbers; summary-only/manual-first only after operator approval |
| Message history | `POST /api/v1/report/` with `client_id`, `api_key`, `whatsapp_client`, `start_date`, `end_date`, `page` | Read-like but high privacy risk; avoid unless an exact minimal date window and redaction policy are approved |
| Send message | `POST /api/v1/send_msg/` | Mutating/send action; unauthorized |
| Schedule message | documented under API docs | Mutating/send action; unauthorized |
| Cancel message | `POST /api/v1/cancel_msg/` | Mutating queue action; unauthorized without a separate write contract |

Important implementation note: WbizTool uses `POST` even for read-like/list/report APIs. Because the repo's reusable `tools/appsumo_readonly_probe.py` is intentionally GET-only, WbizTool should not be added to that tool until a separate, explicit `read_like_post` guard exists with allowlisted endpoints, redacted summaries, and manual confirmation.

## Runtime verification performed

Secure source inventory checked only env variable names and existence, not values:

- `/mnt/c/Users/ohu00/Documents/.env` contains `WBIZTOOL_COM_API_KEY`.
- `tools/.env` does not contain WbizTool credentials.
- No WbizTool-specific `client_id` or `whatsapp_client` env names were found in the checked sources.

A data-minimized credential-shape probe was run against the documented WhatsApp client list route with only the available API key and no `client_id`. Result:

- Request: `POST https://wbiztool.com/api/v1/whatsapp-client/list/`
- Body shape: `api_key` only
- Response summary: HTTP request completed with JSON `{status: 0, message: "Auth Error"}` and no `whatsapp_clients` array.

This narrows the failure to missing/incorrect required credential pairing rather than unknown base URL. The probe did not fetch WhatsApp clients, contact numbers, message history, groups, message bodies, or private customer data.

## Operator inputs required before retry

Ask the operator for the exact WbizTool values below. Do not infer them from unrelated env names.

| Required input | Where WbizTool docs say it lives | Repo/env recommendation | Notes |
|---|---|---|---|
| WbizTool client ID | WbizTool API Keys page | `WBIZTOOL_CLIENT_ID` | Required for all documented API calls checked. |
| WbizTool API key | WbizTool API Keys page | `WBIZTOOL_COM_API_KEY` or preferably a dedicated `WBIZTOOL_API_KEY_AUTOMATION` | Current key exists only in secure runtime source; do not copy into repo docs. |
| WhatsApp client ID | WbizTool WhatsApp Setting page | `WBIZTOOL_WHATSAPP_CLIENT_ID` | Required before message-history/report probes. |
| Scope note | Operator-provided | Document in issue/comment only, no secrets | Confirm whether the connected WhatsApp number/account can be inspected by automation. |
| Approved first-read target | Operator-provided | `whatsapp-client/list` first, report only later | Start with account/client status summary, not message history. |

## Future disabled/manual-first health workflow plan

Do not create or activate an n8n workflow yet. Once the missing credential pair is supplied, the smallest safe plan is:

1. Manual trigger only; disabled by default.
2. Load WbizTool credentials from n8n credential records or runtime env, not repo files.
3. First request: `POST /api/v1/whatsapp-client/list/` with `client_id` and `api_key`.
4. Redact or omit `whatsapp_client_number`; emit only:
   - count of connected clients;
   - count of disconnected clients;
   - list of visible non-sensitive status fields;
   - timestamp and HTTP status.
5. Human review before any schedule/Cron is enabled.
6. Only after a separate approval, add `POST /api/v1/report/` for a narrow date window with `page=1`, summary-only counts, and no contact numbers/messages/message IDs stored.

## Explicitly unauthorized until a separate write contract exists

- Sending WhatsApp messages to phone numbers or groups.
- Scheduling WhatsApp messages or reminders.
- Cancelling queued messages.
- Uploading or fetching media files if it exposes private content.
- Verifying real phone/contact sets.
- Exporting or committing WhatsApp client numbers, contact numbers, group names, message bodies, message IDs, or private report rows.
- Enabling an n8n Cron or Paperclip writeback using operator-discovery credentials.

## Recommended status

Update the AppSumo ledger from `api_signal_unverified` to `credential_pair_incomplete` for WbizTool.

Next action: operator supplies `WBIZTOOL_CLIENT_ID` and, if message-history reporting is desired, `WBIZTOOL_WHATSAPP_CLIENT_ID`; then Automation Engineer can run one manual, redacted `whatsapp-client/list` check and decide whether a disabled/manual-first n8n health spec is warranted.
