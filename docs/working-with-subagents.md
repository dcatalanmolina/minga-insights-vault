# Working with Subagents

Subagents are specialized collaborators built into this repo. Each one has a defined role, a set of skills, and clear constraints on what it will and won't do. You invoke them by name, and they take over the conversation until the task is done.

This document shows a full session with the `peer-reviewer` subagent evaluating [`Analysis/insights/INS-0002.md`](../Analysis/insights/INS-0002.md) — one of the example insight files from the World Cup project.

## What `peer-reviewer` does

The `peer-reviewer` is a Socratic collaborator. It asks questions and names gaps — it does not rewrite your work or fill in answers for you. When you share a complete or near-complete insight file, it runs a structured clarity review and then works through the weakest areas one question at a time.

---

## Full session transcript

---

**You:** invoke peer-reviewer on INS-0002.md

---

**peer-reviewer:** On it. Let me run a clarity review on INS-0002 first, then we can dig into anything that needs attention.

---

**[INS-0002] — Clarity Review**

| Section | Verdict | Notes |
|---|---|---|
| Statement | NEEDS WORK | "Multiple options" is vague — the insight doesn't name the kind of experiences fans are actually seeking. |
| Evidence | NEEDS WORK | Only one data point, and the argument infers that fans want community alternatives from the fact that they're priced out — without direct evidence for that link. |
| Argument | NEEDS WORK | The relevance section surfaces a brand opportunity but doesn't close the loop back to the statement — the connection between "multiple options" and the specific opportunity is implicit. |

**Overall:** NEEDS WORK  
**Top priority fix:** Sharpen the statement by naming what kind of experience fans are seeking, not just "multiple options."

---

Let's start with the statement. You say fans want "multiple options" — what types of options came up most often in your data?

---

**You:** watch parties, pub screenings, and things like office brackets or watching at school

---

**peer-reviewer:** So communal viewing experiences, rather than solo alternatives like streaming at home. Does the data say anything about *why* the communal setting matters to them specifically?

---

**You:** yeah — the fans we spoke to kept talking about atmosphere. Being part of something bigger than just watching a game.

---

**peer-reviewer:** That's a meaningful distinction from "I want to watch the game." Does "remember the experience forever" capture that motivation — or is there a more specific outcome they described?

---

**You:** one fan said she wanted to feel like she was part of the tournament even though she couldn't afford a ticket

---

**peer-reviewer:** That's a strong framing. How does "feel part of the tournament" change your insight statement compared to what you have now?

---

**You:** it's more specific. it's not about having options — it's about belonging to something. the options are just the means.

---

**peer-reviewer:** Exactly. Now look at your evidence row. Your argument says fans are priced out, so community experiences become the source of memories. But does the data directly show that fans *turned to* community experiences because of price — or is that an inference?

---

**You:** inference. the data point is about pricing. we didn't ask directly about what they planned to do instead.

---

**peer-reviewer:** Good to name that gap. Does CDE-0004 say anything about *what* fans said they would do, or is it purely about the cost barrier?

---

**You:** purely cost. there's no mention of alternatives.

---

**peer-reviewer:** So the argument is doing a lot of work that the evidence doesn't fully support. What would make the link between "priced out" and "seeks community alternatives" more defensible — a second source, a quote, or a different framing of the argument?

---

**You:** probably a quote or a second source. or I could reframe the argument to say the inference is a hypothesis, not a conclusion.

---

**peer-reviewer:** That's a clean option — flag it as a hypothesis and note what evidence would confirm it. That's honest and still useful for the team. Before we move to the relevance section, is there anything else in the evidence row you want to address?

---

**You:** no, I think that's it for evidence

---

**peer-reviewer:** The relevance section says there are "plenty of opportunities" to help fans create memories — shared calendars, watch parties, brackets. Those are examples, but the section doesn't explain *why* this insight matters to your team's work specifically. What is your team or product actually trying to do in this space?

---

**You:** we're trying to identify where a sports brand could show up meaningfully for fans who aren't going to games

---

**peer-reviewer:** And does the insight as written make that connection — or does a reader have to infer it?

---

**You:** they'd have to infer it. the relevance section is too broad right now.

---

**peer-reviewer:** What's one sentence that would make the strategic relevance explicit for someone reading this cold?

---

**You:** something like: fans priced out of attending games are still seeking belonging — and that's a moment a sports brand can own if it shows up in the right community contexts.

---

**peer-reviewer:** That's the sentence. Where would you put it in the file?

---

**You:** at the top of the relevance section, before the bullets

---

**peer-reviewer:** Makes sense. You've got a clear list of things to address: tighten the statement around belonging rather than options, flag the community-alternatives link as a hypothesis, and lead the relevance section with that strategic framing. Want to work through a revised statement, or do you want to take it from here?

---

## What the session produced

By the end of the session, three concrete changes were identified:

1. **Statement** — Reframe from "multiple options" to the underlying need: belonging to the tournament experience even without a ticket.
2. **Evidence** — Flag the inference from "priced out" → "seeks community alternatives" as a hypothesis pending a second source or direct quote.
3. **Relevance** — Lead with an explicit strategic framing before the bullet list.

The `peer-reviewer` did not write any of this. It asked questions until the researcher arrived at each answer independently — which is the point. Insights you reason through yourself hold up better in stakeholder reviews than ones filled in for you.

---

## When to invoke `peer-reviewer`

- You have a rough draft and want help thinking through the logic before polishing.
- You have a complete insight file and want a structured clarity review.
- You're stuck on how to connect evidence to a claim and want a thinking partner.

See [`AGENTS.md`](../AGENTS.md) for the full subagent catalog.
