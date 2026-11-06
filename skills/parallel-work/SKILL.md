---
name: parallel-work
description: This skill should be used before the first change to any file in a repository, and before creating or switching a branch, including a spike, a probe or "just looking" that edits files. It governs how far to isolate a unit of work, not the git commands that do it.
license: CC-BY-4.0 (https://creativecommons.org/licenses/by/4.0/)
metadata: {author: Hampton Maxwell, source: "https://github.com/cobarx/build-skills/tree/main/skills/parallel-work"}
---

# parallel-work

Isolate every unit of work at the lowest level that prevents it from colliding with another.

A collision is two units racing on the same mutable thing. Isolation prevents it, and every kind of
isolation is a cost: a branch is free, a database per agent is not. So you isolate only what a unit
actually contends for, and no more.

## Rules

1. **One unit, one worktree, one branch, for every unit.** A unit is `simplicity`'s one sentence
   with no "and". A unit running alone gets its own worktree too: assume other units, agents or
   people may be working in the repo, and do not check whether any are.

2. **The root checkout stays on the default branch.** Never switch it with `git checkout` or
   `git switch`; every branch, including the first, gets a worktree. If a project or the user's
   config names where worktrees live, put them there.

3. **A worktree isolates files and history, nothing else.** Ports, caches, `.env`, the dev
   database, and external services stay shared across every worktree. That shared state is the only
   thing that collides, so enumerate what a unit writes before you run it.

4. **Isolate a shared resource only when a unit contends for it.** The cost rises from the branch,
   which is free, through a separate runtime (ports, caches) to separate data or services, which
   is dear; the more it costs, the stronger the contention must be to justify it. Name the
   resource, or run in the shared one (`simplicity`: *Extract, do not raise the threshold*).

5. **Dependent units are sequenced, not parallelized.** A separate worktree does not dissolve an
   ordering problem (`simplicity`: *Sequence dependencies, do not merge them*); it hides it until
   the merge, where it costs more.

6. **Each branch merges as its own reviewable unit, in dependency order.**

7. **Isolation is removed when the work ends.** A merged or abandoned worktree is pruned and its
   branch deleted. A worktree left behind is state that lies about what is in progress.

## Not here

The git commands that add, list, and prune a worktree are mechanics, not decisions; they live in
git's own documentation. Whether something is one unit or several is `simplicity`. Where isolated
config and data are allowed to live is `platform-correctness`.

---

Decisions affecting this skill: `docs/decisions/*-parallel-work-*.md`
