---
name: contribution-checkin-scan
description: Scans open decision traces for signals that have never been checked in on and drafts a note listing what to ask next, without writing to any canvas. Built to run unattended (scheduled), but can also be invoked directly.
metadata:
  minga-agent: contribution-tracer
  minga-stage: scan
  minga-interactive: false
---

Scan every decision trace for expected signals that have never been checked in on, and draft a note listing what to ask about next — so a scheduled, unattended run surfaces what needs attention without ever fabricating a check-in.

This skill exists because `trace-contribution`'s check-in step requires a real person to answer "has this been observed, and how do you know?" for each signal — something no unattended run can do. This skill never writes to a `.canvas` file. It only drafts a note for a human to act on later, in a live `trace-contribution` session.

# Process

1. **Find decision traces** — List every `Decisions/DCN-####.canvas` file (the sequential-ID pattern from [conventions](../../../docs/conventions.md); skip any `.canvas` file that doesn't match, e.g. `Strategy Canvas.canvas`).

2. **Parse each canvas** — For each one, read its `nodes` and `edges`. An **expected signal** is an uncolored `text` node (no `color` key) whose text starts with `**Signal:**`, per the [`trace-contribution`](../trace-contribution/SKILL.md) convention. A **check-in** is a colored `text` node (`color` is `"1"`, `"3"`, or `"4"`).

3. **Flag signals with zero check-ins** — For each expected-signal node, follow its outgoing edges. If none of them lead to a colored check-in node, this signal has never been checked in on — flag it.
   - **Known limitation**: canvases don't carry a structured check-in date, so this pass can only detect signals with *zero* check-ins, not ones whose last check-in is stale. A signal checked in on once, a year ago, won't be flagged again. If that gap matters, it's a candidate for extending the canvas convention with a parseable date — raise it with the user rather than guessing at one.

4. **Draft the note, don't touch the canvas** — If any DCN has flagged signals, write one file to `Global Notes/Contribution Check-ins/<YYYY-MM-DD>-checkin-draft.md` (create the folder if it doesn't exist), formatted as:

   ```markdown
   # Check-in Draft — <YYYY-MM-DD>

   ## DCN-####
   - **Signal:** <full signal text>
     - Ask: has this been observed since the trace was set up? What, when, how do you know?
   - **Signal:** <full signal text>
     - Ask: ...

   ## DCN-####
   ...
   ```

   If no DCN has any flagged signals, do not write a file — there's nothing to draft.

5. **Never write to any `Decisions/*.canvas` or `Decisions/*.md` file.** This skill only reads them and only writes to `Global Notes/Contribution Check-ins/`.

6. **When run inside a live session** (not unattended), after drafting the note, tell the user it's ready and offer to hand off to `trace-contribution` right now to work through it together, rather than leaving it for later.

# Running unattended on a loop

This skill can be run once, directly, or scheduled to recur (e.g. monthly) via a local `/loop` background session. `ScheduleWakeup` (what `/loop` uses) cannot sleep for 30 days in one hop — it's clamped to at most 3600 seconds (1 hour) per wake-up. A monthly cadence is built from many short hops that mostly do nothing, not one long sleep:

1. On each wake-up, find the most recent filename under `Global Notes/Contribution Check-ins/` (dated `<YYYY-MM-DD>-checkin-draft.md`). If none exists, treat the scan as never having run.
2. If at least 30 days have passed since that date (or none exists), run steps 1–6 above, then schedule the next wake-up 3600 seconds out with `noop: false`.
3. Otherwise, do nothing and schedule the next wake-up 3600 seconds out with `noop: true`.
4. Repeat indefinitely until the background session is stopped.

This means roughly 720 wake-ups a month, nearly all no-ops — real but small overhead for a local, no-paid-plan monthly cadence. See [Contribution Tracing](../../../docs/contribution-tracing.md#scheduled-check-in-scans) for the one-time setup command and how to stop it, and for the paid-cloud-agents alternative that avoids the hourly polling entirely.

# Constraints

- Never invent, infer, or mark a signal as observed — that's `trace-contribution`'s job, with the user answering in real time.
- Never write to a `.canvas` file from this skill.
- Never overwrite an existing check-in draft note — each run gets its own dated file.
