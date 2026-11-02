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
