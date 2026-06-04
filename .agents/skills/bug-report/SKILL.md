# Skill: bug-report

Use this skill when the user describes a bug, unexpected behavior, or something broken in the project.

## Process

1. **Gather context** — Ask the user for any missing details:
   - What did you do? (steps to reproduce)
   - What did you expect to happen?
   - What actually happened?
   - How severe is this? (blocks work / annoying but workable / minor polish)

2. **Draft the issue** — Format the bug report using the template below. Show it to the user and ask for approval before filing.

3. **Create the issue** — Once approved, run:
   ```
   gh issue create --title "<title>" --body "<body>" --label "bug"
   ```

4. **Confirm** — Share the issue URL with the user.

## Bug Report Template

```markdown
## Description
<one-sentence summary of the problem>

## Steps to Reproduce
1. 
2. 
3. 

## Expected Behavior
<what should happen>

## Actual Behavior
<what actually happens>

## Severity
- [ ] Blocks work
- [ ] Annoying but workable
- [ ] Minor / polish

## Additional Context
<screenshots, logs, related files, or links — if any>
```
