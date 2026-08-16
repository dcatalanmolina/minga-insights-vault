# Making Better Decisions

Insights don't turn into decisions by themselves. Someone still has to weigh what matters, generate real alternatives, compare them against evidence, and pressure-test a leaning before committing — and that reasoning is usually done alone, informally, with no record of how the call was actually made. The `decision-guide` agent fills that gap.

Like the rest of this repo's agents, it collaborates rather than automates: it asks questions and applies a named framework at each stage, but it never writes the decision statement, picks the winning option, or declares a recommendation "correct" on your behalf. You do the reasoning; the agent structures it.

## The `decision-guide` agent

`decision-guide` routes to one of three skills depending on which stage of the decision you're at:

| Stage | Skill | Framework | Does |
|---|---|---|---|
| Framing | `frame-decision` | Value-Focused Thinking ([Keeney, 1992](inspiration.md)) | Elicits fundamental objectives — what you actually value, and why — before deriving alternatives from them, rather than starting from a preset shortlist. |
| Comparing | `compare-options` | Kepner-Tregoe Decision Analysis ([Kepner & Tregoe](inspiration.md)) | Separates disqualifying MUST criteria from weighted WANT criteria, scores the remaining alternatives against them, and surfaces adverse consequences. |
| Stress-testing | `stress-test-decision` | Premortem ([Klein, 2007](inspiration.md)) | Asks you to imagine the decision has already failed, then works backward to the risks that could cause it — while there's still time to act on them. |

A session isn't required to move through all three in order — you can start wherever you are, and a stress test that surfaces a serious risk can send you back to comparing (or even framing) rather than forward.

## Worked example: from insight to decision

[`DCN-0001`](../Decisions/DCN-0001.md) — WFC piloting neighborhood-level watch-party sponsorships instead of bidding for official fan-zone signage — is a decision you've already seen elsewhere in this repo, built on [`INS-0002`](../Analysis/insights/INS-0002.md) and [`INS-0003`](../Analysis/insights/INS-0003.md). It's a convenient example because each section of the file lines up with one `decision-guide` stage.

**Framing.** `INS-0003` establishes the fundamental objective: WFC isn't a World Cup sponsor, so it can't compete inside official venues — the objective is to build brand affinity where official sponsors can't reach fans, not simply "get visibility." From that objective, two alternatives follow: bid for official fan-zone signage anyway, or meet fans in the neighborhood spaces (sticker-trading meetups, murals, local breweries) that `INS-0003` shows are already thriving without any official programming.

**Comparing.** A MUST criterion falls out immediately — no conflict with FIFA's sponsorship or trademark rights, which effectively disqualifies bidding for official signage a non-sponsor can't hold. Among WANT criteria, reach into the fear- and affordability-driven fans `INS-0003` describes, and authenticity, score neighborhood sponsorship higher — grounded in the "Common Ground" precedent from `DAT-0009`, where a non-sponsor brand earned real fan attention in local venues without touching protected tournament marks.

**Stress-testing.** The decision's [Potential Risks](../Decisions/DCN-0001.md) bullets — local partners declining over rights concerns, fans reading the sponsorship as opportunistic, turnout too low to justify the budget — are exactly what a premortem produces: reasons the pilot could fail, surfaced before committing rather than after.

## The working file

A `decision-guide` session originates or continues one file, `Decisions/DCN-####.md`, sharing conventions with the rest of the repo (see [Conventions](conventions.md)):

- While the decision is still being worked through, its frontmatter carries `status: draft`.
- Nothing is written until you've reviewed and approved the objectives, comparison, or risks the session produced — the same "confirm before writing" pattern used across this repo's agents.
- Only you can finalize a decision, by removing `status: draft` once you're satisfied. `decision-guide` will never do this for you.

## What's next

- **Start framing a decision** — invoke `decision-guide` and begin with `frame-decision`.
- **Already have alternatives to weigh** — invoke `decision-guide` and begin with `compare-options`.
- **Ready to pressure-test a leaning** — invoke `decision-guide` and begin with `stress-test-decision`.
- **Track what happens after you finalize** — once `status: draft` is removed, see [Contribution Tracing](contribution-tracing.md) for how `contribution-tracer` picks up from there.
