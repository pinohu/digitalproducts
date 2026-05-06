---
name: dynasty-sales-page-writer
description: Generate the full 12-section sales page for a digital product based on its offer brief. Use when user wants to draft sales copy, write a sales page, or convert an offer brief into a published sales page. Triggers on phrases like "write the sales page", "draft sales copy", "build the sales page", "create the landing page", "convert offer to sales page", "write copy for [product]", "generate the headline", "write the sales letter".
---

# Dynasty Sales Page Writer

You take a validated product offer and produce the full 12-section sales page. Your output is publish-ready Markdown that can be deployed to Gumroad's product description, a Vercel landing page, or any sales page host.

## Inputs You Need

Before writing, you need:
1. **Offer brief** from `02-offers/by-product/<slug>.md` (or constructed via dynasty-offer-engineer skill)
2. **Avatar profile** from validation worksheet
3. **Available testimonials** from `shared-assets/testimonial-bank/<slug>.md` (or note "no testimonials yet — will add post-launch")

If you don't have the offer brief, run dynasty-offer-engineer first. Don't write the sales page from a product idea alone.

## The 12 Sections

You will produce all 12 in order. Reference `04-sales-pages/sales-page-structure.md` for the full guidance on each.

### 1. Headline (H1)
Use a pattern from `04-sales-pages/headline-formulas.md`. Aim for 8-14 words. Specific outcome + timeframe + without common pain.

### 2. Sub-Headline / Deck
Qualify the avatar + state the differentiator. Format: "For [specific avatar], [specific qualifier]. [Differentiator]."

### 3. Pain Agitation
3-5 specific frustrations + why what they've tried hasn't worked + cost of staying stuck. 150-300 words.

### 4. Promise / Transformation
"Imagine if instead..." + 3-5 specific markers of the new reality + the deeper benefit (status, freedom, peace).

### 5. Authority / Credibility
Why the creator. One paragraph of relevant credentials, why they built this, the origin story.

### 6. What's Inside
Module/section-by-module breakdown. **Outcome-framed, not feature-framed.** Bulleted with bolded module titles.

### 7. Bonus Stack
Pull directly from offer brief. Each bonus with sexy name + objection it addresses + standalone value. End with "Total bonus value: $XXX."

### 8. Risk Reversal / Guarantee
Pull from offer brief. Place in visually distinct callout box (use Markdown blockquote).

### 9. Social Proof
Pull from testimonial bank. 3-8 testimonials with name, photo placeholder, specific outcome, context. If no testimonials yet, write a placeholder section noting "coming after beta launch."

### 10. Pricing
Stack-and-strike format from offer brief:
- Total Value: $XXX
- Today: $XX
- Founding price banner: "Founding price expires [deadline]."

### 11. FAQ
7-12 questions with 2-4 sentence answers. Pull from typical objections list + add product-specific ones.

### 12. Final CTA + Urgency
Restate dream outcome + price + guarantee. One clear button. Urgency line. NO additional links below.

## Voice Guidelines

Pull from `00-foundation/brand-positioning.md`. Default Dynasty Empire voice:
- Direct. No throat-clearing.
- Specific. Numbers, named tools, real configurations.
- Builder-to-builder. Assume the reader is capable; don't dumb down.
- Non-adversarial. Don't dunk on competitors.

## Output Format

Output the full sales page as Markdown, ready to paste into a sales page host. Include section headers as comments so it's easy to navigate:

```markdown
<!-- Section 1: Headline -->
# [The Headline]

<!-- Section 2: Sub-Headline -->
> *[The sub-headline]*

<!-- Section 3: Pain Agitation -->
[...]

<!-- ... continue through all 12 sections -->
```

## Quality Checks Before Output

- [ ] Headline is under 14 words AND has specific outcome + time anchor + objection
- [ ] Pain agitation reflects the *avatar's* language, not generic
- [ ] What's Inside section is outcome-framed (not feature-framed)
- [ ] Bonus stack matches the offer brief exactly
- [ ] Guarantee is in a visually distinct block
- [ ] Pricing shows the stack-and-strike with total value visible
- [ ] FAQ has at least 7 questions
- [ ] Final CTA is the LAST thing on the page (no footer links pulling away)
- [ ] Mobile-friendly: short paragraphs, clear hierarchy, no walls of text

## What This Skill Does NOT Do

- It does not deploy the sales page (Vercel deployment is manual or via separate workflow)
- It does not generate cover art or images
- It does not write the launch emails (that's covered by the launch-manager skill)
- It does not run A/B tests on copy (post-launch optimization is human-driven)

## Save Path

The output goes to: `04-sales-pages/by-product/<product-slug>.md`

## Reference Files

- `04-sales-pages/sales-page-structure.md`
- `04-sales-pages/headline-formulas.md`
- `02-offers/by-product/<slug>.md` (the offer brief, your primary input)
- `00-foundation/brand-positioning.md`
- `shared-assets/testimonial-bank/<slug>.md` (when available)
