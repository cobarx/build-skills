---
name: format
description: This skill should be used when setting up a project; when choosing a formatter; when a formatting disagreement arises; before a bulk reformat; or when reviewing a diff where formatting noise obscures the change. It removes formatting from the set of things anyone argues about.
license: CC-BY-4.0 (https://creativecommons.org/licenses/by/4.0/)
metadata: {author: Hampton Maxwell, source: "https://github.com/cobarx/build-skills/tree/main/skills/format"}
---

# format

Remove formatting from human judgment.

## Rules

1. **Take the defaults.** Adopt the tool's default configuration unmodified. Every option you set
   is one someone will later want to change, and time spent on brace style or quote style is pure
   loss. The value is uniformity, not the particular choice.

2. **One formatter, every file it can handle.** Partial coverage produces exactly the unreadable
   diffs that formatting exists to prevent.

3. **Formatting changes land alone.** A reformat mixed into a behaviour change cannot be reviewed.
   Separate commit, separate PR, no exceptions.

4. **Record bulk reformats in `.git-blame-ignore-revs`.** Set `blame.ignoreRevsFile` in the repo
   config so it applies without anyone passing a flag. Blame has to survive the reformat or people
   stop reformatting.

5. **Applied, not suggested.** Formats on save locally, checked in CI. A formatter that reports
   instead of fixing is a linter with extra steps.

6. **Not a linter.** Formatting is layout; linting is rules. Keeping them separate means format
   churn cannot hide a rule violation in a diff. One tool may do both, provided it keeps the two
   concerns and their configs separate.

## Not here

Which formatter a project uses is a `decision-log` entry, because the answer differs by language.
Rules about code content belong to `linting` and to the skills that own them.

---

Decisions affecting this skill: `docs/decisions/*-format-*.md`
