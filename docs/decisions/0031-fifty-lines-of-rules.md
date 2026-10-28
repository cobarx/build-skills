# 0031. No skill's rules run past fifty lines

- **Status:** Accepted. Amends [0009](0009-seventy-line-limit.md) and
  [0013](0013-cite-sources-in-footnotes.md) (what is counted, and the number).
- **Decided:** 2026-10-28 · **Recorded:** 2026-10-28 · Claude Opus 5.5
- **Affects:** every skill

## Context

0009 caps a skill at seventy lines by `wc -l` of the whole file, and 0013 leaves footnotes out.
`procedures` in stewardship-skills, which follows this format, reached exactly seventy on
2026-10-28 with the same rules it had a commit earlier; only its wrapping changed. Hampton asked
whether the limit should count the rules only.

The parts around the rules are close to fixed: frontmatter, title, purpose, `## Not here` and the
decisions footer take 17 to 26 lines a skill. What pushes against the limit is rules; every
overrun 0009 records came from added rules. Counted whole, the file pushes trimming onto the
purpose and `## Not here` first, because they aren't rules, though they are what keeps a skill
from being applied to the wrong job. `wc -l` is a rough size measure besides: a 450-character
description is one line, the licence and metadata are two.

## Options

- **Keep seventy for the whole file.** Bounds everything that loads when a skill fires, the cost
  0013 names. Rejected: it spends the budget on the parts that don't grow, and trims those first.
- **Count `## Rules` only.** Rejected: `contracts` keeps a review checkpoint and the rules against
  a system you do not control in their own sections, so it would count 17 lines of 44. Rule-bearing
  text could leave `## Rules` to escape the count.
- **Count every rule-bearing section, at fifty.** The lines from the first `##` heading up to
  `## Not here` (or the `---` before the footer, when there is no `## Not here`): rules, review
  checkpoints, tables such as `skill-versioning`'s levels. Measured 2026-10-28, the most is 48
  (`procedures`), then 46 (`steward`), 44 (`contracts`); every other skill is at 42 or under.

## Decision

Count every rule-bearing section, and cap it at fifty lines. The frontmatter, title, purpose,
`## Not here`, footer and footnotes are not counted; review keeps them short. As in 0009, a skill
that outgrows the cap extracts to `references/` first, and raising it again is a new record.

```sh
awk '/^## Not here/{f=0;next} /^## /{f=1} /^---$/{f=0} f' skills/<name>/SKILL.md | wc -l
```

## Consequences

- Room for rules no longer depends on how long the scaffolding is. Under seventy it ranged from 44
  lines (`spec`, `adopting-standards`) to 53 (`simplicity`); now it is fifty for all. `simplicity`
  loses three lines of room and `format` one; every other skill gains one to six.
- The purpose and `## Not here` have no number. If either grows past a short paragraph, they need
  a limit of their own, and this record is revisited.
- Context cost is bounded less tightly: the uncounted parts still load each time a skill fires.
- stewardship-skills states the old limit in its `AGENTS.md`; it follows when this merges.
