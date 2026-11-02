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
[running-a-skill.md](references/running-a-skill.md) says how to do the first.

## Rules

1. **Check the skill once against the rules for how a skill is written.** The rules in the skill's
   own project come first, and those of any collection of skills it follows cover what they leave
   out. If two documents set different limits, such as a maximum length, check against each and say
   which you held the skill to. This check is quick, and how a skill is written is rarely where it
   goes wrong.

2. **Answer three questions separately: does the skill load, does the agent follow it, and is the
   result better?** Each needs its own evidence, and "it loaded in every run" answers only the
   first. Better means better than the result of the same task without the skill. If one of the
   skill's rules makes no difference between those two runs, report that rule as unproven. Say how
   many runs support each result, because one run is an example, not a rate.

3. **Run a task the skill should not load for, more than once.** Choose ordinary work that shares
   words with the skill's `description`. Repeat the same task because a skill can load on one run
   and not the next. If it loads, compare the answer with a run without the skill, and report how
   the answer changed as well as the fact that it loaded.

4. **Test what the author's demo didn't try.** A demo is the output an author offers to show the
   skill working, and it shows which platforms and kinds of project were tried. The gaps are where a
   run can find something new.

5. **Prove that each run tested what you meant it to.** Before trusting a run, confirm from its log
   that no other instructions, such as the user's global settings, reached it, and that the agent
   could read the skill's reference files. If either went wrong, the answer still looks normal.

6. **For each of the skill's rules, name a way to follow its words and still miss its point.** For
   example, an agent can obey "at most two steps" by giving two steps that run six commands in
   total. That is a loophole. Look for loopholes in the runs, and report each one even if no run
   used it, marking which ones a run used and which you only reasoned could happen.

7. **Check that the skill follows its own rules, and that its rules and reference files agree.**
   Apply the skill's instructions to its own text, reference files and PR: a skill that says "never
   from memory" can't ship commands written from memory. Then compare each rule with the reference
   files, because they can contradict each other unnoticed.

8. **Fact-check the skill's statements most likely to be wrong.** What a common command-line flag
   does is rarely one of them. Check the following against the documentation for the version in
   question, and cite what you used: anything that depends on a version, anything surprising,
   anything the skill offers as a correction to common practice, and each reason a rule gives. Also
   check that the examples cover every platform the project says it supports.

9. **Review what the merge will produce, not only the branch.** Confirm that the commit you reviewed
   is the one on the remote, because a local branch can be behind. Then check what the merge will
   produce, because a merge with no conflicts can still be wrong: for example, a version field can
   reuse a number already released (see the `skill-versioning` skill).

## Not here

How to carry out any review (who may review, what to look for, how to report it) is the `review`
skill, and this skill adds to it, so load both. What a skill's version should be is the
`skill-versioning` skill. Saving test cases so that a skill can be retested later is the job of its
evals, the automated tests of a skill. This skill governs what a review of a skill has to test, not
how a skill is written.

---

Decisions affecting this skill: `docs/decisions/*-skill-review-*.md`
