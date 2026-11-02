skill-review: drop the subagent shell check from running-a-skill

The reference told reviewers to check whether a run got a shell through
a subagent. That check isn't needed, because --disallowedTools Bash also
covers subagents.

Tested on Claude Code 2.1.310. Under --disallowedTools Bash, a
general-purpose subagent had no Bash tool in 4 of 4 runs. Without the
flag and with the command allowed, a subagent ran the command in 1 of 1
runs.

skills/skill-review/references/running-a-skill.md now says the flag
covers subagents. The results are written up in
docs/context/skill-review-lessons.md.
