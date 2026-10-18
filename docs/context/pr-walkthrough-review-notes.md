# PR walkthrough review: working notes

Notes from an interactive review where the author walks the reviewer through a PR. Raw material
for a likely skill; not settled.

## Session 1: PR #11 (definition-of-done eval suite), 2026-10-03

### The method as practiced

- Reviewer asks the author to walk the PR step by step.
- Gate: if the author can't break it into steps, the PR is not ready.
- Author loads the repo's own skills first (`simplicity`), then reads the PR fresh: diff, body,
  linked issue, dependency PR, and how far the branch has drifted from main.

### What the walkthrough surfaced

Being able to list the steps is not the same as passing the gate. Each step has to match what the
title and body claim. Walking the steps exposed these mismatches:

- **Scope vs title.** Titled "triggering only", but two cases carry LLM quality graders and one is
  tagged `adversarial`. The steps do not add up to the sentence.
- **Asserted results.** "Last run reported 4/4", with no command, output, or per-case numbers. The
  PR fails rule 1 of the skill it evaluates.
- **Staleness.** The branch predates its own dependency (#9), and the skill has changed since
  (#14, #37). The reported run measured a version that no longer exists.
- **Layout that doesn't scale.** Cases sit at `evals/<case>/` in a multi-skill repo. The runner
  globs `evals/**`, so nesting by skill costs nothing.
- **Duplication.** The same grader file is copied three times.

### Verdict: fail (the walkthrough, not only the PR)

The reviewer said "fail" with no reason given. The author's best reading of why, not yet confirmed:

- **A file tour is not a breakdown.** "Step 1: .gitignore, Step 2: grader…" can be produced for
  any PR. A gate every PR passes is not a gate. Steps are the claims the change makes, in the
  order a reviewer can check them, each with its evidence.
- **The honest answer was "I can't."** Laid out as claims, PR #11 is: fires when needed, stays
  quiet otherwise, and here is the run. The last step has no output to show, so the breakdown
  can't be completed, and the PR is not ready. The author covered for the missing step with a file
  list and then a list of objections.
- **The author took the reviewer's role.** Asked to walk the PR through, the author critiqued it
  and proposed fixes instead. Doer ≠ critic.

### Correction: a walkthrough is turn by turn

The reviewer called both attempts "a junior engineer answer" and said: "I said walkthrough. Does
a walkthrough happen in one step?" Both attempts put every step in a single message. A
walkthrough presents one step, stops, and lets the reviewer respond before moving on. The
reviewer sets the pace and the questions.

### Candidate rules (unsorted)

- One step per turn. Present it, then stop for the reviewer.
- The walkthrough is a list of the change's claims, each with evidence, not a list of files.
- If a step has no evidence to point at, stop there: the PR is not ready. Don't route around it.
- The author presents; the reviewer judges. Self-critique in place of the walkthrough is a proxy.
- Steps must reconcile with the one-sentence description; a step the sentence doesn't cover is
  scope creep or a wrong title.
- Walk the PR against current main, not the main it branched from.
- Every result in the body is shown (command and output), or it is an assertion.
- Write for the reviewer, not for yourself. The root failure was the choice of audience, not
  assumed context. Text written for its author reads as complete to that author, so names stand
  in for descriptions, roles go undefined and the mechanism goes unexplained. The symptoms are
  listed below, and patching them one at a time doesn't fix the cause.
- A name is not a description. Say what each part does and why it's there.
- Define every role you name, and don't reuse a word that already means something else in the
  same conversation. "Author" meant both the PR's author and the person in the eval prompt.
- Explain the mechanism before the parts. The cases made no sense until the reviewer knew how
  the suite runs. Each patch to a word ("author" → "the user") was fixing a symptom; the missing
  piece was a "how it runs" section.
- A step described incorrectly is a serious bug in the PR, as serious as a bug in the code.
- A fix made in response to review is itself a change. Check it against the source (the files,
  the tool's docs) before publishing it. Three of the inaccuracies in PR #11 came from rewrites
  made in reply to review comments.
- Test inputs have readers too: the reviewer, and the agent under test. A vague scenario ("a
  chart image") makes every reader guess, even when the scenario is only filler.
- Use the words the reader uses. A coinage, even an innocent one like "chart image", is writing
  for yourself. Explaining a coinage with another coinage ("a picture file of a chart") doesn't
  fix it.
- Quote the source rather than paraphrase it. Each paraphrase of the case 1 prompt brought in the
  author's assumptions; the last one put a definition of validation into a prompt that states
  none.
- The reviewer's model of validation: critical elements; sanity checks beyond them; how it was
  tested, and the results; the input provided so someone else can follow the same steps. The
  author validates; the reviewer can repeat it.
- A PR doesn't defer its own incomplete work to a future PR or an issue unless absolutely
  necessary. Repeated deferral ("to follow", "tracked in #N") shows the unit is too big: split it
  until each piece can be finished. Filing is for problems outside the unit, not for the unit's
  own remainder.
- The code must explain itself: what it's for, how it behaves, when to change it. An eval case
  is code. A reader with only the file should be able to answer all three. A PR description
  doesn't count, because it isn't where the next engineer looks.
- Match the house style before inventing a structure. Read recent merged PRs first. Answering a
  new question (hypothesis, result) is no reason for new sections when the existing ones (In one
  sentence, Why, Shown to change behaviour, Review notes) already fit it.
- Before asking for review, check the PR against `definition-of-done` yourself. #61 failed six of
  its eight rules, and the author found that only when the reviewer asked.
- An eval's graders must be shown to fail. A grader seen only to pass has proven nothing, and
  "full marks both ways" is consistent with a rubber stamp.
- Following standards means loading them. A skill the author has to remember to load gets
  missed deep in a session; the only skill loaded on time was the one CLAUDE.md names. The fix
  is a mechanism (a hook at the hand-off, or an always-on rule), not a resolution to remember.
- The reviewer's sanity check, refined: look at the output and judge whether it's in the ballpark
  of what you expected. That catches corruption and bad rendering, which properties never show.
