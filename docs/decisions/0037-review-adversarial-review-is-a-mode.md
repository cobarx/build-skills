# 0037. `review`: adversarial review is a mode with two passes and a blind critic

- **Status:** Accepted. Extends [0007](0007-review-adversarial-stance-is-not-a-skill.md). The
  runtime test is pending.
- **Decided:** 2026-11-02 · **Recorded:** 2026-11-02 · deepseek-flash[1m]
- **Affects:** `review`

## Context

0007 rejected a separate skill for the adversarial stance: a stance with no procedure of its own is
not a skill. It left the stance inside the skills that act, and `review` later took the
independent-critic role. What `review` still lacked was a procedure for the explicitly invoked mode:
when it runs, how the critic stays independent of the author's framing, and how a design pass
differs from a pass over the diff.

The note in [docs/context/planned-skills.md](../context/planned-skills.md) asked for that mode. It
described two passes, at design and after implementation, and said the implementation pass runs
before the author's own review or it anchors on the author's framing.

Searched (`adopting-standards` rule 1), on 2026-11-02: red-team review, the premortem, and
adversarial collaboration. The mode adopts the adversary stance and the premortem's prospective
hindsight. It leaves out the multi-agent panels and tooling the search also turned up, because the
existing `review` skill and `simplicity` make that machinery unnecessary. The sources are in the
footnotes.

## Options

- **A new skill for adversarial review.** Rejected: it duplicates `review` and reopens 0007. The
  stance still has no procedure that is not a way to review.
- **A mode of `review`.** Chosen: the procedure belongs where the critic role already lives, and
  every project that installs the library gets it.
- **A repo-only rule in `AGENTS.md`.** Rejected: the procedure is portable, and the library is the
  product.
- **The status quo.** Rejected: the planned-skills note asked for the mode, and self-review has a
  ceiling that a blind critic is meant to lower.

## Decision

Adversarial review is an explicitly invoked mode of `review`. It has two passes: a design pass
before the build, and a diff pass after it. The critic is not the author, runs in a fresh context,
and does not see the author's summary or self-review before writing findings. Every finding needs a
reproduction, and every check the critic cannot run is `blocked` rather than passed. The author
fixes; the critic rechecks the same record.

The mode runs when the owner asks for it, or when a change adds or changes a skill, changes a public
contract, makes a one-way-door decision, or touches security-sensitive code. It is skipped for
typos, formatting, renames, mechanical refactors, and docs-only edits. The rule and the procedure
are in `skills/review/SKILL.md` and `skills/review/references/adversarial-review.md`.

## Consequences

- `review` gains a rule and a reference. The library version moves by a minor bump, since the
  change adds a rule without changing how the skill loads.
- The runtime test of the new mode is pending. The owner asked for the implementation before the
  test run, so this PR is the first candidate. `skill-review` rules 2 to 5 need runs with and
  without the skill; the owner plans to run it before the PR merges. Until then, the change's
  behavioral claim is unproven.
- If the mode produces mostly preferences or false positives, narrow the triggers or drop it. A
  critic that cannot see enough context is the first thing to fix, not the last.
- 0007 stays accepted. This record extends it; it does not supersede it.

[^redteam]: GDI Consulting, "Red Team Reviews – Part I",
    <https://www.gdicwins.com/proposalwriting/red-team-reviews-part-1/>.
[^premortem]: Gary Klein, "Performing a Project Premortem," *Harvard Business Review*, September
    2007, copy at
    <https://www.boyden.com/media/performing-a-project-premortem/img/performing-a-project-premortem.pdf>.
[^collaboration]: Daniel Kahneman, "Adversarial Collaboration: An EDGE Lecture," Association for
    Psychological Science, <https://www.psychologicalscience.org/news/adversarial-collaboration-an-edge-lecture-by-daniel-kahneman.html>.
