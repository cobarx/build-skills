**Record the decision to cap rule-bearing lines at fifty**

This PR records a decision to cap a skill's rule-bearing sections at fifty lines, replacing the seventy-line cap on the whole file set by decision 0009. No skill needs changing to meet the new cap, which is enforced in review because there is no automatic check yet.

Decision 0009 counted the whole file with `wc -l`, so the frontmatter and footer used up room meant for rules. The new count excludes the frontmatter, title, purpose, the Not here section, footer and footnotes.

These three skills had the most rule-bearing lines when measured on 2026-10-28, so they sit closest to the cap:

| Skill | Rule-bearing lines |
| --- | --- |
| procedures | 48 |
| steward | 46 |
| contracts | 44 |

The record, `docs/decisions/0031-fifty-lines-of-rules.md`, gives an awk command that reproduces the count.
