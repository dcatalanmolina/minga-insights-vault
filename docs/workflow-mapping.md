# Workflow Mapping with BPMN

A workflow diagram in this vault can serve one of two purposes:

1. **As data** — a record of how a process actually works today, captured while conducting discovery interviews or observing a workflow firsthand. Here the diagram *is* evidence: a structured account of what currently happens, the same way a transcript or report is.
2. **As input to a decision** — a sketch of an opportunity or a potential strategy that doesn't exist yet. Here the diagram is a proposal, used to reason through a redesign or a new process before committing to it.

Either way, the goal is the same: frame the process clearly, in a shared vocabulary, before anyone tries to change it.

## The `workflow-mapper` agent

The `workflow-mapper` agent helps with the framing step. It teaches and elicits — it does not draw the diagram for you until you've confirmed what belongs in it.

| Skill | Does |
|---|---|
| `bpmn-basics` | Teaches BPMN's core vocabulary (events, tasks, gateways, sequence flow, pools/lanes) on request, tied to your process rather than abstract definitions. |
| `frame-workflow` | Asks one question at a time — who's involved, what triggers it, what are the steps, where does it branch, how does it end — and produces a structured outline. |
| `workflow-canvas` | Turns a confirmed outline into an Obsidian Canvas diagram, saved under `Workflows/` with a `WKF-####` file name (see [conventions](conventions.md)). |

See [`AGENTS.md`](../AGENTS.md) for how to invoke it.

## Worked example: from data to decision

[`WKF-0001`](../Workflows/WKF-0001.canvas) maps a process you've already seen elsewhere in this repo: how a raw datum in this vault becomes a recorded decision. It's a convenient example because the branching logic isn't hypothetical — it's exactly the verdict logic from the `insight-clarity` skill.

The diagram has four lanes, one per actor:

| Lane | Actor | What happens there |
|---|---|---|
| Researcher / Coder | Collects and codes raw data | Start event: new data arrives. Tasks: save it (`DAT-####`), code it with Quadro (`CDE-####`). |
| Insight Author | Drafts the insight | Task: draft the insight (`INS-####`) using `craft-insight`. |
| Peer Reviewer | Reviews clarity | Task: review with `insight-clarity`. Gateway: the PASS / NEEDS WORK / REVISE verdict — an exclusive gateway, since only one outcome applies. |
| Decision Maker | Acts on the insight | Task: record the decision (`DCN-####`), linked back to the insight. End event: decision recorded. |

Two things worth noticing in how it's built:

- **The gateway has a loop-back.** A NEEDS WORK or REVISE verdict routes back to the Insight Author lane rather than forward — the same way a real review cycle works. Only a PASS continues to the Decision Maker.
- **Lanes, not pools.** All four actors sit inside one process, so sequence-flow arrows crossing lanes are valid BPMN. If this diagram ever needed to show a *different* participant (e.g., an external vendor system), that would be a separate pool connected by message flow instead.

## Reading the notation in Obsidian Canvas

Obsidian's Canvas format has no native circle or diamond shapes, so BPMN's symbols are approximated with color and grouping. Every canvas produced by `workflow-canvas` opens with a legend node explaining this, using the same convention:

| BPMN concept | Canvas approximation |
|---|---|
| Start event | Green node |
| End event | Red node |
| Gateway (decision point) | Yellow node |
| Task | Uncolored node |
| Pool / Lane | A large colored (or custom hex-colored, once presets run out) `group` node in the background |
| Sequence flow | An arrow (edge), with a label for the condition on that branch |

## What's next

- **Map your own process** — invoke `workflow-mapper` and start with `frame-workflow`.
- **Learn the vocabulary first** — invoke `workflow-mapper` and ask it to explain a term via `bpmn-basics`.
- **File naming** — see [conventions](conventions.md) for the `WKF-####` prefix.
