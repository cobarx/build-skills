# Compare what an agent does with and without a skill

To see what a skill changes, run the same prompt twice in a clean directory, once with the skill's plugin and once without it. Then check each run's log before reading its answer.

## Run the comparison

1. Create a throwaway directory that holds only what the task needs.

2. In that directory, add a `.claude/settings.json` file that excludes your global `CLAUDE.md`:

   ```json
   {
     "claudeMdExcludes": ["/home/YOUR_USER/.claude/CLAUDE.md"]
   }
   ```

3. Run the prompt with the plugin, replacing `PROMPT` and `PLUGIN_PATH` with your own values:

   ```sh
   claude -p "PROMPT" --plugin-dir PLUGIN_PATH --add-dir PLUGIN_PATH \
     --output-format stream-json --verbose > ../with-skill.jsonl
   ```

4. Run the same prompt without the plugin, changing nothing else:

   ```sh
   claude -p "PROMPT" \
     --output-format stream-json --verbose > ../without-skill.jsonl
   ```

## Check each log

Check these entries in both logs before you read the answers:

| Log entry | What it tells you |
| --- | --- |
| `init` | What was available to the run |
| `Skill` `tool_use` | Whether the skill loaded |
| `permission_denials` in the final `result` | Which reads or writes were refused |

## Why the setup matters

Two settings prevent problems that the answers alone may not reveal:

- **`claudeMdExcludes`:** `--setting-sources project` alone doesn't keep your global `CLAUDE.md` out of the run.
- **`--add-dir`:** Without this flag, reads of the skill's reference files are refused, and the run carries on as if nothing happened.
