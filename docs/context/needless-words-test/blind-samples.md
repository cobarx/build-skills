# Blind samples for the needless words trial

Each document below appears in three versions, in random order. For each, note which you could understand fully with the least effort, and whether any version leaves out something you need. The key is in `blind-key.json`: leave it closed until you have decided.

## skill-rule

Asked for: one numbered rule for a skill that tells a reviewer how to test an agent skill. Give it a bold title that says what to do, followed by its body.

### Version X

````markdown
1. **Check each run's log before believing it.** A skill run can be contaminated: the user's global settings can reach it, and the skill's reference files can be unreadable if their directory wasn't added. The final answer looks normal either way. Confirm in the log that no global settings reached the run and that the reference files were read. Source: `operate` skill review, 2026-11-01.
````

### Version Y

````markdown
1. **Check a run's log before believing the run.** The user's global settings can reach a skill run, and the skill's reference files can be unreadable if their directory wasn't added. In both cases the final answer looks perfectly normal, so reading it won't reveal the problem. Before treating a run as evidence, the reviewer uses its log to confirm that global settings didn't reach the run and that the skill could read its reference files.[^operate]

[^operate]: This problem came up in the review of the `operate` skill on 2026-11-01.
````

### Version Z

````markdown
1. **Check each run's log before believing the run.** Two problems can contaminate a skill run: the user's global settings can reach it, and the skill's reference files can be unreadable if their directory wasn't added to the run. The final answer looks normal either way, so reading it won't reveal them. Count a run as evidence only after its log shows that global settings stayed out and the reference files were read. (This came up in the review of the `operate` skill on 2026-11-01.)
````

## commit-message

Asked for: a git commit message, with a subject line and a body.

### Version X

````markdown
skill-review: remove the subagent shell check from running-a-skill

The reference told reviewers to check whether a run got a shell through
a subagent. That check is unnecessary because --disallowedTools Bash also
covers subagents. On Claude Code 2.1.310, a general-purpose subagent had
no Bash tool in 4 of 4 runs under the flag. Without the flag and with the
command allowed, a subagent ran the command in 1 of 1 runs, so the test
can detect a subagent's shell access when it exists.

skills/skill-review/references/running-a-skill.md now says the flag also
covers subagents, and the check is gone. The results are written up in
docs/context/skill-review-lessons.md.
````

### Version Y

````markdown
Tell skill reviewers that --disallowedTools covers subagents

skills/skill-review/references/running-a-skill.md told reviewers to check whether a run got a shell through a subagent. That check isn't needed, so the reference now says the flag also covers subagents, and the check is gone.

On Claude Code 2.1.310, a general-purpose subagent had no Bash tool in 4 of 4 runs under --disallowedTools Bash. Without the flag and with the command allowed, a subagent ran the command in 1 of 1 runs.

The results are written up in docs/context/skill-review-lessons.md.
````

### Version Z

````markdown
Remove subagent shell check from skill-review reference

skills/skill-review/references/running-a-skill.md told reviewers to check
whether a run got a shell through a subagent. Testing on Claude Code
2.1.310 shows that --disallowedTools Bash also covers subagents, so the
check is unnecessary:

- Under --disallowedTools Bash, a general-purpose subagent had no Bash
  tool in 4 of 4 runs.
- Without the flag and with the command allowed, a subagent ran the
  command in 1 of 1 runs.

The reference now says the flag also covers subagents.

Results are in docs/context/skill-review-lessons.md.
````

## pr-description

Asked for: a pull request description for a reviewer who has to decide whether to merge it.

### Version X

````markdown
**Cap a skill's rule-bearing sections at fifty lines**

This change records a decision to replace the seventy-line limit on a whole skill file with a fifty-line limit on its rule-bearing sections. No skill needs changing to meet the new cap, so merging affects only how skills are measured from now on.

The old limit, decision 0009, counted the whole file with `wc -l`, so the frontmatter and footer used up room meant for rules. The new limit doesn't count the frontmatter, title, purpose, Not here section, footer or footnotes.

The three longest skills, measured on 2026-10-28, all fit under the cap:

| Skill | Rule-bearing lines |
| --- | --- |
| procedures | 48 |
| steward | 46 |
| contracts | 44 |

There is no automatic check yet, so reviewers enforce the limit. To reproduce the count, use the awk command in the record, `docs/decisions/0031-fifty-lines-of-rules.md`.
````

### Version Y

````markdown
# Cap a skill's rule-bearing sections at fifty lines

This PR records a decision to cap a skill's rule-bearing sections at fifty lines, replacing the seventy-line cap on the whole file. No skill needs changing.

## Why the limit changes

The old limit, decision 0009, counted the whole file with `wc -l`, so the frontmatter and footer used up room meant for rules. The new count leaves out the frontmatter, title, purpose, the Not here section, footer and footnotes.

## How current skills measure up

As measured on 2026-10-28, the skill with the most rule-bearing lines is procedures with 48, followed by steward with 46 and contracts with 44. To reproduce the count, run the awk command in the record, `docs/decisions/0031-fifty-lines-of-rules.md`.

## Enforcement

There is no automatic check yet, so the limit is enforced in review.
````

### Version Z

````markdown
**Record the decision to cap a skill's rule-bearing sections at fifty lines**

This PR adds `docs/decisions/0031-fifty-lines-of-rules.md`, which replaces the seventy-line limit on a whole skill file with a fifty-line limit on its rule-bearing sections. No skill needs changing to meet the new cap, so merging it changes only the rule that future skills and reviews follow.

The old limit, decision 0009, counted the whole file with `wc -l`, so the frontmatter and footer used up room meant for rules. The new limit does not count the following parts of a skill:

- the frontmatter
- the title
- the purpose
- the "Not here" section
- the footer
- the footnotes

Every skill already fits within the cap. These are the highest counts of rule-bearing lines, measured on 2026-10-28:

| Skill | Rule-bearing lines |
| --- | --- |
| `procedures` | 48 |
| `steward` | 46 |
| `contracts` | 44 |

The record gives an `awk` command that reproduces the count. There is no automatic check yet, so reviewers enforce the limit in review.
````

## readme-section

Asked for: a README section telling a developer how to try a skill library in Claude Code without installing it for good.

### Version X

````markdown
## Try the skills without installing them

To try these skills, clone the repository and point Claude Code at the clone with `--plugin-dir`. The skills are available for that session only, and nothing is installed permanently.

1. Clone the repository:

   ```sh
   git clone <repository-url> /path/to/clone
   ```

2. Start Claude Code from your project, using the path to the clone:

   ```sh
   claude --plugin-dir /path/to/clone
   ```

   This works because the repository is a plugin directory, with its manifest at `.claude-plugin/plugin.json`.

3. Ask Claude Code to do a task that matches a skill's description, then watch for a Skill tool call. You don't need to invoke the skill yourself, because skills load on their own when a task matches their description.

Each skill keeps its reference files in its own `references/` directory. If the clone is outside your project, the agent may not be able to read those files until you pass the same path to `--add-dir`:

```sh
claude --plugin-dir /path/to/clone --add-dir /path/to/clone
```
````

### Version Y

````markdown
## Try the skills for one session

You can try this library in Claude Code without installing it permanently. When you load it from a local clone with `--plugin-dir`, the skills are available for that session only.

To load the library and check that it works, follow these steps:

1. Clone the repository, replacing `<repository-url>` and `/path/to/clone` with your own values:

   ```sh
   git clone <repository-url> /path/to/clone
   ```

2. From your project directory, start Claude Code with `--plugin-dir` pointing at the clone:

   ```sh
   claude --plugin-dir /path/to/clone
   ```

3. Ask Claude Code to do a task that matches one of the skills, then watch for a Skill tool call. Skills load on their own when a task matches their description, so you don't need to invoke them by name.

Each skill keeps its reference files in its own `references/` directory. If the clone is outside your project, an agent may not be able to read those files unless you also pass the same path to `--add-dir`:

```sh
claude --plugin-dir /path/to/clone --add-dir /path/to/clone
```

`--plugin-dir` works here because the library is a plugin directory, with its manifest at `.claude-plugin/plugin.json`.
````

### Version Z

````markdown
## Try the skills without installing them

To try the skills for a single Claude Code session, clone the repository and point `--plugin-dir` at the clone. Nothing is installed permanently.

1. Clone the repository:

   ```sh
   git clone <repository-url> /path/to/clone
   ```

2. Start Claude Code with the clone as a plugin directory:

   ```sh
   claude --plugin-dir /path/to/clone
   ```

   If the clone is outside your project, add `--add-dir` with the same path:

   ```sh
   claude --plugin-dir /path/to/clone --add-dir /path/to/clone
   ```

3. Ask Claude Code to do a task that matches a skill's description, and watch for a Skill tool call, which shows that the skill loaded.

Skills load when a task matches their description, so you don't need to invoke them by name.

An agent may need `--add-dir` to read each skill's `references/` directory when the clone is outside your project.

`--plugin-dir` works because the repository is a plugin directory, with its manifest at `.claude-plugin/plugin.json`.
````

## doc-page

Asked for: a short documentation page on how to compare what an agent does with and without a skill.

### Version X

````markdown
# Compare what an agent does with and without a skill

To see what a skill changes, run the same prompt twice in a clean directory, once with the skill's plugin and once without it. Then check each run's log before you read its answer.

## Run the comparison

Replace the example paths and prompt with your own:

1. Create a throwaway directory that holds only what the task needs, and work from there.

2. Add a `.claude/settings.json` file that excludes your global `CLAUDE.md`:

   ```json
   {
     "claudeMdExcludes": ["/home/you/.claude/CLAUDE.md"]
   }
   ```

3. Run the prompt with the plugin:

   ```sh
   claude -p "Your prompt" \
     --plugin-dir /path/to/plugin \
     --add-dir /path/to/plugin \
     --output-format stream-json --verbose \
     > /tmp/with-skill.jsonl
   ```

4. Run the same prompt without the plugin, changing nothing else:

   ```sh
   claude -p "Your prompt" \
     --output-format stream-json --verbose \
     > /tmp/without-skill.jsonl
   ```

5. Check both logs as described in the next section.

6. Compare the two answers.

## Check the logs

Each log shows what the agent could do and what it did. Look for these in each one:

| Log entry | What it tells you |
| --- | --- |
| `init` entry | What was available to the run |
| `Skill` `tool_use` entries | Whether the skill loaded |
| `permission_denials` in the final `result` entry | Which reads or writes were refused |

## Why the setup matters

Two settings prevent results that look valid but aren't:

- **`claudeMdExcludes`:** `--setting-sources project` alone doesn't keep your global `CLAUDE.md` out of the run. If it loads, its instructions can affect both runs and hide the skill's effect.
- **`--add-dir`:** Without this flag, reads of the plugin's reference files are refused, and the run carries on as if nothing happened. The answer alone won't reveal the failure, which is why you check the log first.
````

### Version Y

````markdown
# Compare what an agent does with and without a skill

To see what a skill changes, run the same prompt twice in a clean directory, once with the plugin that provides the skill and once without it. Then check each run's log before reading its answer, because the log shows whether the answer reflects the skill at all.

## Run the comparison

Follow these steps to produce one log for each run:

1. Create a new throwaway directory that holds only what the task needs.

2. Add a `.claude/settings.json` that excludes your global `CLAUDE.md`. You need this because `--setting-sources project` alone doesn't keep that file out.

   ```json
   {
     "claudeMdExcludes": ["/absolute/path/to/.claude/CLAUDE.md"]
   }
   ```

3. From that directory, run the prompt with the plugin:

   ```sh
   claude -p "$PROMPT" --setting-sources project \
     --plugin-dir "$PLUGIN" --add-dir "$PLUGIN" \
     --output-format stream-json --verbose > with-skill.jsonl
   ```

4. Run the same prompt without the plugin, changing nothing else:

   ```sh
   claude -p "$PROMPT" --setting-sources project \
     --output-format stream-json --verbose > without-skill.jsonl
   ```

Set both `--plugin-dir` and `--add-dir` for the first run. Without `--add-dir`, reads of the skill's reference files are refused and the run carries on as if nothing happened, so its answer can look like a fair test of the skill when it isn't.

## Check the logs

Look for these entries in each log before reading its answer:

| Log entry | What it tells you |
| --- | --- |
| The `init` entry | What was available to the run |
| `tool_use` entries for the `Skill` tool | Whether the skill loaded |
| `permission_denials` in the final `result` entry | Which reads or writes were refused |
````

### Version Z

````markdown
# Compare an agent's behavior with and without a skill

To see what a skill changes, run the same prompt twice from the same clean directory: once with the skill's plugin and once without it. Then check each run's log to confirm what the agent could access and what it did before you compare the answers.

## Run the comparison

1. Create a new throwaway directory that holds only what the task needs.

2. In that directory, add a `.claude/settings.json` file that excludes your global `CLAUDE.md`. Replace the path with the full path to your own file:

   ```json
   {
     "claudeMdExcludes": ["/home/your-name/.claude/CLAUDE.md"]
   }
   ```

3. Run the prompt with the plugin, setting both `--plugin-dir` and `--add-dir` to the plugin's directory. This command saves the log outside the task directory:

   ```sh
   claude -p "$PROMPT" \
     --plugin-dir /path/to/plugin \
     --add-dir /path/to/plugin \
     --output-format stream-json --verbose > ../with-skill.jsonl
   ```

4. Run the same prompt without those two flags, changing nothing else:

   ```sh
   claude -p "$PROMPT" \
     --output-format stream-json --verbose > ../without-skill.jsonl
   ```

## Check the logs

Check each log before you read its answer, because an answer doesn't show whether the skill loaded or whether a read was refused. These entries show what happened in the run:

| Log entry | What it tells you |
| --- | --- |
| `init` entry | What was available to the agent |
| `Skill` `tool_use` entries | Whether the skill loaded |
| `permission_denials` in the final `result` entry | Which reads or writes were refused |

## Why the setup matters

Two parts of the setup prevent results that look valid but aren't:

- **`claudeMdExcludes`:** `--setting-sources project` doesn't keep your global `CLAUDE.md` out of a run on its own. Without the exclusion, your personal instructions can affect both runs.
- **`--add-dir`:** Without this flag, reads of the skill's reference files are refused and the run carries on as if nothing happened. The agent then works without those files, and the only sign may be in the log.
````
