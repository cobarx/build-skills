# Cap a skill's rule-bearing sections at fifty lines

This PR records a decision to cap a skill's rule-bearing sections at fifty lines, replacing the seventy-line cap on the whole file. No skill needs changing to meet the new cap. The record is `docs/decisions/0031-fifty-lines-of-rules.md`.

## Why the limit changed

The old limit, decision 0009, counted the whole file with `wc -l`, so the frontmatter and footer used up room meant for rules. The new limit doesn't count the frontmatter, title, purpose, Not here section, footer or footnotes.

## Effect on existing skills

These three skills had the most rule-bearing lines when measured on 2026-10-28, and the highest is two lines under the cap:

| Skill | Rule-bearing lines |
| --- | --- |
| `procedures` | 48 |
| `steward` | 46 |
| `contracts` | 44 |

To reproduce the count, run the awk command given in the record.

## Enforcement

There is no automatic check yet, so the limit is enforced in review.
