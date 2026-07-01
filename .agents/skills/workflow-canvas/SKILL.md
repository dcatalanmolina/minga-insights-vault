---
name: workflow-canvas
description: Use when the user has a confirmed workflow outline (from frame-workflow) and wants it turned into a visual diagram.
---

Turn a confirmed workflow outline into an Obsidian Canvas file, using the BPMN-approximation convention below. Draft the structure, show the user a summary, and get their approval before writing the file.

# Convention

Obsidian Canvas has no native circle or diamond shapes, so BPMN's symbols are approximated with color and grouping. Follow this mapping exactly, and always include the legend node so a reader unfamiliar with the convention can still follow the diagram:

| BPMN concept | Canvas representation |
|---|---|
| Start event | `text` node, `color: "4"` (green) |
| End event | `text` node, `color: "1"` (red) |
| Gateway (decision point) | `text` node, `color: "3"` (yellow) |
| Task | `text` node, no `color` |
| Pool / Lane | `group` node with a `label`, sized to contain that actor's nodes |
| Sequence flow | An edge, with `label` set to the branch condition when leaving a gateway |

**Lane colors**: give each lane a distinct preset (`"1"`–`"6"`) so lanes are visually distinct from each other and from event/gateway markers. If more than six lanes are needed and the presets run out, use a custom hex color (e.g. `"#4477aa"`) instead of reusing a preset — never leave a lane uncolored, since an uncolored background is easy to mistake for a rendering error.

**Legend node**: every canvas gets one `text` node, positioned above the lanes, explaining the color convention in plain language. See [`Workflows/WKF-0001.canvas`](../../../Workflows/WKF-0001.canvas) for a worked reference.

# Process

1. **Confirm the outline** — Use the structured outline `frame-workflow` produced (actors, trigger, steps, gateways, end states). If any part is missing or ambiguous, ask the user rather than guessing — do not invent lane names, task types, or branch conditions.

2. **Lay out the lanes** — One `group` node per actor, stacked vertically, each spanning the full width. Give later steps in the process higher `y` values so the diagram reads top-to-bottom.

3. **Place the elements** — One node per event/task/gateway from the outline, positioned inside its actor's lane, left-to-right in the order the outline lists them.

4. **Connect them** — One edge per sequence flow in the outline. Gateway branches get a `label` matching the branch's condition. A branch that loops back to an earlier step is a normal edge pointing backward — do not treat it differently.

5. **Add the legend** — Positioned above the topmost lane, using the exact wording pattern from `Workflows/WKF-0001.canvas`.

6. **Confirm before writing** — Summarize the lanes, elements, and branches back to the user in plain text. Only write the `.canvas` file after they approve it.

7. **Save it** — Use the next sequential `WKF-####` ID (see [conventions](../../../docs/conventions.md)) and save to `Workflows/WKF-####.canvas`.

# Constraints

- Never present the result as an execution-ready or standard-compliant BPMN file — it's a framing tool, not a substitute for BPMN modeling software.
- Never write the file before the user has approved the drafted summary.
