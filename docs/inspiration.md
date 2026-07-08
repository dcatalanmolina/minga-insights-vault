# Inspiration & Acknowledgments

`minga-insights-vault` builds on ideas, tools, and prior art from other people's work. This page credits them, organized by the component they shaped.

## Frameworks & methods

| Component | Source | Shaped |
|---|---|---|
| `minga-host` and `minga-pm` agents| James Dunseith, [Andamio co-founder](https://www.andamio.io/), see why [here](https://companero.substack.com/p/design-patterns-for-insight-agents). | Agents who guide and help, instead of automating tasks. |
| `reviewer-2` agent / `chain-of-verification` skill | Loosbrock (2026), ["AI Found 11 Usability Problems Humans "Missed." Problem is…10 Were Wrong."](https://www.heykaleb.com/musings/ai-usability-problems-10-of-11-wrong). Dhuliawala et al., ["Chain-of-Verification Reduces Hallucination in Large Language Models"](https://arxiv.org/abs/2309.11495) (2023) | The draft → generate verification questions → check each independently → flag gaps pattern used to stress-test insight evidence. |
| `workflow-mapper` agent / `bpmn-basics` skill | [BPMN 2.0 specification](https://www.omg.org/spec/BPMN/2.0/About-BPMN/) (OMG); practical reference used day-to-day: [Camunda's BPMN reference](https://camunda.com/bpmn/reference/) | The vocabulary (events, tasks, gateways, pools/lanes) used to frame and diagram business processes. |


## Tools & standards

| Component | Source | Shaped |
|---|---|---|
| `Data`/`Codes` qualitative coding workflow | [Quadro](https://github.com/chrisgrieser/obsidian-quadro) (Obsidian community plugin) | Highlighting and coding raw transcripts/notes into themes, and organizing the result automatically. |
| `.agents/` skill and agent structure | [Agent Skill standard](https://agentskills.io/home) | The portable, harness-agnostic format for defining skills and agents used throughout this repo. |

## Adding to this page

If a future agent, skill, or doc draws on someone else's writing, framework, or tool, add a row here (or a new section, if it doesn't fit the existing categories) rather than crediting it only in a commit message or PR description.
