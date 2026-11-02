---
name: simplicity
description: This skill should be used before starting any unit of work; when a task or PR description needs the word "and" to be accurate; when a function grows a third level of nesting; when a new dependency is proposed; when a complexity gate fails; or when asked to do several things at once. It keeps the cost of understanding a change low, so any one part can be reviewed with only its contract in view.
license: CC-BY-4.0 (https://creativecommons.org/licenses/by/4.0/)
metadata: {author: Hampton Maxwell, source: "https://github.com/cobarx/build-skills/tree/main/skills/simplicity"}
---

# simplicity

Make every change cheap to understand. Size is the indicator, not the goal: a change is expensive
when reviewing it means holding several unrelated things at once.

A change is anything handed to a reader. A diff, a PR description, a review comment, a reply.

## Rules

1. **One sentence, no "and".** If you cannot describe the unit in one sentence without "and", it is
   more than one unit. An abstraction invented to make the sentence work is a failure, not a pass.

2. **Cross-cutting concerns are peers.** If a thing references three siblings, it belongs beside
   them, never inside one of them.

3. **Sequence dependencies, do not merge them.** A unit that cannot be built without another is an
   ordering problem.

4. **Exceptions, named so the rule survives.** A greenfield first commit, generated code, and
   mechanical refactors are single units regardless of size. Reviewing them does not require
   holding many things in mind at once.

5. **Extract, do not raise the threshold.** Overriding a default is a decision, and gets logged.

6. **Weigh dependencies both ways.** Prefer the platform, which costs neither. Otherwise: twenty
   lines used once are not worth a supply chain, and a module you would implement is not just
   lines but every decision inside it, each one yours to make, justify and maintain. Neither side
   wins by default.

7. **Propose the split.** When asked for too much at once, say so, and give the units and their
   order. State it once; if reaffirmed, proceed.

8. **The cheapest change to review is the one not written.** Reuse before implementing, delete
   before adding, and produce no documentation or tests beyond what the spec and the standards
   require. Volume is a cost even when every individual piece is small, and it is the cost that
   rises fastest when producing more is nearly free.

   Working notes are not the target. A scratchpad costs nobody but its author, and thinking in
   writing is not the same as shipping prose. The target is output presented as finished.

## Thresholds

Complexity essential to the problem must be paid for; complexity introduced by the solution is
waste. For code, the thresholds that measure it are in
[references/thresholds.md](references/thresholds.md): load it when writing or reviewing code.

Completion is not here. See `definition-of-done`.

---

Decisions affecting this skill: `docs/decisions/*-simplicity-*.md`
