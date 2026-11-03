# 0035. `skill-review`: repeated rules are reported, and condensing stays with the author

- **Status:** Accepted
- **Decided:** 2026-11-02 · **Recorded:** 2026-11-02 · Claude Sonnet 5.5
- **Affects:** `skill-review`

## Context

Hampton asked whether `skill-review` should also look for ways to condense a skill, provided the
skill stays as readable. `skill-review` judges a skill by what it makes an agent do (0033), and
rule 2 already reports a rule that makes no difference as unproven, and rule 10 fails a sentence
that says nothing to do.

## Options

- **A general "look for ways to condense" rule.** Rejected: it judges how a skill reads, which
  `skill-review` leaves to the rules for how a skill is written, and "without making it less
  readable" can't be checked.
- **Rerun the skill with each rule removed and report rules that change nothing.** Rejected by
  Hampton: rule 2 already reports a rule that makes no difference, the runs cost one per rule, and a
  rule that guards a rare failure shows no difference on ordinary tasks.
- **Report a rule that repeats another rule or a reference file.** Chosen: it is found by reading,
  and it extends rule 7, which already compares rules with reference files.

## Decision

Hampton, 2026-11-02: rule 7 also has the reviewer note each rule that repeats another or a reference
file. A repeat is a note, not a failure, and the author decides what to merge or cut.

## Consequences

- Condensing a skill that has no repeats is not a review finding. Advice on it belongs to the
  guide for writing skills, when there is one.
