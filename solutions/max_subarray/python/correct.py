import sys

def solve(line):
    a = list(map(int, line.split()))[1:]
    best = cur = a[0]
    for x in a[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best

def main():
    lines = sys.stdin.read().split("\n")
    t = int(lines[0])
    print("\n".join(str(solve(lines[i])) for i in range(1, t + 1)))

main()
