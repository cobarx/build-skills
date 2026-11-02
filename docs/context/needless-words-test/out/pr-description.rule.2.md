**Cap a skill's rule-bearing sections at fifty lines**

This change records a decision to replace the seventy-line limit on a whole skill file with a fifty-line limit on its rule-bearing sections. No skill needs changing to meet the new cap, so merging affects only how skills are measured from now on.

The old limit, decision 0009, counted the whole file with `wc -l`, so the frontmatter and footer used up room meant for rules. The new limit doesn't count the frontmatter, title, purpose, Not here section, footer or footnotes.

The three longest skills, measured on 2026-10-28, all fit under the cap:

| Skill | Rule-bearing lines |
| --- | --- |
| procedures | 48 |
| steward | 46 |
| contracts | 44 |

There is no automatic check yet, so reviewers enforce the limit. To reproduce the count, use the awk command in the record, `docs/decisions/0031-fifty-lines-of-rules.md`.
