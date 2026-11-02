# Compare what an agent does with and without a skill

To see what a skill changes, run the same prompt twice from a clean directory, once with the skill's plugin and once without it. Then check each run's log before you read its answer, because the log shows whether the skill loaded and whether any reads or writes were refused.

## Run the comparison

Follow these steps, replacing the example prompt and paths with your own:

1. Create a new throwaway directory that holds only what the task needs, and work from there.

2. Add a `.claude/settings.json` file that excludes your global `CLAUDE.md`:

   ```json
   {
     "claudeMdExcludes": ["/home/you/.claude/CLAUDE.md"]
   }
   ```

3. Run the prompt with the plugin, and save the log to a file:

   ```sh
   claude -p "Your prompt" \
     --plugin-dir /path/to/plugin \
     --add-dir /path/to/plugin \
     --output-format stream-json --verbose > with-skill.jsonl
   ```

4. Run the same prompt without `--plugin-dir` and `--add-dir`, changing nothing else:

   ```sh
   claude -p "Your prompt" \
     --output-format stream-json --verbose > without-skill.jsonl
   ```

5. Check both logs, using the entries listed in the next section.

6. Compare the two answers.

## What to check in each log

Each of these log entries answers a different question about the run:

| Log entry | What it tells you |
| --- | --- |
| The `init` entry | What was available to the agent |
| `Skill` `tool_use` entries | Whether the skill loaded |
| `permission_denials` in the final `result` entry | Which reads or writes were refused |

## Why the setup matters

Two settings can quietly invalidate the comparison:

- **`claudeMdExcludes`:** `--setting-sources project` alone doesn't keep your global `CLAUDE.md` out of the run. Without the exclusion, your global instructions can affect both runs.
- **`--add-dir`:** Without this flag, reads of the skill's reference files are refused, and the run carries on as if nothing happened. The answer won't show the problem, so check `permission_denials` in the log.
