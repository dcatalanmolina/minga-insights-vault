---
name: frame-decision
description: Use when the user is framing a decision and needs to generate objectives and options before comparing anything — the earliest stage of the decision-making process.
---

Help the user identify what they value before generating alternatives — using Value-Focused Thinking: start from objectives (what matters and why), then derive options from those objectives, rather than starting from a narrow preset list of choices.

# Process

1. **Identify the decision context** — Ask what decision is on the table and which insights (`INS-####.md`) are motivating it. Read linked insight files for context.

2. **Elicit objectives, not options** — Ask "what are you trying to achieve?" rather than "what are your options?" Options come later.

3. **Distinguish fundamental objectives from means objectives** — For each objective the user names, ask "why does that matter?" Keep asking until the answer is an end in itself (a fundamental objective) rather than a means to something else (a means objective).

4. **Derive alternatives from objectives** — Once fundamental objectives are named, ask the user "given what you value, what actions could satisfy that?" to generate candidate options, rather than starting from a fixed shortlist.

5. **Confirm before writing** — Summarize the objectives and candidate alternatives in plain text. Only write or update `Decisions/DCN-####.md` (frontmatter `status: draft`) after the user approves it.

# Handing off

- Once the user has a short list of alternatives they're ready to weigh, invoke `compare-options`.

# Constraints

- Never suggest an objective or alternative the user hasn't named — ask questions that help them surface it themselves.
- Never write to `DCN-####.md` before the user approves the summarized objectives and alternatives.
- Never mark the file as finalized — only `status: draft`.
