You help the user deliver business insights that improve products and services. Users work in a company's Insights function as UX researchers, product analysts, insight managers, or voice-of-customer managers. Read the Sub-agent and Skill Catalogs of local agent skills below to perform specific tasks. Read the Directory Structure below to understand the contents of each folder in this repository. 

# Sub-Agent and Skill Catalogs

## Sub-Agent Catalog
Sub-agents are available in the `.agents/agents/` directory.

This block is generated from each agent's own frontmatter (`.agents/agents/*.md`) — do not hand-edit it. Run `python3 scripts/skills_ref.py generate` after changing an agent's `name`, `description`, `invoke`, or `skills:` list.

<!-- skills-ref:subagents:begin -->
```html
<available_subagents>
  <subagent>
    <name>contribution-tracer</name>
    <purpose>Helps the user trace how their research and decisions produced outcomes and impacts over time</purpose>
    <invoke>Invoke when the user wants to set up or check in on a contribution trace linking an insight, a decision, and its observed outcomes</invoke>
    <skills>
      <skill>trace-contribution</skill>
    </skills>
  </subagent>
  <subagent>
    <name>decision-guide</name>
    <purpose>Helps the user reason toward a decision recommendation from insights and evidence, using decision-analysis techniques matched to their stage in the process</purpose>
    <invoke>Invoke when the user wants to work through framing options, comparing alternatives, or stress-testing a leaning before committing to a decision</invoke>
    <skills>
      <skill>frame-decision</skill>
      <skill>compare-options</skill>
      <skill>stress-test-decision</skill>
    </skills>
  </subagent>
  <subagent>
    <name>minga-host</name>
    <purpose>Helps the user to understand and use the minga-insights-vault repo</purpose>
    <invoke>Invoke when user is learning how to use the repo</invoke>
    <skills>
      <skill>repo-tour</skill>
      <skill>quadro-intro</skill>
    </skills>
  </subagent>
  <subagent>
    <name>minga-pm</name>
    <purpose>Helps the user identify bugs, scope new features, and manage the backlog via GitHub Issues</purpose>
    <invoke>Invoke when user wants to file a bug, scope a feature, or review the backlog</invoke>
    <skills>
      <skill>bug-report</skill>
      <skill>feature-scope</skill>
      <skill>backlog-manage</skill>
    </skills>
  </subagent>
  <subagent>
    <name>peer-reviewer</name>
    <purpose>Helps the user interpret data and draft insight files by asking questions, not providing answers</purpose>
    <invoke>Invoke when user is forming an insight from observations or wants a structured review of a draft insight file</invoke>
    <skills>
      <skill>insight-clarity</skill>
      <skill>craft-insight</skill>
    </skills>
  </subagent>
  <subagent>
    <name>reviewer-2</name>
    <purpose>Applies Chain of Verification to stress-test the evidence behind a draft insight, surfacing gaps as inline annotations</purpose>
    <invoke>Invoke when an insight file is complete and its evidence needs to be verified, or when peer-reviewer hands off a finished session</invoke>
    <skills>
      <skill>chain-of-verification</skill>
    </skills>
  </subagent>
  <subagent>
    <name>workflow-mapper</name>
    <purpose>Helps the user frame a business process or workflow using BPMN concepts</purpose>
    <invoke>Invoke when user wants to learn BPMN or map/frame a business process or workflow</invoke>
    <skills>
      <skill>bpmn-basics</skill>
      <skill>frame-workflow</skill>
      <skill>workflow-canvas</skill>
    </skills>
  </subagent>
</available_subagents>
```
<!-- skills-ref:subagents:end -->

## Skill Catalog

Local skills are available in the `.agents/skills/` directory. Skill name, description, location, owning agent, pipeline stage, and interactivity are listed here.

This block is generated from each skill's own frontmatter (`.agents/skills/*/SKILL.md`) — do not hand-edit it. Run `python3 scripts/skills_ref.py generate` after adding a skill or changing its frontmatter.

<!-- skills-ref:skills:begin -->
```html
<available_skills>
  <skill>
    <name>trace-contribution</name>
    <description>Use when the user wants to set up a contribution trace for a decision, or check in on one already in progress.</description>
    <location>.agents/skills/trace-contribution/SKILL.md</location>
    <agent>contribution-tracer</agent>
    <stage>trace</stage>
    <interactive>true</interactive>
  </skill>
  <skill>
    <name>frame-decision</name>
    <description>Use when the user is framing a decision and needs to generate objectives and options before comparing anything — the earliest stage of the decision-making process.</description>
    <location>.agents/skills/frame-decision/SKILL.md</location>
    <agent>decision-guide</agent>
    <stage>frame</stage>
    <interactive>true</interactive>
  </skill>
  <skill>
    <name>compare-options</name>
    <description>Use when the user has a defined set of alternatives and needs to weigh them against criteria and evidence — the evaluating stage of the decision-making process.</description>
    <location>.agents/skills/compare-options/SKILL.md</location>
    <agent>decision-guide</agent>
    <stage>compare</stage>
    <interactive>true</interactive>
  </skill>
  <skill>
    <name>stress-test-decision</name>
    <description>Use when the user has a leaning or near-final decision and wants to pressure-test it before committing — the stress-testing stage of the decision-making process.</description>
    <location>.agents/skills/stress-test-decision/SKILL.md</location>
    <agent>decision-guide</agent>
    <stage>stress-test</stage>
    <interactive>true</interactive>
  </skill>
  <skill>
    <name>repo-tour</name>
    <description>Use when the user needs help understanding how to use the minga-insights-vault repo.</description>
    <location>.agents/skills/repo-tour/SKILL.md</location>
    <agent>minga-host</agent>
    <stage>orient</stage>
    <interactive>true</interactive>
  </skill>
  <skill>
    <name>quadro-intro</name>
    <description>Use when the user needs help understanding how to use Quadro (Obsidian plugin) to code qualitative data.</description>
    <location>.agents/skills/quadro-intro/SKILL.md</location>
    <agent>minga-host</agent>
    <stage>tool-intro</stage>
    <interactive>true</interactive>
  </skill>
  <skill>
    <name>bug-report</name>
    <description>Use when the user describes a bug, unexpected behavior, or something broken in the project.</description>
    <location>.agents/skills/bug-report/SKILL.md</location>
    <agent>minga-pm</agent>
    <stage>report</stage>
    <interactive>true</interactive>
  </skill>
  <skill>
    <name>feature-scope</name>
    <description>Use when the user wants to define or explore a new feature or capability for the project.</description>
    <location>.agents/skills/feature-scope/SKILL.md</location>
    <agent>minga-pm</agent>
    <stage>scope</stage>
    <interactive>true</interactive>
  </skill>
  <skill>
    <name>backlog-manage</name>
    <description>Use when the user wants to review, prioritize, or update the project backlog.</description>
    <location>.agents/skills/backlog-manage/SKILL.md</location>
    <agent>minga-pm</agent>
    <stage>triage</stage>
    <interactive>false</interactive>
  </skill>
  <skill>
    <name>insight-clarity</name>
    <description>Use when asked to review the clarity of an insight file.</description>
    <location>.agents/skills/insight-clarity/SKILL.md</location>
    <agent>peer-reviewer</agent>
    <stage>review</stage>
    <interactive>false</interactive>
  </skill>
  <skill>
    <name>craft-insight</name>
    <description>Use when asked for help to craft a new insight file.</description>
    <location>.agents/skills/craft-insight/SKILL.md</location>
    <agent>peer-reviewer</agent>
    <stage>draft</stage>
    <interactive>true</interactive>
  </skill>
  <skill>
    <name>chain-of-verification</name>
    <description>Use to stress-test the evidence and argument in an insight file using a Chain of Verification pass.</description>
    <location>.agents/skills/chain-of-verification/SKILL.md</location>
    <agent>reviewer-2</agent>
    <stage>verify</stage>
    <interactive>false</interactive>
  </skill>
  <skill>
    <name>bpmn-basics</name>
    <description>Use when the user is new to BPMN or asks what a BPMN term or symbol means.</description>
    <location>.agents/skills/bpmn-basics/SKILL.md</location>
    <agent>workflow-mapper</agent>
    <stage>orient</stage>
    <interactive>false</interactive>
  </skill>
  <skill>
    <name>frame-workflow</name>
    <description>Use when the user wants to map or frame a business process or workflow.</description>
    <location>.agents/skills/frame-workflow/SKILL.md</location>
    <agent>workflow-mapper</agent>
    <stage>frame</stage>
    <interactive>true</interactive>
  </skill>
  <skill>
    <name>workflow-canvas</name>
    <description>Use when the user has a confirmed workflow outline (from frame-workflow) and wants it turned into a visual diagram.</description>
    <location>.agents/skills/workflow-canvas/SKILL.md</location>
    <agent>workflow-mapper</agent>
    <stage>diagram</stage>
    <interactive>false</interactive>
  </skill>
</available_skills>
```
<!-- skills-ref:skills:end -->

When a task matches a skill's description, read the SKILL.md at the listed location before proceeding. When a skill references relative paths, resolve them against the skill's directory (the parent of SKILL.md) and use absolute paths in tool calls.

# Directory Structure

```
minga-insights-vault/     # top directory
  .agents/                # agent layer with local skills, rules, hooks, and per-agent short-term memory
  .obsidian/              # obsidian config
  Analysis/               # files recording insights from data analysis process
  Codes/                  # code files generated by quadro (obsidian plugin)
  Data/                   # data folder with transcripts and report notes
  Decisions/              # files recording decisions supported by insights
  Global Notes/           # files with users' notes
  Projects/               # project descriptions and canvas
  Workflows/              # BPMN-framed process diagrams (WKF-####.canvas) produced by workflow-mapper
  docs/                   # documentation: getting started, conventions, working with subagents, workflow mapping
  
```

# Global Rules 

## Must always
- Propose changes and seek approval from the user before implementing changes.

## Must Never
- Edit files in the `Codes/` or `Data/` directories. On Claude Code, this is mechanically enforced — `.claude/settings.json` denies `Edit`/`Write`/`NotebookEdit` on `Codes/**` and `Data/**` at the tool-permission layer, so a violation is blocked outright rather than merely discouraged. Other harnesses should treat this line as the enforceable rule until they have an equivalent mechanism.