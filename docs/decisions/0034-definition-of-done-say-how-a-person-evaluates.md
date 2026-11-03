# 0034. `definition-of-done`: say how a person evaluates the output

- **Status:** Accepted
- **Decided:** 2026-11-02 (#168) · **Recorded:** 2026-11-02 · Claude Opus 5.5
- **Affects:** `definition-of-done`

## Context

Rule 1 shows what the author saw, and `review` rule 3 tells the reviewer to verify by use. Nothing
told the author how to let a reader judge the output. On 2026-11-02 the owner, reviewing a scaffold
PR with a complete evidence section, had to ask how to run it. Their first rule was "every pr must
contain testing instructions", which they refined the same day: "in some cases (docs for example)
there won't be anything to test. however the general principle was, how can a human evaluate the
output of what's generated".

## Options

- **"Testing instructions in every PR."** Solves reproducing code. Rejected: it fails on docs, and
  on outputs that are not PRs, such as a report or a physical part.
- **A PR template in each repo.** Solves the reminder. Rejected: each repo needs its own copy, and
  the skills are what travel between projects. A repo can still add one.
- **Extend rule 5.** Fewer lines. Rejected: rule 5 is about the form of the artifact, so one rule
  would carry two ideas.
- **A rule in `review`.** Rejected: the author is the one who knows how.
- **A new rule in `definition-of-done`, naming the docs case:** "Give the reviewer the steps to
  reach the output and what to look for. A change with nothing to run names what to read and what
  to judge." Rejected: longer, and it is written around running things, which is the narrowness
  the owner was correcting.
- **A new rule in `definition-of-done`, stated generally.** Where the output is, what to do with
  it, and what good looks like. For a document, what to do with it is to read it.

## Decision

The general rule, placed after rule 5, chosen by the owner between the last two options. It reads:
"Say how a person evaluates it. Tell the reader where the output is, what to do with it, and what
good looks like. Try that yourself first, or say you couldn't."

## Consequences

- Rules 6 to 8 become 7 to 9. Nothing in `skills/`, `docs/`, `README.md` or `AGENTS.md` cites those
  three by number; 0009 cites rule 5, which does not move.
- Every PR gains some text. Rule 9 (scale the proof) keeps it short: a rename's evaluation is one
  line.
- Revisit if PR bodies grow without readers using the section, or if evals show the rule changes
  nothing agents write.
