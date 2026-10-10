import sys

def solve(line):
    a = list(map(int, line.split()))[1:]
    return sum(1 for i in range(len(a)) for j in range(i + 1, len(a)) if a[i] > a[j])

def main():
    lines = sys.stdin.read().split("\n")
    t = int(lines[0])
    print("\n".join(str(solve(lines[i])) for i in range(1, t + 1)))

main()
