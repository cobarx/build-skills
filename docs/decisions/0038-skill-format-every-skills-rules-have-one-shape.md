# 0038. `skill-format`: every skill's rules have one shape

- **Status:** Accepted
- **Decided:** 2026-11-02 · **Recorded:** 2026-11-02 · Claude Sonnet 5.5
- **Affects:** `skill-format`, AGENTS.md

## Context

The repo's skills share a rule format: a numbered paragraph with a bold imperative lead, sentences
that each say what to do or how to tell it's done, and a counted limit on the rule-bearing lines
(0031, raised for one skill by 0036). The format lived only in the habits of whoever wrote the last
skill. Runs of a new skill written without the format put 3 lines over 100 characters in each file,
and one in three kept a reason in a rule.

Hampton asked for the format as a rule of its own. It began inside `writing-skills`, but two
independent reviews under `skill-review` failed it on AGENTS.md's test, "if its purpose needs an
'and', it is two skills", because the format of a `SKILL.md` and the examples in a PR
description are two jobs.

## Options

- **Leave the format to AGENTS.md conventions.** Rejected: an author writing a rule does not load
  AGENTS.md as a skill, so nothing triggers on the work.
- **Keep it inside `writing-skills`.** Rejected twice by review.
- **A peer skill.** Chosen.

## Decision

`skill-format` governs the shape of a skill's numbered rules: the numbered paragraph and bold lead,
one instruction or test per sentence, reasons moved to `docs/essays/`, lines wrapped at 100, and the
counted lines kept within the limit. It states the counting command from 0031 but not the limit's
reasons, and defers to a record in `docs/decisions/` for any raised limit, so a change to a limit
needs no edit to the skill.

## Consequences

- AGENTS.md points to the skill, so a rule written in any skill meets it.
- The skill repeats a part of AGENTS.md (every sentence of a rule says what to do or how to tell
  it's done) because the work it triggers on does not load AGENTS.md as a skill.
- It does not govern what a rule says or how its sentences read (`writing-style`), or the examples
  that show a skill change working (`writing-skills`).
