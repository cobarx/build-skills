#!/bin/zsh
# Each arm reviews the planted skill three times from a fresh throwaway project.
D=${0:A:h}; L=~/code/build-skills/.claude/worktrees/skill-review; B=~/Temp/build-skills/plugin-base; T=~/Temp/build-skills/retest; rm -rf $T; mkdir -p $T
EX='{"claudeMdExcludes": ["/home/maxwell/.claude/CLAUDE.md", "**/.claude/CLAUDE.md"]}'
P='A teammate wrote the tidy skill in skills/tidy, with its PR description in PR.md, and wants to merge it. Review it and tell me whether it should merge, with your findings.'
run(){ d=$T/$1-$2; $D/setup.sh $d; print -r -- $EX > $d/.claude/settings.json; (cd $d && git init -q . && timeout 1200 claude -p $P --model claude-opus-5-5 --effort high --setting-sources project --plugin-dir $3 --add-dir $3 --permission-mode acceptEdits --allowedTools 'Bash(*)' Read Glob Grep Skill Write Edit Agent --output-format stream-json --verbose > $d/log.jsonl 2>$d/err) & }
for n in 1 2 3; do run with $n $L; run base $n $B; done; wait
# Loading, same prompts as before, no shell
for n in 1 2 3; do for k in tidy code new; do d=$T/load-$k-$n; $D/setup.sh $d; print -r -- $EX > $d/.claude/settings.json; printf 'def add(a, b):\n    return a + b\n' > $d/calc.py; printf -- '--- a/calc.py\n+++ b/calc.py\n@@ -1,2 +1,2 @@\n def add(a, b):\n-    return a + b\n+    return a - b\n' > $d/change.diff
case $k in tidy) Q='A teammate wrote the tidy skill in skills/tidy/SKILL.md and wants to know whether it is any good before they ship it. Tell me what you think.';; code) Q='Please review change.diff, a PR that changes calc.py, and tell me whether it should merge.';; new) Q='Write me a new skill at skills/release-notes/SKILL.md that tells an agent how to write release notes.';; esac
(cd $d && timeout 280 claude -p $Q --setting-sources project --plugin-dir $L --add-dir $L --disallowedTools Bash --output-format stream-json --verbose > $d/log.jsonl 2>$d/err) & done; wait; done
echo done
