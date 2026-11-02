skill-review: drop the subagent shell check from running-a-skill

The running-a-skill reference told reviewers to check whether a run got
a shell through a subagent. That check isn't needed, because
--disallowedTools Bash also covers subagents.

We tested this on Claude Code 2.1.310. Under --disallowedTools Bash, a
general-purpose subagent had no Bash tool in 4 of 4 runs. Without the
flag and with the command allowed, a subagent ran the command in 1 of 1
runs, so the setup can show a subagent using a shell when one is
available.

The reference now says the flag also covers subagents, and the check is
gone. The results are written up in docs/context/skill-review-lessons.md.
