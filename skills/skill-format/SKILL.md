---
name: skill-format
description: This skill should be used when writing or editing the `## Rules` section of a SKILL.md; when a skill's rules are numbered, worded or counted in a way that differs from the other skills; or when checking a skill's rules against the repo's line limit. It governs the shape of a skill's rules, not what they say or the examples that show them working.
license: CC-BY-4.0 (https://creativecommons.org/licenses/by/4.0/)
metadata: {author: Hampton Maxwell, source: "https://github.com/cobarx/build-skills/tree/main/skills/skill-format"}
---

# skill-format

Every skill's rules have one shape.

A reader moves between skills, and a rule is easy to find, quote and number only when each one is
laid out the same way.

## Rules

1. **Write each rule as a numbered paragraph under `## Rules`.** Start with `N.` and a bold
   sentence that gives the instruction in the imperative. Separate rules with a blank line.

2. **Make every sentence after the lead say what to do or how to tell it's done.** Move a sentence
   that gives a reason (it says "because" or "so that") to `docs/essays/`, and leave the rule
   without it.

3. **Wrap lines at 100 characters.** Count the rule-bearing lines after wrapping, never before.

4. **Keep the counted lines at fifty, or at the limit a record in `docs/decisions/` sets for that
   skill.** Count from the first `##` heading to `## Not here`, and move a rule to `references/`
   when the count passes the limit.

## Not here

What a rule says is the skill's own subject. How its sentences read is `writing-style`. The
examples that show a skill change working are `writing-skills`. Whether the skill works is
`skill-review`.

---

Decisions affecting this skill: `docs/decisions/*-skill-format-*.md`
