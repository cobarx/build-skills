---
name: parallel-work
description: This skill should be used when more than one agent or person works a project at the same time; when creating a worktree or branch to run a unit of work beside another; when deciding whether a change needs its own ports, cache, or database; when two branches would touch the same shared state; or when a worktree or branch outlives the work that created it. It governs how far to isolate concurrent work, not the git commands that do it.
license: CC-BY-4.0 (https://creativecommons.org/licenses/by/4.0/)
metadata: {author: Hampton Maxwell, source: "https://github.com/cobarx/build-skills/tree/main/skills/parallel-work"}
---

# parallel-work

Isolate concurrent units of work at the lowest level that prevents them from colliding.

A collision is two units racing on the same mutable thing. Isolation prevents it, and every kind of
isolation is a cost: a branch is free, a database per agent is not. So you isolate only what a unit
actually contends for, and no more.

## Rules

1. **One unit, one worktree, one branch.** A unit is `simplicity`'s one sentence with no "and".
   Running units in parallel does not change that boundary; it only means each gets its own tree.

2. **A worktree isolates files and history, nothing else.** Ports, caches, `.env`, the dev
   database, and external services stay shared across every worktree. That shared state is the only
   thing that collides, so enumerate what a unit writes before you run it beside another.

3. **Isolate a shared resource only when a unit contends for it.** The cost rises from the branch,
   which is free, through a separate runtime (ports, caches) to separate data or services, which
   is dear; the more it costs, the stronger the contention must be to justify it. Name the
   resource, or run in the shared one (`simplicity`: *Extract, do not raise the threshold*).

4. **Dependent units are sequenced, not parallelized.** A separate worktree does not dissolve an
   ordering problem (`simplicity`: *Sequence dependencies, do not merge them*); it hides it until
   the merge, where it costs more.

5. **Each branch merges as its own reviewable unit, in dependency order.** Parallel work is not one
   diff because it was done at one time.

6. **Isolation is removed when the work ends.** A merged or abandoned worktree is pruned and its
   branch deleted. A worktree left behind is state that lies about what is in progress.

## Not here

The git commands that add, list, and prune a worktree are mechanics, not decisions; they live in
git's own documentation. Whether something is one unit or several is `simplicity`. Where isolated
config and data are allowed to live is `platform-correctness`.

---

Decisions affecting this skill: `docs/decisions/*-parallel-work-*.md`
