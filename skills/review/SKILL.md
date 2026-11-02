---
name: review
description: This skill should be used when reviewing a change, a PR, or another agent's work; when deciding what a reviewer checks or how independent it must be; or when a review needs to report a blocker rather than route around it. It governs the act of reviewing, not the standards reviewed against.
license: CC-BY-4.0 (https://creativecommons.org/licenses/by/4.0/)
metadata: {author: Hampton Maxwell, source: "https://github.com/cobarx/build-skills/tree/main/skills/review"}
---

# review

A reviewer tries to break the work against the standard it claims to meet.

A review that sets out to approve finds reasons to approve. The reviewer's job is the opposite of
the author's (to find what is wrong), and it cannot be done by the one who built it.

## Rules

1. **Review from outside.** The reviewer is not the author and does not share the author's stake in
   the artifact. The moment it owns the fix, it takes on that stake, and stops being a critic.

2. **Check the declared standard, not one you invent.** Hold the change to the skills it is subject
   to (`definition-of-done`, `simplicity`, `naming`, the rest) and to its own stated goal. A
   private preference dressed as a finding wastes the author's time.

3. **Verify by use; what you cannot verify is blocked, not passed.** Run it, don't just read it. A
   dimension you cannot confirm is reported `blocked`, naming what would unblock it; a proxy never
   stands in for the real check. If the check needs a capability you lack (watching playback, using
   hardware), hand it to someone who has it, a human at a player, rather than pass it or let it drop.

4. **Take a viewpoint, and make it break something.** Each pass adopts a lens with a named thing it
   tries to disprove: **correctness** (does it do what it claims), **simplicity** (is it more than
   one thing, is it coupled), the **user's purpose** (does it serve the goal, not merely run). A
   persona with no disproof is costume. More lenses (security, docs) as the work warrants.

5. **Report pass, fail, or blocked, then stop.** Return a verdict per point, with the evidence. The
   fix belongs to the author; a review that rewrites the work has reviewed nothing.

6. **One review of record, kept current.** Edit one comment each pass rather than stack new ones:
   the current verdict on top, then a history of what each pass raised and how it was resolved. A
   reader should see the standing verdict without parsing the thread.

## Not here

What "done" means is `definition-of-done`; a review checks against it, never redefines it. Whether a
unit is one thing is `simplicity`; whether a name is true is `naming`. Running several reviews at
once is `parallel-work`. This governs the act of reviewing, not the standards reviewed against.

---

Decisions affecting this skill: `docs/decisions/*-review-*.md`
