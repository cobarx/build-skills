# 0028. A failure's impact decides when it earns a rule

- **Status:** Accepted
- **Decided:** 2026-10-06, revised 2026-11-02 before merging · **Recorded:** 2026-11-02 · Claude
  Opus 5.5
- **Affects:** every skill, when a failure is weighed as grounds for a new rule

## Context

The library had no stated threshold for when a failure becomes a rule, and practice was split.
`planned-skills.md` parks "own the type you accept" with "One instance, one correction. Needs a
second before it earns a rule." 0011 was adopted after one session's instance, and so was
`durable-context` rule 7 (0027). Asked which applies, Hampton answered on 2026-10-06 that size
decides. Reading that draft on 2026-11-02, he added that count can matter too: a moderate failure
might take two instances and a minor one several, which together amount to impact.

## Options

- **Wait for a second instance.** Keeps one-off mistakes out of the skills. A costly failure gets
  repeated before anything changes.
- **Act on the first.** Every failure is caught early. Skills grow a rule for each mistake, which
  is the volume `simplicity` 8 warns against.
- **By the size of each instance, with no role for count.** A costly failure is acted on at once,
  but repeated small failures never add up to anything.
- **By impact.** What the failure costs decides, across however many instances there are.

## Decision

By impact, including the cost of recovery. Hampton's example: a server goes down and there is no
dashboard to help bring it back up. That is high impact and doesn't need a second failure, and the
dashboard would shorten the recovery rather than prevent the failure.

One large failure can be enough, while a moderate one might take two instances and a minor one
several. Repeated instances add to the impact and can show a pattern. They are not the only
evidence of one: an incident review, the owner's experience, or an agent's research into similar
failures in other projects can show it too, and some of that may be evidence the agent doesn't
have.

The decider judges each case. Hampton: "this isn't a hard science". There is no fixed count, no
measure of impact and no tally to keep.

## Consequences

- A rule adopted on few instances says in its decision record what the failure cost and where the
  evidence came from, as 0027 does for cost, so the judgement can be revisited.
- Candidates not yet ready stay in `docs/context/open-questions.md`, where patterns can be spotted
  as they come up.
- The "needs a second" line in `planned-skills.md` stands as a judgement about its own instance. It
  is not a general rule.
