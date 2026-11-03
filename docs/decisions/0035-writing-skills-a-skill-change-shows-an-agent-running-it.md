# 0035. `writing-skills`: a skill change shows an agent running it

- **Status:** Accepted
- **Decided:** 2026-11-02 · **Recorded:** 2026-11-02 · Claude Sonnet 5.5
- **Affects:** `writing-skills`, AGENTS.md

## Context

PR [#171](https://github.com/cobarx/build-skills/pull/171) adds a rule to `definition-of-done`. Its
reviewer could not judge the rule from the diff, since two lines of wording say little about what an
agent does with them. Hampton asked for examples of the skill working, and then for the repo to
require them on any skill update.

`skill-review` already says how a reviewer tests a skill, and rule 4 there covers a demo an author
offers. Nothing says what an author must offer.

## Options

- **A rule in `skill-review`.** Rejected: it governs the reviewer, and an author never loads it.
- **A PR template only.** Rejected: it can ask for examples but cannot say how to make a fair pair
  or what to report, and the repo has no `.github/` directory.
- **A skill that covers all skill authoring.** Rejected for now: the other conventions are in
  AGENTS.md and do not fail anyone yet. They move in later, each as its own change.
- **A peer skill for the author's side.** Chosen.

## Decision

`writing-skills` governs what an author shows with a skill change. Examples are a before and an
after pair for each kind of task, put in the PR description and not committed. A pair is shown as
an outline of both outputs and the passages only one has, because #171's four full outputs, about
3 KB each, were too long to compare.

## Consequences

- AGENTS.md points to the skill, so a change to any skill meets the rule.
- A skill PR now costs the author agent runs. A change that cannot alter behaviour is exempt by
  rule 8.
- Overlap with `skill-review` rules 2 and 4 is intended: the author shows what the reviewer then
  tests.
