# Browser Ops

Browser automation is part of the operator stack when APIs are missing, partial, or impractical.

## Target Mode

- Windows Chrome runs in a dedicated Hermes profile
- Hermes launches a Windows-side Chrome DevTools MCP bridge
- Paperclip-managed agents inherit browser control through Hermes MCP tooling
- standalone CDP scripts remain available for local debugging and manual inspection

## Profile Intent

The dedicated browser profile should be used for:

- business SaaS logins
- stable cookies and sessions
- browser-only workflows
- reduced cross-contamination with personal browsing

## Required Capabilities

- launch Chrome with a dedicated user data directory
- make that profile reusable across Hermes sessions
- allow Hermes running in WSL to control the Windows browser through MCP
- keep local debug scripts available for direct CDP inspection when needed

## Risk Rules

- prefer APIs when they exist and are adequate
- use browser automation for read-heavy or reversible actions first
- avoid submitting payments, legal forms, credential rotations, or destructive deletions without explicit confirmation
- log blockers when MFA, CAPTCHA, or anti-bot controls prevent completion

## Verification Standard

Browser enablement is not considered live until all are true:

- Chrome launches with the Hermes profile
- the Chrome DevTools MCP bridge can be launched from Hermes on WSL
- Hermes config includes the browser toolset and MCP browser bridge
- a browser-aware agent can be configured to use it
