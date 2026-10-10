"""Judge every (problem, language, variant) against each test suite and report which suite catches which bug.

    python -m judge.study            # ~2-4 min; writes results/verdicts.json and results/summary.md
"""
from __future__ import annotations

import json
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from .catalog import S, source
from .problems import suites
from .runners import Program

SUITES = ["examples", "edge", "random", "stress"]
TIMEOUT = {"examples": 10, "edge": 10, "random": 20, "stress": 4}   # seconds (stress = performance budget)


def judge_one(problem: str, lang: str, variant: str, tests: dict) -> dict:
    prog = Program(lang, source(problem, lang, variant))
    res = {"problem": problem, "lang": lang, "variant": variant, "description": S[problem, lang][variant][0]}
    try:
        if not prog.build():
            res["suites"] = {s: "CE" for s in SUITES}
            res["compile_error"] = prog.compile_error
            return res
        out = {}
        for s in SUITES:
            cases = tests[problem][s]
            stdin = f"{len(cases)}\n" + "\n".join(c[0] for c in cases) + "\n"
            r = prog.run(stdin, TIMEOUT[s])
            if r.verdict != "OK":
                out[s] = r.verdict
                continue
            got = r.stdout.split()
            ok = len(got) == len(cases) and all(g == str(c[1]) for g, c in zip(got, cases))
            out[s] = "AC" if ok else "WA"
        res["suites"] = out
    finally:
        prog.cleanup()
    return res


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    tests = suites(seed=0)
    jobs = [(p, l, v) for (p, l), vs in S.items() for v in vs]
    with ThreadPoolExecutor(6) as ex:
        rows = list(ex.map(lambda j: judge_one(*j, tests), jobs))
    out = Path("results")
    out.mkdir(exist_ok=True)
    (out / "verdicts.json").write_text(json.dumps(rows, indent=1), encoding="utf-8")

    correct = [r for r in rows if r["variant"] == "correct"]
    bugs = [r for r in rows if r["variant"] != "correct"]
    first_catch = {}
    for r in bugs:
        first_catch[(r["problem"], r["lang"], r["variant"])] = next((s for s in SUITES if r["suites"][s] != "AC"), "none")
    n_bugs = len(bugs)
    caught_by = {s: sum(1 for r in bugs if r["suites"][s] != "AC") for s in SUITES}
    first = {s: sum(1 for v in first_catch.values() if v == s) for s in SUITES + ["none"]}

    lines = [f"**{len(correct)} correct solutions**: {sum(all(v == 'AC' for v in r['suites'].values()) for r in correct)} "
             f"pass every suite. **{n_bugs} seeded bugs** across 4 problems × 4 languages.", "",
             "| Test suite | Bugs it catches (alone) | Bugs it is the *first* to catch |", "|---|---|---|"]
    for s in SUITES:
        lines.append(f"| {s} | {caught_by[s]}/{n_bugs} ({caught_by[s] / n_bugs:.0%}) | {first[s]} |")
    lines.append(f"| *(none: bug survives every suite)* | | {first['none']} |")
    lines += ["", "| Problem | Language | Bug | examples | edge | random | stress |", "|---|---|---|---|---|---|---|"]
    for r in rows:
        if r["variant"] == "correct":
            continue
        v = r["suites"]
        lines.append(f"| {r['problem']} | {r['lang']} | {r['description']} | " + " | ".join(v[s] for s in SUITES) + " |")
    (out / "summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines[:9]))
    bad = [r for r in correct if not all(v == "AC" for v in r["suites"].values())]
    for r in bad:
        print("CORRECT SOLUTION FAILED:", r["problem"], r["lang"], r["suites"], r.get("compile_error", "")[:300])


if __name__ == "__main__":
    main()
