# Lessons from the first reviews with skill-review

This is for whoever revises the `skill-review` skill next. It says what the skill must do, what each
rule rests on, and what is still unsettled. The evidence is thin: three reviews, on 2026-11-01, of
two skills.

## What the skill must do

A reviewer can tell whether a skill will change what an agent does for the better, including where
it does harm, from evidence someone else could rerun. A skill can pass this repo's format checks and
still fail that, so reading alone doesn't meet the goal.

The skill belongs in this library beside `review` and adds to it, rather than replacing it
(confirmed 2026-11-01).

## Where the rules came from

The first draft came from a review of [`operate`](https://github.com/cobarx/sysadmin-skills/pull/5),
a skill in another library. Its most useful findings came from running the skill:

- **Wrong load:** `operate` loaded on "run the tests in this project" in 2 of 2 runs, and its cleanup
  rule then added cache-avoiding flags to the test command. Its demo had no task where it shouldn't
  fire. This is rule 3.
- **Run conditions:** `--setting-sources project` left the user's global instructions in place, and
  the skill's reference files couldn't be read without `--add-dir`. Neither showed in the answer.
  This is rule 5.
- **Loopholes:** "at most two steps" was obeyed by one step holding six commands. This is rule 6.
- **Its own rules:** the skill says "never from memory", while its PR says the non-Linux commands
  came from knowledge. This is rule 7.
- **Facts:** a FreeBSD claim held only from version 15.0, and a claim offered as a correction was
  contradicted by systemd's own man pages. This is rule 8.
- **Merge result:** `plugin.json` merged with no conflict at a version the main branch had already
  released. This is rule 9.

## What the comparison changed

Two reviewers then reviewed [`organize-project`](https://github.com/cobarx/sysadmin-skills/pull/21):
one with `review` and the draft, one with `review` alone. Each was limited to two scenarios. Because
this is one comparison of one target, it shows what can differ, not how often.

| Finding | With the draft | `review` alone |
|---|---|---|
| Ran the same task with and without the skill | Yes, 2 of 2 each way | No, skill only |
| Runs free of global instructions | Yes, by the logs | No, and it said so |
| Tried a task where the skill shouldn't fire | Yes: it loaded in 1 of 2 runs | No: passed triggering on two prompts |
| Combining a move and edits in one commit loses a script's history | Found, by running a plan on a copy | Not found |
| Rule 8 contradicts the table in `layouts.md` | **Missed** | Found |
| Spec's source map wrong, `uname -s` doesn't cover Windows | Found | Found |

The draft reviewer spent its effort on runs and passed over the contradiction that a careful read
finds, which is why rule 7 now says to read rules against references. That reviewer's own notes led
to the other changes:

- Rule 3 now asks for more than one run, because loading varied.
- Rule 4 is new, because the demo's gaps were the most productive places to look.
- Rule 6 now asks the reviewer to mark loopholes as seen or argued.
- Rule 8 now covers the reasons rules give and whether examples cover every platform, because the
  draft's "unusual claims" nearly steered the reviewer past both of its best factual findings.
- Rule 9 now asks the reviewer to confirm the commit, because a local `main` was behind and lacked
  the skill entirely.

## How the current text has been tested

The description was tested with three prompts, three runs each, with global instructions excluded.
It loaded on a question about whether a teammate's skill was good (3 of 3), and stayed out of a
review of a code PR (0 of 3) and a request to write a new skill (0 of 3). The first run of each prompt
used the first draft of the rules and the other two used the current text; the description is the
same in both. These runs had no shell, so they test loading and not the full procedure.

The rule changes listed above have **not** been tested by another review.

## Open questions

- **Is there a limit on a description's length?** `operate`'s 782 characters stood out against this
  library's maximum of 516, but no written standard exists.
- **How should a reference say when to load it?** All four of `operate`'s references were read at
  once in two runs, for a question that needed one or two. "On demand" doesn't say how to write that
  condition, and `simplicity` and `steward` do it differently.
- **Does a small change need a run at all?** Rewording a rule may not justify the cost: each of these
  reviews took several minutes and over 100,000 tokens.
- **Does this outlive Claude Code?** The reference gives commands for one agent only.
