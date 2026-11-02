# Lessons from the first reviews with skill-review

This is for whoever revises the `skill-review` skill next. It says what the skill must do, what each
rule rests on, and what is still unsettled. The evidence is thin: three reviews of two real
skills on 2026-11-01, and six reviews of one planted skill on 2026-11-02.

## What the skill must do

Using this skill, a reviewer can tell whether a skill improves what an agent does, and where it does
harm, from evidence someone else could rerun. A skill can pass this repo's format checks and
still fail that, so reading alone doesn't meet the goal.

The owner asked for this skill on 2026-11-01. The agent writing it proposed that it sit in this
library beside `review` and add to it, rather than replace it.

## Where the rules came from

The first draft came from a review of [`operate`](https://github.com/cobarx/sysadmin-skills/pull/5),
a skill in another library that fits each action on a machine to the situation. The review's most
useful findings came from running the skill:

- **Loading on the wrong task:** `operate` loaded on "run the tests in this project" in 2 of 2 runs,
  and its cleanup rule then added cache-avoiding flags to the test command. Its demo had no task
  where it shouldn't load. Rule 3 comes from this.
- **Run conditions:** `--setting-sources project` left the user's global instructions in place, and
  the skill's reference files couldn't be read without `--add-dir`. Neither showed in the answer.
  Rule 5 comes from this.
- **Loopholes:** "at most two steps" was obeyed by one step that ran six commands in one run, and by
  two steps that ran six in total in another. Rule 6 comes from this.
- **Its own rules:** the skill says "never from memory", while its PR says the non-Linux commands
  came "from knowledge". Rule 7 comes from this.
- **Facts:** a FreeBSD claim held only from version 15.0, and a claim offered as a correction was
  contradicted by systemd's own man pages. Rule 8 comes from this.
- **Merge result:** `plugin.json` merged with no conflict at a version the main branch had already
  released. Rule 9 comes from this.

## What a side-by-side review changed

Two reviewers then reviewed [`organize-project`](https://github.com/cobarx/sysadmin-skills/pull/21):
one with `review` and the draft, one with `review` alone. Each was limited to two tasks. Because
this is one comparison of one target, it shows what can differ, not how often.

| What each reviewer did or found | With the draft | `review` alone |
|---|---|---|
| Ran the same task with and without the skill | Yes, 2 of 2 each way | No, skill only |
| Runs free of global instructions | Yes, by the logs | No, and it said so |
| Tried a task the skill shouldn't load for | Yes: it loaded in 1 of 2 runs | No: judged its loading correct from two prompts |
| Combining a move and edits in one commit loses a script's history | Found, by running a plan on a copy | Not found |
| `organize-project`'s rule 8 contradicts the table in its `layouts.md` | **Missed** | Found |
| The source map in the skill's spec is wrong, because `uname -s` doesn't cover Windows | Found | Found |

The draft reviewer spent its effort on runs and passed over the contradiction that a careful read
finds, which is why rule 7 now says to compare rules with reference files. That reviewer's own notes led
to the other changes:

- Rule 3 now asks for more than one run, because loading varied.
- Rule 4 is new, because the demo's gaps were the most productive places to look.
- Rule 6 now asks the reviewer to mark whether a run used a loophole or it was only reasoned.
- Rule 8 now covers the reasons rules give and whether examples cover every platform, because the
  draft's wording, "unusual claims", nearly led the reviewer to skip its two best factual findings.
- Rule 9 now asks the reviewer to confirm the commit, because a local `main` was behind and lacked
  the skill entirely.

## How the current text has been tested

The description was tested with three prompts, three runs each, with global instructions excluded.
It loaded on a question about whether a teammate's skill was good (3 of 3), and stayed out of a
review of a code PR (0 of 3) and a request to write a new skill (0 of 3). The first run of each prompt
used the first draft of the rules and the other two used the current text; the description is the
same in both. These runs had no shell, so they test loading and not the full procedure.

On 2026-11-02 the wording of the rules, the reference and this file changed for a general reader,
after a review against `writing-style` and `writing-structure`. The description changed too, so the
same three prompts were rerun three times each, with the same results (3 of 3, 0 of 3, 0 of 3). An
agent given only SKILL.md then said what each rule told it to do, and its accounts matched the
intended meaning. That agent stands in for a new reader, and no person has done this reading yet.

The review of `operate` saw a run try to get a shell through a subagent, without saying whether that
worked, so the same day this was tested on Claude Code 2.1.310. Under `--disallowedTools Bash`, a
general-purpose subagent asked to run `touch` had no Bash tool in 4 of 4 runs, 2 of them with that
command also allowed by `--allowedTools`. Without the flag and with the command allowed, a subagent
ran it (1 of 1), so the flag is what stopped it. Other kinds of subagent were not tried.

The retest below is the first review to use the rule changes listed above.

## Why rules must say what to do

Reading rules 4, 5 and 6 on 2026-11-02, the owner found that "we are adding clarifying language rather
than affirmative, testable statements", and that `skill-review` could flag such a rule as one that
can't be accepted. So rule 10 is new, and rules 1 to 7 were rewritten to meet it in one quick pass,
which took them from 442 words to about 376. The owner chose to merge this first pass and refine it
later.

The owner then pointed out that many rules checked something without saying what happens to the
result. So each rule now says what makes the skill fail, and rule 11 requires every failure to be
fixed before merge (the owner's call, 2026-11-02).

The owner also wants this caught while a rule is being written as well as in review. For now it is a
convention in AGENTS.md; in the long term it belongs in a skill for writing skills. Whether examples
and reasons need more allowance than rule 10 gives is still open.

A separate trial of a rule against needless words made these rules longer, not shorter (557 words to
about 638), which is part of why the fix here is a test for each sentence and not a rule on length.

## The retest of 2026-11-02

**Result:** reviewers with the skill found no more of the planted defects than reviewers without it,
apart from one loophole. What the skill changed is how they reviewed, at several times the cost. It
also showed a gap in rule 3.

Six reviewers (Opus 5.5, `high` effort) reviewed `tidy`, a synthetic skill with eight planted defects,
as a teammate's PR. Three had `review` and `skill-review`, and three had `review` alone. All six said
not to merge. The agent that wrote these rules also planted the defects and scored the answers, not
blind, so a defect that fits a rule is no surprise. This shows what can differ, not how often.

| Planted defect | With the skill (3) | Without it (3) |
|---|---|---|
| Description so broad it loads on code work | 3, by measuring: loaded in 15 of 15 runs | 3, by reading |
| Breaks its own citation rule | 3 | 3 |
| Rule contradicts a reference file | 3 | 3 |
| False claim about `mv -n` | 3 | 3 |
| False claim about `ls -S` | 3 | 3 |
| "At most two moves" obeyed by moving whole directories | 1, and 1 found a related loophole in a run | 0: all 3 only questioned the limit |
| Sentence that says nothing to do | 3, as something to fix | 3, as a minor note on a weak reason |
| `stat -c` doesn't fit the macOS claim | 3, blocked or from memory | 3, blocked or from memory |

These differences did not depend on the planted defects:

- **Whether the skill helps:** all three with the skill ran the same tasks with and without it (25, 18
  and 37 runs). Without the skill, the reviewers that ran agents ran them only with `tidy` loaded, so
  they couldn't say whether it helped. One found that asking before deleting clearly helps, and another
  that the skill made one task worse.
- **Report:** those with the skill gave a verdict for each rule, and stated run counts.
- **Cost:** $0.54 to $1.41 a review without the skill. With it, $1.55 to $1.92 for the session plus its
  runs, which are billed separately. The one review that stated its run costs came to $6.81 in all.

What the retest showed about `skill-review` itself:

- **Rule 3 lets a wrongly loading skill pass.** `tidy` loaded in every run of tasks it should stay out
  of, and all three reviewers passed that rule because the answers weren't worse. One said it "isn't a
  failure under the review rules".
- **Rule 11 was reported as a failure of the skill under review.** Two reviewers listed it as "Fail"
  because the failures were still open. This is harmless.
- **Reference claim questioned, and it held.** One reviewer doubted that `--setting-sources project`
  alone leaves the global file in place, from one Haiku run. Rerun on Claude Code 2.1.310, asking the
  agent whether it could see that file's rules: seen in 6 of 6 runs with the flag alone (Opus and
  Haiku), 0 of 6 with `claudeMdExcludes` added, and 3 of 3 with user settings on as a control.

Not tested:

- **Rule 9,** because the fixture had no commits or remote, so it came back blocked or untested.
- **The macOS claim,** because no reviewer had a Mac and the test setup refused `WebFetch`, so nobody
  could confirm it.
- **False findings,** which were not counted.
- **A real skill, another model or a lower effort.**

## Open questions

These are unsettled, and each could change a rule.

- **Is there a limit on a description's length?** `operate`'s 782 characters stood out against this
  library's longest description, at 516, but no written standard exists.
- **How should a reference say when to load it?** All four of `operate`'s references were read at
  once in two runs, for a question that needed one or two. "On demand" doesn't say how to write that
  condition, and `simplicity` and `steward` (in the stewardship-skills library) do it differently.
- **Does a small change need a run at all?** Rewording a rule may not justify the cost: each of these
  reviews took several minutes and over 100,000 tokens.
- **Does this work with agents other than Claude Code?** The reference gives commands for one agent
  only.
