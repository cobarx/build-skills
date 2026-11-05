---
name: parallel-work-regression-sequential-units
runs: 3
max_turns: 40
allowed_tools: [Bash, Read, Edit, Write, Glob, Grep, Skill]
---
A dev server is running from this checkout on port 8000 (`./dev.sh` starts one). Make four
separate changes, each on its own branch, in order: add a `--version` flag to
`scripts/greet.sh`, add a `--quiet` flag to it, add a `--name` flag to it, then document all
three in README.md. After each change, restart the dev server and check it.
