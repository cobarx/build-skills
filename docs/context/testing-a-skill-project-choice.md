# What project should a skill be tested in?

Working analysis for [PR 167](https://github.com/cobarx/build-skills/pull/167), written 2026-11-02.
Not a decision yet.

## Summary

**Recommendation:** keep a throwaway project for each scenario, built by a script stored with the
scenario. When the skill's behaviour depends on a project's size, history or mess, that script should
clone a real open source repository at a pinned commit instead of writing files by hand. Don't adopt
a shared test project.

- **Other skill authors do much the same.** The setups I read that describe a project build one per
  case, and some use only a prompt. I found no shared open source project intended for this purpose,
  though my search was not exhaustive.
- **PR 167's throwaway has one gap.** It is hand-made and isn't kept, so others can't rerun it. A
  hand-made project can also hide the failures a skill has on real projects (`fixtures`).
- **The runner may replace part of the reference.** `claude plugin eval` documents a temporary home,
  no `CLAUDE.md`, a no-plugin baseline and scaffold scripts. I have not tried it on `skill-review`.

## The goal and criteria

From PR 167: a reviewer can tell whether a skill changes what an agent does for the better, from
evidence someone else could rerun. I inferred these criteria from that goal:

1. **Rerunnable:** someone else gets the same starting project.
2. **Clean:** no instructions reach the run except the skill's.
3. **Able to expose failure:** the project is real enough for the skill to go wrong in it.
4. **Affordable:** the reviews so far took several minutes and over 100,000 tokens each.

## How others do it

Checked 2026-11-02. "Read" means the primary source; "Excerpts" means I searched it for setup details
and did not read it all.

| Source | Project a run works in | Checked by |
|---|---|---|
| [`claude plugin eval`](https://code.claude.com/docs/en/plugin-evals) | "Each run starts in an empty working directory"; a `scaffold_script` adds files or a git repository | Excerpts |
| [agentskills.io](https://agentskills.io/skill-creation/evaluating-skills) | A prompt plus optional input files, with and without the skill | Read |
| [OpenAI](https://developers.openai.com/blog/eval-skills) | "a real repository or a scratch directory"; its example skill scaffolds its own app into an empty directory | Summary of the page |
| [Phil Schmid](https://www.philschmid.de/testing-skills) | "Use a clean environment for every test case"; no project type given | Summary of the page |
| [superpowers](https://github.com/obra/superpowers/tree/main/tests/claude-code) | `mktemp -d`, then a `package.json`, a plan and `git init`, written in the test script | Excerpts |
| [superpowers scenarios](https://github.com/obra/superpowers/blob/main/skills/writing-skills/references/testing-skills-with-subagents.md) | Often no project at all, only a pressure scenario naming a path such as `/tmp/payment-system` | Excerpts |
| [Skillgrade](https://github.com/mgechev/skillgrade) | Files such as `fixtures/broken-app.js` copied into a container | Excerpts |
| [SkillsBench](https://github.com/benchflow-ai/skillsbench) | Per-task `environment/` with its own skills, plus an oracle and a verifier | Excerpts |
| [learn-agent-skills](https://github.com/debs-obrien/learn-agent-skills) | A practice project, your own repository, or any public one you can clone | Search result only |

This repo already follows the same pattern: #101's case uses `files/` and a `setup.sh` scaffold.

SkillsBench and [`aws-samples/sample-agent-skill-eval`](https://github.com/aws-samples/sample-agent-skill-eval)
are the nearest things to "intended for this purpose". Neither fits. SkillsBench tasks bring their own
skills and measure those, so they can't exercise ours. The AWS repo's fixtures test its own tool.

A search for a standard target repository also found none. That is one search, so it shows nothing
is prominent, not that nothing exists.

## The options

| | Throwaway, hand-made (PR 167) | Throwaway, built by a script | Throwaway, cloned from a pinned real repository | Shared test project |
|---|---|---|---|---|
| Rerunnable | No, unless described exactly | Yes | Yes, while the commit exists | Yes |
| Clean | Yes, by its setting | Yes | Needs care: remove its agent files | Needs care |
| Exposes failure | Only what its author thought of | Same blind spots | Best for project shape and history | Depends on one project's shape |
| Cost | Lowest | Low | Higher: more for the agent to read | Higher, for every scenario |

## The case for a real open source project

Synthetic projects exist because they are small and fully understood, and a grader can check them.
Real projects answer a different weakness: `fixtures` says a file built to fit a test "encodes the
code's assumptions rather than the world's behaviour".

- **It applies to project-shape skills.** `organize-project` is the clearest example. PR 167's
  history-loss finding came from running a plan on a copy of a project.
- **It doesn't apply to most of this library.** `naming` or `writing-style` needs a short file to
  work on, and a large repository would only add cost.
- **A shared project is the weak form of this.** One project gives every scenario the same shape, and
  each skill needs something different. Rule 4 of `skill-review` also asks for runs where the skill's
  demo didn't go, which argues for varied projects.

Two risks of real repositories are argued, not measured:

- **Its own instructions:** a clone can bring an `AGENTS.md` or `CLAUDE.md` into the run, which is
  the contamination rule 5 of `skill-review` guards against. The runner documents that `CLAUDE.md`
  doesn't load, but an agent could still read `AGENTS.md` as a file. The script should delete both.
- **A famous project:** a model may know it from training, so its answer may not depend on looking.
  Prefer a small, ordinary repository.

Cloning at run time also avoids vendoring (`fixtures` rule 9), but still choose a permissive licence.

## What this means for PR 167

- **`running-a-skill.md`:** "Set up a throwaway project" should say the project comes from a script
  the review keeps, and when to clone a pinned repository instead.
- **The runner:** try `claude plugin eval <path> --scaffold` on one `skill-review` scenario. If it
  works, the `claudeMdExcludes` setup may become the fallback rather than the main path.
- **Where the runner won't do:** it loads no project configuration, even one a scaffold writes, and
  turns the Artifact tool off. A skill that depends on either still needs the hand-run path.

## What would reverse this

- A skill's real-repository run finds nothing that its synthetic run missed, over several skills:
  drop the clone option.
- Several scenarios need the same project and rebuilding it dominates the cost: share it among them.
- A shared target appears that other skill authors have converged on: adopt it
  (`adopting-standards` rule 4).

## Not checked

- `claude plugin eval` was not run against `skill-review`, and its docs were read in excerpts.
- Whether a `scaffold_script` can clone within its 120-second limit, and with its minimal environment.
- Whether a real repository finds more than a synthetic one. No comparison exists yet.
- The OpenAI and Schmid rows rest on a fetch tool's summary of each page, not my own full reading.
