"""Solutions: one correct version + two seeded "plausible but wrong" variants per (problem, language).

Each language has an I/O harness with a {SOLVE} slot; each variant supplies the solve() function. Keeping the
variants as whole functions makes the bug easy to read in `python -m judge.export` output (solutions/ folder).
"""

HARNESS = {
    "python": """import sys

{SOLVE}

def main():
    lines = sys.stdin.read().split("\\n")
    t = int(lines[0])
    print("\\n".join(str(solve(lines[i])) for i in range(1, t + 1)))

main()
""",
    "javascript": """const lines = require("fs").readFileSync(0, "utf8").split("\\n");

{SOLVE}

const t = parseInt(lines[0], 10);
const out = [];
for (let i = 1; i <= t; i++) out.push(String(solve(lines[i])));
console.log(out.join("\\n"));
""",
    "java": """import java.io.*;
import java.util.*;

public class Main {
{SOLVE}

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in), 1 << 16);
        int t = Integer.parseInt(br.readLine().trim());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < t; i++) sb.append(solve(br.readLine())).append('\\n');
        System.out.print(sb);
    }
}
""",
    "cpp": """#include <bits/stdc++.h>
using namespace std;

{SOLVE}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string line;
    getline(cin, line);
    int t = stoi(line);
    for (int i = 0; i < t; i++) {
        getline(cin, line);
        cout << solve(line) << "\\n";
    }
}
""",
}

S = {}  # (problem, lang) -> {variant: (description, solve_code)}

# ------------------------------------------------------------------ max_subarray
S["max_subarray", "python"] = {
    "correct": ("Kadane", """def solve(line):
    a = list(map(int, line.split()))[1:]
    best = cur = a[0]
    for x in a[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best"""),
    "zero_init": ("Kadane initialised at 0: returns 0 when every element is negative", """def solve(line):
    a = list(map(int, line.split()))[1:]
    best = cur = 0
    for x in a:
        cur = max(0, cur + x)
        best = max(best, cur)
    return best"""),
    "quadratic": ("Correct but O(n^2): every subarray", """def solve(line):
    a = list(map(int, line.split()))[1:]
    best = a[0]
    for i in range(len(a)):
        s = 0
        for j in range(i, len(a)):
            s += a[j]
            best = max(best, s)
    return best"""),
}
S["max_subarray", "javascript"] = {
    "correct": ("Kadane", """function solve(line) {
  const a = line.trim().split(/\\s+/).map(Number).slice(1);
  let best = a[0], cur = a[0];
  for (let i = 1; i < a.length; i++) {
    cur = Math.max(a[i], cur + a[i]);
    best = Math.max(best, cur);
  }
  return best;
}"""),
    "zero_init": ("Kadane initialised at 0: returns 0 when every element is negative", """function solve(line) {
  const a = line.trim().split(/\\s+/).map(Number).slice(1);
  let best = 0, cur = 0;
  for (const x of a) {
    cur = Math.max(0, cur + x);
    best = Math.max(best, cur);
  }
  return best;
}"""),
    "quadratic": ("Correct but O(n^2): every subarray", """function solve(line) {
  const a = line.trim().split(/\\s+/).map(Number).slice(1);
  let best = a[0];
  for (let i = 0; i < a.length; i++) {
    let s = 0;
    for (let j = i; j < a.length; j++) { s += a[j]; best = Math.max(best, s); }
  }
  return best;
}"""),
}
S["max_subarray", "java"] = {
    "correct": ("Kadane with long accumulators", """    static String solve(String line) {
        StringTokenizer st = new StringTokenizer(line);
        int n = Integer.parseInt(st.nextToken());
        long best = Long.parseLong(st.nextToken()), cur = best;
        for (int i = 1; i < n; i++) {
            long x = Long.parseLong(st.nextToken());
            cur = Math.max(x, cur + x);
            best = Math.max(best, cur);
        }
        return Long.toString(best);
    }"""),
    "zero_init": ("Kadane initialised at 0: returns 0 when every element is negative", """    static String solve(String line) {
        StringTokenizer st = new StringTokenizer(line);
        int n = Integer.parseInt(st.nextToken());
        long best = 0, cur = 0;
        for (int i = 0; i < n; i++) {
            long x = Long.parseLong(st.nextToken());
            cur = Math.max(0, cur + x);
            best = Math.max(best, cur);
        }
        return Long.toString(best);
    }"""),
    "int_overflow": ("Kadane with int accumulators: overflows once sums exceed 2^31", """    static String solve(String line) {
        StringTokenizer st = new StringTokenizer(line);
        int n = Integer.parseInt(st.nextToken());
        int best = Integer.parseInt(st.nextToken()), cur = best;
        for (int i = 1; i < n; i++) {
            int x = Integer.parseInt(st.nextToken());
            cur = Math.max(x, cur + x);
            best = Math.max(best, cur);
        }
        return Integer.toString(best);
    }"""),
}
S["max_subarray", "cpp"] = {
    "correct": ("Kadane with long long accumulators", """string solve(const string& line) {
    istringstream in(line);
    int n; in >> n;
    long long best, cur, x;
    in >> best; cur = best;
    for (int i = 1; i < n; i++) { in >> x; cur = max(x, cur + x); best = max(best, cur); }
    return to_string(best);
}"""),
    "zero_init": ("Kadane initialised at 0: returns 0 when every element is negative", """string solve(const string& line) {
    istringstream in(line);
    int n; in >> n;
    long long best = 0, cur = 0, x;
    for (int i = 0; i < n; i++) { in >> x; cur = max(0LL, cur + x); best = max(best, cur); }
    return to_string(best);
}"""),
    "int_overflow": ("Kadane with int accumulators: overflows once sums exceed 2^31", """string solve(const string& line) {
    istringstream in(line);
    int n; in >> n;
    int best, cur, x;
    in >> best; cur = best;
    for (int i = 1; i < n; i++) { in >> x; cur = max(x, cur + x); best = max(best, cur); }
    return to_string(best);
}"""),
}

# ------------------------------------------------------------------ lower_bound
LB = {
    "python": {
        "correct": ("Binary search for first index with a[i] >= t", """def solve(line):
    v = list(map(int, line.split()))
    n, t, a = v[0], v[1], v[2:]
    lo, hi = 0, n
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < t:
            lo = mid + 1
        else:
            hi = mid
    return lo"""),
        "last_occurrence": ("Returns the LAST index of t when t repeats (upper bound - 1)", """def solve(line):
    v = list(map(int, line.split()))
    n, t, a = v[0], v[1], v[2:]
    lo, hi = 0, n
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] <= t:
            lo = mid + 1
        else:
            hi = mid
    return lo - 1 if lo > 0 and a[lo - 1] == t else lo"""),
        "hi_off_by_one": ("hi starts at n-1: answer n (t larger than every element) is unreachable", """def solve(line):
    v = list(map(int, line.split()))
    n, t, a = v[0], v[1], v[2:]
    lo, hi = 0, n - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < t:
            lo = mid + 1
        else:
            hi = mid
    return lo"""),
    },
}
S["lower_bound", "python"] = LB["python"]
S["lower_bound", "javascript"] = {
    "correct": ("Binary search for first index with a[i] >= t", """function solve(line) {
  const v = line.trim().split(/\\s+/).map(Number);
  const n = v[0], t = v[1];
  let lo = 0, hi = n;
  while (lo < hi) {
    const mid = (lo + hi) >> 1;
    if (v[2 + mid] < t) lo = mid + 1; else hi = mid;
  }
  return lo;
}"""),
    "last_occurrence": ("Returns the LAST index of t when t repeats (upper bound - 1)", """function solve(line) {
  const v = line.trim().split(/\\s+/).map(Number);
  const n = v[0], t = v[1];
  let lo = 0, hi = n;
  while (lo < hi) {
    const mid = (lo + hi) >> 1;
    if (v[2 + mid] <= t) lo = mid + 1; else hi = mid;
  }
  return lo > 0 && v[2 + lo - 1] === t ? lo - 1 : lo;
}"""),
    "hi_off_by_one": ("hi starts at n-1: answer n (t larger than every element) is unreachable", """function solve(line) {
  const v = line.trim().split(/\\s+/).map(Number);
  const n = v[0], t = v[1];
  let lo = 0, hi = n - 1;
  while (lo < hi) {
    const mid = (lo + hi) >> 1;
    if (v[2 + mid] < t) lo = mid + 1; else hi = mid;
  }
  return lo;
}"""),
}
_JAVA_LB = """    static String solve(String line) {
        StringTokenizer st = new StringTokenizer(line);
        int n = Integer.parseInt(st.nextToken());
        int t = Integer.parseInt(st.nextToken());
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = Integer.parseInt(st.nextToken());
        int lo = 0, hi = HI;
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (a[mid] CMP t) lo = mid + 1; else hi = mid;
        }
        RET
    }"""
S["lower_bound", "java"] = {
    "correct": ("Binary search for first index with a[i] >= t",
                _JAVA_LB.replace("HI", "n").replace("CMP", "<").replace("RET", "return Integer.toString(lo);")),
    "last_occurrence": ("Returns the LAST index of t when t repeats (upper bound - 1)",
                        _JAVA_LB.replace("HI", "n").replace("CMP", "<=").replace(
                            "RET", "return Integer.toString(lo > 0 && a[lo - 1] == t ? lo - 1 : lo);")),
    "hi_off_by_one": ("hi starts at n-1: answer n (t larger than every element) is unreachable",
                      _JAVA_LB.replace("HI", "n - 1").replace("CMP", "<").replace("RET", "return Integer.toString(lo);")),
}
_CPP_LB = """string solve(const string& line) {
    istringstream in(line);
    int n, t; in >> n >> t;
    vector<int> a(n);
    for (auto& x : a) in >> x;
    int lo = 0, hi = HI;
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (a[mid] CMP t) lo = mid + 1; else hi = mid;
    }
    RET
}"""
S["lower_bound", "cpp"] = {
    "correct": ("Binary search for first index with a[i] >= t",
                _CPP_LB.replace("HI", "n").replace("CMP", "<").replace("RET", "return to_string(lo);")),
    "last_occurrence": ("Returns the LAST index of t when t repeats (upper bound - 1)",
                        _CPP_LB.replace("HI", "n").replace("CMP", "<=").replace(
                            "RET", "return to_string(lo > 0 && a[lo - 1] == t ? lo - 1 : lo);")),
    "hi_off_by_one": ("hi starts at n-1: answer n (t larger than every element) is unreachable",
                      _CPP_LB.replace("HI", "n - 1").replace("CMP", "<").replace("RET", "return to_string(lo);")),
}

# ------------------------------------------------------------------ inversions
S["inversions", "python"] = {
    "correct": ("Merge sort counting inversions, O(n log n)", """def solve(line):
    a = list(map(int, line.split()))[1:]
    def sort(xs):
        if len(xs) <= 1:
            return xs, 0
        m = len(xs) // 2
        left, cl = sort(xs[:m])
        right, cr = sort(xs[m:])
        out, i, j, c = [], 0, 0, cl + cr
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                out.append(left[i]); i += 1
            else:
                out.append(right[j]); j += 1; c += len(left) - i
        out += left[i:] + right[j:]
        return out, c
    return sort(a)[1]"""),
    "quadratic": ("Correct but O(n^2): checks every pair", """def solve(line):
    a = list(map(int, line.split()))[1:]
    return sum(1 for i in range(len(a)) for j in range(i + 1, len(a)) if a[i] > a[j])"""),
    "counts_equal": ("Merge uses < instead of <=, so equal elements are counted as inversions", """def solve(line):
    a = list(map(int, line.split()))[1:]
    def sort(xs):
        if len(xs) <= 1:
            return xs, 0
        m = len(xs) // 2
        left, cl = sort(xs[:m])
        right, cr = sort(xs[m:])
        out, i, j, c = [], 0, 0, cl + cr
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                out.append(left[i]); i += 1
            else:
                out.append(right[j]); j += 1; c += len(left) - i
        out += left[i:] + right[j:]
        return out, c
    return sort(a)[1]"""),
}
_JS_INV = """function solve(line) {
  const a = line.trim().split(/\\s+/).map(Number).slice(1);
  const tmp = new Array(a.length);
  function sort(lo, hi) {
    if (hi - lo <= 1) return 0;
    const m = (lo + hi) >> 1;
    let c = sort(lo, m) + sort(m, hi), i = lo, j = m, k = lo;
    while (i < m && j < hi) {
      if (a[i] CMP a[j]) tmp[k++] = a[i++];
      else { tmp[k++] = a[j++]; c += m - i; }
    }
    while (i < m) tmp[k++] = a[i++];
    while (j < hi) tmp[k++] = a[j++];
    for (let p = lo; p < hi; p++) a[p] = tmp[p];
    return c;
  }
  return sort(0, a.length);
}"""
S["inversions", "javascript"] = {
    "correct": ("Merge sort counting inversions, O(n log n)", _JS_INV.replace("CMP", "<=")),
    "quadratic": ("Correct but O(n^2): checks every pair", """function solve(line) {
  const a = line.trim().split(/\\s+/).map(Number).slice(1);
  let c = 0;
  for (let i = 0; i < a.length; i++) for (let j = i + 1; j < a.length; j++) if (a[i] > a[j]) c++;
  return c;
}"""),
    "counts_equal": ("Merge uses < instead of <=, so equal elements are counted as inversions", _JS_INV.replace("CMP", "<")),
}
_JAVA_INV = """    static int[] tmp;
    static TYPE sort(int[] a, int lo, int hi) {
        if (hi - lo <= 1) return 0;
        int m = (lo + hi) >>> 1;
        TYPE c = sort(a, lo, m) + sort(a, m, hi);
        int i = lo, j = m, k = lo;
        while (i < m && j < hi) {
            if (a[i] <= a[j]) tmp[k++] = a[i++];
            else { tmp[k++] = a[j++]; c += m - i; }
        }
        while (i < m) tmp[k++] = a[i++];
        while (j < hi) tmp[k++] = a[j++];
        for (int p = lo; p < hi; p++) a[p] = tmp[p];
        return c;
    }
    static String solve(String line) {
        StringTokenizer st = new StringTokenizer(line);
        int n = Integer.parseInt(st.nextToken());
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = Integer.parseInt(st.nextToken());
        tmp = new int[n];
        return String.valueOf(sort(a, 0, n));
    }"""
S["inversions", "java"] = {
    "correct": ("Merge sort counting inversions in a long, O(n log n)", _JAVA_INV.replace("TYPE", "long")),
    "quadratic": ("Correct but O(n^2): checks every pair", """    static String solve(String line) {
        StringTokenizer st = new StringTokenizer(line);
        int n = Integer.parseInt(st.nextToken());
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = Integer.parseInt(st.nextToken());
        long c = 0;
        for (int i = 0; i < n; i++) for (int j = i + 1; j < n; j++) if (a[i] > a[j]) c++;
        return Long.toString(c);
    }"""),
    "int_overflow": ("Merge sort with an int counter: overflows past 2^31 inversions", _JAVA_INV.replace("TYPE", "int")),
}
_CPP_INV = """vector<int> tmpv;
TYPE sortc(vector<int>& a, int lo, int hi) {
    if (hi - lo <= 1) return 0;
    int m = (lo + hi) / 2;
    TYPE c = sortc(a, lo, m) + sortc(a, m, hi);
    int i = lo, j = m, k = lo;
    while (i < m && j < hi) {
        if (a[i] <= a[j]) tmpv[k++] = a[i++];
        else { tmpv[k++] = a[j++]; c += m - i; }
    }
    while (i < m) tmpv[k++] = a[i++];
    while (j < hi) tmpv[k++] = a[j++];
    for (int p = lo; p < hi; p++) a[p] = tmpv[p];
    return c;
}
string solve(const string& line) {
    istringstream in(line);
    int n; in >> n;
    vector<int> a(n);
    for (auto& x : a) in >> x;
    tmpv.assign(n, 0);
    return to_string(sortc(a, 0, n));
}"""
S["inversions", "cpp"] = {
    "correct": ("Merge sort counting inversions in a long long, O(n log n)", _CPP_INV.replace("TYPE", "long long")),
    "quadratic": ("Correct but O(n^2): checks every pair", """string solve(const string& line) {
    istringstream in(line);
    int n; in >> n;
    vector<int> a(n);
    for (auto& x : a) in >> x;
    long long c = 0;
    for (int i = 0; i < n; i++) for (int j = i + 1; j < n; j++) if (a[i] > a[j]) c++;
    return to_string(c);
}"""),
    "int_overflow": ("Merge sort with an int counter: overflows past 2^31 inversions", _CPP_INV.replace("TYPE", "int")),
}

# ------------------------------------------------------------------ unique_substring
S["unique_substring", "python"] = {
    "correct": ("Sliding window; left only moves forward", """def solve(line):
    s = line.strip()
    last, left, best = {}, 0, 0
    for i, c in enumerate(s):
        if c in last:
            left = max(left, last[c] + 1)
        last[c] = i
        best = max(best, i - left + 1)
    return best"""),
    "left_moves_back": ("Missing max(): left can jump BACKWARDS to an old occurrence ('abba')", """def solve(line):
    s = line.strip()
    last, left, best = {}, 0, 0
    for i, c in enumerate(s):
        if c in last:
            left = last[c] + 1
        last[c] = i
        best = max(best, i - left + 1)
    return best"""),
    "reset_window": ("On a repeat, restarts the window at i instead of after the old occurrence ('dvdf')", """def solve(line):
    s = line.strip()
    last, left, best = {}, 0, 0
    for i, c in enumerate(s):
        if c in last and last[c] >= left:
            left = i
        last[c] = i
        best = max(best, i - left + 1)
    return best"""),
}
_JS_U = """function solve(line) {
  const s = line.trim();
  const last = new Map();
  let left = 0, best = 0;
  for (let i = 0; i < s.length; i++) {
    const c = s[i];
    BODY
    last.set(c, i);
    best = Math.max(best, i - left + 1);
  }
  return best;
}"""
S["unique_substring", "javascript"] = {
    "correct": ("Sliding window; left only moves forward",
                _JS_U.replace("BODY", "if (last.has(c)) left = Math.max(left, last.get(c) + 1);")),
    "left_moves_back": ("Missing max(): left can jump BACKWARDS to an old occurrence ('abba')",
                        _JS_U.replace("BODY", "if (last.has(c)) left = last.get(c) + 1;")),
    "reset_window": ("On a repeat, restarts the window at i instead of after the old occurrence ('dvdf')",
                     _JS_U.replace("BODY", "if (last.has(c) && last.get(c) >= left) left = i;")),
}
_JAVA_U = """    static String solve(String line) {
        String s = line.trim();
        int[] last = new int[128];
        Arrays.fill(last, -1);
        int left = 0, best = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            BODY
            last[c] = i;
            best = Math.max(best, i - left + 1);
        }
        return Integer.toString(best);
    }"""
S["unique_substring", "java"] = {
    "correct": ("Sliding window; left only moves forward",
                _JAVA_U.replace("BODY", "if (last[c] >= 0) left = Math.max(left, last[c] + 1);")),
    "left_moves_back": ("Missing max(): left can jump BACKWARDS to an old occurrence ('abba')",
                        _JAVA_U.replace("BODY", "if (last[c] >= 0) left = last[c] + 1;")),
    "reset_window": ("On a repeat, restarts the window at i instead of after the old occurrence ('dvdf')",
                     _JAVA_U.replace("BODY", "if (last[c] >= left) left = i;")),
}
_CPP_U = """string solve(const string& line) {
    string s = line;
    while (!s.empty() && (s.back() == '\\r' || s.back() == ' ')) s.pop_back();
    vector<int> last(128, -1);
    int left = 0, best = 0;
    for (int i = 0; i < (int)s.size(); i++) {
        int c = s[i];
        BODY
        last[c] = i;
        best = max(best, i - left + 1);
    }
    return to_string(best);
}"""
S["unique_substring", "cpp"] = {
    "correct": ("Sliding window; left only moves forward",
                _CPP_U.replace("BODY", "if (last[c] >= 0) left = max(left, last[c] + 1);")),
    "left_moves_back": ("Missing max(): left can jump BACKWARDS to an old occurrence ('abba')",
                        _CPP_U.replace("BODY", "if (last[c] >= 0) left = last[c] + 1;")),
    "reset_window": ("On a repeat, restarts the window at i instead of after the old occurrence ('dvdf')",
                     _CPP_U.replace("BODY", "if (last[c] >= left) left = i;")),
}


def source(problem: str, lang: str, variant: str) -> str:
    return HARNESS[lang].replace("{SOLVE}", S[problem, lang][variant][1])
