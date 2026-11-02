# 0033. `skill-review`: a skill is judged by running it, and a failure stops the merge

- **Status:** Accepted
- **Decided:** 2026-11-02 · **Recorded:** 2026-11-02 · Claude Opus 5.5
- **Affects:** `skill-review`, AGENTS.md

## Context

A skill can pass every rule for how skills are written and still load on the wrong work or change
nothing. Hampton asked for a skill on this on 2026-11-01. The agent writing it proposed that it sit
beside `review` and add to it, because `review` already governs independence, lenses and verdicts.

The first draft came from a review of
[`operate`](https://github.com/cobarx/sysadmin-skills/pull/5), a skill in another library. Its most
useful findings came from running the skill, and each became a rule:

- **Rule 3:** `operate` loaded on "run the tests in this project" in 2 of 2 runs, and its cleanup rule
  added cache-avoiding flags to the test command. Its demo had no task where it shouldn't load.
- **Rule 5:** `--setting-sources project` left the user's global instructions in place, and reference
  files couldn't be read without `--add-dir`. Neither showed in the answer.
- **Rule 6:** "at most two steps" was obeyed by two steps that ran six commands in total.
- **Rule 7:** the skill says "never from memory", while its PR says some commands came "from knowledge".
- **Rule 8:** a FreeBSD claim held only from version 15.0, and a claim offered as a correction was
  contradicted by systemd's own man pages.
- **Rule 9:** `plugin.json` merged with no conflict at a version main had already released.

Two reviewers then reviewed [`organize-project`](https://github.com/cobarx/sysadmin-skills/pull/21),
one with the draft and one with `review` alone, limited to two tasks each. The one with the draft
compared runs with and without the skill, kept global instructions out, found the skill loading where
it shouldn't in 1 of 2 runs, and found that a move and edits in one commit lose a script's history. It
missed a rule that contradicts the skill's `layouts.md`, which the other reviewer found, so rule 7 now
says to compare rules with reference files. Its notes also produced rule 4, because the demo's gaps
were the most productive places to look.

Reading the rules on 2026-11-02, Hampton found "clarifying language rather than affirmative, testable
statements", and rules that checked something without saying what happens to the result.

## Options

- **Add these checks to `review`.** Rejected: they apply only when the thing reviewed is a skill.
- **Report findings and leave the merge to the reader.** Rejected by Hampton: a check needs a result
  that does something.
- **A skill of its own, where each rule says what makes the skill fail.** Chosen.

For a skill that loads on a task it shouldn't:

- **Fail only if the answer is worse.** Tried first. In the retest below, `tidy` loaded in 15 of 15 such
  runs, and all three reviewers passed it because the answers weren't worse.
- **Fail if it loads on any run.** Chosen. A stray load costs little to fix: the author narrows the
  description.

## Decision

Hampton, 2026-11-02:

- Each rule says what makes the skill fail, and a failure stops the merge until the author fixes the
  skill or narrows what it claims to cover.
- A skill fails if it loads on any run of a task it shouldn't load for.
- A blocked check stops the merge too, until someone runs it. Only a person can override that.
- Every sentence of a rule says what to do or how to tell it's done. This is checked during writing
  (AGENTS.md for now, and a `writing-skills` skill in the long term) and during review (rule 10).
- Merged skills meet that test when they are next edited, not now.

A rule against needless words was not the fix for wordy rules: a trial on these rules took them from
557 words to about 638, where rewriting them as testable statements took seven rules from 442 to about
376. Whether examples and reasons need more allowance than rule 10 gives is still open.

## Evidence

Six reviewers (Opus 5.5, `high` effort) reviewed `tidy`, a synthetic skill with eight planted defects,
on 2026-11-02, three with `skill-review` and three with `review` alone. All six said not to merge. The
agent that wrote the rules also planted the defects and scored the answers, not blind, so this shows
what can differ, not how often.

| Planted defect | With the skill (3) | Without it (3) |
|---|---|---|
| Description so broad it loads on code work | 3, measured | 3, by reading |
| Breaks its own citation rule | 3 | 3 |
| Rule contradicts a reference file | 3 | 3 |
| False claim about `mv -n` | 3 | 3 |
| False claim about `ls -S` | 3 | 3 |
| "At most two moves" obeyed by moving whole directories | 1, and 1 found a related loophole in a run | 0 |
| Sentence that says nothing to do | 3, as something to fix | 3, as a minor note |
| `stat -c` doesn't fit the macOS claim | 3, blocked or from memory | 3, blocked or from memory |

So the skill found little that careful reading didn't, on a skill whose defects could be read. What it
changed was the method: all three with the skill ran tasks with and without `tidy` (25, 18 and 37
runs), so they could say whether it helped, and reviewers without it could not. That method costs
several times as much: a review without the skill cost $0.54 to $1.41. A review with it cost $1.55 to
$1.92 for its own session, and those runs are billed separately. The one of these three that stated
its run costs came to $6.81 in all.

After the rules changed, one more review with the skill confirmed the two new outcomes. It failed `tidy`
on rule 3 (loaded in 5 of 5 runs), and said that failures and blocked checks both stop the merge. It
cost $5.28 in all. A second review hit a usage limit and produced nothing. This review wasn't blind:
it read this record, which names `tidy` as a fixture, before its runs.

The retest didn't cover rule 9 (the fixture had no commits or remote) or confirm the macOS claim (no
Mac, and the setup refused `WebFetch`). False findings were not counted. Rule 9 did catch a real case
in this skill's own PR: main twice took the version number the PR had chosen, and the first time git
reported no conflict.

## Consequences

- A review costs more than reading, at several dollars when it runs tasks both ways. A batch of
  reviews can use up a plan's usage limit, as this retest did.
- A skill with a broad description now fails review, so authors have to narrow it.
- Most merged skills have sentences rule 10 would fail, and they stay as they are until next edited.
- The reference's commands are for Claude Code only.
