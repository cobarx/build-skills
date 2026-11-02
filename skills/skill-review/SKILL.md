---
name: skill-review
description: This skill should be used when reviewing a new or changed agent skill, a SKILL.md or a PR that adds or edits one; when testing whether a skill loads when it should, or changes what an agent does; or when a skill's demo is offered as evidence that it works. It governs what a review of a skill has to test, not the act of reviewing or the format of a skill.
license: CC-BY-4.0 (https://creativecommons.org/licenses/by/4.0/)
metadata: {author: Hampton Maxwell, source: "https://github.com/cobarx/build-skills/tree/main/skills/skill-review"}
---

# skill-review

Judge a skill by what it makes an agent do, not by how it reads.

A skill can meet every format rule and still load on the wrong work, or change nothing. Reading finds
the first kind of problem; only running the skill finds the others.

## Rules

1. **Find which format binds, then measure it once.** The skill's own project comes first, and the
   library it follows fills the gaps. If two documents set different limits, measure against each
   and say which you held it to. This check is quick, and it is rarely where a skill goes wrong.

2. **Keep three questions apart: does it load, does the agent follow it, is the result better.** Each
   needs its own evidence, and "it loaded in every run" answers only the first. Better means better
   than the same task without the skill. If a rule changes nothing between the two, report it as
   unproven. Say how many runs back each result, since one run is an example, not a rate.

3. **Run a task it should not fire on, more than once.** Choose ordinary work that shares words with
   the description, because loading varies between runs. If it loads, report what the wrong load
   changed in the answer as well as the fact that it loaded.

4. **Spend the other runs where the skill's own demo didn't go.** Its demo shows which platforms and
   kinds of project were tried, and the gaps are where a run can find something new.

5. **Prove each run tested what you think.** Before trusting a run, confirm from its log that no
   other instructions shaped it and that the skill's references could be read. Both failures look
   like a normal run. See [running-a-skill.md](references/running-a-skill.md) before the first run.

6. **For each rule, say what would obey its words and miss its point.** Then look for that in the
   runs: "at most two steps" is obeyed by two steps holding six commands. A loophole is a finding
   even if no run took it, so mark which ones were seen and which are only argued.

7. **Hold the skill to its own rules, and its parts to each other.** Apply what it tells agents to
   its own text, references and PR: a skill that says "never from memory" can't ship commands written
   from memory. Then read each rule against its references, where the two can quietly disagree.

8. **Spend fact checks where a skill goes wrong.** Common flags rarely are. Check what depends on a
   version, what is surprising, what is offered as a correction and each reason a rule gives, against
   the source for that version, and cite it. Check too that an example covers every platform the
   project says it covers.

9. **Review what will land.** Confirm the commit against the remote, since a local branch can be
   behind. A conflict list doesn't show what merges cleanly and is still wrong, such as a version
   field that reuses a released number (`skill-versioning`), so check the merged result.

## Not here

The act of reviewing (independence, lenses, verdicts, one review of record) is `review`, and this
skill adds to it, so load both. What a skill's version should be is `skill-versioning`. Keeping
cases that rerun a skill is the job of its evals. This governs what a review of a skill has to
test, not how a skill is written.

---

Decisions affecting this skill: `docs/decisions/*-skill-review-*.md`
