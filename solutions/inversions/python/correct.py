import sys

def solve(line):
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
    return sort(a)[1]

def main():
    lines = sys.stdin.read().split("\n")
    t = int(lines[0])
    print("\n".join(str(solve(lines[i])) for i in range(1, t + 1)))

main()
