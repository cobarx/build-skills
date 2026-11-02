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
