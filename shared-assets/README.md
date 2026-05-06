# Shared Assets

Reusable materials that are referenced from multiple products. Single source of truth — never duplicate across product folders.

## Subfolders

| Folder | Contents |
|---|---|
| [`swipe-files/`](./swipe-files/) | Sales copy, email examples, headlines from other products that work — annotated with what makes them work. |
| [`testimonial-bank/`](./testimonial-bank/) | All testimonials collected, tagged by product, theme, and use-case so they can be pulled into sales pages quickly. |
| [`headlines/`](./headlines/) | Tested headlines and sub-headlines, with conversion data where available. |
| [`stock-bonuses/`](./stock-bonuses/) | Reusable bonuses (curated tool lists, generic checklists) that can be plugged into multiple product offers. |
| [`brand-elements/`](./brand-elements/) | Logos, color palette, fonts, voice/tone reference for consistent brand across products. |

## Usage Pattern

When building a new product:
1. Search `headlines/` for relevant headline patterns
2. Pull testimonials from `testimonial-bank/` filtered by relevance
3. Check `stock-bonuses/` for bonuses that fit the product's avatar
4. Reference `brand-elements/` to ensure design consistency

When finishing a launch:
1. Add new testimonials to `testimonial-bank/`
2. Add the highest-converting headlines to `headlines/`
3. Add winning email subject lines to `swipe-files/`

## What Goes Here vs. What Doesn't

- ✅ Reusable across 2+ products
- ✅ Conversion-data-attached (we know what works)
- ✅ Brand-level standards
- ❌ Product-specific content (lives in `/03-products/<slug>/`)
- ❌ Drafts and works-in-progress (lives in the relevant per-product folder)
