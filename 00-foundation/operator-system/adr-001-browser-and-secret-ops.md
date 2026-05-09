# ADR-001: Browser Bridge and Secret-Backed Agent Operations

## Status

Accepted

## Date

2026-05-07

## Context

The `digitalproducts` company is operated through Paperclip with Hermes running inside Ubuntu WSL on a Windows workstation.

We needed to solve four practical problems:

- agents need durable access to a large cross-platform SaaS stack
- browser-only tools must still be operable when API coverage is weak or missing
- sensitive credentials should never be copied into repo files or long-lived prompt text
- the company needs a path to grow its own agent roster without manual rewiring each time

Direct WSL access to a Windows Chrome remote-debugging port was not reliable in this environment, so a plain CDP URL approach was not durable enough for production operations.

## Decision

Use the following operating model:

1. Run Chrome automation through a Windows-side `chrome-devtools-mcp` bridge exposed to Hermes as the `chromeops` MCP server.
2. Give Paperclip-managed Hermes agents browser capability by enabling `browser`, `mcp-chromeops`, and `mcp-local-deep-research` in their toolsets.
3. Store operator credentials in Paperclip `local_encrypted` secrets and attach them to agents as `secret_ref` bindings instead of raw values.
4. Keep operator policy in repo canon under `00-foundation/operator-system/`.
5. Grant the `Chief of Staff` controlled org-building permissions so the company can create new agents when the work demands it.
6. Add a dedicated `Browser Operations Lead` for browser-first execution paths.

## Alternatives Considered

### Direct WSL CDP connection to Windows Chrome

- Pros: simpler on paper, no extra MCP process
- Cons: unreliable localhost/gateway reachability from WSL in this environment
- Rejected because the bridge was not consistently reachable enough for autonomous operations

### Raw secrets in repo `.env` files or agent prompt templates

- Pros: faster initial setup
- Cons: poor security posture, harder rotation, higher risk of accidental leakage into logs or artifacts
- Rejected because the company needs durable autonomous operations, not session-only convenience

### One monolithic agent with all responsibilities

- Pros: less up-front configuration
- Cons: weaker specialization, blurrier accountability, harder debugging, and poorer scaling into sub-agents
- Rejected because the business benefits from explicit roles and controlled delegation

## Consequences

- Browser automation is now durable across Windows Chrome while Hermes continues running in WSL.
- New API credentials can be added through the Paperclip secret manifest without changing repo files.
- Agents can use a shared SaaS access layer without secrets being committed to git.
- The operating model is more structured and safer, but it depends on the Paperclip secret store and the Windows-side Chrome MCP bridge remaining healthy.
- NoCodeBackEnd can be added later, but only after a clearly identifiable credential path is available in the vault.
