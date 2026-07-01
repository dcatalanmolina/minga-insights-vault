---
name: frame-workflow
description: Use when the user wants to map or frame a business process or workflow.
---

Help the user frame their process using BPMN's structure by asking questions, not filling in gaps yourself. Ask one question at a time and wait for the user's answer before asking the next. Never invent an actor, step, condition, or outcome the user hasn't confirmed — if they're unsure, ask a narrower question rather than guessing.

# Process

Work through these in order. Skip a question only if the user has already answered it unprompted.

1. **Actors** — Who is involved in this process? Each distinct role, team, or system becomes a lane.

2. **Trigger** — What starts this process? Is it a specific request or event (message), a schedule (timer), something broadcast from elsewhere (signal), or does it just begin (none)?

3. **Steps** — Walk through the sequence one step at a time, in order. For each step, ask: which actor does it, and what kind of task is it (a person doing something by hand, a person interacting with a system, an automated system action, sending or receiving a message, or applying a business rule)?

4. **Decision points** — Where does the path split depending on a condition or decision? For each split, ask whether exactly one path is taken (exclusive), every path happens at once (parallel), or one-or-more paths can be taken depending on conditions (inclusive).

5. **End states** — How can this process end? A process can have more than one ending — ask about the happy path first, then ask if there are other ways it ends (an error, a cancellation, a timeout).

# Output Format

Once all five are answered, summarize the workflow back to the user in this exact structure before moving on to anything else. Do not add commentary outside it.

```
# Workflow: <name>

## Actors (Lanes)
- <actor 1>
- <actor 2>

## Trigger (Start Event)
- <trigger, and its type: none / message / timer / signal>

## Steps (Tasks, in order)
1. [<actor>] <step> (type: manual / user / service / send / receive / business rule)
2. ...

## Decision Points (Gateways)
- After step <n>: <condition> → <exclusive / parallel / inclusive> gateway
  - <branch a> → ...
  - <branch b> → ...

## End States (End Events)
- <end state 1>
- <end state 2>
```

After presenting the summary, ask the user to confirm or correct it. Tell them this outline is what a future `workflow-canvas` skill will turn into a visual diagram — this skill only produces the outline, not the diagram itself.
