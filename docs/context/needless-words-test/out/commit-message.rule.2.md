skill-review: remove the subagent shell check from the reference

skills/skill-review/references/running-a-skill.md told reviewers to
check whether a run got a shell through a subagent. The check is not
needed, because --disallowedTools Bash also covers subagents. The
reference now says so.

Testing on Claude Code 2.1.310 showed that under --disallowedTools
Bash, a general-purpose subagent had no Bash tool in 4 of 4 runs.
Without the flag and with the command allowed, a subagent ran the
command in 1 of 1 runs.

The results are written up in docs/context/skill-review-lessons.md.
