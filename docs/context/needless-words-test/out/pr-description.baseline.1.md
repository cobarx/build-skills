**Record the decision to cap a skill's rule-bearing sections at fifty lines**

This PR adds `docs/decisions/0031-fifty-lines-of-rules.md`, which replaces the seventy-line limit on a whole skill file with a fifty-line limit on its rule-bearing sections. No skill needs changing to meet the new cap, so merging it changes only the rule that future skills and reviews follow.

The old limit, decision 0009, counted the whole file with `wc -l`, so the frontmatter and footer used up room meant for rules. The new limit does not count the following parts of a skill:

- the frontmatter
- the title
- the purpose
- the "Not here" section
- the footer
- the footnotes

Every skill already fits within the cap. These are the highest counts of rule-bearing lines, measured on 2026-10-28:

| Skill | Rule-bearing lines |
| --- | --- |
| `procedures` | 48 |
| `steward` | 46 |
| `contracts` | 44 |

The record gives an `awk` command that reproduces the count. There is no automatic check yet, so reviewers enforce the limit in review.
