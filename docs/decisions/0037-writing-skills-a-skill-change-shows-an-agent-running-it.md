# 0037. `writing-skills`: a skill change shows an agent running it

- **Status:** Accepted
- **Decided:** 2026-11-02 · **Recorded:** 2026-11-02 · Claude Sonnet 5.5
- **Affects:** `writing-skills`, AGENTS.md

## Context

PR [#171](https://github.com/cobarx/build-skills/pull/171) adds a rule to `definition-of-done`. Its
reviewer could not judge the rule from the diff, since two lines of wording say little about what an
agent does with them. Hampton asked for examples of the skill working, and then for the repo to
require them on any skill update. `skill-review` says how a reviewer tests a skill; nothing says
what an author must offer.

A first draft also held the format of a skill's numbered rules. Two independent reviews under
`skill-review` failed it on AGENTS.md's test, "if its purpose needs an 'and', it is two skills", so
the format is a separate skill and a separate decision.

## Options

- **A rule in `skill-review`.** Rejected: it governs the reviewer, and an author never loads it.
- **A PR template only.** Rejected: it can ask for examples but cannot say how to make a fair pair,
  and the repo has no `.github/` directory.
- **A skill that covers all skill authoring.** Rejected: its purpose needed an "and".
- **A peer skill for the author's side.** Chosen.

## Decision

`writing-skills` governs the examples an author brings to a skill change: a before and an after pair
for each kind of output, put in the PR description and not committed. A pair is shown as an outline
of both outputs and the passages only one has, because #171's four full outputs, about 3 KB each,
were too long to compare. The full outputs go in a PR comment.

## Consequences

- AGENTS.md points to the skill, so a change to any skill meets the rule.
- A skill PR costs the author agent runs. A spelling or whitespace fix is exempt (rule 8).
- Overlap with `skill-review` rules 2 and 4 is intended: the author shows what the reviewer then
  tests.
