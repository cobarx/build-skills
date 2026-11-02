---
name: platform-correctness
description: This skill should be used when deciding where configuration, data, cache, or logs live; when choosing how a program is configured or invoked; when naming things or laying out files; when choosing between a platform primitive and a hand-rolled equivalent; when setting or relying on a support baseline; when a deprecated API is involved; or whenever a convention is about to be asserted from memory rather than looked up.
license: CC-BY-4.0 (https://creativecommons.org/licenses/by/4.0/)
metadata: {author: Hampton Maxwell, source: "https://github.com/cobarx/build-skills/tree/main/skills/platform-correctness"}
---

# platform-correctness

Meet the conventions of the environment the software runs in.

Conventions are an interoperability contract. Env vars compose with the shell, systemd, containers
and CI; plain text composes with grep, diff, git and any editor; stderr composes with pipes.
Following them buys interoperability with tools you have not heard of. Deviating removes you from
that ecosystem, and nothing fails loudly when it does.

## Rules

1. **Cite, do not recall.** Look the convention up in the platform's own documentation or
   specification and link it where it lands. A convention asserted from memory is the main failure
   mode, because ecosystems move and training data does not.

   Scope: if `linting` enforces it, the lint config is the record and no prose citation is needed.
   Cite what a linter cannot check: storage locations, wire formats, exit codes, the support
   baseline, how the program is configured and invoked.

2. **Name the layers first.** OS, runtime, language, distribution channel, ecosystem. Each has its
   own conventions, and a choice can be correct at one layer and wrong at another.

3. **Use the platform as intended.** Its idioms, its primitives, its APIs. `AbortController` not a
   cancel flag; `URLSearchParams` not string splitting; discriminated unions not type assertions.
   This is which API to reach for, not whether to add a dependency, which is `simplicity`: *Weigh
   dependencies both ways*. A site or service you attach to is **not** a platform layer; it is an
   uncontracted dependency, and choosing whether to use its official API belongs to `contracts`.

4. **Put state where the platform says.** Config, data, cache, logs and secrets each have a
   designated location. Get it from the specification (XDG on Linux, `chrome.storage` in an
   extension), not from habit. Getting this wrong is invisible until it bites.

5. **Feature-detect, do not version-sniff.** State the support baseline explicitly, once, where
   someone will find it.

6. **Do not build on deprecations.** If a platform has announced a removal, the removed thing is
   already unavailable for new code.

7. **Precedence.** A logged project decision beats a platform convention, which beats personal
   preference. **At an interoperability boundary the boundary's convention wins**, over a logged
   decision too, whatever the language says inside. Deviating from a platform convention is a
   decision, and gets logged.

8. **Mechanize what can be mechanized.** Naming, import order, formatting and ecosystem lints go
   to `linting`. Anything a linter can check should not depend on a reviewer noticing.

## Not here

Error handling is `error-taxonomy`. Module boundaries are `contracts`. Complexity and dependency
admission are `simplicity`. Why a technology was chosen is `decision-log`. Whether to adopt a
standard from beyond the platform (a record format, a version scheme) is `adopting-standards`.

---

Decisions affecting this skill: `docs/decisions/*-platform-correctness-*.md`
