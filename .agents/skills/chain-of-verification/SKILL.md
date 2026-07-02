---
name: chain-of-verification
description: Use to stress-test the evidence and argument in an insight file using a Chain of Verification pass.
---

# Task: Chain of Verification

Apply a Chain of Verification (CoV) pass to an insight file found in `Analysis/insights/`. For each claim in the Statement, Evidence, and Relevance sections, verify it against direct, checkable evidence — do not treat a claim as true just because it's stated confidently.

## Process

1. **Interrogate each claim.** Ask: Did this actually happen? At what timestamp? What's the direct evidence?

2. **Trace every reference back to its source.** For each `CDE-####` or `DAT-####` reference, open the source file and confirm the underlying quote or data point actually supports the claim being made — not just that a link exists.

3. **Check the argument, not just the evidence.** Does the evidence actually justify the "so what" in Relevance, or is there an unsupported leap between what was observed and what's being claimed?

4. **Flag, don't fix.** Anything that cannot be traced to a direct source, is phrased more strongly than its evidence supports, or connects evidence to the bottom-line insight without a stated argument, gets flagged — it is not your job to rewrite it.

## Output Format

Insert an inline HTML comment annotation directly after each claim you check. Never rewrite, remove, or reorder any existing text in the file — only add annotations.

```
<!-- COV: <PASS | GAP> — <one-sentence finding> -->
```

- `PASS` — the claim traces to direct, checkable evidence.
- `GAP` — the claim cannot be verified, overstates its evidence, or its connection to the bottom-line argument is missing.

After annotating the file, summarize the findings for the user as a list of every `GAP` (with its location and one-sentence explanation). Do not resolve the gaps yourself — that is the insight author's job.
