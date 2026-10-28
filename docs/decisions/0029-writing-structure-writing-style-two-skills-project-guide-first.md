# 0029. Writing is two skills, and the project's own guide comes first

- **Status:** Accepted
- **Decided:** 2026-10-26 · **Recorded:** 2026-10-26 · Claude Opus 5.5
- **Affects:** `writing-structure` (new), `writing-style` (new, in its own PR)

## Context

In a sysadmin-skills session the owner reviewed a document an agent had written (a list of
lessons from solved troubleshooting cases, sysadmin-skills#7) and found it hard to use. His
corrections, in order: a line "doesn't read like english"; nothing connected the header to the
list, so "it's not even clear what the findings are"; the items were called findings "when really
these are lessons. If you approach it that way, you may see that it shapes the doc"; and the way to
write is to "start with end goals in mind and then work backwards," so that "you are filling in
details that help you arrive at the conclusion rather than just throwing information at the
problem." Rebuilt around what its reader would do with it, the document worked.

No skill covered this. The repo's skills govern code, specs and records; the closest, `essays`,
says writing an essay well "is a wider skill than this." sysadmin-skills had just added a "Writing
for readers" section to its AGENTS.md, but that reaches only one repo.

Two constraints came from the owner. Skills travel with the person, not the repo: "I'm going to be
using build skills with other people's repos where they aren't using it," and someone may clone a
repo of his without build-skills. And he separated two things: skills "that help shape how I
contribute documentation and PR descriptions," and "standards or best practices that are going to
define what docs should look like in a given repo."

Searched (`adopting-standards` rule 1), on 2026-10-26: classic style guides (Strunk 1920, Strunk &
White, Orwell, Williams, Zinsser, with Pullum's critique), structure methods (Covey's Habit 2,
Minto, BLUF in AR 25-50, the inverted pyramid, Diátaxis, DITA, minimalism), plain-language
standards (ISO 24495-1, the Federal Plain Language Guidelines), the Google and Microsoft developer
style guides, conventions for commits, PRs, issues and READMEs, and documented failure modes of AI
prose. The research is in [docs/context/writing-research.md](../context/writing-research.md).

## Options

- **One writing skill.** Most single-volume guides cover sentences and documents together. But
  its purpose needs an "and" (order the document and write the sentences), and the candidate rules
  for both fill well over seventy lines.
- **Two skills, structure and style.** Williams draws this line himself (*Style*, Part Two,
  "Clarity", for sentences; Part Three, "Clarity of Form", for whole documents), as do the Federal
  Plain Language Guidelines ("Organize" apart from "Write your document"). The failures split the
  same way: a bare list under a heading is structure, clipped phrasing is style. Each loads when
  its own work happens.
- **`organize`** (another library, for READMEs and project layout). Rejected by the owner: "a more
  specific skill that's tuned to writing is probably going to produce better results."
- **Rules in each repo's agent instructions only.** Reaches no repo the owner contributes to but
  does not own.

## Decision

Two peer skills, `writing-structure` and `writing-style`. Point-first belongs to structure at the
scale of a document, section and paragraph; within a sentence, word and punctuation choices belong
to style. Each names the other under "Not here".

**Rule 1 of each is precedence, adopted from Google's style guide** (CC BY 4.0): "Follow style
guidance specific to your project or product. ... If project-specific style guidelines don't provide
explicit guidance, then follow this guide," and "Depart from it when doing so improves your
content." Adapted in one way, which is ours and not Google's: a project's visible conventions (its
existing docs, its `git log`, per the git project's SubmittingPatches) count as its guidance. This
is what lets the skills travel: in a repo with its own standard they fill gaps, and the owner's
personal preferences (no em dashes, for one) stay in his own agent instructions, not in the skills.

**Only rules the owner holds with confidence are adopted now.** He asked to "adopt the things that
I have high confidence in, and then do some tests with the other ideas." The classic sentence
rules (active voice as a default, omitting needless words, positive form, concrete language,
characters as subjects, old information before new) are held for testing;
active voice in particular is not always better, by Pullum's and Williams's evidence. Conventions
for specific artifacts (commit messages, PR descriptions, issues, READMEs) are held for the same
issue, [#159](https://github.com/cobarx/build-skills/issues/159).

**Standing on its own (structure rule 7) has no exception for readers who were there.** Asked
about a commit message written with and without the session's context, the owner noted that the
participants may not need the context stated, "however, the second one still reads better even if
you do have the context," and a writer can't tell where the text will be read: "are you squashed
and merging or relying on the PR description or relying on the commit log? ... So generalizing to
the more complete case is probably better."

Each rule cites its source in a footnote (0013). In the skills, text from public-domain, CC0 and
CC BY sources is quoted, and share-alike and in-copyright sources (Diátaxis, Minto, Covey, Strunk &
White, Williams) are paraphrased and credited. Essays and decisions may quote a short passage from
an in-copyright source, attributed.

## Consequences

- A repo that wants its own writing standard keeps it in its own files; these skills defer to it.
  sysadmin-skills keeps its "Writing for readers" section for readers without build-skills.
- Both skills rest on one session's corrections plus converged published guidance, with no evals
  yet. [#159](https://github.com/cobarx/build-skills/issues/159) covers evals along with the held
  style rules.
- How build-skills as a whole should behave in a repo that has not adopted it is wider than
  writing, and is its own open issue,
  [#160](https://github.com/cobarx/build-skills/issues/160).
