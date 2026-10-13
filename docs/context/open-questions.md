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

## Candidates from a LaptopPad session (2026-10-09)

From designing a laptop pad (`Projects/Hardware/LaptopPad`) and tuning Dota 2 on the same laptop.
The owner agreed 1 to 4 should be drafted as skill changes; 5 waits for more data; 6 is the
owner's rule and needs a home.

1. **One folder per design revision** (`durable-context`). Renders and mockups go in
   `artifacts/<subject>/revN/`, indexed by a README section per revision. Generator scripts hold
   only the current design, so the images are the history. Owner's request when the folder got
   cluttered. Refined the same day: superseded revisions move to `archive/` (still indexed), so
   only current work sits at the top.
2. **Every revision reports its own requirement checks** (`definition-of-done`). The mockup script
   prints clearance, envelope fit and tip-over force on every render. Rev 3 looked right and put
   the laptop's feet on the pad; only the printed check caught it.
3. **Primary sources over project docs** (`platform-correctness`). A project doc said gamescope's
   `-s` was sharpness; the tool's own help said mouse sensitivity, which was the root cause being
   chased. Owner's rule: always go back to the primary source; the man page usually beats
   `--help` for detail. A project doc or memory describing a tool is a claim to check against it.
   Only when the man page or help is wrong (exceedingly rare) or ambiguous does testing the
   behaviour or reading the source decide. The same holds for APIs: check the provider's own
   reference docs, not our summary of them or docs generated from them, unless no primary source
   exists.
4. **Check the owner's named mechanism against their goal** (an example for `spec`). The owner
   asked for metal-to-metal contact to move heat; bare contact conducts worse than a thin thermal
   pad. The goal held and the mechanism changed.
5. **Fair A/B tests: equal starting state, alternating order, say what a stand-in can't
   reproduce.** One example so far (a tablet standing in for the pad, whose 60s run started 10°C
   cooler than the baseline and soaked heat into its own mass). Needs more cases before it
   generalises, and has no obvious home.
6. **Confirm the setup with the person before every interactive test run.** Owner's rule. When a
   person sets up the physical conditions (hardware placement, power, what's plugged in), state the
   setup and wait for their OK before each run; never assume it carried over from an earlier
   message or session. An agent started a run assuming a tablet was still under the laptop from the
   night before; it wasn't, and the run was stopped and discarded. Home not decided: it is an
   event-triggered check like `spec`'s, but about test execution rather than the goal.

## Stranded elsewhere

Research for the **playhead** project, including the caption test corpus (Sintel's ~40 languages,
`w3c/imsc-tests` with PNG reference renderings, the real-versus-synthetic fixture split, and the
caution against vendoring OpenSubtitles), currently exists only in the session plan file at
`~/.claude/plans/`. It belongs in `~/code/playhead/docs/` and should be moved there when that
project is next picked up.
