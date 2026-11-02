#!/usr/bin/env python3
"""Regrades results.json by majority of three votes, as claude plugin eval's judge does (0024).
The single-vote grade in run.py proved unreliable: its known-good control flipped between all true and
all false on the same input. Controls run here too. Writes results.json in place. Also writes the blind
samples for the owner: the median-length run per document and arm."""
import json, os, random, re, statistics as st, subprocess, tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
HERE = Path(__file__).parent
BOX = tempfile.mkdtemp(prefix="nw-", dir=os.path.expanduser("~/Temp/build-skills"))
os.makedirs(BOX + "/.claude")
json.dump({"claudeMdExcludes": [os.path.expanduser("~/.claude/CLAUDE.md"), "**/.claude/CLAUDE.md"]}, open(BOX + "/.claude/settings.json", "w"))
briefs = {b["id"]: b for b in json.loads((HERE / "briefs.json").read_text())}
data = json.loads((HERE / "results.json").read_text())
rows = data["rows"]

def vote(facts, text):
    p = ("For each numbered fact, decide whether a reader of the text below would learn it. Judge meaning, not wording. "
         "Return only a JSON array of true or false, one per fact.\n\nFacts:\n" + "\n".join(f"{i+1}. {f}" for i, f in enumerate(facts)) + "\n\nText:\n" + text)
    r = subprocess.run(["claude", "-p", p, "--model", "claude-sonnet-5-5", "--setting-sources", "project", "--tools", "", "--output-format", "json"], cwd=BOX, capture_output=True, text=True)
    return json.loads(re.search(r"\[.*\]", json.loads(r.stdout)["result"], re.S).group(0))

def grade(facts, text):
    votes = [vote(facts, text) for _ in range(3)]
    return [sum(v[i] for v in votes) >= 2 for i in range(len(facts))], votes

with ThreadPoolExecutor(6) as ex:
    res = list(ex.map(lambda r: grade(briefs[r["doc"]]["facts"], r["text"]), rows))
    ctl = list(ex.map(lambda b: (b["id"], len(b["facts"]), sum(grade(b["facts"], "\n".join(b["facts"]))[0]), sum(grade(b["facts"], "The weather in Lisbon was mild this week, and the ferries ran on time.")[0])), briefs.values()))
flips = 0
for r, (g, votes) in zip(rows, res):
    r["facts"] = g; r["kept"] = sum(g); r["votes"] = votes
    flips += any(len({v[i] for v in votes}) > 1 for i in range(len(g)))
data["controls"] = [{"doc": d, "facts": n, "known_good": a, "known_bad": b} for d, n, a, b in ctl]
(HERE / "results.json").write_text(json.dumps(data, indent=1))
print("controls", data["controls"]); print("docs with a split vote", flips, "of", len(rows))
for a in ("baseline", "rule", "review"):
    rs = [r for r in rows if r["arm"] == a]
    print(a, "facts", sum(r["kept"] for r in rs), "of", sum(len(r["facts"]) for r in rs), "misses", [(r["doc"], r["n"]) for r in rs if r["kept"] < len(r["facts"])])
base = {d: st.mean(r["words"] for r in rows if r["doc"] == d and r["arm"] == "baseline") for d in briefs}
for a in ("rule", "review"):
    ch = {d: round(100 * (st.mean(r["words"] for r in rows if r["doc"] == d and r["arm"] == a) / base[d] - 1)) for d in briefs}
    print(a, ch, "mean", round(st.mean(ch.values())))
random.seed(159)
key, md = {}, ["# Blind samples for the needless words trial", "", "Each document below appears in three versions, in random order. For each, note which you could understand fully with the least effort, and whether any version leaves out something you need. The key is in `blind-key.json`: leave it closed until you have decided.", ""]
for d, b in briefs.items():
    md += [f"## {d}", "", f"Asked for: {b['doc']}", ""]
    arms = ["baseline", "rule", "review"]; random.shuffle(arms); key[d] = {}
    for label, a in zip("XYZ", arms):
        rs = sorted((r for r in rows if r["doc"] == d and r["arm"] == a), key=lambda r: r["words"]); r = rs[1]
        key[d][label] = {"arm": a, "run": r["n"], "words": r["words"]}
        md += [f"### Version {label}", "", "````markdown", r["text"], "````", ""]
(HERE / "blind-samples.md").write_text("\n".join(md)); (HERE / "blind-key.json").write_text(json.dumps(key, indent=1))
