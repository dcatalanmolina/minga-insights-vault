---
name: stress-test-decision
description: Use when the user has a leaning or near-final decision and wants to pressure-test it before committing — the stress-testing stage of the decision-making process.
---

Help the user pressure-test a leaning before committing — using Klein's Premortem: imagine the decision has already failed, work backward to why, and surface risks while there's still time to act on them.

# Process

1. **Identify the leaning** — Ask which alternative the user is leaning toward and why (read from `Decisions/DCN-####.md` draft if `compare-options` already ran).

2. **Run the premortem prompt** — Ask the user to imagine it's a year (or another appropriate horizon) from now and the decision failed badly: "What happened?" Let them generate as many reasons as they can before narrowing — don't supply the reasons yourself.

3. **Sort the reasons** — For each one, ask whether it's a foreseeable risk the plan should account for, or an unlikely edge case. Don't discard a reason unless the user judges it unlikely themselves.

4. **Translate into risks** — Turn each surviving foreseeable reason into a "Potential Risks" bullet for `Decisions/DCN-####.md`.

5. **Check for a change in direction** — Ask if any risk is severe enough to revisit the comparison or even the framing; if so, hand back to `compare-options` or `frame-decision` rather than pushing forward.

6. **Confirm before writing** — Summarize the risks. Only write or update `Decisions/DCN-####.md` (`status: draft`) after the user approves it.

# Handing off

- This skill never finalizes the decision. Once the user is satisfied and finalizes the `DCN-####.md` themselves (removing `status: draft`), suggest invoking `contribution-tracer` to begin tracing its outcomes.

# Constraints

- Never invent a failure reason, risk, or its severity — the user judges these, not the agent.
- Never mark `status: draft` as resolved or final — that's the user's call.
- Never write to `DCN-####.md` before the user approves the summarized risks.
