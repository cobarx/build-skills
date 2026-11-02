---
name: essays
description: This skill should be used when writing or editing an essay in docs/essays/; when an essay needs an author line or a date; or when an essay is revised and the change should be recorded. It governs how an essay is signed and versioned (one part of writing one), not what it says.
license: CC-BY-4.0 (https://creativecommons.org/licenses/by/4.0/)
metadata: {author: Hampton Maxwell, source: "https://github.com/cobarx/build-skills/tree/main/skills/essays"}
---

# essays

An essay carries its provenance.

An essay is where the reasoning lives that a skill leaves out (why a practice exists, what it cost
to learn, what it shapes). Writing one well is a wider skill than this; for now these rules cover
its provenance, the byline and the revision history, and will grow.

## Rules

1. **Byline every essay.** Under the title, a `date · author` line. The author is whoever actually
   wrote it (an agent names its model, a person names themselves), not the committer, and not a
   reviewer who only steered.

2. **Log every substantive revision.** A change to what the essay claims appends a dated, bylined
   entry to a `## Revisions` section, naming what changed and why. A typo or a rewrap earns none.

3. **Version each revision by how much it moved.** Semantic (`MAJOR.MINOR.PATCH`), an inexact
   signal of magnitude, not a precise measure, in the spirit of a document's revision history. The
   first version is `1.0`.

   | Change to the essay | Level | Example |
   |---|---|---|
   | A fix or a clarified line | patch | `1.0` → `1.0.1` |
   | A new point, or one meaningfully reworked | minor | `1.0.1` → `1.1` |
   | A reversal, or a rewrite of the argument | major | `1.1` → `2.0` |

4. **The revision ships with the change.** The version bump and its log entry land in the same PR
   as the edit they record.

## Not here

Where an essay sits among the other kinds of record is `durable-context`. Versioning the skill
library is `skill-versioning`.

---

Decisions affecting this skill: `docs/decisions/*-essays-*.md`
