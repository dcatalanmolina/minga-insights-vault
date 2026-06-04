# Skill: feature-scope

Use this skill when the user wants to define or explore a new feature or capability for the project.

## Process

1. **Understand the need** — Ask the user for any missing details:
   - Who benefits from this? (which user role: researcher, analyst, manager, etc.)
   - What problem does it solve or what job does it help them get done?
   - What does "done" look like? (acceptance criteria)
   - How much effort does this feel like? (small / medium / large)

2. **Draft the issue** — Format the feature request using the template below. Show it to the user and ask for approval before filing.

3. **Create the issue** — Once approved, run:
   ```
   gh issue create --title "<title>" --body "<body>" --label "enhancement"
   ```

4. **Confirm** — Share the issue URL with the user.

## Feature Request Template

```markdown
## User Story
As a <role>, I want <capability> so that <outcome>.

## Problem It Solves
<what friction or gap this addresses>

## Acceptance Criteria
- [ ] 
- [ ] 
- [ ] 

## Effort Estimate
- [ ] Small (hours)
- [ ] Medium (days)
- [ ] Large (week+)

## Open Questions
<anything that needs to be decided before or during implementation>

## Related Issues / Context
<links or references — if any>
```
