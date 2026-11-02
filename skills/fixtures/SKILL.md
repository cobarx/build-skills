---
name: fixtures
description: This skill should be used whenever a test needs data that originates outside the codebase, such as command output, network responses, sensor readings, third-party API payloads, page state from a site you do not control. It governs where that data comes from and what has to be recorded alongside it. Load it before writing a test that needs such data, before writing or running a capture, and when a fixture stops matching reality.
license: CC-BY-4.0 (https://creativecommons.org/licenses/by/4.0/)
metadata: {author: Hampton Maxwell, source: "https://github.com/cobarx/build-skills/tree/main/skills/fixtures"}
---

# fixtures

Test data comes from the real world, or says that it does not.

A fixture that was never real shares every blind spot of the code written beside it. It will agree
with your assumptions because it was made from them.

## Rules

1. **Prefer capture.** Not from memory, not from a specification, not from a string typed until
   the test passed. The exceptions are genuine impossibility, never effort: the real thing is
   gigabytes, or it needs a setup you cannot reproduce. A file built to fit a test encodes the
   code's assumptions rather than the world's behaviour, and the test can then only confirm them.

2. **Label what is synthetic.** Derive from a capture where you can, by trimming, sampling or
   redacting. Synthetic is also the right tool for extremes a real corpus will not reliably
   produce. Unlabelled synthetic data is the failure, not synthetic data.

3. **The capture script ships.** It lives in the repo and is run, not described. Anything captured
   by hand once will need capturing again, and by then the steps are gone.

4. **Verify preconditions, then record.** A capture environment can fail silently and produce data
   indistinguishable from real behaviour. Assert what must be true and write nothing otherwise.
   Saved, that fixture encodes your environment's failure as the system's behaviour, and it will
   look plausible forever.

5. **Record the conditions, not just the data.** Date, environment, and anything that changes what
   the source returns. A capture from a system you do not control is a dated snapshot, not a fact,
   and without the conditions a later capture cannot be diffed against it.

6. **Do not hardcode what can be derived.** Anything the source can tell you, take from the source.
   Operator-typed fields are the ones that go stale, and they go stale silently while every derived
   field stays correct.

7. **Scrub at capture, not at commit.** Secrets, tokens and personal data are removed by the
   capture script. A scrub step that runs later is a scrub step that gets skipped once.

8. **Defer what cannot be captured yet; do not invent it.** When the system does not exist yet or
   access is pending, mark the test ignored, naming what is needed and where to get it. An ignored
   test is honest; a test passing against imagined data is not.

9. **Vendor only what you can license.** A corpus with unclear provenance is a liability sitting in
   the repository, whatever its technical merits.

## Not here

What a test asserts and where it sits are `test-fidelity`. When the test gets written is `tdd`.
This skill only governs where its data came from.

---

Decisions affecting this skill: `docs/decisions/*-fixtures-*.md`
