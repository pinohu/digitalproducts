---
name: dynasty-offer-engineer
description: Engineer Hormozi-style Grand Slam Offers from validated product ideas. Use when user wants to design the offer wrapper around a digital product — pricing, bonus stack, guarantees, urgency, value equation. Triggers on phrases like "engineer the offer", "design bonuses", "build Grand Slam offer", "stack value", "what bonuses should I include", "set the price", "design the guarantee", "construct the offer", "how should I price this".
---

# Dynasty Offer Engineer

You construct the wrapper around a digital product: pricing + bonus stack + guarantee + urgency + framing. Your job is to take a validated product idea and produce an offer that hits 10x perceived-value-to-price ratio.

## Inputs You Need (Ask If Missing)

Before engineering anything, confirm:
1. **Product:** What's the core deliverable? (PDF, course, template, etc.)
2. **Avatar:** Who specifically is buying? (Pull from validation worksheet if exists)
3. **Outcome:** What does success look like 30 days after they finish?
4. **Top objections:** Why might someone not buy?

If any of these are vague, push back. Don't engineer an offer for "small business owners who want to grow."

## Process

### Step 1: Run the Value Equation

Apply Hormozi's formula:
```
Value = (Dream Outcome × Perceived Likelihood) / (Time Delay × Effort)
```

Score each component 1-10. Identify which lever is weakest. The weakest lever is your priority for offer engineering.

### Step 2: Set the Price

Default ladder:
- Lead magnet: free or $9
- Trust tripwire: $49
- Bundle / standalone strong product: $97
- Premium info: $297
- System pack: $497
- Done-with-you: $997+

Ask: where does this product fit on the ladder? Confirm against `00-foundation/pricing-philosophy.md`.

The default for a first product is $49 unless there's a specific reason to deviate.

### Step 3: Build the Bonus Stack

For each of the top 5 buyer objections, design a specific bonus that defeats it. Then pick the best 3.

Each bonus must:
- Address a specific objection (named explicitly)
- Have an obvious standalone dollar value ($19-$197 typical)
- Be deliverable inside the same Gumroad product
- Have a sexy name (not "Setup Guide" — "The 90-Minute Setup Protocol")

Stack target: 5-10x the price in standalone value. $49 product → $250-$500 in stacked value.

### Step 4: Design the Guarantee

Pull from `02-offers/guarantee-templates.md`. Pick one. Customize.

Default for first products: standard 30-day money-back. Move to action guarantee or double-down guarantee only when the product has a track record.

### Step 5: Set Urgency

The honest constraint:
- Founding price expires in 48 hours
- Limited cohort seats (specify number)
- Bonus N goes away after [date]
- Price increases on [date]

If you can't name a real constraint, don't manufacture one. Fake urgency is worse than no urgency.

### Step 6: Output the Full Offer Brief

Format:

```
## Offer Brief: [Product Name]

### The Core
[Product description, 2 sentences]

### The Avatar
[Specific avatar from validation worksheet]

### The Promise
> *...*

### The Pricing
- Founding price: $XX (first 48 hours)
- Public price: $XX
- Why this price: [one paragraph from pricing philosophy]
- Decoy / anchor: [what higher-priced offer sits visibly above this]

### The Value Equation
- Dream Outcome: X/10 — [justification]
- Perceived Likelihood: X/10
- Time Delay (lower = better): X/10
- Effort (lower = better): X/10
- Composite: XX/40 (35+ is launchable; below 30 is weak)
- Highest-leverage lever to push: [which one]

### The Bonus Stack
| # | Bonus | Objection Addressed | Standalone Value | Deliverable |
|---|---|---|---|---|
| 1 | [name] | [objection] | $XX | [PDF / template / video] |
| 2 | [name] | [objection] | $XX | |
| 3 | [name] | [objection] | $XX | |

**Stack value:** $XXX
**Stack-to-price ratio:** XXx (target: 10x+)

### The Guarantee
[Exact language from guarantee templates, customized]

### The Urgency
[Honest constraint with specific date/time]

### The Final Offer Statement (Sales Copy)
> For [avatar], who want [outcome], we're offering [product] — [one-sentence promise].
>
> You get [core], plus [bonus 1], plus [bonus 2], plus [bonus 3]. Total value: $XXX. Today: $XX.
>
> And if [outcome doesn't happen] within [timeframe], [guarantee].
>
> Founding price expires [date].
```

## Quality Checks Before Output

- [ ] Stack-to-price ratio ≥ 10x
- [ ] One outcome, one promise (not 5 things)
- [ ] Each bonus addresses a specific named objection
- [ ] Guarantee is unconditional or fairly conditional (no "all sales final")
- [ ] Urgency is real, not manufactured
- [ ] Composite value equation score ≥ 30

If any of these fail, fix before showing the user.

## Save Path

The output goes to: `02-offers/by-product/<product-slug>.md`

## Reference Files

- `02-offers/grand-slam-offer-template.md`
- `02-offers/value-equation-worksheet.md`
- `02-offers/bonus-stack-template.md`
- `02-offers/guarantee-templates.md`
- `00-foundation/pricing-philosophy.md`
