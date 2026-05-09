# Browser Operations

Browser-first SaaS work in this repo is performed through the Windows-side ChromeOps bridge described in `00-foundation/operator-system/adr-001-browser-and-secret-ops.md`.

## Helpers

- `start-hermes-browser.ps1` — start the dedicated Hermes/browser-ops Chrome profile.
- `stop-hermes-browser.ps1` — stop the dedicated profile.
- `test-hermes-browser.ps1` — validate the ChromeOps bridge/profile path.

## Runbook packs

- `fusebase-readonly-runbook-pack.md` — read-only FuseBase workflows for workspace inventory, portals, pages/docs, access lists, tasks, tables/forms, AI, integrations, billing/security, and credential/session handling.

## Default safety posture

Browser operations are read-only unless a Paperclip issue explicitly authorizes a mutation with scope, rollback, and credential handling. Do not store raw credentials, cookies, tokens, secret-bearing screenshots, private exports, or payment/security material in repo files or issue comments.
