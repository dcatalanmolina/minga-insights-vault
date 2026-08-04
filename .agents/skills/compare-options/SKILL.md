---
name: compare-options
description: Use when the user has a defined set of alternatives and needs to weigh them against criteria and evidence — the evaluating stage of the decision-making process.
---

Help the user weigh alternatives against criteria and evidence — using Kepner-Tregoe Decision Analysis: separate MUST criteria (disqualifying) from WANT criteria (weighted), score the remaining alternatives, and surface adverse consequences before committing.

# Process

1. **Identify the alternatives** — Read them from a `Decisions/DCN-####.md` draft (if `frame-decision` already ran) or ask the user to state them directly.

2. **Elicit MUST criteria** — Ask what any acceptable option absolutely has to satisfy. A MUST is a disqualifying threshold, not a preference. Eliminate any alternative that fails a MUST criterion, and confirm the elimination with the user before dropping it.

3. **Elicit WANT criteria and weights** — Ask the user to name what else matters and how they'd weigh it relative to the others (e.g., 1-10). Never assign a weight yourself.

4. **Score remaining alternatives** — For each WANT criterion, ask the user to score each alternative and explain why, grounding the rationale in evidence from linked `INS-####.md` files where possible. Never invent a score.

5. **Surface adverse consequences** — For the top-scoring alternative(s), ask "what could go wrong specifically with this option?" Carry anything substantive into a `stress-test-decision` session.

6. **Confirm before writing** — Summarize the MUST/WANT criteria, scores, and adverse consequences. Only write or update `Decisions/DCN-####.md` (`status: draft`) after the user approves it.

# Handing off

- Once scoring surfaces a leaning or near-final recommendation, invoke `stress-test-decision` before the user commits.

# Constraints

- Never assign a MUST/WANT criterion, a weight, or a score the user hasn't confirmed.
- Never declare a "winning" alternative — present the scores and let the user draw the conclusion.
- Never write to `DCN-####.md` before the user approves the summarized comparison.
