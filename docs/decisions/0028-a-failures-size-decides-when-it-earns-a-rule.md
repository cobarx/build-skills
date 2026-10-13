# 0028. A failure's size, not its count, decides when it earns a rule

- **Status:** Accepted
- **Decided:** 2026-10-06 · **Recorded:** 2026-10-06 · Claude Opus 5.5
- **Affects:** every skill, when a failure is weighed as grounds for a new rule

## Context

The library had no stated threshold for when a failure becomes a rule, and practice was split.
`planned-skills.md` parks "own the type you accept" with "One instance, one correction. Needs a
second before it earns a rule." 0011 was adopted after one session's instance, and so was
`durable-context` rule 7 (0027). Asked which applies, Hampton answered on 2026-10-06.

## Options

- **Wait for a second instance.** Keeps one-off mistakes out of the skills. A costly failure gets
  repeated before anything changes.
- **Act on the first.** Every failure is caught early. Skills grow a rule for each mistake, which
  is the volume `simplicity` 8 warns against.
- **By size.** The cost of the failure decides.

## Decision

By size. Hampton: a large enough failure demands immediate action; a smaller one may tolerate
repeated mistakes. No count is the threshold. The decider judges the size of each instance.

## Consequences

- A rule adopted on one instance says in its decision record what that instance cost, as 0027
  does, so the judgement can be revisited.
- The "needs a second" line in `planned-skills.md` stands as a judgement that its instance was
  small. It is not a general rule.
- There is no measure of size. If judgements start to diverge, that is the time to define one.
