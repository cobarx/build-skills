# 0039. `parallel-work`: assume parallel by default, so every change gets a worktree

- **Status:** Accepted
- **Decided:** 2026-11-05 · **Recorded:** 2026-11-05 · Claude Sonnet 5.5
- **Affects:** `parallel-work`

## Context

On 2026-11-05, in career-playbooks-app, an agent created four branches with `git checkout -b` in
the root checkout and ran a dev server from it. It never loaded `parallel-work`. The skill's
description triggered on "creating a worktree or branch to run a unit of work beside another". The
agent read "beside another" as "units running at the same time", judged its units sequential, and
skipped the skill, although the work was in fact concurrent. The trigger depended on the agent
noticing parallelism, and a worktree is what makes parallel work possible in the first place.

The same weakness shows in the cases added in `evals/parallel-work/`. Run against the old
description (the one on `main` at `d0cbb3f`, Claude Code 2.1.318, three runs per case), the skill loaded in none
of the 12 runs of the regression, smallest-change, spike and single-unit cases. It loaded in 2 of
3 branch-request runs and 3 of 3 second-unit runs, where the prompt names a branch or a worktree.
It loaded in none of the 3 read-only runs, which is correct.

## Options

Criteria, from the goal that the skill fire from its own description with no help from a project
or global instruction, a minimum-skills list or a hook: it fires for a lone unit, a spike and the
smallest change; it does not fire for a read-only question; and it keeps the rules that size
isolation.

- **Keep the parallel-only trigger.** Fails the first criterion, since firing depends on noticing
  parallelism. The old-description runs above are the evidence.
- **Widen the trigger.** Add conditions for sequential units, single units and branch creation.
  Each added condition is another thing to notice, and an agent that edits a file without making a
  branch reaches none of them. Not run.
- **Assume parallel by default.** Treat other units, agents and people as always possibly working
  in the repo. The trigger names the change itself and no condition about parallelism.

## Decision

Assume parallel by default. The description has one trigger: before the first change to any file
in a repository, and before creating or switching a branch, including a spike, a probe or "just
looking" that edits files. Rule 1 applies to every unit, even one running alone. A new rule 2 keeps
the root checkout on the default branch, never switched with `git checkout` or `git switch`, with
a worktree for every branch including the first, in the location a project or the user's config
names.

This option won because it is the only one whose trigger needs no judgment about the repo's state,
which is the judgment that failed on 2026-11-05.

## What went, and why

The premise makes any trigger or clause whose only job was to decide whether parallelism exists
redundant.

- Trigger "when more than one agent or person works a project at the same time": decided whether
  parallelism exists.
- Trigger "when creating a worktree or branch to run a unit of work beside another": same, and the
  one that failed.
- Rule 1, "Running units in parallel does not change that boundary; it only means each gets its own
  tree": the boundary now holds for every unit.
- Rule 2's "beside another" (now rule 3): a unit's writes are enumerated before any run.
- Rule 5's "Parallel work is not one diff because it was done at one time" (now rule 6): the rule
  states the requirement alone.

The triggers for deciding on ports, caches or a database, for two branches touching shared state,
and for a worktree outliving its work decided something other than whether parallelism exists. They
folded into the single trigger because the brief asked for one condition, and their rules stay
(now rules 4, 3 and 7). The rules that size isolation beyond the worktree, sequence dependent units,
merge one reviewable PR per unit and clean up all stay, and none contradicts the new premise.

## Consequences

- The skill loads on every first file change in a repository, so its context cost is paid on
  every unit. It is 29 lines of rules.
- The cleanup trigger is gone. Rule 7 now applies because the skill loaded at the first change and
  is still in context, not because anything fires at cleanup.
- Revisit if the evals show the skill loading for a read-only task, which would mean the trigger is
  wider than "a change".
- The evals grade the skill load only. The runner's sandbox blocks git and offers no
  `EnterWorktree`, so the evals cannot show that an agent then creates a worktree and leaves the
  root checkout on the default branch. That check is tracked in the repository's issues.
- The library version moves from 0.27.0 to 0.28.0: a rule is added and rule 1 changes what it
  requires (`skill-versioning`).
