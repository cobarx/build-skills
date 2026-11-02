# Cap a skill's rule-bearing sections at fifty lines

This PR records a decision to cap a skill's rule-bearing sections at fifty lines, replacing the seventy-line cap on the whole file. No skill needs changing.

## Why the limit changes

The old limit, decision 0009, counted the whole file with `wc -l`, so the frontmatter and footer used up room meant for rules. The new count leaves out the frontmatter, title, purpose, the Not here section, footer and footnotes.

## How current skills measure up

As measured on 2026-10-28, the skill with the most rule-bearing lines is procedures with 48, followed by steward with 46 and contracts with 44. To reproduce the count, run the awk command in the record, `docs/decisions/0031-fifty-lines-of-rules.md`.

## Enforcement

There is no automatic check yet, so the limit is enforced in review.
