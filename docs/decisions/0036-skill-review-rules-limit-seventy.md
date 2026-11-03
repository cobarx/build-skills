# 0036. `skill-review`: its rules may run to seventy lines

- **Status:** Accepted. Amends [0031](0031-fifty-lines-of-rules.md) for this skill only.
- **Decided:** 2026-11-02 · **Recorded:** 2026-11-02 · Claude Sonnet 5.5
- **Affects:** `skill-review`

## Context

0031 caps every skill's rules at fifty lines. `skill-review` reached fifty on 2026-11-02 with
eleven rules (0033, 0035), and the next rule would have forced a move to `references/`.
Hampton observed that its rules are mostly procedural steps, a list of checks to run, and not
policies that together give the skill a shape. A list has no outline to protect by keeping it short:
each check stands alone, and dropping one loses that check without leaving the others misshapen.

## Options

- **Keep fifty and move checks to `references/`.** Rejected: the checks are the rules, so moving them
  leaves a `SKILL.md` that doesn't say what to do.
- **Raise the cap for every skill.** Rejected: the other skills are policies and sit at 48 or under
  (0031), so the cap still bounds them.
- **Raise it for this skill.** Chosen.

## Decision

Hampton, 2026-11-02: `skill-review`'s rule-bearing sections may run to seventy lines, counted as in
0031. Every other skill stays at fifty. The seventy is the old whole-file cap in 0009, reused for lack
of a measurement of its own.

## Consequences

- A skill that is a checklist can ask for the same exception with a record that shows its rules are
  independent steps, not a policy.
- Seventy is a guess. If `skill-review` nears it, revisit this record before adding rules.
