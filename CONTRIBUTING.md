# Contributing

This repo welcomes contributions from the community, in the spirit of a minga. Whether you're adding agents, skills, or refining the file system, this guide covers what you need to know.

## Get oriented first

- Read `AGENTS.md` for an overview of the repo structure, available agents, and skills.
- Browse `docs/` for guided examples of each file type and workflow. *(Coming soon — tracked in #3.)*
- Dependencies: Obsidian, Quadro, `gh` CLI, and your favorite harness.

## What you can contribute

- **Docs** — examples, walkthroughs, and recommendations in `docs/`
- **Agents & skills** — new agents in `.agents/agents/` or skills in `.agents/skills/`
- **Bug reports & feature ideas** — GitHub Issues are always welcome

## Workflow

1. For anything non-trivial, open a GitHub Issue before starting work.
2. Branch off `main` using the pattern `feature/short-description` or `fix/short-description`.
3. Keep commits small and focused. Commit messages should complete the sentence *"This commit…"*
4. Open a pull request against `main` when ready for review.

## Pull request conventions

- **Title** — use imperative mood ("Add XX agent", not "Added"). Optionally prefix with `feat:`, `fix:`, or `docs:`.
- **Description** — explain why the change was made; link to the related issue with "Closes #N".
- **Scope** — one logical change per PR; avoid bundling unrelated edits.
- **Review** — at least one approval before merging; the author merges after approval.
- **Branch hygiene** — delete the branch after merging.

## File and naming conventions

Each file type uses a prefixed ID (e.g. `DAT-0001`, `INS-0002`). IDs are assigned sequentially — check the highest existing number before creating a new file. Full conventions are documented in `docs/conventions.md`.

## What not to edit manually

- **`Codes/`** — managed automatically by Quadro (Obsidian plugin). Never edit files here by hand; changes will be overwritten.
- Agent and skill definitions in `.agents/` follow the [Agent Skill standard](https://agentskills.io/home). Read the standard before modifying them.
- Data, insights, decisions, and project overview files in the main branch should represent generic examples. Avoid committing files or changes that reveal your team's data.

## Contributing agents and skills

The `.agents/` layer follows the [Agent Skill standard](https://agentskills.io/home). This section explains how to add a new sub-agent or skill and register it so harnesses can discover it.

### Agent Skill standard fields used in this project

Both agents and skills use YAML frontmatter with these fields:

| Field | Required | Description |
|---|---|---|
| `name` | Yes | Kebab-case identifier (e.g., `peer-reviewer`) |
| `description` | Yes | One-line summary of what the agent or skill does |
| `skills` | Agents only | List of skill names the agent can invoke |

### Adding a new skill

1. Create a directory under `.agents/skills/` named after the skill (e.g., `.agents/skills/my-skill/`).
2. Add a `SKILL.md` file inside it with frontmatter and instructions:

```yaml
---
name: my-skill
description: Use when the user wants to <do something specific>.
---
```

Below the frontmatter, describe the skill's task, process steps, and any output format the skill should produce.

3. Register the skill in `AGENTS.md` by adding an entry to the `<available_skills>` block:

```xml
<skill>
  <name>my-skill</name>
  <description>Use when the user wants to …</description>
  <location>.agents/skills/my-skill/SKILL.md</location>
</skill>
```

4. If an existing agent should invoke the skill, add the skill name to that agent's `skills:` list in its `.agents/agents/<agent>.md` file.

### Adding a new sub-agent

1. Create a file under `.agents/agents/` named `<agent-name>.md`.
2. Add frontmatter and a behavior body:

```yaml
---
name: my-agent
description: Helps the user to <one-line purpose>
skills:
  - skill-a
  - skill-b
---

Your goal is to <describe the agent's purpose and approach>.

## Behavior
- When the user does X, invoke the `skill-a` skill.
- When the user does Y, invoke the `skill-b` skill.

## Constraints
- <Any guardrails the agent must follow.>
```

3. Register the agent in `AGENTS.md` by adding an entry to the `<available_subagents>` block:

```xml
<subagent>
  <name>my-agent</name>
  <purpose>Helps the user to …</purpose>
  <invoke>Invoke when …</invoke>
</subagent>
```

### Testing locally

To test a new agent or skill, invoke it through your harness and verify:

- The agent or skill is discovered (appears in the harness's available list).
- Invoking the agent triggers the expected behavior and invokes the correct skills.
- Skills produce output that matches their documented format.
- Constraints hold — the agent refuses or redirects when it should.

Test with at least one realistic prompt before opening a PR.

## Proposing changes

Open a GitHub Issue for any non-trivial change — new doc topics, agent ideas, convention updates, or bugs. The backlog is at [github.com/dcatalanmolina/minga-insights-vault/issues](https://github.com/dcatalanmolina/minga-insights-vault/issues).
