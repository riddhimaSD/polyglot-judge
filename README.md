# polyglot-judge

**A small local code judge for Python, JavaScript, Java and C++. It runs a study of *which kind of test catches which kind of bug*, using 48 solutions: one correct version and two seeded "plausible but wrong" variants for each of 4 problems × 4 languages.**

```bash
pip install -e ".[dev]"      # also needs: python, node, a JDK (javac/java) and g++ on PATH
python -m judge.study        # ~20 s → results/summary.md, results/verdicts.json
pytest -q                    # 20 tests
python -m judge.export       # writes every variant to solutions/<problem>/<lang>/ for reading
```

---

## Why

Reviewing code that someone (or a model) wrote is mostly about deciding **whether it's actually correct**. The examples in a problem statement are a weak signal. Code that passes them can still fail on edge cases, on inputs a brute-force reference would disagree with, or at scale. This repo measures that directly, across four languages, because the *same* algorithm can be right in one language and wrong in another.

## How it works

- **Problems** ([`judge/problems.py`](judge/problems.py)): maximum subarray sum, lower bound (first index ≥ t in a sorted array with duplicates), counting inversions, and longest substring without repeated characters.
- **Four test suites per problem:**
  - `examples`: the cases a problem statement would show;
  - `edge`: hand-picked boundaries (all-negative, duplicates, target beyond the end, `"abba"`, `"dvdf"`, single elements);
  - `random`: 300 small random cases checked against a **brute-force reference** (differential testing);
  - `stress`: one input with n = 200,000 under a 4-second budget, to expose O(n²) time and 32-bit overflow.
- **Runners** ([`judge/runners.py`](judge/runners.py)): each solution is compiled (javac, `g++ -O2`) and run in a temp directory with a timeout. Verdicts are AC / WA / TLE / RE / CE.
- **Solutions** ([`judge/catalog.py`](judge/catalog.py), exported to [`solutions/`](solutions/)): per (problem, language), one correct version and two bugs:

| Bug | Languages | What's wrong |
|---|---|---|
| `zero_init` | all | Kadane starts `best` at 0, so it returns 0 when every element is negative |
| `quadratic` | all (max_subarray: Py/JS) | correct answer, O(n²) time |
| `int_overflow` | Java, C++ | 32-bit accumulator; sums or counts pass 2³¹ at scale |
| `last_occurrence` | all | returns the *last* index of a repeated target, not the first |
| `hi_off_by_one` | all | `hi = n − 1`, so "insert at the end" (answer n) is unreachable |
| `counts_equal` | Py, JS | merge uses `<` instead of `<=`, so equal pairs count as inversions |
| `left_moves_back` | all | missing `max()`, so the window's left edge jumps backwards (`"abba"`) |
| `reset_window` | all | on a repeat, restarts the window at i instead of just past the old occurrence (`"dvdf"`) |

## Results (`python -m judge.study`)

All **16 correct solutions pass every suite**. For the **32 seeded bugs**:

| Test suite | Bugs it catches | Bugs only it catches first |
|---|---|---|
| examples (from the statement) | **0/32 (0%)** | 0 |
| edge cases | 22/32 (69%) | 22 |
| random differential (vs brute force) | 22/32 (69%) | 0 |
| stress (n = 200,000) | 18/32 (56%) | **10** |
| *survives everything* | | **0** |

Full matrix: [`results/summary.md`](results/summary.md).

**What it shows**
1. **Passing the examples means little.** By construction these bugs are the kind that pass a statement's examples, and all 32 did. That's the realistic failure mode when judging code by "it works on the sample".
2. **Edge cases and differential testing find logic bugs; only scale finds the rest.** All 10 complexity and overflow bugs passed the edge and random suites (small n) and failed only at n = 200,000.
3. **…but a single large random test misses most logic bugs.** `zero_init`, `last_occurrence`, `counts_equal` and `reset_window` all *passed* the stress test, because random data almost never hits the boundary that triggers them. You need both kinds of test.
4. **Correctness is language-dependent.** The identical Kadane and merge-sort logic with a 32-bit accumulator is wrong in Java and C++ (n = 200,000 → about 2×10¹⁰ inversions), while the Python and JavaScript versions are safe: Python has big integers, and JS doubles are exact to 2⁵³.

## Limitations
- Four classic problems; the bugs are hand-seeded, not mined from real submissions.
- The "examples catch 0%" result follows from choosing bugs that pass the examples. The interesting numbers are the *edge vs random vs stress* split.
- Time limits are wall-clock on one machine (JVM start-up included), not CPU-time with memory limits.

## License
MIT
