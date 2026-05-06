# Audience Reply Mining Prompt

The single highest-signal data source on Earth: replies from your own audience. People who already trust you, telling you in their own words what they need.

## When to Use

Weekly. Always. This is your most important mining session.

Sources:
- Replies to newsletter / nurture emails
- DMs on LinkedIn / X
- Replies to launch sequence emails
- Post-purchase email replies
- Refund email feedback (yes — this is some of the most actionable data you'll ever get)

## The Prompt (Copy-Paste into Claude)

```
You are mining direct audience replies for digital product opportunities.

Critical context: These are replies from people who already trust the creator
enough to write back. The signal-to-noise ratio is higher than any other source.
Every "I wish you'd cover..." or "I'm struggling with..." is gold.

Input: A dump of email replies, DMs, or post-purchase feedback below.

For each pattern you observe across MULTIPLE replies (not single one-offs),
output ONE record in this format:

### Candidate: [Concise idea name]

- Source: Audience replies (newsletter / launch / post-purchase / DM / refund feedback)
- Pattern frequency: [how many distinct people raised this — be specific:
  "5 separate replies in the last 30 days" not "several people"]
- Verbatim quotes (give 3+ if pattern is real):
  > "[quote 1]"
  > "[quote 2]"
  > "[quote 3]"
- One-sentence pitch: I help [the avatar — your existing audience's
  predominant profile] solve [specific problem] without [common objection].
- Pre-score (rough): Pain X, Power X, Target X, Growth X, Fit X
  (Note: "Easy to Target" is essentially 10/10 for these — they're already
   on your list. "Personal Fit" is also typically 8+ since they came to you.)
- Format guess: [PDF / template / mini-course / etc.]
- Price guess: $XX
- Existing-audience advantage: [Why this idea uniquely benefits from being
  sold to YOUR list specifically vs. cold traffic]
- Notes: [Context on which segment of audience this came from]

Hard rules:
- Pattern must appear across 3+ separate replies. A single person's question
  is interesting but might be idiosyncratic; 3+ is signal.
- Quote verbatim. Don't paraphrase audience language — their words ARE the
  positioning for the future product.
- Note the segment if relevant: "This came from buyers of Product X" vs.
  "this came from new subscribers" — those are different signals.
- Refund feedback is gold. Don't skip it. The reasons people refund tell you
  what your offering is missing or who it's not for.
- Limit output to top 3 candidates. The audience reply stream is the most
  valuable but most precious — don't overfit.

If no strong patterns: "No candidates yet. Observed [N] replies, but no
pattern recurred 3+ times. Continue collecting."

Now process:

[PASTE AUDIENCE REPLIES HERE]
```

## What to Look For

- **Recurring questions you've already answered** → those should become a product (you're answering this every week, monetize it)
- **"I wish your [framework / template / approach] also covered..."** → direct request, often a perfect Product N+1
- **"I bought [Product X] but I'm stuck because..."** → companion product opportunity
- **"What about for [adjacent niche]?"** → variation strategy candidate
- **Refund reasons** → either fix the product OR identify a niche the product wasn't designed for (which is now a new opportunity)

## Daily Practice

Don't run this prompt only when you remember. Build a habit:

1. Have a dedicated folder/label in your inbox for "audience signals"
2. Every time you reply to an audience message, copy the original question into that folder
3. Every Friday, run the prompt on the week's accumulated questions
4. Update `idea-backlog.md` with any candidates that recurred

The compounding effect: after 3 months, you'll have hundreds of audience-reply data points. The patterns become impossible to miss.
