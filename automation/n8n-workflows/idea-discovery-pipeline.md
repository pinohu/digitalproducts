# Workflow: Idea Discovery Pipeline

Mines Reddit weekly, runs Claude analysis, appends new candidate ideas to `01-market-research/idea-discovery/idea-backlog.md` via Git commit.

## Schedule

Cron: `0 8 * * MON` (every Monday at 8 AM EST)

## Node-by-Node Build

### Node 1: Cron Trigger
- Type: Schedule Trigger
- Mode: Cron expression
- Expression: `0 8 * * MON`
- Timezone: America/New_York

### Node 2: Set Variables
- Type: Set
- Variables to set:
  - `subreddits` = `["SaaS", "Solopreneur", "Entrepreneur", "SmallBusiness", "indiehackers"]`
  - `lookback_days` = `7`
  - `top_threads_per_sub` = `10`
  - `min_score_threshold` = `25`

### Node 3: Loop Over Subreddits
- Type: Split In Batches
- Batch size: 1 (process one subreddit at a time)

### Node 4: Reddit API Call (per subreddit)
- Type: HTTP Request
- Method: GET
- URL: `https://www.reddit.com/r/{{$node["Set Variables"].json["subreddit"]}}/top.json?t=week&limit={{$node["Set Variables"].json["top_threads_per_sub"]}}`
- Authentication: Reddit OAuth2 (configured credential)
- Headers: `User-Agent: dynasty-empire-mining/1.0`

### Node 5: Extract Thread Content
- Type: Code (JavaScript)
- Code:
```javascript
const threads = items[0].json.data.children;
const extracted = threads.map(thread => ({
  title: thread.data.title,
  selftext: thread.data.selftext,
  url: `https://reddit.com${thread.data.permalink}`,
  score: thread.data.score,
  num_comments: thread.data.num_comments,
  created_utc: thread.data.created_utc,
  subreddit: thread.data.subreddit
}));
return extracted.map(t => ({ json: t }));
```

### Node 6: Aggregate Threads Into Single Payload
- Type: Aggregate
- Field: All threads from this subreddit batch into one object

### Node 7: Anthropic API — Mining Prompt
- Type: HTTP Request
- Method: POST
- URL: `https://api.anthropic.com/v1/messages`
- Authentication: Generic Credential Type / Header Auth
  - Header name: `x-api-key`
  - Header value: `{{$credential["anthropic"].api_key}}`
- Body (JSON):
```json
{
  "model": "claude-opus-4-7",
  "max_tokens": 4096,
  "messages": [
    {
      "role": "user",
      "content": "[PASTE FULL REDDIT MINING PROMPT FROM 01-market-research/idea-discovery/mining-prompts/reddit-mining.md]\n\nNow process the following Reddit data:\n\n{{$node['Aggregate Threads'].json['threads_text']}}"
    }
  ]
}
```

### Node 8: Parse Claude Output
- Type: Code (JavaScript)
- Logic: Extract candidate records from Claude's response. Format each as a structured object.

### Node 9: Filter By Score Threshold
- Type: Filter
- Condition: `pre_score_total >= 25`

### Node 10: Format As Markdown Backlog Entry
- Type: Code
- Generates the `## [Idea N] — [Idea Name]` block matching `idea-backlog.md` format.

### Node 11: GitHub API — Commit to Repo
- Type: HTTP Request
- Method: PUT
- URL: `https://api.github.com/repos/pinohu/digitalproducts/contents/01-market-research/idea-discovery/idea-backlog.md`
- Authentication: GitHub PAT
- Logic: Read current content, append new entries, base64-encode, commit with message `"feat: add N new candidate ideas from weekly mining"`

### Node 12: Notification (Slack/Email)
- Type: Email Send (or Slack)
- Trigger: On success
- Body: "Mining complete. {{N}} new candidates added. Top score: {{X}}/50."

## Error Handling

- **Reddit API rate limit:** Built-in retry with exponential backoff
- **Claude API timeout:** Retry up to 3 times, then fail gracefully and log
- **GitHub commit conflict:** Pull latest, retry once
- **Empty mining output:** Skip commit, send "no candidates this week" notification

## Variations

### For X/Twitter (when API access is set up)
Same structure, different Node 4 (Twitter API) and Node 7 (uses `twitter-mining.md` prompt).

### For LinkedIn (manual collection)
Webhook-triggered version: receives a JSON payload of LinkedIn comments via a manual paste endpoint, runs Claude analysis, commits to repo.

## Testing

1. Run manually with a known good subreddit (r/SaaS) and a 7-day lookback
2. Verify Claude output matches the standard format
3. Verify commit lands in idea-backlog.md correctly
4. Verify notification fires
5. Run on schedule once and check next-week behavior

## Cost Per Run (Estimate)

- Reddit API: free (within rate limits)
- Anthropic API: ~$0.50-$2.00 per run depending on volume of threads
- GitHub API: free
- n8n hosting: existing
- **Weekly cost: < $5**

vs. ~5-10 hours of manual mining time saved. Cost-benefit ratio: extremely favorable.
