# Sorting a session's notes before they are committed: rule, record, or neither?

Analysis, 2026-10-06, Claude Opus 5.5. For Hampton to decide.

## Summary

**Recommendation: a `durable-context` rule and its decision record, in one PR, the way #44 shipped
rule 6 with 0011.** "Decision record or rule" was a false choice on my part: in this repo a new rule
lands with the record that explains it. The rule is the part that changes behaviour, because an
agent loads `durable-context` at the moment it decides where a note goes, and nothing loads a
decision record at that moment. Doing nothing is the strongest alternative: existing rules arguably
cover it already. It loses because AGENTS.md invites "working notes" into `docs/context/` with no
point at which they get sorted, and that invitation is how #89-91 happened.

Questions only you can settle:

1. **Do working notes belong on main at all?** If not, the fix is to drop "and working notes" from
   AGENTS.md, and the rule becomes "sort before committing". If they do, the rule needs a trigger
   for when notes get sorted.
2. **Is one instance enough?** `planned-skills.md` holds one candidate rule back until it has a
   second instance. 0011 was adopted on one. Which applies here is yours to say.

## The problem

On 2026-10-05 a session's notes were committed as three PRs (#89, #90, #91), about 700 lines in
`docs/context/`. Each file grew in the order the conversation went, and mixed several kinds of
content: project values, proposed rule changes, settled reasoning, research and asides. Your
criterion, from 2026-10-06: generic context like this "is going to be hard to parse through and
convert into something useful." Converting it took a full session: two essays, ten issues and a
`planned-skills.md` edit.

The proposal is to sort at the end of a session, before committing. Each open question becomes an
open-questions entry or an issue, each proposed change an issue, settled reasoning an essay, and
each settled choice a decision record. Asides stay in the PR or branch.

## Criteria

1. **The output is something a reader can use without converting it** (yours, above).
2. **An agent applies it at the moment it matters**, which is when it decides where a note goes.
3. **Low cost**: as few new words in skills as will work (`simplicity` 8).
4. **It doesn't block deliberate raw material.** `pr-walkthrough-session-2026-10-03.md` is a session
   recording kept on purpose as essay source, with distilled notes beside it.

## Options

**A. A `durable-context` rule plus a decision record (recommended).** A rule along these lines:
*Working notes are sorted before they are committed: each open question, proposed change, settled
reasoning and settled choice goes to its own home, and the rest stays in the PR.* The decision
record would explain why, citing #89-91.
- Criterion 1: meets it.
- Criterion 2: meets it. `durable-context` already triggers on "recording ... project knowledge, or
  working state" and on "deciding where a note should live".
- Criterion 3: costs one rule, a version bump (`skill-versioning`) and one record.
- Criterion 4: needs an explicit carve-out for deliberate source material, or it would block the
  2026-10-03 recording.
- Precedent: #44 changed the skill and added 0011 in one PR.

**B. A decision record only.** It records the convention without touching a skill.
- Criterion 3: cheapest.
- Criterion 2: fails. A decision is found through the glob at a skill's foot, read on demand, so an
  agent writing notes has no trigger to open it.

**C. Neither; the existing rules already cover it.** The steelman:
- `durable-context` 5 already says one home per kind.
- `simplicity` 8 already says "working notes are not the target ... the target is output presented
  as finished."
- AGENTS.md's "draft long, then keep only what is a rule" already treats the long draft as a
  discovery tool and not the deliverable.
- On this reading, #89-91 were a failure to apply those rules, not a missing rule. A fourth
  statement of the same idea adds words, which is the cost `simplicity` 8 warns about.
- It is also what the "needs a second instance" norm in `planned-skills.md` would say.

Does C apply now? Partly. The rules are there, but they pull against AGENTS.md, which lists "open
questions and working notes" as what `docs/context/` holds. An agent following AGENTS.md committed
working notes there correctly, and nothing told it when they had to be sorted. C leaves that
conflict in place.

## Why A, where it loses

A loses on cost (criterion 3) and on the second-instance norm. It still wins, for two reasons. The
cost of this one instance was a full session of sorting. And the cause is structural: AGENTS.md
invites working notes with no exit, so it will recur unless something changes.

If your answer to question 1 is that working notes don't belong on main, the cheapest form of A is
a one-line AGENTS.md edit plus the rule's wording "sort before committing", with no carve-out to
maintain.

## What would reverse it

- Unsorted notes keep arriving after the rule ships. The rule isn't triggering, and it belongs
  somewhere always on, such as AGENTS.md.
- Sorting at the end of a session costs more than it saves. That would show as sessions that end
  without their notes recorded anywhere.
- The carve-out for deliberate source material is used as a way around the rule.

## Facts and how they were checked

- #44 changed `skills/durable-context/SKILL.md` and added 0011 in one commit. Checked with
  `git show --stat 6f9e7c1`, 2026-10-06.
- AGENTS.md line 45 reads "what is not settled yet: open questions and working notes". Checked on
  `origin/main`, 2026-10-06.
- `durable-context` rules 2 and 5, and their trigger wording, were read on `origin/main`,
  2026-10-06.
- The "needs a second" line is in `planned-skills.md` (the parked "own the type you accept" entry),
  read 2026-10-06. It is stated for one candidate rule. Whether it is a repo-wide norm is not
  recorded anywhere I found.
- That 0011 was decided on one instance: its Context section describes one pubnet-tools session.
  Read 2026-10-06.
