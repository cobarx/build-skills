---
name: adopting-standards
description: This skill should be used when about to invent a file format, file or directory layout, marker or config file name, schema, versioning scheme, protocol, record format, or process convention that other tools or people will read; when choosing between a published standard and a home-grown one; when two standards compete for the same need; or when adopting a draft standard or only part of one. It governs whether to adopt an existing standard, not the conventions of the runtime environment.
license: CC-BY-4.0 (https://creativecommons.org/licenses/by/4.0/)
metadata: {author: Hampton Maxwell, source: "https://github.com/cobarx/build-skills/tree/main/skills/adopting-standards"}
---

# adopting-standards

Adopt an existing standard before inventing your own.

A standard brings two things you cannot make yourself. Readers, people and tools, that already
understand it; and thinking done by people with more context than you, which keeps answering
questions the work has not asked yet. SemVer settled what a breaking change means below 1.0 before
anyone here needed to know. Inventing gives up both, and nothing fails loudly when it does.

## Rules

1. **Search before you coin; recall is not a search.** Before inventing anything another tool,
   person or project will read (a file on disk, a wire format, a version scheme, a record, a
   convention others follow), run a search for a standard that already covers it: a web search, not
   only the platform's own docs. A convention you remember is a lead to verify, not a finding. Name
   what you searched; "no standard fits" needs a search behind it.

   Scope: names and shapes that never leave one unit are `naming`'s, not this.

2. **Weigh it for this work.** Two benefits: others already understand it, and it carries thinking
   you would otherwise redo. Two costs: learning and fitting to it, and leaving it if it fades. A
   mature standard carries more of both benefits and is less likely to need leaving. The best are
   cheap to learn and carry a lot, as Markdown and SemVer do. Who the work is for and how long it
   must last decide the balance: a quick tool for one person can rightly roll its own when adopting
   is costly, and a system others will build on rarely should.

   When an agent builds it, fitting costs the agent little. The cost that counts is the owner's:
   one more thing to learn, one more decision to understand.

3. **A young standard only when leaving is cheap.** A draft has had little thinking put into it
   and may not last. Adopt one when switching away later is a rename or a line, not a migration.

4. **Among several, take the one the ecosystem converged on,** not the one you judge best.
   Convergence is what buys the readers.

5. **Adopt part, and say which part.** A subset is fine. Name what was taken and what was left, and
   do not claim conformance you do not have.

6. **Log the choice either way.** Adopting a standard, adopting a draft, and inventing despite one
   that fits are each a decision. The record names what was searched and how it was weighed.

## Not here

The conventions of the environment the software runs in (storage locations, primitives, platform
APIs) are `platform-correctness`. Terms for domain concepts are `glossary` (planned). Whether to take
on a code dependency is `simplicity`: *Weigh dependencies both ways*. How a decision is recorded is
`decision-log`. This governs whether to adopt an existing standard.

---

Decisions affecting this skill: `docs/decisions/*-adopting-standards-*.md`
