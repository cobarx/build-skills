---
name: readme
description: This skill should be used when writing or updating a README, an AGENTS.md or CLAUDE.md, or the README that indexes a folder; when a project's status, setup or layout changes; or when an index entry says what a file is rather than when to open it. It governs what an entry point says, not whether every document can be reached from one.
license: CC-BY-4.0 (https://creativecommons.org/licenses/by/4.0/)
metadata: {author: Hampton Maxwell, source: "https://github.com/cobarx/build-skills-cobarx/tree/main/skills/readme"}
---

# readme

A README answers the questions its reader arrives with.

An entry point is the first file a reader opens: the project `README.md`, the agent instructions
file, a folder's `README.md`. They open it to decide what this is and where to go next. If they
have to read further to find that out, the entry point has failed.

## Rules

1. **Know which reader it is for.** The project `README.md` is for someone who will use the
   project. `AGENTS.md` (or `CLAUDE.md`, where the tool reads only that) is for whoever works on it,
   agent or human.[^agents] A folder's `README.md` is for someone who has landed in that folder.
   What each one says follows from who reads it.

2. **A project README answers four questions, in order.** What is it, in one sentence? Why does it
   exist? How do I use it: install, then a minimal working example? What else do I need: config,
   contributing, licence? Use Standard Readme's section names and order for these.[^standard-readme]
   Architecture, a full API reference and a changelog belong somewhere else, linked from here.

3. **The agent file is a briefing, then an index.** Summary, setup commands, conventions, what to
   avoid, then the documentation index. Keep it short enough to read before starting work: a
   section that outgrows a screen becomes its own document, with a link.

4. **Every index entry says when to open it.** One clause naming the occasion ("read before
   changing auth", "follow when deploying"), not the topic ("documentation about auth"). This holds
   for a file in a folder index as much as for a document in the agent file's index.

5. **Say each thing once, in one place.** The README and the agent file do not repeat each other;
   each links to the other, and both link deeper material rather than expanding it.

6. **The entry point changes with what it describes.** When status, setup or layout changes, the
   README or agent file that describes it changes in the same PR. A stale README is worse than a
   missing one, because the reader believes it.

## Not here

That every document can be reached from an entry point, and where each kind of document lives, is
`durable-context`. How a project's directories are laid out is `project-setup` (planned). What a
decision record says is `decision-log`. Doc comments on an exported surface are `contracts`. This
governs what an entry point says.

---

Decisions affecting this skill: `docs/decisions/*-readme-*.md`

[^agents]: AGENTS.md, *AGENTS.md*, https://agents.md. An open format that calls itself "a README for
    agents".
[^standard-readme]: Richard Littauer, *Standard Readme*,
    https://github.com/RichardLitt/standard-readme/blob/main/spec.md. Adopted for section names and
    order only, not its badge, banner or table-of-contents rules.
