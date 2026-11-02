---
name: spec
description: This skill should be used when asked whether or how something can be done; when about to recommend, compare, or propose a tool, library, rule, heuristic, model, or design, in conversation as much as in code; when handed a choice between options; when starting a project or a unit of work; or when it is unclear how much of the behaviour to pin down. It governs defining what the system must do, and how deeply, before choosing how.
license: CC-BY-4.0 (https://creativecommons.org/licenses/by/4.0/)
metadata: {author: Hampton Maxwell, source: "https://github.com/cobarx/build-skills/tree/main/skills/spec"}
---

# spec

Say what the system must do before choosing how.

A solution proposed before its criteria is a guess dressed as an answer. The spec holds the target
(what the change must accomplish, and what it is judged against), kept current as the owner finds
it, so a choice can be weighed instead of picked.

## Rules

1. **What before how.** Write what the change must do, and its criteria, before choosing a tool, a
   library, or a design; options offered first are unframed work. A "can we" or "which is better"
   still needs its what.

2. **Explore to find the what.** Data, spikes and prototypes answer open questions about the goal;
   they don't choose the how. What they turn up is a hypothesis until the goal says it fits.

3. **The goal comes from its owner, often in pieces.** Ask the person whose problem it is; don't
   fill the gap with the convenient reading. Ask what the next step depends on, and keep working
   without the rest.

4. **Keep the goal written down where both can see it.** Keep open questions beside it and date
   each answer as it lands. Mark what you inferred as a guess until the owner confirms it. When the
   goal changes, recheck the decisions and work built on the old one. A product goal holds while
   its features move through discovery, each with its own goal that serves the product's.

5. **The goal is what the output lets its user do.** Not what it is (a role: "a clip captions
   play against") nor a number it hits (an exact byte count). Refining it by what was learned is
   the process working; fitting it to what was built passes by construction.

6. **Specify the general problem, not the example.** Name the problem the case in hand is one
   example of, and spec that. A fix fitted to the examples on hand is a hypothesis to test, not the
   solution.

7. **Criteria come from the goal.** They are what `definition-of-done` checks against, and what a
   `decision-log` entry weighs an option by. No goal, no criteria, no spec.

8. **Spec what would be gotten wrong if left unsaid.** Not every behaviour, not just the
   architecture. What the builder gets right from convention can rest on convention; what bears on
   the goal, reads two ways, or would be filled with the convenient guess must be written.

9. **Set the depth by the cost of a wrong guess, and by the builder.** The more a bad guess costs
   (safety, an irreversible action, a builder who builds exactly and only what is written, like a
   vendor or an agent), the closer to exhaustive. A builder who fills gaps with judgement needs less.

10. **Complete when it cannot be met while missing the goal.** If someone could satisfy the
    whole spec and still miss the point, it has a hole; if a line could be cut and nothing would
    be gotten wrong, it is over-specced.

## Not here

Registering the terms a spec uses (the vocabulary chain, industry to code) is `glossary`
(planned); binding code to those terms is `naming`. Whether the goal was met is `definition-of-done`.
How a choice among options is made and recorded is `decision-log`. Understanding the problem and the
evidence behind a goal is the planned *why* skill. This governs what the system must do, and how
deeply, not how it is built.

---

Decisions affecting this skill: `docs/decisions/*-spec-*.md`
