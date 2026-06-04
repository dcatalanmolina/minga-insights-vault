# Skill: backlog-manage

Use this skill when the user wants to review, prioritize, or update the project backlog.

## Commands

### View the backlog
List all open issues grouped by label:
```
gh issue list --state open --label "bug"
gh issue list --state open --label "enhancement"
gh issue list --state open --label "backlog"
```

Or list everything at once:
```
gh issue list --state open
```

### View a specific issue
```
gh issue view <number>
```

### Add a label to an issue
```
gh issue edit <number> --add-label "<label>"
```

### Remove a label from an issue
```
gh issue edit <number> --remove-label "<label>"
```

### Close an issue
Always confirm with the user before closing. Then run:
```
gh issue close <number> --comment "<closing note>"
```

### Reopen an issue
```
gh issue reopen <number>
```

## Milestones

Use milestones to group issues by project phase. Recommended convention for this project:

| Milestone | Purpose |
|---|---|
| `Foundation` | Core infrastructure, stability, agent/skill scaffolding |
| `Beta` | Features needed before sharing the repo broadly |
| `v1.0` | Switch to version-based naming once the project stabilizes |

### Milestone commands

Create a milestone:
```
gh api repos/{owner}/{repo} /milestones --method POST --field title="Foundation"
```

Assign an issue to a milestone:
```
gh issue edit <number> --milestone "Foundation"
```

List issues by milestone:
```
gh issue list --milestone "Foundation"
```

## Prioritization guidance

When the user asks "what should we work on next?", surface issues in this order:
1. Open `bug` issues marked as blocking
2. Open `bug` issues that are annoying but workable
3. Open `enhancement` issues (ordered by user-stated priority or creation date)
4. Open `backlog` issues

Present a short summary of each issue (number, title, label) and ask the user if they want to dig into any of them.
