import sys

def solve(line):
    v = list(map(int, line.split()))
    n, t, a = v[0], v[1], v[2:]
    lo, hi = 0, n
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < t:
            lo = mid + 1
        else:
            hi = mid
    return lo

def main():
    lines = sys.stdin.read().split("\n")
    t = int(lines[0])
    print("\n".join(str(solve(lines[i])) for i in range(1, t + 1)))

main()
