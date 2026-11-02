# Cap a skill's rule-bearing sections at 50 lines

This PR records a decision to cap a skill's rule-bearing sections at 50 lines, replacing the 70-line cap on the whole file. Merging it requires no changes to any skill, because all of them already meet the new cap.

## Why the limit is changing

The old limit, decision 0009, counted the whole file with `wc -l`, so the frontmatter and footer used up room meant for rules. The new limit counts only the lines that carry rules. These parts of a skill are no longer counted:

- Frontmatter
- Title
- Purpose
- The "Not here" section
- Footer
- Footnotes

## How current skills measure up

A count on 2026-10-28 found that the largest skill has 48 rule-bearing lines, 2 under the cap. These three skills have the most:

| Skill | Rule-bearing lines |
| --- | --- |
| `procedures` | 48 |
| `steward` | 46 |
| `contracts` | 44 |

To reproduce the count, run the `awk` command given in `docs/decisions/0031-fifty-lines-of-rules.md`.

## Enforcement

There is no automatic check yet, so reviewers have to enforce the limit during review.
