# Compare an agent's behavior with and without a skill

To see what a skill changes, run the same prompt twice in a clean directory, once with the skill's plugin and once without it. Then check each run's log to confirm what the agent actually had and did before you compare the answers.

## Run the comparison

Follow these steps to produce one log for each run:

1. Create a new throwaway directory that holds only what the task needs, and run the remaining steps from it.

2. Add a `.claude/settings.json` file that excludes your global `CLAUDE.md`, using its actual path:

   ```json
   {
     "claudeMdExcludes": ["/home/you/.claude/CLAUDE.md"]
   }
   ```

3. Run the prompt with the plugin, saving the output to a file:

   ```sh
   claude -p "<prompt>" \
     --plugin-dir /path/to/plugin \
     --add-dir /path/to/plugin \
     --output-format stream-json --verbose > with-skill.jsonl
   ```

4. Run the same prompt without the two plugin flags, changing nothing else:

   ```sh
   claude -p "<prompt>" \
     --output-format stream-json --verbose > without-skill.jsonl
   ```

## Check each log before reading the answer

Check these entries in both logs:

| Log entry | What it tells you |
| --- | --- |
| The `init` entry | What was available to the agent |
| `Skill` `tool_use` entries | Whether the skill loaded |
| `permission_denials` in the final `result` entry | Which reads or writes were refused |

The comparison holds only if the logs show that the skill loaded in the first run and that no refused read or write affected either run. Compare the answers only after that.

## Why these settings matter

- **`claudeMdExcludes`:** `--setting-sources project` alone doesn't keep your global `CLAUDE.md` out of the run, so its instructions could affect both runs and hide the skill's effect.
- **`--add-dir`:** Without this flag, reads of the plugin's reference files are refused and the run carries on as if nothing happened. The answer gives no sign of the refusal, which is why you check the log first.
