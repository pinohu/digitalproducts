# Claude Skills

Skill specs that can be installed into Claude's user skill directory at `/mnt/skills/user/<skill-name>/SKILL.md`.

Each file in this folder is a **complete skill** following Anthropic's skill format. Copy the content into a SKILL.md file in the appropriate folder structure to activate it.

## Available Skills

| Skill | Purpose | When Triggered |
|---|---|---|
| [`idea-validator.md`](./idea-validator.md) | Score ideas against 50-point rubric, run validation worksheet | "validate idea", "score this idea", "is this a good product idea" |
| [`offer-engineer.md`](./offer-engineer.md) | Build Grand Slam Offer from product brief | "engineer offer", "design bonuses", "build Grand Slam offer" |
| [`sales-page-writer.md`](./sales-page-writer.md) | Generate 12-section sales page from offer brief | "write sales page", "draft sales copy", "build sales page" |
| [`launch-manager.md`](./launch-manager.md) | Orchestrate 14-day launch + post-launch reviews | "launch product", "manage launch", "post-launch review" |

## Installation

For each skill you want to install:

1. Create the folder: `mkdir -p /mnt/skills/user/dynasty-<skill-name>/`
2. Copy this folder's content as SKILL.md: `cp <skill>.md /mnt/skills/user/dynasty-<skill-name>/SKILL.md`
3. Restart Claude session — skill is now discoverable

For Dynasty Empire convention, prefix all skill names with `dynasty-` to match existing skills (`dynasty-brain-trust`, `dynasty-directory-factory`, etc.).

## How These Skills Work Together

```
[idea-validator]    →  scores candidate, runs validation worksheet
        ↓
[offer-engineer]    →  takes validated idea, produces full offer brief
        ↓
[sales-page-writer] →  takes offer brief, produces 12-section sales page
        ↓
[launch-manager]    →  orchestrates 14-day launch + reviews
```

Each skill produces output that the next skill can ingest. This creates a coherent assistant pipeline: a single conversation can validate → engineer → write → launch.

## Skill Conventions

- Each skill has a clear `<description>` so Claude knows when to trigger it
- Each skill references the relevant template files in this repo
- Each skill produces output in the standard format (markdown matching repo conventions)
- Each skill is *focused* — narrow scope, deep capability, not a generalist
