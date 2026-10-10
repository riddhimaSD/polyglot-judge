"""Problems, reference solutions (Python, brute force where possible) and test-suite generators.

I/O protocol for every language: first line T, then T lines (one test each); print T answers, one per line.
Test suites per problem:
  examples - the cases a problem statement would show
  edge     - hand-picked boundary cases
  random   - 300 small random cases, answers from a brute-force reference (differential testing)
  stress   - one large case (n = 200,000) that exposes O(n^2) time and 32-bit overflow
"""
from __future__ import annotations

import random
from bisect import bisect_left


def ref_max_subarray(a):            # brute force O(n^2) for small n
    return max(sum(a[i:j]) for i in range(len(a)) for j in range(i + 1, len(a) + 1))


def ref_lower_bound(a, t):
    return bisect_left(a, t)


def ref_inversions(a):
    return sum(1 for i in range(len(a)) for j in range(i + 1, len(a)) if a[i] > a[j])


def ref_unique(s):
    best = 0
    for i in range(len(s)):
        seen = set()
        for j in range(i, len(s)):
            if s[j] in seen:
                break
            seen.add(s[j])
            best = max(best, j - i + 1)
    return best


def _fmt(n, xs):
    return " ".join(map(str, [n, *xs]))


def suites(seed: int = 0) -> dict:
    rnd = random.Random(seed)
    P = {}

    # ---- max_subarray: "n a1..an" -> max non-empty subarray sum
    ex = [[-2, 1, -3, 4, -1, 2, 1, -5, 4], [1], [5, 4, -1, 7, 8]]
    edge = [[-3], [-5, -2, -9], [0, 0, 0], [10 ** 9, -1, 10 ** 9], [-1, 0, -2]]
    rand = [[rnd.randint(-20, 20) for _ in range(rnd.randint(1, 12))] for _ in range(300)]
    big = [rnd.randint(1, 10 ** 9) for _ in range(200_000)]
    P["max_subarray"] = {
        "examples": [(_fmt(len(a), a), ref_max_subarray(a)) for a in ex],
        "edge": [(_fmt(len(a), a), ref_max_subarray(a)) for a in edge],
        "random": [(_fmt(len(a), a), ref_max_subarray(a)) for a in rand],
        "stress": [(_fmt(len(big), big), sum(big))],
    }

    # ---- lower_bound: "n t a1..an" (sorted, may repeat) -> first index i with a[i] >= t
    ex = [([1, 3, 5, 6], 5), ([1, 3, 5, 6], 2), ([1, 3, 5, 6], 0)]
    edge = [([1, 3, 5, 6], 7), ([2, 2, 2, 2], 2), ([1, 2, 2, 2, 3], 2), ([5], 5), ([5], 6), ([1, 1, 2], 1)]
    rand = []
    for _ in range(300):
        a = sorted(rnd.randint(0, 10) for _ in range(rnd.randint(1, 12)))
        rand.append((a, rnd.randint(-1, 11)))
    big = sorted(rnd.randint(0, 10 ** 6) for _ in range(200_000))
    P["lower_bound"] = {k: [(_fmt(len(a), [t, *a]), ref_lower_bound(a, t)) for a, t in v]
                        for k, v in {"examples": ex, "edge": edge, "random": rand,
                                     "stress": [(big, 10 ** 6 + 1)]}.items()}

    # ---- inversions: "n a1..an" -> number of pairs i<j with a[i] > a[j]
    ex = [[2, 4, 1, 3, 5], [5, 4, 3, 2, 1], [1, 2, 3]]
    edge = [[1], [2, 2, 2], [3, 1, 2, 1], [1, 1, 0]]
    rand = [[rnd.randint(0, 6) for _ in range(rnd.randint(1, 12))] for _ in range(300)]
    n = 200_000
    big = list(range(n, 0, -1))
    P["inversions"] = {
        "examples": [(_fmt(len(a), a), ref_inversions(a)) for a in ex],
        "edge": [(_fmt(len(a), a), ref_inversions(a)) for a in edge],
        "random": [(_fmt(len(a), a), ref_inversions(a)) for a in rand],
        "stress": [(_fmt(n, big), n * (n - 1) // 2)],
    }

    # ---- unique_substring: "s" -> length of the longest substring without repeated characters
    ex = ["abcabcbb", "bbbbb", "pwwkew"]
    edge = ["a", "abba", "dvdf", "tmmzuxt", "au"]
    rand = ["".join(rnd.choice("abcd") for _ in range(rnd.randint(1, 12))) for _ in range(300)]
    big = "".join(rnd.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(200_000))
    P["unique_substring"] = {
        "examples": [(s, ref_unique(s)) for s in ex], "edge": [(s, ref_unique(s)) for s in edge],
        "random": [(s, ref_unique(s)) for s in rand],
        "stress": [(big, _fast_unique(big))],
    }
    return P


def _fast_unique(s):
    last, left, best = {}, 0, 0
    for i, c in enumerate(s):
        if c in last and last[c] >= left:
            left = last[c] + 1
        last[c] = i
        best = max(best, i - left + 1)
    return best
