# Governance Workspace

Machine-readable governance and release-policy assets live here.

## Files

- `release-state.json` - current release blockers and quality evidence state
- `policies/release.rego` - OPA release gate policy
- `storyboard/` - Storybook review stories for governed surfaces

## Launch governance lane

`release-state.json` is the machine-readable release truth. It must agree with:

- `ROADMAP.md` Definition of Done and Shipped Catalog status
- `06-launch-playbooks/by-product/01-suitedash-good-parts-dig33-shipped-gate.md` for the DIG-33 shipped-gate evidence ledger
- `00-foundation/operator-system/manual-actions-ledger.md` for operator-only launch inputs
- `00-foundation/operator-system/mobile-control-center.md` for mobile continuation context

Current launch truth: the SuiteDash product is repo package-ready and Vercel staging is live, but production launch is still blocked. Do not mark launch ready, close DIG-33/DIG-2, or add the product to the Shipped Catalog until the release policy passes and every ROADMAP DoD row has live evidence, including first sale and manual approval.

## Commands

- `npm run observability:summary` - print the release truth, blocked checks, DIG-33 ledger path, manual-action path, and mobile handoff path
- `npm run policy:release` - fail until the release-state booleans and testimonial threshold satisfy the policy
- `npm run quality:setup` - install Chromium browser dependencies for local quality runs; use Windows PowerShell or GitHub Actions for current browser evidence if WSL is missing shared libraries
- `npm run quality:all` - rebuild quality, accessibility, and Lighthouse evidence before any release-state quality flag is changed
