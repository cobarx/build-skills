skill-review: remove the subagent shell check from running-a-skill

The reference told reviewers to check whether a run got a shell through
a subagent. That check is unnecessary because --disallowedTools Bash also
covers subagents. On Claude Code 2.1.310, a general-purpose subagent had
no Bash tool in 4 of 4 runs under the flag. Without the flag and with the
command allowed, a subagent ran the command in 1 of 1 runs, so the test
can detect a subagent's shell access when it exists.

skills/skill-review/references/running-a-skill.md now says the flag also
covers subagents, and the check is gone. The results are written up in
docs/context/skill-review-lessons.md.
