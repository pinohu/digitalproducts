# Deliverable Packaging Checklist — The Good Parts of SuiteDash

Status: Gumroad-ready v1 export package exists in repo; platform upload is still pending.

Use this file when uploading the manuscript, bonuses, and lightweight launch assets into Gumroad.

## Package contents

Required v1 files:

- [x] Core PDF: `The-Good-Parts-of-SuiteDash.pdf`
- [x] Bonus 1 PDF/checklist: `90-Minute-SuiteDash-Lock-In-Protocol.pdf`
- [x] Bonus 2 PDF/template pack: `7-SuiteDash-Automation-Recipes.pdf`
- [x] Bonus 3 PDF/checklist: `SuiteDash-Kill-List.pdf`
- [x] Optional ZIP: `The-Good-Parts-of-SuiteDash-Bonus-Pack.zip`
- [x] README / start-here source exists: `START-HERE.md`
- [x] Gumroad hero image: `suitedash-good-parts-gumroad-hero.png`
- [x] Social card: `suitedash-good-parts-social-card.png`
- [x] PDF cover image: `suitedash-good-parts-cover.png`
- [x] Square thumbnail: `suitedash-good-parts-square-thumbnail.png`
- [x] Full Gumroad package ZIP: `The-Good-Parts-of-SuiteDash-Gumroad-Package.zip`

## Source files

| Final file | Source |
|---|---|
| Core PDF | `../manuscript/02-v1-manuscript.md` |
| Lock-In Protocol | `../bonuses/01-90-minute-lock-in-protocol.md` |
| Automation Recipes | `../bonuses/02-automation-recipes.md` |
| Kill List | `../bonuses/03-kill-list.md` |
| Cover / hero | `../assets/asset-brief.md` |
| Start here | `./START-HERE.md` |

## Quality checks before export

- [x] Pricing references match final launch decision.
- [x] Refund guarantee matches offer brief and sales page.
- [x] No fake testimonials or placeholder proof.
- [x] No untested claim that automation recipes are importable if not tested.
- [x] Every checklist is usable without reading repo context.
- [x] Links and file names are human-readable.
- [x] PDF metadata/title is set.
- [x] Final page includes support/reply-to instruction.
- [x] Final page includes testimonial request or next-step prompt.
- [x] Manuscript source exists in a single export-ready markdown file.
- [x] Bonus sources are complete enough to export as standalone PDFs.
- [x] Buyer-facing start-here source exists for ZIP or Gumroad packaging.

## Exported files

| File | Purpose | Status |
|---|---|---|
| `The-Good-Parts-of-SuiteDash.pdf` | Core Gumroad download | Exported locally from manuscript source |
| `90-Minute-SuiteDash-Lock-In-Protocol.pdf` | Bonus 1 | Exported locally from bonus source |
| `7-SuiteDash-Automation-Recipes.pdf` | Bonus 2 | Exported locally from bonus source; recipes are not import-tested configs |
| `SuiteDash-Kill-List.pdf` | Bonus 3 | Exported locally from bonus source |
| `The-Good-Parts-of-SuiteDash-Bonus-Pack.zip` | Convenience bonus package for Gumroad upload | Includes three bonus PDFs and `START-HERE.md` |
| `The-Good-Parts-of-SuiteDash-Gumroad-Package.zip` | Full upload handoff package | Includes core PDF, bonus PDFs, `START-HERE.md`, and launch images |
| `suitedash-good-parts-gumroad-hero.png` | Gumroad product hero | Generated from asset brief; no SuiteDash logo/screenshots used |
| `suitedash-good-parts-social-card.png` | Launch/social image | Generated from asset brief; no SuiteDash logo/screenshots used |
| `suitedash-good-parts-cover.png` | Cover/launch art | Generated from asset brief; matches the exported PDF cover direction |
| `suitedash-good-parts-square-thumbnail.png` | Optional square thumbnail | Generated from asset brief |
| `../assets/suitedash-good-parts-hero.svg` | Editable vector source | Stored in `assets/` for future handoff |

## Gumroad upload checklist

- [ ] Product title matches sales page.
- [ ] Price/founding discount configured.
- [ ] Files uploaded.
- [ ] Product description mirrors sales page promise.
- [ ] 30-day guarantee stated.
- [ ] Post-purchase workflow download link inserted.
- [ ] Abandoned cart workflow enabled.
- [ ] Test purchase completed.

## Open blockers

- Gumroad product/admin access not available here; files still need external upload and test purchase. DIG-22 blocker handoff lives at `../../../06-launch-playbooks/by-product/01-suitedash-good-parts-gumroad-activation-status.md`.
- Testimonials missing; do not imply buyer proof until DIG-14 resolves.
- Automation recipes are recipe drafts, not import-tested config files.
- Platform URLs, live workflow links, storefront/sitemap links, ikeohu.com link, abandoned cart, and first-sale evidence remain open ROADMAP DoD items.

## Do not mark shipped until

The ROADMAP.md Definition of Done is satisfied, including upload to Gumroad, live sales page, workflow activation, testimonials, abandoned cart, storefront/sitemap links, ikeohu.com link, first sale, and shipped catalog update.
