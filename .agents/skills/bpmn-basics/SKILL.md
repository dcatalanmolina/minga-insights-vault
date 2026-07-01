---
name: bpmn-basics
description: Use when the user is new to BPMN or asks what a BPMN term or symbol means.
---

Help the user understand BPMN (Business Process Model and Notation) well enough to describe their own process in its terms. Follow the principles below.

# Principles

1. Ask what the user is trying to do before teaching anything. If they already want to map a specific process, keep the lesson short and point them to `frame-workflow` instead of lecturing.

2. Start with the four core building blocks, not the full symbol catalog. Everything else is a variant of these:

| Element | Shape | Means |
|---|---|---|
| Event | Circle | Something that happens (starts, interrupts, or ends the process) |
| Task | Rounded rectangle | A single unit of work |
| Gateway | Diamond | A decision or branching point |
| Sequence Flow | Solid arrow | The order things happen in, within one actor's lane |

3. Only go deeper into a sub-category if the user's process actually needs it. Common ones worth explaining on request:
   - **Start/End event variants** — None (unspecified), Message (triggered by/sends a message), Timer (scheduled), Signal (broadcast).
   - **Gateway variants** — Exclusive/XOR (exactly one path), Parallel/AND (all paths, simultaneously), Inclusive/OR (one or more paths, condition-based).
   - **Pools and lanes** — A pool is a participant (e.g., a company or system); lanes subdivide a pool by role, department, or system.
   - **Message flow vs. sequence flow** — Sequence flow (solid) is order within a lane; message flow (dashed) is communication between separate pools.

4. Tie every element back to a question the user can answer about their own process, not an abstract definition. For example, instead of "a gateway is a branching point," ask "where does this process split depending on some condition or decision?"

5. Use plain language first, BPMN vocabulary second. Say "starts when X happens (BPMN calls this a start event)," not the reverse.

# Reference

Full element catalog (events, tasks, gateways, connectors, pools/lanes, data objects, artifacts): https://camunda.com/bpmn/reference/
