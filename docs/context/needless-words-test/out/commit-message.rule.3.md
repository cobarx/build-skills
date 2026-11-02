Tell skill reviewers that --disallowedTools covers subagents

skills/skill-review/references/running-a-skill.md told reviewers to check whether a run got a shell through a subagent. That check isn't needed, so the reference now says the flag also covers subagents, and the check is gone.

On Claude Code 2.1.310, a general-purpose subagent had no Bash tool in 4 of 4 runs under --disallowedTools Bash. Without the flag and with the command allowed, a subagent ran the command in 1 of 1 runs.

The results are written up in docs/context/skill-review-lessons.md.
