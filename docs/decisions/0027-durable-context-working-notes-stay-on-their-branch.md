# 0027. Working notes stay on their branch

- **Status:** Accepted
- **Decided:** 2026-10-06 · **Recorded:** 2026-10-06 · Claude Opus 5.5
- **Affects:** `durable-context` (rule 7), AGENTS.md

## Context

On 2026-10-05 a session's notes were opened as three PRs to `docs/context/` (#89, #90, #91), about
700 lines. Each file grew in the order the conversation went, and mixed project values, proposed
rule changes, settled reasoning, research and asides. Hampton: generic context like that is hard to
parse and convert into something useful. Converting it took a session of its own: two essays, ten
issues and a `planned-skills.md` edit, after which the three PRs were closed.

The notes were where AGENTS.md said they could go. It listed `docs/context/` as "open questions
and working notes", and nothing said when notes had to be sorted. `durable-context` rule 5 (one
home per kind) and `simplicity` 8 (working notes are not the target) pointed the other way, and
lost to the explicit invitation.

## Options

- **No change.** Rule 5 and `simplicity` 8 already cover it. This leaves AGENTS.md contradicting
  them.
- **A decision record only.** It records the convention, but nothing loads a record at the moment
  an agent decides where a note goes.
- **Notes are allowed on main, sorted at a trigger** (the end of a session, or a size). The trigger
  is the hard part, and it leaves unsorted notes on main between triggers.
- **Working notes never merge.** They are a unit of work on their own branch, and only their sorted
  output reaches main.

## Decision

The last. Hampton, 2026-10-06: working notes do not belong on main; they are a unit of work and
have their own branch like any other work. This also needs no trigger: the merge is the trigger.
`durable-context` gains rule 7, and AGENTS.md drops "working notes" from what `docs/context/`
holds. One instance is enough: the failure cost a session to recover from.

Hampton, 2026-11-02: the notes also stay apart from anything that will merge. Agents given the first
wording put notes and sorted records on one branch, where a normal merge carries the notes to main.

## Consequences

- `durable-context` loads when an agent records working state or decides where a note lives,
  which is the moment rule 7 applies.
- `docs/context/deming-points-in-successors.md` is a working note already on main, marked as an
  unfinished draft, and the TQM essay links to it. #115 rebuilds that analysis, and its sorted
  output replaces the note.
- A session starting on main can't see notes on their branch until it is told the branch's name.
- A closed PR is a working note's archive. The essays cite #89 and #90 for their source sessions.
