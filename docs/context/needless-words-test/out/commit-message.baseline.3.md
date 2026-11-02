skill-review: remove the subagent shell check from running-a-skill

The reference told reviewers to check whether a run got a shell through a
subagent. Testing shows the check is unnecessary because --disallowedTools
Bash also covers subagents, so the reference now says that and no longer
asks for the check.

On Claude Code 2.1.310, a general-purpose subagent had no Bash tool in 4 of
4 runs under --disallowedTools Bash. As a control, without the flag and with
the command allowed, a subagent ran the command in 1 of 1 runs.

The results are written up in docs/context/skill-review-lessons.md.
