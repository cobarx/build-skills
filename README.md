# build-skills

Skills for designing and building high-quality software and physical products with AI assistance.
They help you define your vision, allowing the AI to implement it.

Most were written while building software; however, the principles carry over, and the skills are
designed to be adapted to other domains. Measuring the real part before designing around it is
`fixtures`; building a drawer organizer on the [Gridfinity](https://gridfinity.xyz) grid rather
than inventing your own is `adopting-standards`.

Each skill is a short set of rules, loaded by an AI agent when it applies. They are
deliberately brief: a skill costs context every time it fires, so it holds rules and nothing else.
The reasoning behind them lives in [docs/essays/](docs/essays/).

## Lineage

The skills are a close match for total quality management (TQM). TQM holds that quality is defined
by the customer and built into the work by everyone who does it, not checked for at the end.
[Quality is defined by the customer](docs/essays/quality-is-defined-by-the-customer.md) explains TQM
for a reader new to it and shows where the skills match it. TQM grew from the work of W. Edwards
Deming.

## Skills

| Skill | Purpose |
|---|---|
| [simplicity](skills/simplicity/SKILL.md) | Make every change cheap to understand. |
| [platform-correctness](skills/platform-correctness/SKILL.md) | Meet the conventions of the environment the software runs in. |
| [naming](skills/naming/SKILL.md) | A name tells the truth about the thing it names. |
| [format](skills/format/SKILL.md) | Remove formatting from human judgment. |
| [contracts](skills/contracts/SKILL.md) | Units meet only at explicit contracts, never internals. |
| [fixtures](skills/fixtures/SKILL.md) | Test data comes from the real world, or says that it does not. |
| [skill-versioning](skills/skill-versioning/SKILL.md) | Version the skill library by how its skills changed. |
| [parallel-work](skills/parallel-work/SKILL.md) | Isolate concurrent units of work at the lowest level that prevents them from colliding. |
| [definition-of-done](skills/definition-of-done/SKILL.md) | Done is the goal shown to be met. |
| [essays](skills/essays/SKILL.md) | An essay carries its provenance. |
| [review](skills/review/SKILL.md) | A reviewer tries to break the work against the standard it claims to meet. |
| [durable-context](skills/durable-context/SKILL.md) | Context lives in the project, where the next reader, human or agent, will find it. |
| [spec](skills/spec/SKILL.md) | Say what the system must do before choosing how. |
| [decision-log](skills/decision-log/SKILL.md) | A decision is reasoned in the open. |
| [decision-analysis](skills/decision-analysis/SKILL.md) | Give the decider what they need to weigh a choice themselves. |
| [adopting-standards](skills/adopting-standards/SKILL.md) | Adopt an existing standard before inventing your own. |

Planned: `linting`, `test-fidelity`, `glossary`, `harness`, `project-setup`, a skill for the *why*
behind a goal (name not settled), plus ports of `tdd` and `error-taxonomy`.

## Context cost

Measured on 2026-10-12 in Claude Code 2.1.296 with Claude Opus 5.5, with the 17 skills under
`skills/` installed:

| What | When it is paid | Tokens |
|---|---|---|
| The skill index: every name and description | Every session | 2,078 |
| One skill's body | Each time that skill loads | 550 to 1,119, median 907 |

The index figure is the difference in prompt tokens between two headless sessions that differ only
in whether the plugin is enabled. Each body figure is that `SKILL.md` without its front matter,
counted the same way. Other models tokenize differently, so the counts hold for this one only.

## Installation

### Claude Code

Install from GitHub, for every project on this machine:

```bash
claude plugin marketplace add cobarx/build-skills
claude plugin install build-skills@build-skills
```

Inside a session, `/plugin marketplace add cobarx/build-skills` then
`/plugin install build-skills@build-skills` does the same, and asks for a scope.

#### Updating

Auto-update is off by default for marketplaces outside Anthropic's own. Either turn it on
(`/plugin`, **Marketplaces** tab, select `build-skills`, **Enable auto-update**), or update
by hand:

```bash
claude plugin update build-skills@build-skills
```

`plugin.json` sets a version, so an update arrives when that version changes.

#### From a clone

To work on the skills, point the marketplace at your clone instead, so `git pull` is the update:

```bash
claude plugin marketplace add ./build-skills
claude plugin install build-skills@build-skills
```

Run that from the directory that holds the clone. Edits to an existing skill load in the next
session; after adding or removing a skill, run `/plugin marketplace update build-skills`.
To load a clone for one session without installing, use `claude --plugin-dir ./build-skills`.

### Other agents

OpenAI Codex, GitHub Copilot (CLI, VS Code, JetBrains), Cursor, and Gemini CLI read the same
[Agent Skills](https://agentskills.io) format, and all four load skills from `~/.agents/skills/`.
Install there with the GitHub CLI:

```bash
gh skill install cobarx/build-skills --all --dir ~/.agents/skills
```

Update with `gh skill update --all`. For an agent with its own directory, swap `--dir` for
`--agent <name> --scope user`; `gh skill install --help` lists the names. `gh skill` is in preview
in the GitHub CLI.

Without the GitHub CLI, copy each folder under `skills/` into `~/.agents/skills/`, one folder per
skill, directly under that directory.

## How these are written

Two conventions do most of the work:

**The outline is the skill.** No expanded rationale, no worked examples where the rule is already
unambiguous. No skill here runs past seventy lines, not counting footnoted citations.

**Draft long, then keep only what is a rule.** The long draft is a discovery tool, not the
deliverable. The test applied to every line: does this change what anyone does? See
[docs/essays/outline-is-the-skill.md](docs/essays/outline-is-the-skill.md).

## License

The skills and documentation are licensed under [CC BY 4.0](LICENSE), © 2026 Hampton Maxwell.
Everything under `evals/`, prose, data, and code alike, is licensed under
[Apache-2.0](evals/LICENSE) instead. See [0014](docs/decisions/0014-license-cc-by-4-0.md) and
[0019](docs/decisions/0019-evals-take-apache-2-0.md).

To credit a skill you copy or adapt, give its title, author, source, licence, and what you
changed:

> Adapted from "simplicity" by Hampton Maxwell,
> <https://github.com/cobarx/build-skills>, CC BY 4.0. Changes: …
