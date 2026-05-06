# LinkedIn Mining Prompt

Use this prompt with Claude to extract B2B digital product candidates from LinkedIn comment threads, posts, and DMs.

## When to Use

LinkedIn is the highest-quality B2B mining source for the Dynasty Empire avatar (technical operators). Use weekly on:
- Comments on top posts in your niche (other creators' posts about tools, processes, frameworks)
- Replies to "what's broken in [niche]?" -style posts
- DMs you receive from prospects asking questions
- Comments on AppSumo / SaaS founder posts asking for feedback

## The Prompt (Copy-Paste into Claude)

```
You are mining LinkedIn content for B2B digital product opportunities.

Goal: Extract candidate digital product ideas from comment patterns, complaint
threads, and direct questions in B2B contexts.

Input: A dump of LinkedIn comments / posts / DMs below.

For each candidate, output ONE record in this exact format:

### Candidate: [Concise idea name]

- Source: [URL of the LinkedIn post or "DM from [pseudonym]"]
- Commenter context: [their job title, company size if visible — these are
  available on LinkedIn unlike most platforms, USE THEM]
- Pattern matched: [one of: explicit feature request / "anyone use X for Y?"
  / "we're struggling with..." / "spent $X on Y and..." / repeated complaint]
- Verbatim quote: "[exact words]"
- One-sentence pitch: I help [specific person — use their actual job title]
  solve [specific problem] without [common objection].
- Pre-score (rough): Pain X, Power X, Target X, Growth X, Fit X
- Format guess: [PDF / template / mini-course / done-with-you service]
- Price guess: $XX (LinkedIn audience tolerates higher prices than X — adjust upward)
- Watering holes:
  1.
  2.
  3.
- Notes: [include the commenter's job context as part of the avatar definition]

Hard rules:
- LinkedIn comments come with REAL job titles. Use them. Don't generalize to
  "professionals" when the commenter says "Director of Operations at a 50-person agency."
- Engagement signal matters: a comment with 20+ likes from other relevant
  professionals is a much stronger signal than a 0-like comment.
- B2B audiences pay more, so price guesses can be higher: $97-$497 range
  is normal for LinkedIn-sourced ideas, vs. $19-$97 for Reddit-sourced.
- Skip if the commenter is in a consumer space (real estate, fitness, etc.) —
  unless they're in a B2B *role within* that space (e.g., "broker tools" not
  "homebuyer tools").

If no strong candidates: "No candidates meeting threshold. Patterns observed: [list]."

Now process:

[PASTE LINKEDIN DATA HERE]
```

## Why LinkedIn Mining Is Higher-Signal Than Reddit

- **Real names + job titles.** You can verify avatar fit immediately.
- **B2B context default.** No filtering out hobbyist noise.
- **Higher price tolerance.** LinkedIn audiences pay $97-$497 routinely vs. $19-$49 elsewhere.
- **Buyer-grade behavior.** People on LinkedIn are in work mode; they actually buy tools and services.

## How to Pull LinkedIn Data

LinkedIn API is restricted. Practical methods:

1. **Browser-based copy:** Use Chrome / your browsing tool, scroll comment threads, copy text manually
2. **Sales Navigator searches:** If you have it, run searches and export CSV
3. **Taplio analytics:** If using Taplio, export top-performing posts in your niche to see what their commenters complain about
4. **DM history:** Periodically scan your own DMs — these are the highest-signal of all
