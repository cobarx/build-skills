**Cap a skill's rule-bearing sections at fifty lines instead of the whole file at seventy**

This change records the decision in `docs/decisions/0031-fifty-lines-of-rules.md`. It can be merged without changing any skill, because every skill already meets the new cap.

The old limit, decision 0009, counted the whole file with `wc -l`, so the frontmatter and footer used up room meant for rules. The new limit no longer counts:

- frontmatter
- title
- purpose
- the Not here section
- footer
- footnotes

On 2026-10-28, these skills had the most rule-bearing lines:

| Skill | Rule-bearing lines |
| --- | --- |
| procedures | 48 |
| steward | 46 |
| contracts | 44 |

The limit has no automatic check yet, so reviewers enforce it. The decision record gives an `awk` command that reproduces the count.
