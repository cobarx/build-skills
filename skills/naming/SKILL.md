---
name: naming
description: This skill should be used when naming a function, variable, type, or file; when reviewing a diff; when no single name seems to fit what something does; when a name reaches for process, handle, manage, data, or info; or when a function body does something its name did not lead you to expect. It governs what a name means, not what shape it takes.
license: CC-BY-4.0 (https://creativecommons.org/licenses/by/4.0/)
metadata: {author: Hampton Maxwell, source: "https://github.com/cobarx/build-skills/tree/main/skills/naming"}
---

# naming

A name tells the truth about the thing it names.

## The review checkpoint

Run this on every function in a diff. It costs seconds and it is the only check that catches a
name that lies.

1. Read the name. Do not read the body.
2. Write down what you expect the body to do.
3. Read the body.

If the body does something you did not predict, one of two things is true, and both are defects:
**the name is wrong**, or **the function does more than one thing**. Fix whichever it is. Do not
resolve it by widening the name, which is how `updateTimestamp` becomes `processEvent`.

Predict before reading, never read then judge. Once you know what a function does, its name always
looks reasonable enough.

## Rules

1. **Name what it does, not what it accomplishes or how it behaves.** `updateTimestamp`, not
   `refreshUI` (the outcome) and not `mutateInPlace` (the mechanism).

2. **A name excludes implementations; it does not admit them.** If two functions with different
   behaviour could both plausibly carry the name, the name says nothing. `parseManifest` admits
   one thing. `handleInput` admits anything.

3. **If no single accurate name exists, the function is too big.** This is the one-thing rule with
   a test attached. Splitting is the fix; a vaguer name is not.

4. **Vagueness is denied, not discouraged.** `process`, `handle`, `manage`, `do`, `perform`,
   `util`, `helper`, `data`, `info`, `temp`, `val`, `obj`. `linting` (planned) makes this a build
   failure; until it exists, a reviewer blocks on it.

5. **Booleans read as assertions.** `isReady`, `hasCaptions`, `shouldRetry`. Not `ready`,
   `captions`, `retry`.

6. **Use the registered vocabulary.** Code uses the term registered for a concept, one term per
   concept, everywhere.

7. **A rename is its own change.** Mechanical refactors are single units regardless of size
   (`simplicity`: *Exceptions, named so the rule survives*), so rename in its own PR rather than
   smuggling it alongside behaviour.

## Not here

The *shape* of a name (casing, prefixes, platform convention) is `platform-correctness`. The
*meaning* is here. Which term a domain concept is registered under is `glossary` (planned).
Complexity thresholds are `simplicity`. Where module boundaries fall is `contracts`. Enforcement
is `linting`.

---

Decisions affecting this skill: `docs/decisions/*-naming-*.md`
