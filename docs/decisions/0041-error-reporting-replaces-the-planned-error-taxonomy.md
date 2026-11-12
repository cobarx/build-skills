# 0041. `error-reporting`: this skill replaces the planned `error-taxonomy`

- **Status:** Accepted
- **Decided:** 2026-11-11, by the owner in build-skills ("we should resolve the conflict with
  error-taxonomy, either renaming this skill or changing that name") · **Recorded:** 2026-11-11 ·
  Claude Sonnet 5.5
- **Affects:** `error-reporting`, `platform-correctness`

## Context

`error-reporting` classifies errors (failure type and reason), gives each a code, and says how to
log it. `error-taxonomy` was planned as a port, and `platform-correctness` and the README name it
as the home of error handling. Two skills would cover the same ground under two names.

## Options

- **Rename this skill to `error-taxonomy`.** Rejected: the skill is more than a taxonomy. It sets
  codes, runbooks, context capture, redaction and what the caller sees.
- **Keep both.** Rejected: the port would repeat `error-reporting`'s classification, or contradict
  it.
- **Keep `error-reporting` and retire the planned name** (chosen).

## Decision

The planned `error-taxonomy` entry is removed from the README and `docs/context/planned-skills.md`.
`platform-correctness` still names it; changing a skill's text needs its own example pair
(`writing-skills`), so that pointer is retargeted in a separate PR (issue #195).

## Consequences

- Until #195 merges, `platform-correctness` points at a skill that does not exist.
- The library version moves from 0.29.0 to 0.30.0: a skill is added (`skill-versioning`).
