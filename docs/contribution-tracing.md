# Contribution Tracing

Do you ever wonder about the downstream effects of your research? What happened after you delivered insights? In an ideal world, you deliver insights that shape strategy and outcomes. Yet tracking these effects is hard and rarely done. The `contribution-tracer` subagent fills this gap.

It's built on **contribution tracing**, a method for evaluating whether an intervention worked by stating up front what you'd expect to observe if it did, then checking for that evidence later — see [Befani (2016)](inspiration.md) for the source. Applied here: a decision's "Expected Outcomes" become falsifiable, checkable signals, and the agent helps you track what was actually observed as time passes.

## The `contribution-tracer` agent

The `contribution-tracer` agent has a single skill, `trace-contribution`, used both to set up a trace and to revisit it later for check-ins. Like the rest of this repo's agents, it collaborates rather than automates: it never invents an observable signal, a check-in observation, or an outcome you haven't confirmed yourself, and it never claims to have *proven* your research caused an outcome — only that the evidence is (or isn't) consistent with what you expected.

| Step | What happens |
|---|---|
| **First trace** | Reads the decision (`DCN-####.md`) and its linked insight(s), then asks — for each Expected Outcome and Potential Risk — "what would you actually see, and when, if this happened?" Vague bullets get narrowed with a follow-up question rather than turned into a signal outright. |
| **Check-in** | Walks through each expected signal and asks whether it's been observed since the last check-in, pressing for specifics (what, when, how you know) rather than a yes/no. |

Either way, nothing is written until you've reviewed and approved the canvas layout.

## Output: one canvas per decision

Each decision gets exactly one companion file, `Decisions/DCN-####.canvas`, sharing the decision's own ID (see [Conventions](conventions.md)). It embeds the decision and its insights as file nodes rather than duplicating their content, and grows over time as check-ins are added:

| Element | Canvas representation |
|---|---|
| Traced decision | `file` node embedding `DCN-####.md` |
| Supporting insight(s) | `file` node embedding each linked `INS-####.md` |
| Expected signal (not yet checked) | Uncolored `text` node |
| Check-in: observed | Green `text` node |
| Check-in: partially observed / mixed | Yellow `text` node |
| Check-in: not observed / gap | Red `text` node |

## Worked example

[`Decisions/DCN-0001.md`](../Decisions/DCN-0001.md) records a real decision from the World Cup project — sponsoring neighborhood watch parties instead of official fan-zone signage — built on [`INS-0002`](../Analysis/insights/INS-0002.md) and [`INS-0003`](../Analysis/insights/INS-0003.md). Its companion [`DCN-0001.canvas`](../Decisions/DCN-0001.canvas) shows the first-time trace: both insights and the decision linked to seven qualitative, plain-language signals — no tracking infrastructure required to start. Open it in Obsidian to see the full layout, or use it as a template for tracing your own decisions.

**Learn more:**
- [Conventions](conventions.md) — the `DCN-####.canvas` file-naming convention
- [Inspiration & Acknowledgments](inspiration.md) — the Contribution Tracing method this agent is built on
