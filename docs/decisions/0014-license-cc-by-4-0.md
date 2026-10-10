# 0014. License the text under CC BY 4.0; code takes a software licence

- **Status:** Accepted. Scope amended by [0029](0029-third-party-images-keep-their-own-licence.md).
- **Decided:** 2026-10-04 · **Recorded:** 2026-09-28 · Claude Opus 5.5
- **Affects:** every file; how others credit what they copy or adapt

## Context

The repo is being prepared for release and has no licence, so no one may legally reuse it. It is
all Markdown and JSON today; an evals suite with scripts is in progress.

The choice was worked through on 2026-09-25, in the owner's working notes. What decided it:

- **A licence governs copies of the text, not the practice.** Ideas and methods are not
  copyrightable (17 U.S.C. §102(b)), so anyone who rewrites a skill in their own words owes
  nothing under any licence. Copyleft has little to hold in a skill.
- **Credit is pursued apart from the licence.** The owner wants to
  "establish derivation by citation," but most reuse is a borrowed idea or an agent following a
  skill, which no licence reaches. Citation is a norm, and how to encourage it is
  [#63](https://github.com/cobarx/build-skills-cobarx/issues/63). For the copies a licence does
  reach, CC BY §3(a) requires credit, a link to the source, and a note of changes, and the cure
  period (§6(b)) makes asking for them a correction, not a threat. MIT and BSD require only a
  pasted notice, with no link back.
- **Adopters should not need a licence review.** The first planned adopters are a corporate team.
  ShareAlike is the term that draws review: skillboss-dojo moved its skills from BY-SA to
  Apache-2.0 so that "can I use this at work?" is a yes "with no clause to reason about"
  ([mazzyst/skillboss-dojo#13](https://github.com/mazzyst/skillboss-dojo/pull/13)).
- **Creative Commons does not recommend its licences for software.** They say nothing of source
  code or patents.

## Options

- **AGPL, with a CLA.** Buys friction and no protection for a method; no skills repository
  surveyed uses it.
- **MIT or Apache-2.0.** The ecosystem's usual choice for skills. Treats a skill as a software
  component; credit is a notice, not a citation.
- **CC BY-SA 4.0.** Keeps every public adaptation under the same terms. Its reach is narrow:
  private use and borrowed ideas owe nothing, and an unmodified copy only keeps its notice. It
  lost on two costs that documentation cannot remove: a closed product cannot ship a modified
  skill, and blanket copyleft policies and licence scanners stop it before anyone reads its
  scope. Weighed in [#55](https://github.com/cobarx/build-skills-cobarx/issues/55).
- **CC BY 4.0.**

## Decision

CC BY 4.0 for the skills and documentation, copyright Hampton Maxwell. The evals take a software
licence, settled in a decision of their own.

`LICENSE` is the verbatim legal code from creativecommons.org. `plugin.json` declares `CC-BY-4.0`,
its SPDX identifier. The README says how to credit a skill: title, author, source, licence, and
what was changed (Creative Commons' TASL, plus §3(a)'s note of changes).

## Consequences

- The licence is irrevocable for any copy already shared. Going public is the one-way door; adding
  the licence to a private repo is not.
- Moving to BY-SA later stays possible, for future releases only: copies released under BY stay
  BY, and a fork of the last BY release may close its changes. Outside contributions do not block
  the move, since BY material may go into a BY-SA work.
- Much of this repo was written by agents. Text without human authorship may not be copyrightable
  (US Copyright Office, *Copyright and Artificial Intelligence, Part 2*, 2025), which limits what
  attribution can bind. The owner's selection, arrangement, and edits remain protected.
- Skills do not yet carry the licence in their frontmatter (the Agent Skills spec's `license`
  field). A skill copied out of the repo carries no notice until they do. Open.
