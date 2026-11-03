---
name: writing-skills
description: This skill should be used when adding, editing, or renaming a skill (a SKILL.md or its reference files); when opening a PR that changes a skill; or when a PR description for a skill says the skill "works" without showing an agent using it. It governs what an author shows with a skill change, not how the skill's rules are worded or how the change is reviewed.
license: CC-BY-4.0 (https://creativecommons.org/licenses/by/4.0/)
metadata: {author: Hampton Maxwell, source: "https://github.com/cobarx/build-skills/tree/main/skills/writing-skills"}
---

# writing-skills

A skill change shows an agent running it.

A reader of a skill diff sees wording. What the wording makes an agent do shows only when an agent
runs it. An example is that run's output, put where the reviewer can read it.

## Rules

1. **Put examples in the PR description.** Every PR that changes a `SKILL.md` or a reference file
   carries them under a heading such as "Examples". Do not commit them: they are a
   record of one test, and the repo keeps rules.

2. **Run each example as a pair.** Give one agent the skill text from `main` (or no skill, for a new
   one) and another the changed text, with the same task and nothing else loaded. Each output is an
   example, labelled "before" or "with the change".

3. **Cover each kind of task the change touches.** Name the kinds (a document, code, a question) and
   run a pair for each. A change that reads right for one kind and wrongly for another shows only
   when both are run.

4. **Show the comparison, not the runs.** For each pair give the prompt, the commit of the skill
   text loaded, the section headings of both outputs side by side, and the passages that exist in
   only one, quoted exactly. Keep the full outputs and say where they are, so a reviewer who doubts
   a quote can ask for them.

5. **Say what the examples show.** State the difference between each pair in one sentence, or
   "no difference": a rule whose pair shows none has not earned its lines. State how many runs
   stand behind each, because one run per cell is an example, not a rate.

6. **Say what they leave open.** List what no example covered: the failure the change targets if it
   wasn't reproduced, kinds of task not run, anything the agents could not do. A reviewer relies on
   the examples for exactly what this list does not name.

7. **Tell the reviewer what to compare.** Point to the lines in each pair to read, and say what good
   looks like (`definition-of-done` rule 6).

8. **A change that cannot alter an agent's behaviour says so instead.** A typo or a link fix takes
   one line saying why no example applies. When unsure, run the pair.

## Not here

Whether the examples hold up (loading, following, better or worse) is `skill-review`. How the
skill's rules are worded is the project's conventions. How a PR description is organised is
`writing-structure`. What a skill change's version is, is `skill-versioning`.

---

Decisions affecting this skill: `docs/decisions/*-writing-skills-*.md`
