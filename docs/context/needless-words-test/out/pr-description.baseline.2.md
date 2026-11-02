**Cap a skill's rule-bearing sections at 50 lines instead of the whole file at 70**

This PR records a decision in `docs/decisions/0031-fifty-lines-of-rules.md`: a skill's rule-bearing sections are now limited to 50 lines, replacing the 70-line limit on the whole file from decision 0009. Merging it requires no changes to any skill, because all of them already meet the new cap.

The old limit counted the whole file with `wc -l`, so the frontmatter and footer used up room meant for rules. The new count leaves out these parts of a skill:

- Frontmatter
- Title
- Purpose
- The "Not here" section
- Footer
- Footnotes

The closest skills to the cap, measured on 2026-10-28, have this many rule-bearing lines:

| Skill | Lines |
| --- | --- |
| `procedures` | 48 |
| `steward` | 46 |
| `contracts` | 44 |

To check these numbers, run the `awk` command given in the decision record.

There is no automatic check yet, so the limit is enforced in review for now.
