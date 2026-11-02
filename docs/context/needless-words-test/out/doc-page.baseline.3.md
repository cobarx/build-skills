# Compare an agent's behavior with and without a skill

To see what a skill changes, run the same prompt twice in a clean directory, once with the skill's plugin and once without it. Then check each run's log to confirm what the agent could access and did before you compare the answers.

## Run the comparison

Follow these steps to produce one log for each run:

1. Create a new throwaway directory that holds only what the task needs, and change into it.

2. Add a `.claude/settings.json` file that excludes your global `CLAUDE.md`, using its absolute path:

   ```json
   {
     "claudeMdExcludes": ["/home/you/.claude/CLAUDE.md"]
   }
   ```

3. Set the prompt, the plugin path and a log directory outside the throwaway directory:

   ```sh
   PROMPT="The task you want to test"
   PLUGIN=/path/to/plugin
   LOGS=/path/to/logs
   ```

4. Run the prompt with the plugin:

   ```sh
   claude -p "$PROMPT" --plugin-dir "$PLUGIN" --add-dir "$PLUGIN" \
     --output-format stream-json --verbose > "$LOGS/with-skill.jsonl"
   ```

5. If the first run changed any files in the directory, restore them.

6. Run the same prompt without the plugin:

   ```sh
   claude -p "$PROMPT" --output-format stream-json --verbose > "$LOGS/without-skill.jsonl"
   ```

## Check the logs

Check these entries in each log before you read the answer:

- **The `init` entry** shows what was available to the agent.
- **`Skill` `tool_use` entries** show whether the skill loaded.
- **`permission_denials` in the final `result` entry** lists any refused reads or writes.

The comparison is valid only if the plugin is available in the first run and absent from the second, and the first run's skill loaded with no refused reads. Otherwise, fix the setup and run the comparison again.

## Why the setup matters

Each part of the setup keeps the two runs comparable or exposes a failure that the answer alone would hide:

- **`claudeMdExcludes`:** `--setting-sources project` alone doesn't keep your global `CLAUDE.md` out of the run, and its instructions could affect both results.
- **`--add-dir`:** Without this flag, reads of the skill's reference files are refused and the run carries on as if nothing happened. The answer gives no sign that the agent worked without those files.
- **A log directory outside the throwaway directory:** The second run can't read the first run's log.
