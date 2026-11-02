# Which model and effort should a skill review use?

Working analysis for [PR 167](https://github.com/cobarx/build-skills/pull/167), written 2026-11-02.
Not a decision yet.

## Summary

**Recommendation:** choose separately for the three agents in a review, because each has a different
job, and record the full model ID and effort in the review.

- **The agent running the skill:** use what the skill's users run, because that is the behaviour
  being judged. Vary it only to answer a specific question.
- **The reviewer:** start at Opus 5.5 with `high` effort, then test that choice by giving reviewers a
  skill with planted defects. Use the lowest setting that finds them all.
- **The judge, if there are LLM graders:** already settled by decisions 0018 and 0024. It is a pinned,
  qualified model, and its effort can't be set. None is approved yet (#99 is open).

PR 167's run commands name neither a model nor an effort, so its runs depend on defaults that can
change.

**Question for you:** what should "what its users run" mean for this library? Your own settings are
`opus[1m]` at `medium`. I'd use that unless you expect other people's setups to matter.

## The goal and criteria

The goal comes from PR 167: evidence someone else could rerun. So the criteria are that:

1. **The result applies** to the setups the skill will be used in.
2. **The review finds defects,** which is what `review` asks of a reviewer.
3. **It can be rerun,** so a model release can't pass for a change in the skill.
4. **The cost is justified.** Reviews so far took over 100,000 tokens each.

## The three roles

### The agent running the skill

This agent is the thing under test, so a stronger model is not automatically better. A skill that only
works at `max` on the top model has failed for someone on Sonnet at `medium`.

- **Default:** one setup, the one users run, in both the with-skill and without-skill arms. Comparing
  across different setups would measure the setup as well as the skill.
- **Vary it to answer a question.** Run a second setup when the skill claims to support it, when a
  rule depends on judgement that may vary with effort, or when a user's setup differs. Lower effort is
  the likelier place for a rule to be skipped, but that is argued, not measured.
- **Check the skill's frontmatter.** A skill can set its own `effort`, which overrides the session's
  for that turn. The review should then test at that level as well as reading it.
- **Pin it.** The [plugin eval docs](https://code.claude.com/docs/en/plugin-evals) say to pin the model
  in CI "so a model rollout isn't mistaken for a plugin regression". `claude -p` takes `--model` and
  `--effort`. `claude plugin eval` has `--model`, but its help shows no effort flag.

### The reviewer

Nothing in this repo measures this yet, so the starting point rests on vendor guidance:

- [Claude Code's model docs](https://code.claude.com/docs/en/model-config) describe `high` for "work
  where verification matters or edge cases are likely", which fits a review. They warn that `max` may
  show diminishing returns and be prone to overthinking.
- Anthropic's API guidance suggests a minimum of `high` for intelligence-sensitive work. Opus 5.5
  defaults to `medium`, so a reviewer that doesn't set it gets one level lower.

**How to determine it, rather than assume it.** This adapts the controls in decision 0017:

1. Plant known defects in a copy of a skill, one per `skill-review` rule. PR 167 already supplies real
   ones, such as the rule that contradicts `layouts.md`, which one reviewer missed.
2. Run reviewers at a few settings: Sonnet 5.5 and Opus 5.5, at `medium` and `high`, several runs each.
3. Count defects found, false findings and cost. Choose the lowest setting that finds them all.
4. Repeat when the model changes.

The PR's own comparison gives a reason to look at more than the setting: the reviewer who missed that
contradiction was busy with runs. That was a matter of what the skill told it to do, so rule 7 changed.
A higher setting might not have helped.

Current list prices per million tokens, input then output, from the skill's cached table of 2026-10-06:
Fable 5.1 $10/$50, Opus 5.5 $4/$20, Sonnet 5.5 $2/$10, Haiku 5.5 $0.10/$0.50.

### The judge

Decisions [0018](../decisions/0018-skill-evals-judges-are-pinned-and-qualified.md) and
[0024](../decisions/0024-skill-evals-a-judge-is-pinned-by-its-model-alone.md) settle this: pin the
model by full ID, qualify it by a fixed procedure, and don't pin effort because the runner exposes no
control. The first candidate is `claude-sonnet-5-5`, under #99. Until that closes, LLM-graded results
are provisional. A review that reads replies itself doesn't need a judge.

## What this means for PR 167

- **`running-a-skill.md`:** add `--model` with a full ID and `--effort` to both commands. The current
  commands use `--setting-sources project`, so I can't say what they inherit without testing.
- **Rule 5 or the log table:** have the review record the model and effort of each run, so they can be
  compared later.
- **`skill-review`:** rule 2 could say to keep the setup the same across arms. Whether this belongs in
  the rules or the reference is a judgement for you, against the 50-line limit.

## What would reverse this

- Results for a skill barely change across models and efforts, over several skills: stop varying them
  and use the cheapest setup that users really run.
- The planted-defect test shows no difference between settings: use the cheapest for reviewers too.
- The test shows reviewers miss defects at every setting: the fix is the skill's instructions, not a
  stronger model.

## Not checked

- No planted-defect run has been done, so `high` on Opus 5.5 is a starting point, not a result.
- Whether the run log records the effort used. The `init` entry's contents were not inspected.
- Which model and effort PR 167's commands inherit under `--setting-sources project`.
- Whether effort settings reach the agent under test in `claude plugin eval`. Decision 0024 tested the
  judge only.
- The docs' effort descriptions and the frontmatter `effort` field come from a search summary of
  [the skills docs](https://code.claude.com/docs/en/skills) and the model docs, not a full reading.
