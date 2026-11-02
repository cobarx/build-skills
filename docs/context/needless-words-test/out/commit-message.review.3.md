skill-review: drop subagent shell check from running-a-skill

The running-a-skill reference told reviewers to check whether a run got
a shell through a subagent. That check is unnecessary, because
--disallowedTools Bash also covers subagents.

On Claude Code 2.1.310, a general-purpose subagent had no Bash tool in
4 of 4 runs under --disallowedTools Bash. Without the flag and with the
command allowed, a subagent ran the command in 1 of 1 runs, so the
absence of Bash came from the flag.

The reference now says the flag also covers subagents. Results are in docs/context/skill-review-lessons.md.
