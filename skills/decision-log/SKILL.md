---
name: decision-log
description: This skill should be used when a choice is made between options (a tool, a library, an architecture); when an agent is about to hand someone a decision to make; or when a past decision is revisited or reversed. It governs how a decision is made and recorded, not which decisions must be made before starting.
license: CC-BY-4.0 (https://creativecommons.org/licenses/by/4.0/)
metadata: {author: Hampton Maxwell, source: "https://github.com/cobarx/build-skills/tree/main/skills/decision-log"}
---

# decision-log

A decision is reasoned in the open.

The choice is the least of it. What a later reader needs is why this option and not the others, so
the record carries the reasoning, and the reasoning happens before the choice, not after it.

## Rules

1. **Frame it before you make it.** Establish the criteria (from `spec`), the real options, and the
   tradeoffs first. A choice made before it is framed is made in the dark.

2. **Record the how, not just the what.** The entry says what was weighed and why this one won, so
   the decision can be revisited on its reasoning rather than re-argued from scratch.

3. **Do not hand a raw menu to the decider.** When a person is in the decision, give them the framed
   choice and a recommendation; ask only when their preference or context is the deciding input, not
   to dodge the analysis. A choice among options the decider cannot weigh is an overload, not a
   decision.

4. **Architecture and tooling choices are decisions.** They are logged like any other, not settled
   in passing because they felt like implementation detail.

5. **Supersede, never edit.** A decision that changes becomes a new, dated entry that supersedes the
   old; the old one stays, so the history of the reasoning survives.

## Not here

Defining what the change must do, and the criteria a decision is weighed by, is `spec`. Which
decisions must be made before starting is `project-setup`. Where a record lives so it can be found
is `durable-context`. Performing the analysis a decider weighs is `decision-analysis`. This governs
how a decision is made and recorded.

---

Decisions affecting this skill: `docs/decisions/*-decision-log-*.md`
