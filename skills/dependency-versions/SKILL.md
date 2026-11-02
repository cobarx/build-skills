---
name: dependency-versions
description: This skill should be used when choosing which version of a runtime, language, framework, library, or tool to use; when setting `engines`, a version file, or a base image; when a generator, template, or old pin has already chosen a version; when a dependency's minimum seems to settle the question; or when adding or upgrading a dependency. It governs which version to use, not whether to take on the dependency.
license: CC-BY-4.0 (https://creativecommons.org/licenses/by/4.0/)
metadata: {author: Hampton Maxwell, source: "https://github.com/cobarx/build-skills/tree/main/skills/dependency-versions"}
---

# dependency-versions

Use the best-supported version of everything the project depends on.

An older line is closer to end of life and lacks newer fixes, features and performance, so the
best-supported version is usually the latest stable release.

## Rules

1. **Start from the latest stable release, not the lowest that works.** A dependency's minimum is
   the limit of what it tolerates, not a target. A version a generator or template pinned is an
   input to check, not a choice already made. Where a runtime has long-term support, stable means
   its newest LTS line.[^node]

2. **Read the versions on the day you choose.** Take them from the project's release schedule and
   its registry, and name what you read. A remembered version is a lead to check.

3. **Let a release settle before taking it.** A runtime's own stability signal, such as promotion
   to LTS, decides for that runtime. Anything else waits out a cooldown of at least three
   days,[^cooldown] and a new major line waits for its first patch release as well. A security fix
   doesn't wait: exempt that package from any gate.

   Have the tool enforce the cooldown, because a gate also covers indirect dependencies and makes
   an open package range safe. If the project already sets a release-age gate or a pinning policy,
   follow it. If not, set a three-day gate where the package manager has one (npm's
   `min-release-age`[^gate]), and pin exact versions where it doesn't.

4. **Once a release has settled, only compatibility holds it back, and the hold is named.** When something that relies
   on the dependency can't take the latest, use the newest version it accepts. Say which dependency
   blocks it and file the follow-up, so the hold is lifted when the blocker moves. Confirm by
   installing and running, because a declared range is only a claim.

5. **Test on the version you ship.** Developer machines, CI and production run the same runtime
   line, so pin the line rather than a range where the platform allows it. A range lets each
   environment pick a different version, and then nothing tests what ships. A lockfile does this
   for packages. A library others install is the exception: it declares the oldest line it supports,
   leaves the top open, and tests every supported line.

6. **Apply the same test later, not only at the start.** A version chosen once ages. An upgrade is
   its own unit of work, and a line nearing end of life is a reason to schedule one.

## Not here

Whether to take on a dependency at all is `simplicity`: *Weigh dependencies both ways*. Stating the
support baseline, and not building on deprecations, is `platform-correctness`. Whether to adopt a
standard is `adopting-standards`. Recording a held-back version or an exception is `decision-log`, and where a follow-up lives is
`durable-context`.
This governs which version to use.

---

Decisions affecting this skill: `docs/decisions/*-dependency-versions-*.md`

[^node]: The Node.js project, "Node.js Releases", <https://nodejs.org/en/about/previous-releases>:
    "Production applications should only use *Active LTS* or *Maintenance LTS* releases."
[^cooldown]: GitHub, "Dependabot options reference",
    <https://docs.github.com/en/code-security/reference/supply-chain-security/dependabot-options-reference>,
    paraphrased: `cooldown` delays version updates by a set number of days, 3 by default, and doesn't
    apply to security updates. Renovate calls the same idea `minimumReleaseAge`.
[^gate]: npm, "config", <https://docs.npmjs.com/cli/v11/using-npm/config>: "only versions that were
    available more than the given number of days ago will be installed."
