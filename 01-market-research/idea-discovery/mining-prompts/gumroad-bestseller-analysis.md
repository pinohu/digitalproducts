# Gumroad Bestseller Analysis Prompt

Reverse-engineering proven categories. Other creators have already validated price points and demand for you — your job is to find adjacent or complementary opportunities.

## When to Use

Monthly. Browse Gumroad's bestseller pages in categories adjacent to your niche, list top 20 products, run this prompt.

Also useful with Etsy bestsellers (printables/templates), Notion template marketplaces, and Creative Market.

## The Prompt (Copy-Paste into Claude)

```
You are analyzing top-selling digital products on Gumroad to find adjacent
opportunities, gaps, and underserved sub-niches.

Input: A list of top-selling products with their titles, descriptions, prices,
and (where visible) sales volumes.

Output a structured analysis with three sections:

SECTION 1: Categories That Are Working
For each clear category visible in the data:
- Category name (e.g., "Notion templates for solopreneurs")
- Estimated total category revenue (rough — based on visible sales counts)
- Top 3 products in category, with prices
- Common pattern across these products (what they all share)

SECTION 2: Adjacent Opportunities (5-10 candidates)
For each opportunity:

### Candidate: [Idea name]

- Pattern: [Adjacent niche / gap in existing offerings / different format
  for existing demand / variation for an underserved sub-segment]
- Existing proof: [Reference the top-selling products that prove this
  category works]
- The gap: [What's missing or what's not optimized]
- One-sentence pitch: I help [specific person] solve [specific problem]
  without [objection].
- Pre-score (rough): Pain X, Power X, Target X, Growth X, Fit X
- Format guess: [Match the format that's already winning in the category]
- Price guess: [Use the median price in the proven category]
- Differentiator: [Why someone would buy this instead of the existing top sellers]
- Notes:

SECTION 3: What to Skip
Categories that look attractive but you should NOT enter:
- Saturated categories (race-to-the-bottom pricing, 50+ near-identical products)
- Declining categories (top sellers from 2-3 years ago, no fresh entrants)
- Categories where the top seller has unfair advantages (massive audience,
  brand, etc. that you can't replicate)

Hard rules:
- Don't recommend cloning a top-seller. Recommend adjacent or complementary.
- Use existing top-sellers' prices as the anchor for price guesses. If $49
  is the median, your guess should also be ~$49 (not $9 to undercut, not $99
  to be different).
- Skip categories that don't match the creator's avatar/positioning. If the
  creator is in B2B/operator space, skip "watercolor wedding invitations"
  even if they sell well.

Now analyze:

[PASTE BESTSELLER LIST]
```

## How to Pull Gumroad Data

Gumroad doesn't have an open bestseller API, but the discovery feed at gumroad.com/discover shows top sellers. Practical methods:

1. **Manual:** Browse `/discover/category` pages, copy product titles + prices into a doc
2. **Browser extension:** Various scrapers exist; respect Gumroad's ToS
3. **Marketplace alternative:** Etsy has a clean bestseller view (Etsy → Sellers → Top 100), use that for printable / template categories

## Why This Source Is Underrated

Most creators ignore competitive analysis or treat it as just "what's everyone else doing." That's the wrong frame. The right frame is: **other creators have already done the validation work for me. Where they're winning, I have proof of demand. Where they're not optimal, I have my opportunity.**

A 5-minute Gumroad bestseller scan has saved more digital product launches than any other single activity.
