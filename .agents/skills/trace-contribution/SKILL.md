---
name: trace-contribution
description: Use when the user wants to set up a contribution trace for a decision, or check in on one already in progress.
---

Help the user trace whether a decision's expected outcomes actually happened, and how much their research contributed — using contribution-tracing logic: state what you'd expect to see if the decision worked, then check whether you actually saw it.

# Convention

Each decision gets exactly one Canvas: `Decisions/DCN-####.canvas`, matching the decision's own ID (no new folder, no new ID prefix). The canvas embeds the source files rather than duplicating them, and grows over time as check-ins are added.

| Element | Canvas representation |
|---|---|
| Traced decision | `file` node embedding `DCN-####.md` |
| Supporting insight(s) | `file` node embedding each linked `INS-####.md` |
| Expected observable signal (not yet checked) | `text` node, no color |
| Check-in: signal observed | `text` node, `color: "4"` (green) |
| Check-in: signal partially observed / mixed | `text` node, `color: "3"` (yellow) |
| Check-in: signal not observed / gap | `text` node, `color: "1"` (red) |
| Sequence | Edge from insight → decision → expected signal → check-in node(s), in that order |

**Legend node**: every canvas gets one `text` node, positioned above everything else, explaining the color convention in plain language — same pattern as `workflow-canvas`.

# Process

## First time tracing a decision (canvas doesn't exist yet)

1. **Identify the decision** — Ask which `DCN-####` this trace is for. Read that file and its linked `INS-####` file(s) for context — never edit them.

2. **Turn Expected Outcomes into observable signals** — For each bullet under the decision's "Expected Outcomes" (and "Potential Risks", if relevant), ask the user: "What would you actually see, and when, if this happened?" Don't invent a signal the user hasn't confirmed — an outcome bullet that's too vague to observe needs to be narrowed with a follow-up question before it becomes a node.

3. **Lay out the canvas** — Insight file node(s) on the left, decision file node next, expected-signal nodes to the right, one per confirmed signal, connected by edges. Add the legend node above.

4. **Confirm before writing** — Summarize the nodes and connections in plain text. Only write `Decisions/DCN-####.canvas` after the user approves it.

## Checking in on an existing trace (canvas already exists)

1. **Identify the decision** — Ask which `DCN-####` this check-in is for, and read its existing `.canvas` file to see the expected signals and any prior check-ins.

2. **Walk through each expected signal** — Ask the user, one at a time: has this been observed since the last check-in? Get specifics (what, when, how they know) rather than a yes/no.

3. **Add check-in nodes** — One new `text` node per signal discussed this session, dated, colored per the convention above, connected by an edge from the expected-signal node it responds to.

4. **Confirm before writing** — Summarize the new check-in nodes in plain text. Only update the `.canvas` file after the user approves it.

# Constraints

- Never present a confirmed signal as proof of causal contribution — contribution tracing surfaces evidence consistent (or inconsistent) with a decision's expected effects; whether the research *caused* the outcome is the user's judgment call, not this skill's.
- Never edit `DCN-####.md` or `INS-####.md` files — only the sibling `.canvas` file.
- Never write the canvas before the user has approved the drafted summary.
