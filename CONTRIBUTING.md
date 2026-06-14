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

## Proposing changes

Open a GitHub Issue for any non-trivial change — new doc topics, agent ideas, convention updates, or bugs. The backlog is at [github.com/dcatalanmolina/minga-insights-vault/issues](https://github.com/dcatalanmolina/minga-insights-vault/issues).
