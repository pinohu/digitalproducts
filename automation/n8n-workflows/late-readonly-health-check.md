# Late / Zernio Read-Only Health Check (Draft n8n Pack)

Related issue: DIG-66
Owner: Automation Engineer
Status: Draft only; manual-first; disabled by default
Safety class: GET-only, data-minimized, no posting/social mutations

## Purpose

Provide a repeatable n8n implementation plan for a Late/Zernio health digest after the local `tools/appsumo_readonly_probe.py late ...` checks were verified. This pack is repo-side only: no live n8n workflow was created, imported, activated, or scheduled by this issue.

## Non-negotiable safety rules

- Keep the workflow disabled after import.
- Start with Manual Trigger only; do not enable Cron until a human reviews one full digest.
- Use only read-only GET probes through the local Python tool or equivalent HTTP Request nodes.
- Use `--summary-only --json`; never emit raw profiles, account handles, profile URLs, usernames, users, post bodies, captions, media URLs, tokens, or API response bodies.
- Do not create, schedule, queue, edit, publish, validate-send, or delete posts.
- Do not connect/disconnect social accounts or mutate webhooks, API keys, users, profile settings, account settings, inbox/comment/DM state, or billing settings.
- Store credentials only in n8n credential records or an injected runtime secret, not in workflow JSON or repo files.

## Required credentials and runtime assumptions

- Preferred n8n credential/env name: `GETLATE_DEV_API_KEY_AUTOMATION` or a dedicated n8n Late/Zernio credential.
- Existing discovery key name: `GETLATE_DEV_API_KEY`.
- Local debug command assumes the repo exists on the n8n worker/host and that `tools/.venv` has been created with `tools/setup.sh`.
- If n8n runs outside this WSL host, replace `/mnt/c/Users/ohu00/Desktop/digitalproducts` and `/mnt/c/Users/ohu00/Documents/.env` with the deployed repo path and a secure n8n credential/env injection.

## Node plan

1. Manual Trigger
   - Operator starts the workflow manually.

2. Set Runtime Config
   - Fields:
     - `repoPath`: `/mnt/c/Users/ohu00/Desktop/digitalproducts`
     - `python`: `tools/.venv/bin/python`
     - `secretName`: `GETLATE_DEV_API_KEY_AUTOMATION` (or `GETLATE_DEV_API_KEY` for manual discovery only)
     - `resources`: `profiles,accounts,account-health,posts,usage-stats,users`
     - `pageSize`: `1`

3. Execute Command: Late profiles summary
   - Command shape:
     - `cd {{$json.repoPath}} && {{$json.python}} tools/appsumo_readonly_probe.py late profiles --page-size 1 --summary-only --json`
   - Inject credential via n8n env/credential handling; do not place key text in the command.

4. Execute Command: Late accounts summary
   - Same pattern with `late accounts`.

5. Execute Command: Late account-health summary
   - Same pattern with `late account-health`.

6. Execute Command: Late posts summary
   - Same pattern with `late posts`.
   - Keep `--page-size 1` and `--summary-only` because posts can contain content, media, and social metadata.

7. Execute Command: Late usage-stats summary
   - Same pattern with `late usage-stats`.
   - Treat billing/usage indicators as account-sensitive; notification should only include coarse status/count signals.

8. Execute Command: Late users summary
   - Same pattern with `late users`.
   - Suppress raw users and current user identifiers.

9. Normalize summaries
   - Parse each JSON result.
   - Keep only:
     - resource name
     - HTTP status
     - record count visible
     - status counts if present
     - visible field names after probe redaction
     - success/error state
   - Drop `sample`, `request_url`, full payloads, command stdout beyond parsed JSON, and stderr unless it has been manually redacted.

10. Build digest
   - Produce a short operator digest:
     - `Late/Zernio read-only health: profiles=1, accounts=8, account-health=8, posts=1, usage/users reachable`
     - Include any non-2xx status as an action item.
   - Do not include profile/account/post/user names, handles, URLs, captions, media, or emails.

11. Notify reviewer
   - Send only the normalized digest to the approved internal channel.
   - Do not post back to Paperclip automatically until a separate issue approves writeback and confirms Paperclip API headers.

## Manual verification checklist before any schedule

- [ ] Workflow is imported disabled.
- [ ] Trigger is manual, not Cron.
- [ ] Credential is configured in n8n and not embedded in JSON.
- [ ] One manual run returns HTTP 200 for the intended resources.
- [ ] Execution log does not contain raw API keys, bearer headers, raw profile/account handles, post text, media URLs, users, or account-specific URLs.
- [ ] Digest is reviewed by a human before any Paperclip/GitHub notification or schedule.
- [ ] Dedicated automation credential is used before recurring execution.

## Promotion criteria

Only consider enabling a low-frequency schedule after:

1. A dedicated automation-owned Late/Zernio key exists.
2. A human verifies the digest is free of PII/content leakage.
3. Retry/backoff behavior is configured.
4. A separate Paperclip issue approves any writeback destination and headers.
5. Mutation scopes remain excluded from the workflow.

## Rollback

- Disable the workflow immediately.
- Remove/rotate the n8n credential if logs show accidental key or data exposure.
- Delete any execution logs containing sensitive data according to the n8n retention policy.
- Do not retry until the normalization/redaction path is fixed and manually reviewed.
