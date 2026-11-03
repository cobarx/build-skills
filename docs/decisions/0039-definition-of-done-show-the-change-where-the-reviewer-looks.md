# 0039. `definition-of-done`: show the change where the reviewer looks

- **Status:** Accepted
- **Decided:** 2026-11-03 · **Recorded:** 2026-11-03 · deepseek-flash[1m]
- **Affects:** `definition-of-done`

## Context

On 2026-11-03 the owner of career-playbooks-app asked that a frontend pull request show a
screenshot or video of the change, and that its "What changed" come above "How to evaluate it"
([#44](https://github.com/avngr-asmbld/career-playbooks-app/pull/44), then
[#53](https://github.com/avngr-asmbld/career-playbooks-app/pull/53)). Rule 5 sends the artifact to
the reviewer, and rule 7 tells the author how to let them evaluate it, but neither asks the author
to show the change itself. Rule 5's "never a screenshot of one" reads as a ban on the screenshot the
owner asked for.

## Options

- **Amend rule 5 alone.** Rejected: [0034](0034-definition-of-done-say-how-a-person-evaluates.md)
  already rejected extending rule 5 with a second idea, because rule 5 is about the form of the
  artifact. A screenshot's place in a PR description is about presentation.
- **A new rule 6, with rule 5 narrowed to "never only a screenshot of one".** Chosen: the two rules
  then agree, and the screenshot keeps its job of pointing at the artifact.
- **Put the ordering half in the library too.** Rejected: "What changed above How to evaluate it"
  names a project's sections. `writing-structure` gives the principle, and career-playbooks-app
  keeps the convention in its own `AGENTS.md` (#53).
- **Leave the library alone.** Rejected: the case is general, and rule 5 would keep reading as a
  ban.

## Decision

Rule 6 reads: "Show the change where the reviewer looks. Put a screenshot of a change in
appearance, or a short clip of a change in movement such as a drop, a spinner or a transition, in
the PR description. It points at the artifact; it does not stand in for it."

Rule 5 changes "never a screenshot of one" to "never only a screenshot of one".

## Consequences

- Rules 6 to 9 become 7 to 10. 0034 cites rule 5, which does not move.
- The version moves 0.27.0 to 0.28.0, a minor bump for an added rule.
- The ordering convention stays in career-playbooks-app (#53) as that project's own rule.
- Whether the rule changes what an agent writes is shown by the examples in this PR.
