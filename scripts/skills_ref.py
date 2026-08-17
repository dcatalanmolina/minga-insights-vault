#!/usr/bin/env python3
"""Generate/validate the Sub-Agent and Skill catalogs in AGENTS.md from the
frontmatter of .agents/agents/*.md and .agents/skills/*/SKILL.md.

This is the source of truth for issue #35: catalog prose should never be
hand-edited in AGENTS.md again — edit an agent's or skill's own frontmatter
and re-run `generate`.

Usage:
    python3 scripts/skills_ref.py generate   # rewrite the generated blocks in AGENTS.md
    python3 scripts/skills_ref.py validate   # exit 1 if AGENTS.md is stale or cross-refs are broken

Stdlib only — no external YAML dependency, since the frontmatter this repo
uses is a small, predictable subset of YAML (scalars, one-level lists, one
level of nested map). Do not add fields with commas, colons, or multi-line
values without extending the parser below.
"""

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
AGENTS_DIR = REPO_ROOT / ".agents" / "agents"
SKILLS_DIR = REPO_ROOT / ".agents" / "skills"
AGENTS_MD = REPO_ROOT / "AGENTS.md"

SUBAGENTS_BEGIN = "<!-- skills-ref:subagents:begin -->"
SUBAGENTS_END = "<!-- skills-ref:subagents:end -->"
SKILLS_BEGIN = "<!-- skills-ref:skills:begin -->"
SKILLS_END = "<!-- skills-ref:skills:end -->"


def _strip_quotes(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def parse_frontmatter(path: Path) -> dict:
    """Parse the small subset of YAML frontmatter used in this repo:
    top-level scalars, a `skills:` list, and one nested `metadata:` map.
    Returns {} if the file has no frontmatter block."""
    text = path.read_text()
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    body = text[4:end]

    data: dict = {}
    current_list = None
    current_map = None
    for raw_line in body.split("\n"):
        if not raw_line.strip():
            continue
        indent = len(raw_line) - len(raw_line.lstrip(" "))
        line = raw_line.strip()

        if indent == 0:
            current_list = None
            current_map = None
            if line.endswith(":"):
                key = line[:-1].strip()
                if key == "skills":
                    current_list = key
                    data[key] = []
                elif key == "metadata":
                    current_map = key
                    data[key] = {}
                continue
            key, _, value = line.partition(":")
            data[key.strip()] = _strip_quotes(value)
        elif line.startswith("- ") and current_list:
            data[current_list].append(_strip_quotes(line[2:]))
        elif current_map and ":" in line:
            key, _, value = line.partition(":")
            value = _strip_quotes(value)
            if value == "true":
                value = True
            elif value == "false":
                value = False
            data[current_map][key.strip()] = value

    return data


def load_agents() -> dict:
    agents = {}
    for path in sorted(AGENTS_DIR.glob("*.md")):
        fm = parse_frontmatter(path)
        if not fm.get("name"):
            continue
        agents[fm["name"]] = {
            "description": fm.get("description", ""),
            "invoke": fm.get("invoke", ""),
            "skills": fm.get("skills", []),
        }
    return agents


def load_skills() -> dict:
    skills = {}
    for skill_dir in sorted(SKILLS_DIR.iterdir()):
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            continue
        fm = parse_frontmatter(skill_md)
        if not fm.get("name"):
            continue
        meta = fm.get("metadata", {})
        skills[fm["name"]] = {
            "description": fm.get("description", ""),
            "location": f".agents/skills/{skill_dir.name}/SKILL.md",
            "agent": meta.get("minga-agent", ""),
            "stage": meta.get("minga-stage", ""),
            "interactive": meta.get("minga-interactive", ""),
        }
    return skills


def check_cross_refs(agents: dict, skills: dict) -> list:
    """Every skill's minga-agent <-> its owning agent's skills: list must agree
    in both directions. Returns a list of error strings (empty if consistent)."""
    errors = []

    for agent_name, agent in agents.items():
        for skill_name in agent["skills"]:
            if skill_name not in skills:
                errors.append(
                    f"agent '{agent_name}' lists skill '{skill_name}' which has no SKILL.md"
                )
                continue
            owner = skills[skill_name]["agent"]
            if owner != agent_name:
                errors.append(
                    f"agent '{agent_name}' lists skill '{skill_name}', but that "
                    f"skill's minga-agent is '{owner}'"
                )

    for skill_name, skill in skills.items():
        owner = skill["agent"]
        if not owner:
            errors.append(f"skill '{skill_name}' has no minga-agent set")
        elif owner not in agents:
            errors.append(f"skill '{skill_name}' has minga-agent '{owner}', which is not a known agent")
        elif skill_name not in agents[owner]["skills"]:
            errors.append(
                f"skill '{skill_name}' has minga-agent '{owner}', but that agent's "
                f"skills: list does not include it"
            )

    return errors


def render_subagents_block(agents: dict, skills: dict) -> str:
    lines = ["<available_subagents>"]
    for name in sorted(agents):
        agent = agents[name]
        lines.append("  <subagent>")
        lines.append(f"    <name>{name}</name>")
        lines.append(f"    <purpose>{agent['description']}</purpose>")
        lines.append(f"    <invoke>{agent['invoke']}</invoke>")
        lines.append("    <skills>")
        for skill_name in agent["skills"]:
            lines.append(f"      <skill>{skill_name}</skill>")
        lines.append("    </skills>")
        lines.append("  </subagent>")
    lines.append("</available_subagents>")
    return "\n".join(lines)


def render_skills_block(agents: dict, skills: dict) -> str:
    lines = ["<available_skills>"]
    # Group by agent (alphabetical), preserving each agent's own pipeline
    # order for its skills — do not alphabetize skill names globally, that
    # would scramble sequences like frame -> compare -> stress-test.
    for agent_name in sorted(agents):
        for skill_name in agents[agent_name]["skills"]:
            skill = skills.get(skill_name)
            if skill is None:
                continue
            lines.append("  <skill>")
            lines.append(f"    <name>{skill_name}</name>")
            lines.append(f"    <description>{skill['description']}</description>")
            lines.append(f"    <location>{skill['location']}</location>")
            lines.append(f"    <agent>{skill['agent']}</agent>")
            lines.append(f"    <stage>{skill['stage']}</stage>")
            lines.append(f"    <interactive>{'true' if skill['interactive'] else 'false'}</interactive>")
            lines.append("  </skill>")
    lines.append("</available_skills>")
    return "\n".join(lines)


def replace_block(text: str, begin: str, end: str, new_body: str) -> str:
    pattern = re.compile(re.escape(begin) + r".*?" + re.escape(end), re.DOTALL)
    replacement = f"{begin}\n```html\n{new_body}\n```\n{end}"
    if not pattern.search(text):
        raise SystemExit(f"AGENTS.md is missing markers {begin} / {end}")
    return pattern.sub(lambda _: replacement.replace("\\", "\\\\"), text, count=1)


def build_agents_md(current_text: str, agents: dict, skills: dict) -> str:
    text = replace_block(current_text, SUBAGENTS_BEGIN, SUBAGENTS_END, render_subagents_block(agents, skills))
    text = replace_block(text, SKILLS_BEGIN, SKILLS_END, render_skills_block(agents, skills))
    return text


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ("generate", "validate"):
        print(__doc__)
        sys.exit(2)
    mode = sys.argv[1]

    agents = load_agents()
    skills = load_skills()

    errors = check_cross_refs(agents, skills)
    if errors:
        print("skills_ref: cross-reference errors found:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)

    current_text = AGENTS_MD.read_text()
    new_text = build_agents_md(current_text, agents, skills)

    if mode == "generate":
        if new_text != current_text:
            AGENTS_MD.write_text(new_text)
            print("skills_ref: AGENTS.md regenerated.")
        else:
            print("skills_ref: AGENTS.md already up to date.")
    else:  # validate
        if new_text != current_text:
            print("skills_ref: AGENTS.md is stale — run `python3 scripts/skills_ref.py generate` and commit the result.")
            sys.exit(1)
        print("skills_ref: AGENTS.md is up to date and cross-references are consistent.")


if __name__ == "__main__":
    main()
