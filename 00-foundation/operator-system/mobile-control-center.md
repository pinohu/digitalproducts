# Mobile Control Center

This is the fastest way to continue work with Codex or ChatGPT from a mobile device without losing the real operating context.

## What to open on mobile

Open these first:

- `00-foundation/operator-system/mobile-control-center.md`
- `00-foundation/operator-system/manual-actions-ledger.md`
- `10-execution-sprints/current-sprint.md`
- `ROADMAP.md`
- `01-market-research/appsumo/2026-05-08-operator-input-bundle.md`

If you are checking launch truth specifically, also open:

- `06-launch-playbooks/by-product/01-suitedash-good-parts-operator-unblock-packet.md`
- `06-launch-playbooks/by-product/01-suitedash-good-parts-dig33-shipped-gate.md`

## Preferred mobile flow

1. Open this repo on GitHub or in Google Drive on your phone.
2. Read the current sprint note and the manual-actions ledger.
3. Paste the continuation prompt below into Codex or ChatGPT on mobile.
4. If you are giving secrets, sessions, OTPs, or credential updates, do not paste them into Git or shared docs. Put them into the secure source (`C:\Users\ohu00\Documents\.env` on the workstation) or deliver them through the approved secure credential/session path.

## Mobile continuation prompt

Copy and paste this:

```text
Continue the digitalproducts production push from the current repo state. Use these files as the source of truth first: governance/release-state.json, ROADMAP.md, 10-execution-sprints/current-sprint.md, 00-foundation/operator-system/manual-actions-ledger.md, 00-foundation/operator-system/governance-stack.md, and 01-market-research/appsumo/2026-05-08-operator-input-bundle.md. Preserve truthful launch status: SuiteDash is repo package-ready and Vercel staging is live, but production launch is not ready while the releaseReadiness checks are false and DIG-33 remains blocked. Keep the SuiteDash live-launch blockers explicit, keep advancing the highest-value non-blocked lane, and summarize exactly what manual actions are still required from me.
```

## What you can expect to see

- The AppSumo operator lane will keep expanding as more safe read-only surfaces are verified.
- The SuiteDash launch lane remains blocked until real external launch inputs are provided.
- GitHub Actions should carry the new quality, accessibility, Lighthouse, policy, and scorecard evidence once the repo is pushed.

## How observability works now

- `npm run observability:summary` prints the current machine-readable release block list.
- `governance/release-state.json` is the machine-readable release-policy source of truth. Its `shippedGate` block points back to the DIG-33 evidence ledger, and its manual-action/mobile paths point to the docs you should open next.
- `Paperclip` remains the live work orchestration surface.
- GitHub Actions artifacts provide test, Storybook, and Lighthouse evidence.
