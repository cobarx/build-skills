# Least privilege, and the conventional option in an analysis

Written 2026-10-30 by Claude Opus 5.5 for Hampton, who asked whether an agent's
recommendation that a web app build documents in the browser calls for a change to
build-skills: a platform-correctness rule, and a principle of least privilege for data
("minimize the number of systems that touch data to only those necessary"). Not
decided.

## Summary

**Recommendation: two changes, neither in `platform-correctness`. First, a rule in
`decision-analysis`: put the conventional option on the table, and say when the
recommendation departs from it. Second, a new peer skill for least privilege, data
and credentials alike, built on Saltzer and Schroeder's principle and data
minimisation, recorded in `planned-skills.md` now and drafted as its own unit.**

- **The failure was in the analysis, not the platform.** The agent never weighed the
  usual option (render on the server with the same libraries), recommended an unusual
  one without saying it was unusual, and argued from a criterion nobody had given it.
  `decision-analysis` already forbids the last; nothing requires the first two.
- **There is no platform convention to cite.** Building PDFs in the browser is a
  common, documented technique, so "render on the server" isn't a platform rule, and
  `platform-correctness` rule 1 requires citing one. 0010 added a rule to that skill
  and was reverted because it "did not change behaviour and did not belong" there.
- **Least privilege is real, cross-cutting, and established.** The same session hit
  it four times (below), and it would have exposed the browser recommendation's false
  premise. It touches `spec`, `contracts`, and `platform-correctness` without being any
  of them, so by `AGENTS.md` it is their peer.

Where it loses: the `decision-analysis` rule is one more rule in a skill at 41 of 50
lines, for a failure seen once. It still wins because it is the cheapest change that
would have stopped this failure, and an eval case can show whether it does.

## What happened

A web app takes an uploaded resume, has Claude rewrite it as structured data, and
returns a .docx and a .pdf. The original prompt converted .docx to .pdf with
LibreOffice, which doesn't fit a serverless function (about 420 MB installed against a
250 MB bundle limit). The agent's analysis recommended building both files *in the
browser* with JavaScript libraries. The owner reversed it: "browser does not build
anything. work is done in the lambdas", and asked why such an unexpected approach was
proposed.

The agent's own account of why:

1. It conflated "LibreOffice doesn't fit the function" with "rendering doesn't belong
   in the function". The same JavaScript libraries run on the server; that option was
   never weighed.
2. It argued from a criterion of its own, "keep the function a thin proxy that only
   holds the API key", found in neither the spec nor the owner's words.
3. It believed browser rendering served "the site stores no resume". It doesn't: the
   resume passes through the function on its way to the model either way.
4. It presented the recommendation without saying it departed from how such apps are
   usually built.

## What the skills already say

- `decision-analysis` rule 1: criteria come from the decider "first", and "The rest
  come from the goal (`spec`)". Point 2 broke this rule; the rule exists.
- `decision-analysis` rule 5 steelmans the option *the decider* resists. Here the
  decider resisted nothing yet; the conventional option was simply missing. No rule
  requires it to be present.
- `platform-correctness` rules 3 and 7: use the platform as intended, and deviating
  from a platform convention "is a decision, and gets logged". These apply only where
  a convention can be cited (rule 1).

## Options for the "unexpected approach" failure

### A. A `platform-correctness` rule or trigger on where work runs

Its case: the skill exists so software runs the way its environment intends, and its
trigger list doesn't mention choosing between client and server. But neither tier is
the documented convention for generating documents, so the rule would rest on recall,
which rule 1 forbids, and it would repeat 0010. **Not recommended.**

### B. A `decision-analysis` rule on the conventional option (recommended)

Draft wording, to be cut to the skill's register when drafted:

> **Put the usual way on the table.** Among the options, include the one most
> practitioners would reach for first, and say which it is. A recommendation that
> departs from it says so in the summary, with the reason.

It would have forced server rendering into the options and made the departure visible
to the owner before it reached the architecture. Pair it with an eval case from this
incident (0015: cases sit under their skill), so the rule is shown to change
behaviour rather than assumed to.

### C. No change; treat it as an application failure

The invented criterion is already forbidden. Its case: rules don't fix lapses, evals
do. But the missing conventional option is a gap no current rule covers, so an eval
alone would test for behaviour the skill never asks for.

## Options for least privilege

### The standards to adopt

- Saltzer and Schroeder, *The Protection of Information in Computer Systems* (1975),
  least privilege: "Every program and every user of the system should operate using
  the least set of privileges necessary to complete the job." Also least common
  mechanism: "Minimize the amount of mechanism common to more than one user and
  depended on by all users."
- GDPR Article 5(1)(c), data minimisation: personal data "adequate, relevant and
  limited to what is necessary in relation to the purposes for which they are
  processed"; and Article 25(2), data protection by default: "only personal data which
  are necessary for each specific purpose of the processing are processed."

Hampton's wording, "minimize the number of systems that touch data to only those
necessary", is data minimisation applied to systems rather than fields, and least
privilege applied to data access. Both standards are decades old and widely adopted;
`adopting-standards` says to cite them, not coin a new name.

### Evidence from the same session

1. The model API key must never reach the browser (credential).
2. A usage dashboard needs an Admin API key that can manage the whole organization;
   keeping it in the same deployment as a public site widens what a breach exposes
   (credential reach).
3. A hosted .docx-to-.pdf converter was set aside partly because each resume would
   pass through one more party (data).
4. Session-replay analytics would record the resume on screen unless masked (data).

And the case that prompted the question: counted by systems, browser and server
rendering are equal (browser, function, model provider), so the principle would have
shown the agent's privacy argument for the browser to be empty.

### Where it could live

- **`platform-correctness`:** it governs the environment's conventions; least
  privilege holds on every platform. Not recommended.
- **`contracts`:** it governs what units know of each other's *implementation*, not
  what data or authority flows between them. Folding it in would put a cross-cutting
  concern inside one of the things it cuts across, which `AGENTS.md` forbids. Not
  recommended.
- **`spec`:** a spec could list privacy criteria, but least privilege is a design
  default that holds whatever a spec says. Not recommended.
- **A new peer skill (recommended).** Working purpose: "Give each part of a system
  the least privilege its job needs, data included." Its rules would cover which
  systems see a piece of data, which credentials sit where, and how far each
  credential reaches. Recorded in `planned-skills.md` first, with the evidence above,
  then drafted as its own unit.

## Order

Two units, in this order: the `decision-analysis` rule with its eval case (small,
evidence in hand), then the least-privilege planned entry and later the skill. The
second doesn't depend on the first.

## What would reverse it

- The eval case passes without the new rule: then the failure was application only,
  and option C stands.
- A citable platform convention for where document rendering runs turns up: then
  `platform-correctness` rule 7 already covers it, and no new rule is needed there
  either.
- Drafting the least-privilege skill can't produce rules distinct from `spec` and
  `contracts`: then it's a section in an essay, not a skill.

## Not checked

- How a case for this would be graded. Checked 2026-10-30: no skill has eval cases
  yet (`evals/` holds only its licence, and no `skills/*/evals` exists), so this
  would be among the first, under the 0015 to 0018 decisions.
- Whether a least-privilege skill would pass the one-sentence test once drafted; the
  working purpose above is a first attempt.
