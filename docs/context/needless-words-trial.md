# Trial: a rule against needless words

Working results for [#159](https://github.com/cobarx/build-skills/issues/159), run 2026-11-02. Not a
decision yet: the owner judges the blind samples first.

## Result so far

The candidate rule cut words by 14% on average, and a second agent proposing cuts took that to 21%.
No lost critical fact was found in any arm, although that check is weak (see below). Whether the shorter text takes less effort to
understand is the owner's concern, and only his reading of the
[blind samples](needless-words-test/blind-samples.md) can answer that.

## What was tested

Five documents, each written three times in each of three arms, by `claude-opus-5-5` at `medium`, with
global instructions excluded and no tools. A probe confirmed that the global instructions were absent.

- **Baseline:** `writing-structure` and `writing-style`, as merged.
- **Rule:** the same, plus [the candidate rule](needless-words-test/rule.md).
- **Rule and review:** the same as the rule arm, and then a second agent proposed cuts, all of which
  were applied without further judgement.

The briefs are in [briefs.json](needless-words-test/briefs.json). They are written by hand from real
material in this repo, so they are synthetic in form, and each lists the facts a reader must get.
To repeat the trial, run `run.py` and then `regrade.py` from that directory.

## Results

| Document | Baseline words (3 runs) | Rule | Rule and review | Change with rule | Change with review |
|---|---|---|---|---|---|
| Skill rule | 103, 90, 90 | 85, 72, 88 | 64, 73, 61 | -13% | -30% |
| Commit message | 102, 109, 95 | 84, 86, 84 | 85, 86, 92 | -17% | -14% |
| PR description | 178, 173, 194 | 147, 150, 166 | 136, 139, 121 | -15% | -27% |
| README section | 186, 189, 174 | 156, 176, 161 | 124, 151, 157 | -10% | -21% |
| Doc page | 334, 323, 365 | 327, 263, 277 | 245, 306, 314 | -15% | -15% |
| Mean of the changes | | | | -14% | -21% |

**Facts kept.** Every fact the grader reported missing turned out to be present when read by hand.

The LLM grade can't be relied on, so it doesn't support this result. `claude-sonnet-5-5` is only a
candidate judge (0018), and here it misbehaved: one known-good control went all false on some repeats,
even with three votes (commit message, 0 of 6), and 9 of 45 documents had a split vote. Its known-bad
controls behaved, at 0 every time. Under 0017, a result counts only when both controls behave, so the
scores in `results.json` are recorded but not used.

The grader's misses after three votes were read by hand:

| Document | Arm | Reported missing | By reading |
|---|---|---|---|
| Skill rule, run 2 | Rule | Confirm before trusting; the log is where | Present: "Check each run's log before believing the run" |
| Doc page, run 1 | Baseline | New directory; `claudeMdExcludes` reason | Both present |
| Doc page, runs 2 and 3 | Baseline | New directory | Present: "Create a new throwaway directory that holds only what the task needs" |
| Doc page, run 2 | Rule | New directory | Present, same sentence |
| Doc page, run 3 | Rule and review | New directory | Present, except that it says "throwaway" and not "new" |

The documents the grader passed were not all read by hand, so a fact it wrongly passed could be
missing.

## What this doesn't show

- **Effort:** word count is a stand-in for the owner's measure, which is how much effort it takes a
  person to fully understand the text. That is what the blind samples are for.
- **The review arm's cuts** were applied without judgement, so a real author could keep or reject each.
- **Size:** three runs of five short documents, by one model at one effort. Other rules in #159
  weren't tested, and neither was the rule's effect when loaded as a skill instead of supplied directly.
- **The self-check alone:** the candidate combines "ask of each word" with the list of kinds of word,
  so this trial can't say which part did the work.

## Second round: skill rules (2026-11-02)

The owner pointed out that the documents above are too long to compare and aren't what the rule is
for, so `rules_trial.py` rewrote each of `skill-review`'s nine rules under the candidate rule, keeping
their meaning. The result went the other way: the nine rules total 557 words now, about 638 rewritten
under the rule (up 14%), and about 585 after a second agent's cuts (up 5%). The prompt asked for
understanding with the least effort, which may have encouraged adding words.

The owner's reading of rules 4, 5 and 6 (versions in `rules-out.json`, key in `rules-key.json`):

- **Rule 4:** "the ones is hard to decipher. i'm not sure i understand the rule here. what are we
  trying to find"
- **Rule 5:** "Z is good, up to the last line, where normal implies a standard that's not clear"
- **Rule 6:** "such a way. this sentence is a terrible starter. it highlights perhaps another issue
  with our rules. we are adding clarifying language rather than affirmative, testable statements"
