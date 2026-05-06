# X / Twitter Mining Prompt

Use this prompt with Claude to extract digital product candidates from X/Twitter complaint threads, "I wish" tweets, and reply chains.

## When to Use

X is noisier than Reddit but faster. Best for catching emerging problems before they hit Reddit / forum threads. Use weekly on:
- Replies to influencers in your niche complaining about tools
- Search results for "I wish" + your niche keywords
- Search results for "looking for" + your niche keywords
- Quote-tweets of viral "tool X is broken" posts

## The Prompt (Copy-Paste into Claude)

```
You are mining X/Twitter posts for digital product opportunities.

Goal: Extract candidate digital product ideas from explicit complaints,
"I wish there was..." posts, and "looking for..." requests.

Input: A dump of tweets and replies below.

For each candidate, output ONE record in this exact format:

### Candidate: [Concise idea name, ~5-8 words]

- Source: [URL of the tweet]
- Pattern matched: [one of: "I wish there was..." / "Looking for..." /
  "Anyone know a tool for..." / "Why isn't there..." / "[Tool X] doesn't do Y" /
  "Spent $X on this and it didn't work" / repeated complaint pattern]
- Verbatim quote: "[copy exact words from the tweet, no paraphrasing]"
- Engagement signal: [likes, replies, quote-tweets — high engagement = stronger signal]
- One-sentence pitch: I help [specific person] solve [specific problem]
  without [common objection].
- Pre-score (rough, 1-10 each): Pain X, Power X, Target X, Growth X, Fit X
- Format guess: [PDF / template / mini-course / etc.]
- Price guess: $XX
- Watering holes:
  1.
  2.
  3.
- Notes: [1-2 sentences of context]

Hard rules:
- Heavy filter for quality: X has high noise, lots of performative complaints
  that aren't real pain. If the tweet is funny or aphoristic but doesn't reflect
  someone actually paying to solve the problem, skip it.
- Engagement signal matters MORE on X than Reddit. A tweet with 500 likes and
  100 replies is a much stronger signal than 5 likes / 0 replies. Note this.
- Only include candidates where the avatar is a professional context. Skip
  consumer / lifestyle complaints.
- Limit output to top 3 candidates per session.

If no strong candidates: "No candidates meeting threshold. Patterns observed: [list]."

Now process:

[PASTE X/TWITTER DATA HERE]
```

## How to Pull X Data

X's API is now restricted and expensive. Cheap alternatives:

1. **Manual collection:** Open X search, scroll target queries, copy text of high-engagement posts into a doc, paste into the prompt.
2. **Nitter (when working):** RSS feeds from public Nitter instances.
3. **Tools:** Hypefury, Taplio (already in Dynasty stack) can export thread data.
4. **Tweetdeck-style aggregators:** TweetDeck, Tweeten — manual but efficient for live monitoring.

## Common Failure Modes

- ❌ **Mistaking jokes for pain.** "I'd pay $1000 for an extra hour of sleep" is funny, not actionable. Skip.
- ❌ **Echo chamber sampling.** If you only mine your own follow graph, you're seeing the same takes repeated. Mine *outside* your bubble too.
- ❌ **Lifestyle topics.** Health/fitness/relationship complaints rarely convert to B2B digital products. Skip unless you're explicitly in those markets.
