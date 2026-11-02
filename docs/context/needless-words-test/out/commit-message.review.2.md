Remove subagent shell check from skill-review reference

skills/skill-review/references/running-a-skill.md told reviewers to check
whether a run got a shell through a subagent. Testing on Claude Code
2.1.310 shows that --disallowedTools Bash also covers subagents, so the
check is unnecessary:

- Under --disallowedTools Bash, a general-purpose subagent had no Bash
  tool in 4 of 4 runs.
- Without the flag and with the command allowed, a subagent ran the
  command in 1 of 1 runs.

The reference now says the flag also covers subagents.

Results are in docs/context/skill-review-lessons.md.
