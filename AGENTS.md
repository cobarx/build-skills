# build-skills

## Summary

Skills for designing and building high-quality software and physical products with AI assistance:
sizing units of work, platform conventions, naming, formatting, linting, testing, contracts.

Each skill is `skills/<name>/SKILL.md`; the README says how to install them.

## Load `simplicity` first

**Before starting any unit of work in this repo, load `simplicity`.** That includes changes to
skills themselves. This repo governs itself by its own skills: a new skill is a unit that passes
the one-sentence test, and a change to a skill passes the same gates as a change to code.

## Conventions

- **The outline is the skill.** SKILL.md holds rules and nothing else. Bulky material lives in
  `references/` and `templates/`, loaded on demand. See
  [docs/essays/outline-is-the-skill.md](docs/essays/outline-is-the-skill.md).
- **Draft long, then keep only what is a rule.** The long draft is a discovery tool. The test for
  every line: does this change what anyone does?
- **Each skill's purpose fits one sentence with no "and".** If it needs one, it is two skills.
- **Industry terms over our own.** Coinage is permitted for constructs local to this repo, and is
  recorded as ours.
- **Skills never link to context; context links to skills.** Each skill carries one stable glob at
  its foot rather than a list that grows.

## What to avoid

- Do not expand a skill with rationale. The rationale goes in `docs/essays/`, the settled choice
  goes in `docs/decisions/`, and the skill keeps the rule.
- Do not fold a cross-cutting concern into one of the things it cuts across. If it references
  three siblings, it is their peer.
- Do not give a skill policy that belongs to another. `linting` enforces; the other skills decide.

## Documentation index

- [README.md](README.md) - what this is, how to install, the skill index
- [skills/](skills/) - the skills themselves, one directory each
- [docs/essays/](docs/essays/) - the narrative behind a practice: where it came from, what it cost
  to learn, what it shapes. One per idea, not per decision
- [docs/decisions/](docs/decisions/) - terse, dated, append-only record of what was settled.
  Superseded rather than edited
- [docs/context/](docs/context/) - what is not settled yet: open questions. Working notes stay on
  their branch (`durable-context` rule 7)
