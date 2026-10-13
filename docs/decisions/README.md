# Decisions

What has been settled, one record per decision: terse, dated, append-only. The narrative behind a
decision lives in [docs/essays/](../essays/); what is still open lives in
[docs/context/](../context/).

Records follow [MADR](https://adr.github.io/madr/): `NNNN-title-with-dashes.md`, numbered in order
and never reused. The title starts with the name of each skill the decision governs, so the glob at
the foot of a skill (`docs/decisions/*-<skill>-*.md`) finds it; a library-wide decision names no
skill. A reversed decision gets a new record, and the old one is marked superseded. See 0001.

| # | Decision | Status |
|---|---|---|
| [0001](0001-decision-log-durable-context-record-decisions-as-madr.md) | Record decisions as numbered MADR files | Accepted |
| [0002](0002-outline-is-the-skill.md) | The outline is the skill | Accepted |
| [0003](0003-linting-owns-mechanism-not-policy.md) | `linting` owns the mechanism, not the policy | Accepted |
| [0004](0004-definition-of-done-simplicity-kept-apart.md) | `definition-of-done` stays apart from `simplicity` | Accepted |
| [0005](0005-simplicity-essential-and-accidental-complexity.md) | Brooks's essential and accidental complexity, not a coinage | Accepted |
| [0006](0006-glossary-industry-terms-over-coinage.md) | Industry terms over our own | Accepted |
| [0007](0007-review-adversarial-stance-is-not-a-skill.md) | The adversarial stance is not a skill | Accepted |
| [0008](0008-durable-context-essays-three-documentation-classes.md) | Three documentation classes, not two | Accepted |
| [0009](0009-seventy-line-limit.md) | No skill runs past seventy lines | Accepted, amended by 0013 |
| [0010](0010-platform-correctness-look-for-a-standard-before-inventing-one.md) | Look for a standard before inventing one | Superseded by 0012 |
| [0011](0011-durable-context-file-problems-by-default.md) | A problem you notice is filed by default | Accepted |
| [0012](0012-adopting-standards-a-peer-skill.md) | Adopting standards is a peer skill, not a platform rule | Accepted |
| [0013](0013-cite-sources-in-footnotes.md) | Cite sources in footnotes, outside the line limit | Accepted |
| [0014](0014-license-cc-by-4-0.md) | License the text under CC BY 4.0; code takes a software licence | Accepted |
| [0015](0015-skill-evals-cases-sit-under-their-skill.md) | `skill-evals`: cases sit under the skill they test | Accepted |
| [0016](0016-skill-evals-each-case-explains-itself.md) | `skill-evals`: each case explains itself in a README | Accepted |
| [0017](0017-skill-evals-llm-graded-cases-ship-known-bad-and-known-good-controls.md) | `skill-evals`: an LLM-graded case ships a known-bad and a known-good control | Accepted |
| [0018](0018-skill-evals-judges-are-pinned-and-qualified.md) | `skill-evals`: a judge is a pinned model, approved by a repeatable qualification | Accepted |
| [0019](0019-evals-take-apache-2-0.md) | The evals directory takes Apache-2.0 | Accepted |
| [0020](0020-spec-triggers-on-events-and-builds-the-goal-with-its-owner.md) | `spec` triggers on observable events, and builds the goal with its owner | Accepted |
| [0021](0021-decision-analysis-decision-log-analysis-is-a-peer-of-the-record.md) | Decision analysis is a peer skill of the decision log | Accepted |
| [0022](0022-simplicity-thresholds-move-to-a-reference.md) | `simplicity`'s thresholds move to a reference | Accepted |
| [0024](0024-skill-evals-a-judge-is-pinned-by-its-model-alone.md) | `skill-evals`: a judge is pinned by its model alone | Accepted |
| [0028](0028-a-failures-size-decides-when-it-earns-a-rule.md) | A failure's size, not its count, decides when it earns a rule | Accepted |
