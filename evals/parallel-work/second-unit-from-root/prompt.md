---
name: parallel-work-second-unit-from-root
runs: 3
max_turns: 15
allowed_tools: [Bash, Read, Edit, Write, Glob, Grep, Skill]
---
You are in the original checkout, on `main`. A teammate's branch `add-logging` is already
checked out in a worktree under `.claude/worktrees/`. Start a second, separate unit: add a
`--debug` flag to `scripts/greet.sh`.
