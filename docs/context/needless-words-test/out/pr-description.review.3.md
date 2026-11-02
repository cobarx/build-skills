This pull request records a decision to cap a skill's rule-bearing sections at fifty lines, replacing the seventy-line cap on the whole file. No skill needs changing to meet the new cap. The record is `docs/decisions/0031-fifty-lines-of-rules.md`.

The old limit, decision 0009, counted the whole file with `wc -l`, so the frontmatter and footer used up room meant for rules. The new count leaves out the frontmatter, title, purpose, the Not here section, footer and footnotes.

These three skills had the most rule-bearing lines on 2026-10-28:

- `procedures`: 48 lines
- `steward`: 46 lines
- `contracts`: 44 lines

To check these numbers, run the awk command in the record.

There is no automatic check yet, so the limit is enforced in review.
