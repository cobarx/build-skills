# 0037. `skill-format` and `writing-skills`: a rule's format and a change's examples are two skills

- **Status:** Accepted
- **Decided:** 2026-11-02 · **Recorded:** 2026-11-02 · Claude Sonnet 5.5
- **Affects:** `skill-format`, `writing-skills`, AGENTS.md

## Context

PR [#171](https://github.com/cobarx/build-skills/pull/171) adds a rule to `definition-of-done`. Its
reviewer could not judge the rule from the diff, since two lines of wording say little about what an
agent does with them. Hampton asked for examples of the skill working, and then for the repo to
require them on any skill update. `skill-review` says how a reviewer tests a skill; nothing says what
an author must offer.

Hampton then asked for the format of numbered rules in the same skill. Two independent reviews under
`skill-review` rule 1 failed that skill on AGENTS.md's test, "if its purpose needs an 'and', it is
two skills". The format of a `SKILL.md` and the contents of a PR description are two jobs. A
reworded purpose did not remove the second one.

## Options

- **One skill covering both.** Rejected twice by review: the purpose needed "and".
- **A rule in `skill-review`.** Rejected: it governs the reviewer, and an author never loads it.
- **A PR template only.** Rejected: it can ask for examples but cannot say how to make a fair pair,
  and the repo has no `.github/` directory.
- **Two peer skills.** Chosen.

## Decision

`skill-format` governs the shape of a skill's numbered rules. `writing-skills` governs the examples
an author brings to a skill change: a before and an after pair for each kind of output, put in the
PR description and not committed, shown as an outline of both outputs and the passages only one has.
The comparison, not the full outputs, is shown because #171's four full outputs, about 3 KB each,
were too long to compare.

## Consequences

- AGENTS.md points to both, so a change to any skill meets both.
- A skill PR costs the author agent runs. A spelling or whitespace fix is exempt (`writing-skills`
  rule 8).
- `skill-format` states the counting command from 0031 but not the cap's reasons, and defers to a
  record in `docs/decisions/` for any raised limit (0036), so a change to a limit needs no edit to it.
- Overlap with `skill-review` rules 2, 4 and 10 is intended: the author shows what the reviewer then
  tests.
