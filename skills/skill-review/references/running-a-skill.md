# Running a skill to review it

These steps run a skill in Claude Code without an interactive session (headless) and save a log of
what really happened. A different agent tool needs its own equivalent of each step. They were
checked on Claude Code 2.1.310.

## Set up a throwaway project

Create a new directory holding only what the task needs, such as a few project notes or a small test
suite. Add this `.claude/settings.json`, so the user's global instructions stay out of the run:

```json
{"claudeMdExcludes": ["/home/<user>/.claude/CLAUDE.md", "**/.claude/CLAUDE.md"]}
```

`--setting-sources project` alone doesn't do this: the global file still applied with that flag.

## Run with and without the skill

Set `$PROMPT` to the task, and `$LIBRARY` to the directory of the plugin that contains the skill.
Then run the same prompt both ways, changing nothing else:

```sh
# with the skill
claude -p "$PROMPT" --setting-sources project --plugin-dir "$LIBRARY" --add-dir "$LIBRARY" \
  --output-format stream-json --verbose > with.jsonl

# without it
claude -p "$PROMPT" --setting-sources project \
  --output-format stream-json --verbose > without.jsonl
```

`--plugin-dir` makes the library's skills available, and `--add-dir` lets the run read a skill's
references, which sit outside the project. Without `--add-dir`, those reads are refused and the run
carries on as if nothing happened.

Add `--permission-mode acceptEdits` when the task has the agent write files, since a refused
write can also go unnoticed.

Add `--disallowedTools Bash` when the task must not touch the machine. Say so in the review, because
a run with no shell can't carry out the task and shows only what the agent would do. To judge a plan
from such a run, carry out its commands on a copy of the project.

Check too whether the agent tried to get a shell through a subagent, and whether it got one, because
a subagent with a shell could change the real machine.

Claude Code also keeps a session log of each run in `~/.claude/projects/`, so deleting the throwaway
project doesn't remove those logs.

## Read the log

Check these in `with.jsonl` and `without.jsonl` before reading the answer:

| Look for | Where | What it tells you |
|---|---|---|
| Tools, plugins and skills available | the `init` entry at the start of the log | What the run could really do |
| Signs of the user's global instructions | the opening of the final answer, any habit the prompt didn't ask for | Whether those instructions reached the run. If they did, the number of runs where the skill loaded can't be trusted |
| `Skill` tool calls | `tool_use` entries in `assistant` messages | Whether the skill loaded |
| `Read` calls on `references/` | `tool_use` entries | Which references loaded, and whether they all did at once |
| `permission_denials` | the final `result` entry | Reads or writes that were refused without showing in the answer |
