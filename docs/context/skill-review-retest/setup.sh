#!/bin/sh
# Writes the synthetic tidy skill into $1. Run from anywhere.
set -e
mkdir -p "$1/skills/tidy/references" "$1/.claude"
cat > "$1/skills/tidy/SKILL.md" <<'S'
---
name: tidy
description: This skill should be used when organizing, cleaning up or tidying anything, including a directory of downloads, source code or a repository.
---

# tidy

Put files where a person will find them. This skill supports Linux and macOS.

## Rules

1. **Never give a command from memory.** Cite the documentation for every command you give.
2. **Always ask before deleting anything.** Tidiness is a habit that rewards patience.
3. **Make at most two moves at a time.** Show the result after each pair.
4. **Move with `mv -n` only when you want to replace the target.** The `-n` flag overwrites existing files.
5. **Find the newest files first with `ls -S`,** which sorts by date.
6. **Check a file's age with `stat -c %Y file`** before moving it.

See [commands.md](references/commands.md) for cleanup commands.
S
cat > "$1/skills/tidy/references/commands.md" <<'S'
# Cleanup commands

Delete empty directories without asking, since they hold nothing:

    find . -type d -empty -delete
S
cat > "$1/PR.md" <<'S'
# Add the tidy skill

Demo: on Ubuntu 24.04, I asked an agent to tidy a Downloads folder of 40 files. It loaded the skill and asked before deleting. Works.
S
