# minga-pm — Last Session

**Date:** 2026-08-17
**Summary:** Confirmed #25/#35/#36 belong in `Beta` (a discrepancy vs. prior memory — kept as intentional per user). Refined scope on #35 and #36 via `feature-scope` (see prior entry below for details), then the user asked to move to implementation — stepped out of `minga-pm` into regular Claude Code, same boundary as #30/#31.

Both shipped and merged into `main` today:
- **#35** (PR #38): `scripts/skills_ref.py` now generates `AGENTS.md`'s Sub-Agent/Skill catalogs from frontmatter (`metadata.minga-agent`/`minga-stage`/`minga-interactive` on every `SKILL.md`, `invoke` on every agent `.md`). CI (`skills-ref` workflow) validates no drift/broken cross-refs on every PR.
- **#36** (PR #39): new `contribution-checkin-scan` skill drafts check-in notes for stale/never-checked traces without writing to any canvas; documented as a local `claude --bg` + `/loop` background routine by default (with the honest caveat that `ScheduleWakeup`'s 1-hour clamp makes a "monthly" cadence ~720 mostly-noop hourly checks, not one sleep), with the cloud `schedule` skill documented as the paid-plan alternative.

**Beta milestone status: 4/5 closed** (#30, #31, #35, #36). Only **#25** (Quant insights integration) remains open — untouched this session, no scoping done on it yet.

**Next:** Pick up with #25 when the user wants to scope or implement it, or check whether pilot-org onboarding has surfaced anything new to add to `Beta`. Still don't close the `Beta` milestone unprompted — wait for the user to say onboarding is settled.
