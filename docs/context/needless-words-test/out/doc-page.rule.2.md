# Compare what an agent does with and without a skill

To see what a skill changes, run the same prompt twice in a clean directory, once with the skill's plugin and once without it. Then check each run's log before you compare the answers.

## Run the comparison

1. Create a new throwaway directory that holds only what the task needs.

2. Add a `.claude/settings.json` that excludes your global `CLAUDE.md`, because `--setting-sources project` alone doesn't keep it out:

   ```json
   {
     "claudeMdExcludes": ["/home/you/.claude/CLAUDE.md"]
   }
   ```

3. Run the prompt with the plugin, saving the log to a file:

   ```sh
   claude -p "PROMPT" \
     --plugin-dir /path/to/plugin \
     --add-dir /path/to/plugin \
     --output-format stream-json --verbose > with-skill.jsonl
   ```

4. Run the same prompt without `--plugin-dir` and `--add-dir`, changing nothing else:

   ```sh
   claude -p "PROMPT" \
     --output-format stream-json --verbose > without-skill.jsonl
   ```

## Check each log before reading the answer

An answer can look normal even when the run didn't test what you intended. Look for these entries in each log to confirm what happened:

| Log entry | What it tells you |
| --- | --- |
| `init` entry | What was available to the run |
| `Skill` `tool_use` entries | Whether the skill loaded |
| `permission_denials` in the final `result` entry | Which reads or writes were refused |

## Why the plugin run needs `--add-dir`

`--plugin-dir` alone doesn't let the agent read the plugin's reference files. Without `--add-dir`, those reads are refused and the run carries on as if nothing happened, so the refusals may only be visible in `permission_denials`.
