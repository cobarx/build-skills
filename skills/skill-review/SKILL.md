---
name: skill-review
description: This skill should be used when reviewing a new or changed agent skill (a SKILL.md, or a PR that adds or edits one); when testing whether a skill loads when it should, or changes what an agent does; or when a skill's demo is offered as evidence that it works. It governs what a review of a skill has to test, not the act of reviewing or how a skill is written.
license: CC-BY-4.0 (https://creativecommons.org/licenses/by/4.0/)
metadata: {author: Hampton Maxwell, source: "https://github.com/cobarx/build-skills/tree/main/skills/skill-review"}
---

# skill-review

Judge a skill by what it makes an agent do, not by how it reads.

A skill is a set of instructions, a SKILL.md and any reference files, that an agent loads when its
`description` field matches the task. A skill can follow every rule for how skills are written and
still load for tasks it wasn't meant for, or make no difference. Reading finds problems in how it is
written, but only running it finds those two. To run a skill, give an agent a task with the skill
installed and see what it does. Each attempt is one run, and
[running-a-skill.md](references/running-a-skill.md) says how to do the first. A demo is the output
an author offers to show the skill working.

## Rules

1. **Check the skill once against the rules for how a skill is written.** Use the rules in the
   skill's own project first, and those of any collection of skills it follows for what they leave
   out. If two documents set different limits, check against each and report which you held the
   skill to. The skill fails if it breaks a limit or rule that applies.

2. **Answer three questions separately: does the skill load, does the agent follow it, and is the
   result better?** Give each its own evidence: "it loaded in every run" answers only the first. The
   skill fails if the result is worse than the same task without the skill. Report any of its rules
   that makes no difference as unproven. State how many runs support each answer, because one run is
   an example, not a rate.

3. **Run a task the skill should not load for, more than once.** Choose ordinary work that shares
   words with the skill's `description`, and repeat the same task, because a skill can load on one
   run and not the next. The skill fails if it loads on any run.

4. **Run the skill on at least one platform or kind of project the author's demo didn't cover.** The
   skill fails if the result is wrong or worse than a run without the skill.

5. **Confirm from each run's log that it tested what you meant.** Check that no other instructions,
   such as the user's global settings, reached it, and that the agent could read the skill's
   reference files, because its answer won't show either failure. If either fails, rerun it.

6. **For each of the skill's rules, write down one way an agent could follow its words and miss its
   point.** For example, an agent can obey "at most two steps" with two steps that run six commands
   in total. The skill fails if a run did this. Report the others as only reasoned.

7. **Check that the skill follows its own rules, and that its rules and reference files agree.**
   Apply the skill's instructions to its own text, reference files and PR: a skill that says "never
   from memory" can't ship commands written from memory. The skill fails if it breaks its own rule
   or a rule contradicts a reference file. A rule that repeats another or a reference is a note.

8. **Verify every factual statement in the skill, and run every command it gives.** Check each
   statement, including the reasons rules give, against the documentation for its version, and cite
   what you used. Run each command on every supported platform, on a disposable machine if it could
   do harm. The skill fails if a statement is wrong or a command doesn't do what the skill says.
   Report anything you couldn't check as blocked.

9. **Review what the merge will produce, not only the branch.** Confirm that the commit you reviewed
   is the one on the remote, because a local branch can be behind. The skill fails if the merged
   result is wrong, even with no conflicts: for example, a reused version number.

10. **Check that every sentence of a rule says what to do or how to tell it's done.** An example of
    what the rule requires counts. The skill fails on any other sentence.

11. **Report each rule as pass, fail or blocked, and stop the merge on any failure or blocked
    check.** The author fixes the skill or narrows what it claims to cover, or someone runs the
    blocked check. Only a person can override a blocked check.

## Not here

How to carry out any review (who may review, what to look for, how to report it) is the `review`
skill, and this skill adds to it, so load both. What a skill's version should be is the
`skill-versioning` skill. Saving test cases so that a skill can be retested later is the job of its
evals, the automated tests of a skill. This skill governs what a review of a skill has to test, not
how a skill is written.

---

Decisions affecting this skill: `docs/decisions/*-skill-review-*.md`
