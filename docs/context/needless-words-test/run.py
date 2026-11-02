#!/usr/bin/env python3
"""Trial for #159: does a rule against needless words help? Run from the repo root.

Arms: baseline (writing-structure + writing-style), rule (baseline + rule.md), review (rule, then a
second agent proposes cuts that are applied as given). Writes out/ and results.json beside this file.
Facts are graded by claude-sonnet-5-5, which is a candidate judge and not yet qualified (0018).
"""
import json, os, random, re, statistics, subprocess, sys, tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).parent
ROOT = HERE.parents[2]
OUT = HERE / "out"
RUNS = 3
WRITER = "claude-opus-5-5"
EFFORT = "medium"
JUDGE = "claude-sonnet-5-5"
BOX = Path(tempfile.mkdtemp(prefix="nw-", dir=os.path.expanduser("~/Temp/build-skills")))
(BOX / ".claude").mkdir()
(BOX / ".claude/settings.json").write_text(json.dumps({"claudeMdExcludes": [os.path.expanduser("~/.claude/CLAUDE.md"), "**/.claude/CLAUDE.md"]}))

def body(name):
    return (ROOT / f"skills/{name}/SKILL.md").read_text()

BASE = "Follow these two writing skills.\n\n" + body("writing-structure") + "\n\n" + body("writing-style")
RULE = (HERE / "rule.md").read_text()
SYSTEMS = {"baseline": BASE, "rule": BASE + "\n\nAlso follow this rule of writing-style:\n\n" + RULE}

def ask(prompt, model, system=None, effort=None):
    cmd = ["claude", "-p", prompt, "--model", model, "--setting-sources", "project", "--tools", "", "--output-format", "json"]
    if effort: cmd += ["--effort", effort]
    if system: cmd += ["--append-system-prompt", system]
    for attempt in range(3):
        r = subprocess.run(cmd, cwd=BOX, capture_output=True, text=True, timeout=400)
        try:
            o = json.loads(r.stdout)
            if not o.get("is_error"): return o["result"].strip(), o.get("total_cost_usd", 0)
        except json.JSONDecodeError:
            pass
    raise RuntimeError(r.stderr[:300] or r.stdout[:300])

def brief_prompt(b):
    return f"Write {b['doc']} Use these notes, and return only the finished text.\n\nNotes:\n" + "\n".join("- " + n for n in b["notes"])

def write(b, arm, n):
    text, cost = ask(brief_prompt(b), WRITER, SYSTEMS["rule" if arm == "review" else arm], EFFORT)
    cuts = None
    if arm == "review":
        p = ("You are reviewing another author's text. Find words that carry nothing: filler, repetition, words other words imply. "
             "Keep whatever the reader needs to understand or act. Return only a JSON array of objects with exact \"old\" and \"new\" strings, "
             "each old string copied exactly from the text. Return [] if nothing should change.\n\nText:\n" + text)
        raw, c2 = ask(p, WRITER, None, EFFORT); cost += c2
        m = re.search(r"\[.*\]", raw, re.S)
        cuts = json.loads(m.group(0)) if m else []
        applied = 0
        for e in cuts:
            if e.get("old") and e["old"] in text:
                text = text.replace(e["old"], e.get("new", ""), 1); applied += 1
        cuts = {"proposed": len(cuts), "applied": applied}
    return {"doc": b["id"], "arm": arm, "n": n, "text": text, "words": len(text.split()), "cost": cost, "cuts": cuts}

def grade(facts, text):
    p = ("For each numbered fact, decide whether a reader of the text below would learn it. Judge meaning, not wording. "
         "Return only a JSON array of true or false, one per fact.\n\nFacts:\n" + "\n".join(f"{i+1}. {f}" for i, f in enumerate(facts)) +
         "\n\nText:\n" + text)
    raw, cost = ask(p, JUDGE)
    return json.loads(re.search(r"\[.*\]", raw, re.S).group(0)), cost

def main():
    OUT.mkdir(exist_ok=True)
    briefs = json.loads((HERE / "briefs.json").read_text())
    probe, _ = ask("Quote any instructions you have about em dashes or about file paths starting with ~. If you have none, reply NONE.", WRITER)
    print("isolation probe:", probe[:200], flush=True)
    assert probe.strip().startswith("NONE"), "global instructions reached the run"
    jobs = [(b, a, n) for b in briefs for a in ("baseline", "rule", "review") for n in range(1, RUNS + 1)]
    with ThreadPoolExecutor(6) as ex:
        rows = list(ex.map(lambda j: write(*j), jobs))
    by = {b["id"]: b for b in briefs}
    # Controls per 0017: all the notes must score full marks, and an unrelated text must score none.
    controls = []
    for b in briefs:
        good, _ = grade(b["facts"], "\n".join(b["facts"]))
        bad, _ = grade(b["facts"], "The weather in Lisbon was mild this week, and the ferries ran on time.")
        controls.append({"doc": b["id"], "known_good": sum(good), "known_bad": sum(bad), "facts": len(b["facts"])})
    with ThreadPoolExecutor(6) as ex:
        graded = list(ex.map(lambda r: grade(by[r["doc"]]["facts"], r["text"]), rows))
    for r, (g, c) in zip(rows, graded):
        r["facts"] = g; r["kept"] = sum(g); r["total"] = len(g); r["cost"] += c
        (OUT / f"{r['doc']}.{r['arm']}.{r['n']}.md").write_text(r["text"] + "\n")
    (HERE / "results.json").write_text(json.dumps({"controls": controls, "rows": rows}, indent=1))
    print(json.dumps(controls))
    print(f"{'doc':16}{'arm':10}words per run      facts kept")
    for b in briefs:
        for a in ("baseline", "rule", "review"):
            rs = [r for r in rows if r["doc"] == b["id"] and r["arm"] == a]
            print(f"{b['id']:16}{a:10}{str([r['words'] for r in rs]):20}{[r['kept'] for r in rs]} of {rs[0]['total']}")
    for a in ("baseline", "rule", "review"):
        rs = [r for r in rows if r["arm"] == a]
        print(a, "median words", statistics.median(r["words"] for r in rs), "facts", sum(r["kept"] for r in rs), "of", sum(r["total"] for r in rs))
    print("cost", round(sum(r["cost"] for r in rows), 2))

main()
