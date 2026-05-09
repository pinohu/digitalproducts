# SuiteDash Preview Site

Preview-only static landing page for `The Good Parts of SuiteDash`.

## Purpose

- give the offer a real reviewable surface
- keep checkout honest while Gumroad activation is still pending
- provide a clean Vercel preview target without exposing the whole repo root

## Files

- `index.html` - staging landing page copy
- `styles.css` - standalone visual system for the preview
- `vercel.json` - explicit static-site headers and noindex staging defaults
- `manual-accessibility-audit-2026-05-08.md` - manual-first accessibility/usability audit findings and remaining AT verification notes

## Governance

This preview is now covered by the repo-level governance stack:

- `npm run test:e2e`
- `npm run test:a11y`
- `npm run test:lighthouse`
- `npm run storybook:build`

Latest local quality truth after the 2026-05-09 preview-asset pass:

- Playwright governance checks pass on desktop and mobile.
- Pa11y passes with 0 accessibility errors.
- Lighthouse warnings are narrowed to 2 intentional/known items:
  - `categories:seo` stays below target because the preview remains `noindex` until a real production URL is attached.
  - `render-blocking-insight` still reports the single local stylesheet as render-blocking.

See:

- `00-foundation/operator-system/governance-stack.md`
- `00-foundation/operator-system/manual-actions-ledger.md`
- `governance/release-state.json`

## Deployment

Deploy this folder as a Vercel preview:

```bash
vercel deploy 08-platforms/vercel-sites/suitedash-good-parts-preview -y
```

Windows helper from the repo root:

```powershell
.\ops\vercel\deploy-suitedash-preview.ps1
```

By default, the helper creates a protected Vercel preview deployment. Use `-Prod` only when this page is ready to serve as the public alias.

Do not treat the preview URL as production until the real Gumroad checkout, proof, and launch timestamps are attached.
