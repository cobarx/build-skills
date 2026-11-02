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
