# 0009. No skill runs past seventy lines

- **Status:** Accepted. Line count amended by [0013](0013-cite-sources-in-footnotes.md) and
  [0031](0031-fifty-lines-of-rules.md).
- **Decided:** 2026-09-22 (#42) · **Recorded:** 2026-09-22 · Claude Opus 5.5
- **Affects:** every skill

## Context

The README said every skill was under sixty lines. It was false: `simplicity` at 67 since #4,
`contracts` at 64 since #7 (65 after #42), `naming` at 61 after #41. The same sixty-line pressure
had cost `definition-of-done` rule 5 its guardrail in #14.

## Options

- **Drop the gate, keep sixty as a diagnostic.** Proposed in #42's first round; rejected because
  enforcing has genuine value, and overruns are rare: three skills ever, two of them in the first
  two days.
- **Keep sixty and trim.** Tried in #42's second round. The cuts deleted formative reasoning (the
  reading boundary a linter cannot see, the lineage of "data dominates", why the exceptions are
  exceptions, what adopting a contract adopts) and were undone.
- **Seventy.**

## Decision

Seventy lines, by `wc -l`, which holds every skill with its reasoning intact. A skill that outgrows
it extracts to `references/` first (`simplicity`: *Extract, do not raise the threshold*); raising
the gate again is a new record.

## Consequences

- Enforced in review for now. A CI check is deferred: the repo is not ready for CI yet.
- Trimming a skill moves its reasoning or keeps it; a line limit is not a reason to delete it.
