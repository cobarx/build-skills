# 0040. `definition-of-done`: a change that carries out a decision ships with its record

- **Status:** Accepted
- **Decided:** 2026-11-11, by the owner in career-playbooks-app ("we should not be making changes
  without first capturing the decision. the decision record should either go into the
  implementation pr or a pr merged prior to that that notes that the implementation is coming.
  this should be a dod merge blocker") · **Recorded:** 2026-11-11 · Claude Opus 5.5
- **Affects:** `definition-of-done`

## Context

On 2026-11-11, in career-playbooks-app PR #144, the owner changed the rule for when a company with
several titles appears once or twice on a resume three times in one day. An agent built each
answer into code, the spec and a PR comment, and none into a decision record. When the PR merged
and the owner asked which decisions needed capturing, two had no record; they were written
afterwards (career-playbooks-app #163), from the conversation.

`decision-log` rule 1 says to frame a decision before making it, and `durable-context` says
where its record lives. Neither says a change is unfinished without one, so nothing stopped the
merge.

## Options

- **A rule in `decision-log`.** It already governs making and recording a decision. Rejected: the
  agent preparing a PR for merge loads `definition-of-done`, and the owner named it as a merge
  blocker. `decision-log` loads when a choice is being made, which in #144 was mid-conversation,
  not at the merge.
- **A PR template or checklist in each repo.** Rejected: each repo needs its own copy, and the
  skills are what travel between projects (as in 0034). A repo can still add one.
- **A rule in `definition-of-done`** (chosen). A change that carries out a decision is not done
  until the record is in the same PR or in one merged before it that says the implementation
  follows.

## Decision

`definition-of-done` gains rule 10: ship a decision's record with the change that carries it out,
in the same PR or in an earlier merged PR that says the implementation follows, and block the merge
until it has one.

The earlier-PR option exists so a decision can be reviewed and settled before the work is built,
when the implementation is large or comes later.

## Consequences

- An owner's call on behavior made in a review conversation needs a record before the PR that
  builds it can merge. That is more records, most of them short.
- The rule doesn't say what counts as a decision; `decision-log` does.
- Rules: 44 counted lines against the limit of 50 (0031).
- The library version moves from 0.28.0 to 0.29.0: a rule is added (`skill-versioning`).
