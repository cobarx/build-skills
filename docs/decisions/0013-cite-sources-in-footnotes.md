# 0013. Cite sources in footnotes, outside the line limit

- **Status:** Accepted. Amends [0009](0009-seventy-line-limit.md) (how lines are counted). Count
  amended by [0031](0031-fifty-lines-of-rules.md).
- **Decided:** 2026-09-28 · **Recorded:** 2026-09-28 · Claude Opus 5.5
- **Affects:** every skill, essay, and decision that credits a source

## Context

Credit here is uneven. Decisions name their sources (MADR in 0001, Brooks in 0005); one skill cites
inline (`skill-versioning`, SemVer §4); a copied `simplicity` carries Brooks's idea with no Brooks.
The motivating case: `review` rule 1 (*Review from outside*) restates Don Nelson's "The worst
evaluator of talent is a player trying to evaluate himself," which reached the owner through Mark
Cuban's *How to Win at the Sport of Business*, and credits neither.

The owner wants the citation to follow the text it credits, room for a short note beside it, and
the seventy-line limit (0009) not to crowd credit out.

Searched (`adopting-standards` rule 1): Creative Commons' recommended practices for attribution,
the Chicago notes-bibliography system, and GitHub's Markdown footnote support.

## Options

- **Inline links** (as `skill-versioning` does now). Counts toward the seventy lines, and leaves no
  room for a note.
- **A separate sources file** (`references/`). Costs no context until read, but the citation stops
  following the text: agents and people alike are much more likely to ignore it, or drop it when
  they copy or adapt the skill (the owner's objection, and decisive).
- **Frontmatter `metadata`** (Agent Skills spec). Travels with the file (#70 relies on it for each
  skill's licence and source), but is a string map with no place for a note, and sits far from the
  text it credits.
- **Footnotes, excluded from the count.**

## Decision

Footnotes. A Markdown footnote (`[^nelson]` in the text, its definition at the end of the file)
stays in the file an agent copies, reads as plain text to one, and renders on GitHub.

- **Credit for an idea:** who, the work, and where to find it. Adopted from Chicago
  notes-bibliography: the note form only, not its bibliography or punctuation rules.
- **Attribution for copied or adapted text:** add the licence and what was changed. Adopted from
  Creative Commons: TASL (title, author, source, licence) and CC BY 4.0 §3(a)'s "indicate if
  modifications were made"; the disclaimer of warranties is not carried.
- **In a skill, a footnote is the citation plus at most one short note.** Anything longer goes in
  an essay, which links to the skill, never the reverse.
- **Essays and decisions** use the same form, with notes as long as they need.

Example:

```markdown
[^nelson]: Don Nelson, via Mark Cuban, *How to Win at the Sport of Business* (2011), "Don't Lie to
    Yourself." Nelson's reason is perspective; this rule adds the author's stake.
```

Footnotes go last in a skill, after the decisions glob. 0009's count becomes `wc -l` of the lines
before the first footnote definition.

Weighed: footnotes still load into context every time a skill fires, which is the cost 0009
exists to bound. Excluding them from the count is safe only while they stay short, hence the one
note. GitHub's spec does not formally describe footnotes, but leaving them is a text edit.

## Consequences

- Enforced in review, as 0009 is.
- Follow-ups, each its own PR: `skill-versioning`'s SemVer link becomes a footnote; `review` rule 1
  credits Nelson via Cuban, with the longer note in an essay.
- A library-wide decision is found by no skill's glob, so an agent adding a citation will not meet
  this record unless pointed to it. Open.
