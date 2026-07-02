<!-- Banner auto-swaps with the viewer's GitHub light/dark theme -->
<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset=".github/assets/minga-banner-dark.png">
    <img src=".github/assets/minga-banner-light.png" alt="minga-insights-vault" width="640">
  </picture>
</p>

<p align="center">
  <em>Communal knowledge, gathered.</em>
</p>

<p align="center">
  <a href="https://github.com/dcatalanmolina/minga-insights-vault/releases"><img alt="Release" src="https://img.shields.io/github/v/release/dcatalanmolina/minga-insights-vault"></a>
  <a href="https://github.com/dcatalanmolina/minga-insights-vault/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/github/license/dcatalanmolina/minga-insights-vault"></a>
  <a href="https://github.com/dcatalanmolina/minga-insights-vault/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/dcatalanmolina/minga-insights-vault"></a>
  <a href="https://github.com/dcatalanmolina/minga-insights-vault/issues"><img alt="Issues" src="https://img.shields.io/github/issues/dcatalanmolina/minga-insights-vault"></a>
</p>

---

`minga-insights-vault` is an open-source vault to gather insights, influence decisions, and track strategy, powered by collaboration-first agents. It's built on three pillars:

- **Free, open-source tooling for small teams.** No paid platform required — Obsidian, a handful of community plugins, and your AI harness of choice.
- **Collaboration over automation.** Agents ask questions and name gaps instead of writing your insights for you. See the [`peer-reviewer` → `reviewer-2` pipeline](#agents--skills) for what that looks like in practice.
- **Portable Agent Skills.** The folder structure and conventions are harness-agnostic — use Claude Code, Codex, etc. — and follow the [Agent Skill standard](https://agentskills.io/home).

See the [Releases page](https://github.com/dcatalanmolina/minga-insights-vault/releases) for what's new.

Get started by firing up your harness and giving it this instruction:

```
Review the AGENTS.md file and invoke minga-host to help me get started
```

## Agents & Skills

Five collaboration-first agents ship with this repo. Each has a defined role, a set of skills, and clear constraints on what it will and won't do — the full catalog lives in [`AGENTS.md`](AGENTS.md).

| Agent | Does | Invoke when |
|---|---|---|
| `minga-host` | Helps you understand and use the repo | You're learning how to use the vault |
| `minga-pm` | Files bugs, scopes features, manages the backlog via GitHub Issues | You want to file a bug, scope a feature, or review the backlog |
| `peer-reviewer` | Asks questions and names gaps while you form an insight — doesn't write it for you | You're drafting an insight or want a structured review of one |
| `reviewer-2` | Runs Chain of Verification on a finished insight, annotating evidence gaps inline | An insight is complete and its evidence needs stress-testing |
| `workflow-mapper` | Frames a business process using BPMN, then turns it into a canvas diagram | You want to learn BPMN or map a workflow |

The `peer-reviewer` → `reviewer-2` pipeline is the clearest embodiment of the "collaborate, don't automate" pillar: `peer-reviewer` brings drafting rigor through Socratic questioning, then `reviewer-2` follows up with evidence verification, surfacing gaps as inline `COV: PASS/GAP` annotations. See a full transcript in [Working with Subagents](docs/working-with-subagents.md).

Eleven skills back these agents — see the [Skill Catalog in `AGENTS.md`](AGENTS.md#skill-catalog) for the complete list.

## How to analyze and organize insights

- Use the `Projects` folder to share an overview of the projects associated with data, insights, and decisions.
- Use the `Data` folder to add new documents with interview transcripts, meeting notes, and other sources of qualitative data. Within each document, highlight paragraphs or sentences to code into different themes using Quadro's side panel. 
- Everything you code will be automatically organized in the `Codes` folder. Quadro does this for you. You shouldn't edit documents in the `Codes` folder.
- Create a new document under `Analysis` to take notes. Your notes will depend on the question you are answering and the themes and categories you notice inside `Codes`.
- Synthesize your analyses by writing insights in a format that makes product development easier. 
- Create a new canvas in `Global Notes` to organize insights and to facilitate discussion with others.
- Record decisions supported by those insights in `Decisions` (`DCN-####`, Strategy Canvas) — this is where insights actually influence what the team does next.
- Frame a business process as a `WKF-####.canvas` diagram in `Workflows`, produced with the `workflow-mapper` agent. Use it either as data (how a process works today) or as input to a decision (a proposed redesign).

**New here?** Follow the [Getting Started](docs/getting-started.md) walkthrough for a step-by-step example.

**Learn more:**
- [Getting Started](docs/getting-started.md) — a step-by-step walkthrough of the full workflow
- [Conventions](docs/conventions.md) — file naming and structure conventions
- [Working with Subagents](docs/working-with-subagents.md) — a full `peer-reviewer` session transcript
- [Workflow Mapping](docs/workflow-mapping.md) — how to frame a process with BPMN and the `workflow-mapper` agent

## About the name

A *minga* is a tradition of communal labor and reciprocity from rural southern Chile — neighbors coming together to raise a house or bring in a harvest, work shared and given back in turn. This project is a vault built the same way: knowledge gathered by many hands.

## Contributing

Contributions are welcome — in the spirit of the minga. See [CONTRIBUTING.md](CONTRIBUTING.md) to get started.
- If you have an idea for a collaboration-first agent, but don't know how to implement it, add a new issue describing its goals, principles, and skills. We can build it together.

- If you find bugs or gaps in the file system or agent layer, add a new issue describing what doesn't work for you, why, and in what situation. The more gaps people report, the easier it will be to build something that scales.

- If you want to contribute as an active developer building new features, let me know!

## License

MIT