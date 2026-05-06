# 03 · Products

The actual product builds. One folder per product. Each folder follows the same internal structure so any product can be picked up by anyone (or any future Claude session) with zero context loss.

## Standard Per-Product Structure

```
NN-product-slug/
├── README.md           ← product overview, status, links to all related work
├── manuscript/         ← the actual content (drafts, final, source files)
├── assets/             ← cover art, hero images, social card images
├── bonuses/            ← bonus deliverables (templates, checklists, videos)
└── deliverables/       ← final shippable files ready for upload to Gumroad
```

## Naming Convention

`NN-slug-with-hyphens` where `NN` is the ship-order number from the roadmap.

- `01-suitedash-good-parts` ← priority, in progress
- `02-pdf-slot-2` ← placeholder until named after #1 ships
- `07-pdf-slot-7` ← final slot

## Status Tracking

Each product's `README.md` tracks its current status against the Definition of Done (see `ROADMAP.md`). Update on each commit that affects that product.

## Don't Skip a Stage

When a product enters this folder, the upstream work must already exist:
- Validation in `01-market-research/by-product/<slug>/`
- Offer construction in `02-offers/` (using the templates, customized for the product)
- Sales page draft in `04-sales-pages/by-product/<slug>.md`
- Email workflow drafted in `05-email-workflows/by-product/<slug>/`

If those don't exist, go back. Don't build the product first and hope to back-fill.
