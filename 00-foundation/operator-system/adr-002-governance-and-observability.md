# ADR-002: Governance and Observability Stack

Date: 2026-05-08

## Status

Accepted

## Context

`digitalproducts` had real execution momentum but no durable enforcement layer for:

- quality gates;
- accessibility verification;
- mobile UX review;
- release governance;
- observable status handoff to the operator on mobile.

The repo also had no root Node workspace, so even the static preview surface lacked a shared automation contract.

## Decision

Add a repo-level governance workspace that:

- treats the static Vercel preview as the first governed production surface;
- uses `Playwright`, `axe-core`, `Pa11y`, and `Lighthouse CI` for enforceable checks;
- uses `Storybook` for visual/mobile review;
- uses `Changesets` for intentional release-note governance;
- uses `OPA` and `governance/release-state.json` for release policy;
- uses `OpenSSF Scorecard` for security posture observability;
- creates a mobile continuation packet and a manual-action ledger so the operator can unblock the system from a phone without guessing.

## Consequences

Positive:

- quality and accessibility now have named owners and executable gates;
- release claims can be checked against policy instead of memory;
- mobile handoff is explicit and reusable;
- GitHub Actions can produce evidence artifacts instead of invisible local-only work.

Tradeoffs:

- the repo now has a Node-based governance toolchain to maintain;
- the release policy will fail until the real external blockers are actually resolved;
- some surfaces are reviewed through iframe/preview governance rather than a full componentized app architecture.
