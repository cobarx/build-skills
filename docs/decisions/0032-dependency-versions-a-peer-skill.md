# 0032. Which version to use is a peer skill, and the answer is the best-supported one

- **Status:** Accepted.
- **Decided:** 2026-11-02 · **Recorded:** 2026-11-02 · Claude Opus 5.5
- **Affects:** `dependency-versions`, `platform-correctness`

## Context

On 2026-11-02 an agent set a new web app's Node.js version to 22.12. That was the lowest version
its dependencies allowed, although Node.js 26 was the current LTS line and the host's default. The
result would have left the floor, a developer's machine, CI and production on different versions,
with nothing testing what ships. Asked which rule caused it, the agent could name none: no skill
says how to choose a version. `platform-correctness` says to state the support baseline and not to
build on deprecations, and `simplicity` says whether to take on a dependency.

Hampton, 2026-11-02: "the goal is to use the best supported version of software. older lts versions
are closer to end of life, lack newer bug fixes, features and perf enhancements. in most cases this
would be the latest stable release, provided it has been out long enough to have a good chance of
being stable and that it is compatible with the dependencies that rely on it."

## Options

- **One rule in `platform-correctness`.** Smallest. Rejected: a library or tool version isn't a
  platform convention, and that skill's triggers don't fire on adding or upgrading a dependency.
- **A rule in `simplicity` beside *Weigh dependencies both ways*.** Rejected: that rule asks whether
  to depend on something, which is a different question from which version.
- **A peer skill.** The question cuts across runtimes, frameworks, libraries and tools, and it has
  its own trigger. Same reasoning as [0012](0012-adopting-standards-a-peer-skill.md).

## Decision

A peer skill, `dependency-versions`, named for what it decides. Hampton's goal is the skill's
purpose and its first rule.

Four things in the rules are Claude's proposals from that goal, not Hampton's words, and are
accepted only as he reviews this record:

- **The cooldown of three days** comes from Dependabot's default, the only number found in official
  documentation. It was chosen over a coined number. It's also a supply-chain measure more than a
  stability one, so it may be too short for Hampton's "good chance of being stable".
- **A new major line waits for its first patch release** as a cheap sign that early bugs have been
  through a round of fixes. This one is judgment, with no source.
- **Pin the line rather than a range** (rule 5) follows from the failure above, and libraries are
  excepted because their users choose the version.
- **Apply the same test later** (rule 6) extends the goal from choosing to keeping.

## Consequences

- A generator's pinned versions become inputs to check, so a fresh scaffold may need upgrades on day
  one, each as its own unit.
- Pinned lines need moving when a new LTS arrives. That is a small, regular cost, and rule 6 accepts
  it.
- Upgrades are sometimes blocked by another package's range, and the skill makes those holds visible
  rather than removing them.
