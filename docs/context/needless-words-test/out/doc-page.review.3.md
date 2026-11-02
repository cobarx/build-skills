# Compare an agent's behavior with and without a skill

To see what a skill changes, run the same prompt twice in a throwaway directory, once with the plugin that contains the skill and once without it. Then compare the two logs and answers.

## Run the comparison

1. Create a throwaway directory that holds only what the task needs, and move into it.

2. Add `.claude/settings.json`, replacing the path with the location of your global `CLAUDE.md`:

   ```json
   {
     "claudeMdExcludes": ["/home/your-user/.claude/CLAUDE.md"]
   }
   ```

3. Run the prompt with the plugin, replacing `/path/to/plugin` with its location:

   ```sh
   claude -p "YOUR PROMPT" \
     --setting-sources project \
     --plugin-dir /path/to/plugin \
     --add-dir /path/to/plugin \
     --output-format stream-json --verbose > with-skill.jsonl
   ```

4. Run the same prompt without the plugin:

   ```sh
   claude -p "YOUR PROMPT" \
     --setting-sources project \
     --output-format stream-json --verbose > without-skill.jsonl
   ```

5. Check each log using the table below.

6. Compare the two answers.

## What to check in each log

Each log shows what the agent could use and what it did. Check these entries:

| Log entry | What it tells you |
| --- | --- |
| `init` entry | What was available to the run |
| `Skill` `tool_use` entries | Whether the skill loaded |
| `permission_denials` in the final `result` entry | Which reads or writes were refused |

## Why the setup matters

The two runs should differ only in `--plugin-dir` and `--add-dir`, so any difference in behavior can be traced to the plugin.

**`claudeMdExcludes`:** `--setting-sources project` doesn't keep your global `CLAUDE.md` out of the run on its own, so the file has to be excluded.

**`--add-dir`:** Without this flag, reads of the skill's reference files are refused and the run carries on as if nothing happened. The answer won't show that the agent missed those files, which is why you check the log before reading the answer.
