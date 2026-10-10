import sys

def solve(line):
    s = line.strip()
    last, left, best = {}, 0, 0
    for i, c in enumerate(s):
        if c in last and last[c] >= left:
            left = i
        last[c] = i
        best = max(best, i - left + 1)
    return best

def main():
    lines = sys.stdin.read().split("\n")
    t = int(lines[0])
    print("\n".join(str(solve(lines[i])) for i in range(1, t + 1)))

main()
