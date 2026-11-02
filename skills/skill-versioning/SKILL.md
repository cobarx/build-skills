---
name: skill-versioning
description: This skill should be used when opening a PR that changes a skill library by adding, removing, editing, or renaming a skill; when choosing the next version for the library's plugin.json; or whenever that version is about to be bumped by habit rather than by what changed in the skills.
license: CC-BY-4.0 (https://creativecommons.org/licenses/by/4.0/)
metadata: {author: Hampton Maxwell, source: "https://github.com/cobarx/build-skills/tree/main/skills/skill-versioning"}
---

# skill-versioning

Version the skill library by how its skills changed.

The version in `plugin.json` is a claim about the library, read by whoever installs it. A bump that
ignores what changed makes no claim; it is a counter, and the commit SHA is already that.

## Rules

1. **Bump by what changed.** Read the diff and pick the level from the table below. Never default
   to patch to dodge the decision, and never bump with no skill change to describe.

2. **The bump ships with the change.** The new version lands in the same PR as the skill change, so
   a release has one place to be read. A bump in its own later commit has lost what it was for.

3. **One version for the library.** The version lives in the library's `plugin.json`, one number
   for the whole set. Skills have no version of their own; they inherit the library's.

4. **Below 1.0, a break need not force 1.0.** Per the [SemVer spec §4](https://semver.org/#spec-item-4),
   `0.y.z` is initial development, so a breaking change may take the minor slot. Reach `1.0.0` when
   the skills are a set you will keep stable; after that, a break is a major bump.

5. **A version only rises.** Never reuse or lower a released number. A wrong bump is corrected by
   the next one, not by rewriting the last.

## Levels

Semantic versioning, `MAJOR.MINOR.PATCH`:

| Change to the library | Level | Example |
|---|---|---|
| Fix or reword a rule without changing what it requires | patch | `1.4.0` → `1.4.1` |
| Add or remove a rule, or change what one requires | minor | `1.4.1` → `1.5.0` |
| Add or remove a skill | minor | `1.5.0` → `1.6.0` |
| Rename a skill, or change how it is loaded or invoked | major | `1.6.0` → `2.0.0` |

Below `1.0`, a break may take the minor slot instead of forcing a major (rule 4).

## Not here

Whether a change is one skill or several is `simplicity`. What a skill's name means is `naming`.
Why a version boundary was chosen is `decision-log`.

---

Decisions affecting this skill: `docs/decisions/*-skill-versioning-*.md`
