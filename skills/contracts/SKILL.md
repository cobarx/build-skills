---
name: contracts
description: This skill should be used when drawing a boundary between two parts of the same system; when starting a module, package or service; when adding a public entry point to one; when a change to one unit forces simultaneous edits in its callers; when you are about to open another unit's implementation to answer a question; when an implementation is getting clever; or when integrating with a system you do not control. It governs what units are allowed to know about each other, inside a system as much as at its edges.
license: CC-BY-4.0 (https://creativecommons.org/licenses/by/4.0/)
metadata: {author: Hampton Maxwell, source: "https://github.com/cobarx/build-skills/tree/main/skills/contracts"}
---

# contracts

Units meet only at explicit contracts, never internals.

This applies inside a system as much as at its edges. External boundaries announce themselves;
internal ones do not, which is where coupling actually accumulates. A subtitle renderer should
know nothing of the settings UI, the config format, or where its cues came from.

## The review checkpoint

Work from the other unit's spec and public API only. If you open its implementation to answer a
question, **that question is the contract gap**. Record it, extend the contract, then continue. Do
not answer it by reading.

A linter enforces the import boundary, not the reading boundary. Nothing stops a person or an
agent opening a file, understanding it, and writing a client that depends on undocumented
behaviour while passing every gate. Testable in review by asking what you had to open.

## Rules

1. **Two sources, and no third.** The public API gives shape; the spec gives behaviour. A client
   built from those alone is thereby proof that the contract is complete.

2. **Completeness is falsifiable.** A gap you cannot fill from the contract means the contract is
   incomplete. Never argue about whether it is complete; try to build a client and find out.

3. **Extend the contract first, in the same PR.** A missing piece is a contract gap, not a licence
   to reach inside.

4. **Clever code is a symptom of a bad data structure.** When an implementation has to be smart,
   look at the shape it was handed before improving the code. Data dominates: the structure is the
   contract's substance and the code follows from it. Brooks, Pike's rule 5, Raymond.

5. **Documentation on the exported surface is part of the contract.** Internally a good name
   carries it. `linting` enforces presence; whether the doc says anything is a review question.

## The same rules, against a system you do not control

6. **Establish what it documents before integrating.** Three branches. Documented and free to
   adopt: build against it. Undocumented: scaffold. **Documented, but with terms that forbid what
   you are building: log a decision** (`decision-log`) naming which terms bind you on every
   surface. Adopting the contract adopts its terms; staying off it does not escape the provider's
   general terms.

7. **Choose the attachment point deliberately.** There is usually more than one way in. Enumerate
   them and choose on stability, testability and coupling. Taking the first that works is not a
   decision.

8. **Scaffold what has no contract.** Wrap the dependency behind a contract of the behaviour you
   assume, derived from capture rather than from documentation. Assumptions and divergences then
   localise to the scaffold, and a genuine upstream bug can be driven upstream.

## Not here

What the system must do is `spec`. Whether a name is accurate is `naming`. How much rides in a
single unit is `simplicity`.

---

Decisions affecting this skill: `docs/decisions/*-contracts-*.md`
