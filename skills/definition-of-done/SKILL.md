---
name: definition-of-done
description: This skill should be used when preparing a change for review or deciding whether a unit is complete; when a PR description would otherwise say "tested", "verified", or "works" without showing it; when a change produces output someone should exercise (a rendered file, a running script, a page); or when checking a change against its spec. It governs what a change shows, not what its tests assert.
license: CC-BY-4.0 (https://creativecommons.org/licenses/by/4.0/)
metadata: {author: Hampton Maxwell, source: "https://github.com/cobarx/build-skills/tree/main/skills/definition-of-done"}
---

# definition-of-done

Done is the goal shown to be met.

The goal lives in the spec; checking every dimension against it is also how a hole in the spec
shows. An assertion asks the reviewer to trust; an artifact lets them decide by looking. Silence is
not approval, and neither is a green check.

## Rules

1. **Show, don't assert.** A claim ("tested", "works", "all green") is the thing evidence would
   replace, not evidence. Every check shows its measured value beside the expected one; a bare
   check mark is an assertion.

2. **No stated goal, nothing to check.** A unit smaller than its spec states its own goal, the
   slice of the spec's goal it delivers; the unit that completes the spec also shows the whole
   goal met. A missing goal, or one fitted afterward to what was built, is a spec defect: fix it
   (`spec`) rather than assert past it.

3. **Check every dimension; a skipped one is a failure.** Enumerate what the artifact must be and
   show each, rather than the routine you find convenient. A dimension the spec never named (the
   clip's audio, say) is not out of scope; it is a gap in the spec, surfaced by checking
   exhaustively.

4. **Use the output as the person it is for would.** Not a metadata read, not one file in
   isolation; the whole of it, put to the purpose it exists for. A website is done when it loads,
   every page works, and it communicates to a visitor; that its HTML validates and `ffprobe` reads
   30 fps is nothing the person it is for cares about.

5. **Show the artifact in the form its user consumes.** Put a page that loads or a clip that plays
   in front of the reviewer, never a screenshot of one. The artifact carries the property under
   test; commit the command that regenerates it, not the artifact, and trim a large one along the
   axis that preserves it.

6. **Build the tell into the artifact.** A demo that could look right while being wrong shows
   nothing. Put the check on screen (the burned-in timecode beside the cue) so a reviewer sees
   the defect, not only the feature.

7. **Demo for quality, not only correctness.** Following the spec is not the same as being good,
   and the demo is where a spec that missed the point shows it. Show the output and judge it against
   what you wanted.

8. **Scale the proof to the blast radius.** A rename defends itself; core logic does not. Match the
   evidence to what breaks if the change is wrong.

## Not here

How a test earns the right to fail is `test-fidelity`. What a good spec contains is `spec`. Where a
fixture's data comes from is `fixtures`. Whether the unit is one thing is `simplicity`.

---

Decisions affecting this skill: `docs/decisions/*-definition-of-done-*.md`
