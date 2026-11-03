---
name: writing-skills
description: This skill should be used when writing the PR description, commit message or review request for a change under a `skills/` directory or to any SKILL.md or skill reference file; when adding, editing, renaming or removing a skill; or when such a description says the skill "works" without showing an agent using it. It governs what an author brings so that a reviewer can judge a skill change: rules in house format, examples of an agent running them. It does not govern whether the skill is good or how the change is reviewed.
license: CC-BY-4.0 (https://creativecommons.org/licenses/by/4.0/)
metadata: {author: Hampton Maxwell, source: "https://github.com/cobarx/build-skills/tree/main/skills/writing-skills"}
---

# writing-skills

A skill change is ready to judge.

A reader of a skill diff sees wording. The wording is easy to read when every rule has the same
shape, and what it makes an agent do shows only when an agent runs it. An example is that run's
output, put where the reviewer can read it.

## Rules

1. **Write each rule as a numbered paragraph under `## Rules`.** Start with `N.` and a bold
   sentence that gives the instruction in the imperative. Follow it with sentences that each say
   what to do or how to tell it's done, and leave the reasoning to `docs/essays/`. Separate rules
   with a blank line. Count the lines from the first `##` heading to `## Not here`, and keep the
   count at fifty or fewer.

2. **Put examples in the PR description.** Every PR that changes a `SKILL.md` or a reference file
   carries them under a heading such as "Examples". Do not commit them.

3. **Run each example as a pair.** Install the skill text under test in a throwaway project, as
   `skill-review` describes, and do not paste it into the prompt. Run one agent with the skill text
   from `main` (or no skill, for a new one) and another with the changed text, with the same task,
   model and tools and nothing else loaded. Label each output "before" or "with the change".

4. **Cover each kind of output the change governs.** Name the kinds (a document, code, an answer)
   from the change itself, not from this list, and run a pair for each.

5. **Show the comparison, not the runs.** For each pair give the prompt, the commit of the skill
   text loaded, the section headings of both outputs side by side (an output without headings gets
   its parts listed in order), and the passages that exist in only one, quoted exactly. Keep the
   full outputs somewhere that outlasts the PR, not `/tmp`, and say where they are.

6. **Say what the examples show.** State the difference between each pair in one sentence, or "no
   difference", and cut or rework any rule whose pair shows none. State how many runs stand behind
   each pair.

7. **Say what they leave open.** List what no example covered: the failure the change targets if it
   wasn't reproduced, kinds of output not run, anything the agents could not do. Run the pairs
   whenever the tools allow it, and write "could not run" only for a tool you tried and lacked. When
   no pair could be run, say so in one line and name the pairs owed; do not draft tables or outputs
   for runs that did not happen.

8. **Tell the reviewer what to compare.** Point to the lines in each pair to read, and say what good
   looks like (`definition-of-done` rule 6). Write it as a property the reviewer can read in the
   output, such as a heading, a number or a quoted line, not as a restatement of the change.

9. **Replace the examples with one line when the change cannot alter an agent's behaviour.** A
   spelling or whitespace fix qualifies, and the line says so. A changed link, name, number or
   pointer does not: run the pair. When unsure, run the pair.

## Not here

Whether the examples hold up (loading, following, better or worse) is `skill-review`. What a rule
should say is the skill's own subject; how its sentences read is `writing-style`. How a PR
description is organised is `writing-structure`. What a skill change's version is, is
`skill-versioning`.

---

Decisions affecting this skill: `docs/decisions/*-writing-skills-*.md`
