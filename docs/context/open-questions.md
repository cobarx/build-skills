# Open questions

Unsettled. Moved here out of conversation so it survives.

## This repo

**The five thresholds in `simplicity` are borrowed, not chosen.** Cognitive complexity 15, nesting
depth 3, function 50 lines, file 300 lines, parameters 4. These are common SonarJS and ESLint
defaults. They are plausible and unconfirmed, and presenting them as settled is fake precision.

**`docs/essays/` is a coinage.** There is no strong industry term for a post-hoc narrative about
why a practice exists. Oxide's RFDs are the closest published model but are pre-decision. Recorded
as ours per the vocabulary rule, and open to a better name.

**No linting or formatting configured in this repo yet.** A skills repo that preaches lint-from-day-one
and ships without it is its own counterexample. Markdown is the only file type here, so the
question is whether non-code linting counts, which is itself an open question below.

**Do Deming's successors carry his 14 points?** TQM, Lean, Six Sigma and ISO 9000/9001, compared
point by point. Raised in review of #110. An unfinished draft in
[deming-points-in-successors.md](deming-points-in-successors.md); the proper analysis is #115.

## For `linting`, before it can be written

**How is a linter chosen for a stack?** Settled as an ordered procedure, kept here because it was
agreed and the tool examples still need verifying before they go in the skill:

1. Does the toolchain ship one? If yes that is the answer, unless step 3 disqualifies it.
2. Has the ecosystem converged? Take the dominant tool, not the best one.
3. Can it express the rules our skills require? The only disqualifying check.
4. Fast enough to run on save? Tie-breaker.
5. Escape hatch for a custom rule? Tie-breaker.

Two rule names verified rather than recalled, since they are what make `naming` enforceable:
[`@typescript-eslint/naming-convention`](https://typescript-eslint.io/rules/naming-convention/)
takes `custom: { regex, match }`, and [`id-denylist`](https://eslint.org/docs/latest/rules/id-denylist)
bans generic identifiers by name.

**Does non-code linting belong in scope?** Markdown, YAML, shell. Real, but arguably a different
concern from code quality gates, and including it starts the scope creep this skill is most
vulnerable to.

**How does lint run locally?** Rule 6 of the draft says local and CI share a config, but not *how*
local runs. Pre-commit hook versus editor integration versus a watch task is a tooling choice, and
naming one felt like policy rather than mechanism.

**Should waivers expire?** MetanoiaFramework's `feature-flags` has review-by dates. The same idea
could stop an inline disable outliving its reason. Probably over-engineering for solo work, but it
is the kind of thing that rots quietly.

## Method

**Does "draft long, then keep only what is a rule" need a home of its own?** It generalises past
skill authoring to specs, docs, and any distillation task. Currently it lives only in
`docs/essays/outline-is-the-skill.md` and in `AGENTS.md` as a convention.

**How much proof is enough?** `definition-of-done` says to check every dimension and to scale the
proof to the blast radius. "Exhaustive" and "proportionate" pull against each other, and the line is
not yet drawn. Raised in `docs/essays/define-what-good-looks-like.md`.

**Is survey-then-dive a real pattern**, or an artifact of one probe? Survey first is cheap and
tells you which dive is worth doing, but that is one data point. Raised in
`docs/essays/simplicity-is-not-size.md`.

**Do skills still load deep in a long session?** In a fresh session `spec` loads when handed a
choice (3/3), but in a long CampaignStop session it did not, at the same kind of moment. A
fresh-session check can't reproduce that. Testing it needs a replayed long conversation before the
prompt; the fallback is an always-on rule in CLAUDE.md. Raised in 0020; the test and the
decision it feeds are #58.

**Is it depth, or a trigger that arrives mid-conversation?** A second instance, 2026-10-13, in a
short session (twelve brief prompts, small context, a repo unrelated to the work). The talk was
about a web UI bug and a blog post. Hampton said "i think the better approach is to create a chrome
extension to block it", and the agent began building: it opened a browser tab to inspect the page.
`spec` was listed and its "starting a unit of work" trigger matched; it did not load. Depth does not
explain this one. Claude's guess, untested: what the two sessions share is a trigger arriving as a
turn in a running conversation, not as a fresh request. The 0020 check used fresh sessions only; a
replay with a few turns of chat before the prompt would test it. Bears on #58.

**When does talk become a request to build?** From the same session. Hampton's correction: "i did
not tell you to build it. i said that would be a good solution", and "the agent is an assistant. it
recommends and requests." A candidate rule, "An opinion is not an instruction: ask before starting
new work", was added to `spec` rule 3 and taken out again the same day: one instance, and a rule
inside a skill that did not load would not have helped. Its always-on home may be the entry-point
statement of #127. Two limits Hampton set on it: it gates starting work, not finishing it, which is
a separate rule that may not generalise; and work a person has asked to run unattended is already
requested.

Hampton's wider point, which any such rule has to leave room for: a spec is arrived at through
discussion, and the agent is used to research and understand the lay of the land as well as to
build, "like jotting down notes as i'm browsing". Those notes may go through a spec pass later or
never. The flow is not linear, and "it is ok for creativity to wander". Claude's reading: `spec`
rule 2 (explore to find the what) and 0020 already allow a goal built in pieces, but nothing says
that a conversation may stay a conversation, with no spec and no build expected of it. The model
that came out of this, and the loose check built on it, are in
[co-working-session.md](co-working-session.md).

## Stranded elsewhere

Research for the **playhead** project, including the caption test corpus (Sintel's ~40 languages,
`w3c/imsc-tests` with PNG reference renderings, the real-versus-synthetic fixture split, and the
caution against vendoring OpenSubtitles), currently exists only in the session plan file at
`~/.claude/plans/`. It belongs in `~/code/playhead/docs/` and should be moved there when that
project is next picked up.
