#!/usr/bin/env python3
"""Same trial as run.py, on what the rule is for: skill rules. Each rule of skill-review is rewritten,
keeping its meaning, under the candidate rule, and then again with a second agent's cuts. The current
text is the baseline. Writes rules-out.json, with the median-length run of each arm, and a blind key."""
import json, os, random, re, statistics as st, subprocess, tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
HERE = Path(__file__).parent; ROOT = HERE.parents[2]
SKILL = (ROOT / ".claude/worktrees/skill-review/skills/skill-review/SKILL.md").read_text()
BOX = tempfile.mkdtemp(prefix="nw-", dir=os.path.expanduser("~/Temp/build-skills"))
os.makedirs(BOX + "/.claude"); json.dump({"claudeMdExcludes": [os.path.expanduser("~/.claude/CLAUDE.md"), "**/.claude/CLAUDE.md"]}, open(BOX + "/.claude/settings.json", "w"))
SYS = "Follow these writing skills.\n\n" + (ROOT / "skills/writing-style/SKILL.md").read_text() + "\n\nAlso follow this rule of writing-style:\n\n" + (HERE / "rule.md").read_text()
sec = re.search(r"^## Rules\n(.*?)^## Not here", SKILL, re.S | re.M).group(1)
rules = [" ".join(x.split()) for x in re.split(r"^(?=\d+\. )", sec, flags=re.M) if re.match(r"\d+\. ", x)]
intro = " ".join(re.search(r"^A skill is .*?(?=^## )", SKILL, re.S | re.M).group(0).split())
def ask(p, sys=None):
    c = ["claude", "-p", p, "--model", "claude-opus-5-5", "--effort", "medium", "--setting-sources", "project", "--tools", "", "--output-format", "json"]
    if sys: c += ["--append-system-prompt", sys]
    return json.loads(subprocess.run(c, cwd=BOX, capture_output=True, text=True, timeout=400).stdout)["result"].strip()
def rewrite(rule):
    return ask(f"This rule is from a skill that tells a reviewer how to test an agent skill. The skill opens with:\n\n{intro}\n\nRewrite the rule below so a person can understand it fully with the least effort. Keep its number, its bold title and everything it requires. Return only the rule.\n\n{rule}", SYS)
def cut(text):
    raw = ask("You are reviewing another author's rule. Find words that carry nothing: filler, repetition, words other words imply. Keep everything the rule requires. Return only a JSON array of objects with exact \"old\" and \"new\" strings copied from the text, or [] if nothing should change.\n\nText:\n" + text)
    m = re.search(r"\[.*\]", raw, re.S)
    for e in (json.loads(m.group(0)) if m else []):
        if e.get("old") and e["old"] in text: text = text.replace(e["old"], e.get("new", ""), 1)
    return text
def med(xs): return sorted(xs, key=lambda t: len(t.split()))[1]
jobs = [(i, n) for i in range(len(rules)) for n in range(3)]
with ThreadPoolExecutor(6) as ex:
    one = list(ex.map(lambda j: rewrite(rules[j[0]]), jobs))
    two = list(ex.map(cut, one))
random.seed(159); out, key = [], {}
for i, r in enumerate(rules):
    a = med(one[i*3:i*3+3]); b = med(two[i*3:i*3+3]); v = [("current", r), ("rule", a), ("review", b)]; random.shuffle(v)
    out.append({"rule": i + 1, "X": v[0][1], "Y": v[1][1], "Z": v[2][1]}); key[i + 1] = {l: (x[0], len(x[1].split())) for l, x in zip("XYZ", v)}
(HERE / "rules-out.json").write_text(json.dumps(out, indent=1)); (HERE / "rules-key.json").write_text(json.dumps(key, indent=1))
print("rule  words: current rule review")
for i, r in enumerate(rules):
    print(i + 1, len(r.split()), st.mean(len(t.split()) for t in one[i*3:i*3+3]), st.mean(len(t.split()) for t in two[i*3:i*3+3]))
