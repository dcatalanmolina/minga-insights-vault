# Getting Started

This walkthrough takes you from an empty project to a finished insight file using a worked example. By the end, you will have seen every folder in action: `Projects/`, `Data/`, `Codes/`, and `Analysis/`.

## Prerequisites

- [Obsidian](https://obsidian.md/) with the [Quadro](https://github.com/chrisgrieser/obsidian-quadro) community plugin installed.
- A harness that supports the [Agent Skill standard](https://agentskills.io/home) (e.g., Claude Code, Codex).
- The `gh` CLI, authenticated, if you plan to use the project-management agent.

## The example: World Football Company

Throughout this guide we follow a fictional insights project:

> **World Football Company** is looking for opportunities to improve its brand with US consumers around the 2026 FIFA World Cup. The C-suite has tasked the insights team with finding gaps, needs, and opportunities based on how local governments and official sponsors are engaging with fans.

You can find the project overview in [`Projects/World Cup/World Cup - Overview.md`](../Projects/World%20Cup/World%20Cup%20-%20Overview.md).

## Step 1: Define a project

Create a folder inside `Projects/` named after your project, and add an overview file.

```
Projects/
  World Cup/
    World Cup - Overview.md
```

The overview file is free-form. State the project goal and enough context for a collaborator (or an agent) to understand the scope. For example:

```
Project goal: Identify opportunities to engage fans in the US with
the World Cup beyond the stadium.

World Football Company is looking for opportunities to improve its
brand with US consumers. WFC is not a World Cup sponsor, so it is
looking to find other opportunities to engage with fans. The C-suite
tasked the insights team to find gaps, needs, and opportunities based
on how local governments and official sponsors are engaging with fans.
```

## Step 2: Add data files

Add interview transcripts, meeting notes, or report summaries to the `Data/` folder. Each file uses the `DAT-` prefix and a sequential four-digit ID (see [conventions](conventions.md) for the full list of prefixes).

Every data file starts with YAML frontmatter:

```yaml
---
type:
  - Interview
project: "[[World Cup - Overview]]"
date: 2026-06-05
interviewer: ESPN
coder:
report-source: https://example.com/source-article
---
```

Below the frontmatter, paste the transcript or notes. In this example the project has three data files sourced from public interviews:

| File | Source | Topic |
|---|---|---|
| [`DAT-0005`](../Data/DAT-0005.md) | ESPN | Security challenges for the 2026 World Cup |
| [`DAT-0006`](../Data/DAT-0006.md) | KSHB | Fan fests and ticket pricing |
| [`DAT-0007`](../Data/DAT-0007.md) | NPR | Fans priced out of attending games |

## Step 3: Code excerpts with Quadro

Open a data file in Obsidian and use Quadro's side panel to highlight passages and assign them to a code (a theme or sub-theme). Quadro handles the rest:

- It adds a highlight marker (`==…==`) and a block ID (`^id-…`) to the data file.
- It creates or updates a code file in `Codes/` with an Obsidian embed (`![[...]]`) that points back to the highlighted passage.

For example, highlighting a passage in `DAT-0005` and assigning it to the code "Fan safety" produces [`CDE-0003`](../Codes/CDE-0003.md):

```markdown
---
code description: "Fan safety"
---

![[Data/DAT-0005#^id-2026-06-08--22-00-00]]
![[Data/DAT-0005#^id-2026-06-08--22-00-38]]
![[Data/DAT-0005#^id-2026-06-08--22-01-48]]
![[Data/DAT-0005#^id-2026-06-08--22-02-14]]
```

Each embed is a backlink to a specific block in the data file. In Obsidian's reading view, the highlighted text renders inline so you can review all evidence for a theme in one place.

> **Do not edit files in `Codes/` by hand.** Quadro manages them. Manual edits will be overwritten.

In this example, the team ended up with two codes:

| Code file | Theme | Sources |
|---|---|---|
| [`CDE-0003`](../Codes/CDE-0003.md) | Fan safety | DAT-0005 |
| [`CDE-0004`](../Codes/CDE-0004.md) | Fan access | DAT-0006, DAT-0007 |

## Step 4: Write an insight

Once you see a pattern across your codes, create an insight file in `Analysis/insights/` using the `INS-` prefix. The insight file has three sections:

1. **Insight** — a bottom-line statement, ideally framed as a job story.
2. **Evidence** — a table linking to codes or data files that support the statement.
3. **Relevance** — bullets explaining why the insight matters for decision-making.

Here is what [`INS-0002`](../Analysis/insights/INS-0002.md) looks like:

```yaml
---
tags:
  - "#fan-access"
user-customer:
  - Football Fan
project: "[[World Cup - Overview]]"
---
```

**Insight** (job story format):

> When my country hosts the World Cup, I want multiple options to enjoy games with friends and family, so I can remember the experience forever.

**Evidence:**

| Evidence | Source | Argument |
|---|---|---|
| Fans are priced out of the World Cup. | CED-0004 | Watching WC games in person is a unique, memorable experience. If fans are priced out, other community experiences become the source of long-term memories. |

**Relevance:**

- Fans will look for exciting alternatives to attending games.
- There are opportunities to help fans create memories in their daily lives — shared calendars, watch parties, brackets — and the question becomes how to create long-term memories through a brand.

## What's next

- **Refine your insight** — invoke the `peer-reviewer` agent to get Socratic feedback on your draft, or ask it to run a clarity review. See [Working with Subagents](working-with-subagents.md) for a full example session.
- **Manage the backlog** — invoke the `minga-pm` agent to file bugs, scope features, or triage open issues.
- **Contribute** — read [CONTRIBUTING.md](../CONTRIBUTING.md) to learn how to add new agents, skills, or documentation.
