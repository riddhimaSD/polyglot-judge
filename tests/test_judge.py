import pytest

from judge.catalog import S
from judge.problems import ref_unique, suites
from judge.study import judge_one

TESTS = suites(seed=0)


@pytest.mark.parametrize("problem,lang", [k for k in S])
def test_correct_solution_passes_everything(problem, lang):
    r = judge_one(problem, lang, "correct", TESTS)
    assert all(v == "AC" for v in r["suites"].values()), r


@pytest.mark.parametrize("lang", ["java", "cpp"])
def test_int_overflow_only_visible_at_scale(lang):
    r = judge_one("inversions", lang, "int_overflow", TESTS)["suites"]
    assert r["examples"] == r["edge"] == r["random"] == "AC" and r["stress"] == "WA"


def test_quadratic_times_out_only_on_stress():
    r = judge_one("max_subarray", "python", "quadratic", TESTS)["suites"]
    assert r["random"] == "AC" and r["stress"] == "TLE"


def test_references():
    assert ref_unique("abba") == 2 and ref_unique("dvdf") == 3
