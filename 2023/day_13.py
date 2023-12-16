def pattern_gen():
    with open("2023/data/day_13.txt") as f:
        yield from (line.strip().split("\n") for line in f.read().split("\n\n"))


def col(arr, i):
    return [arr[r][i] for r in range(len(arr))]


def sym(pat, smudges):
    size = len(pat[0])
    for i in range(size - 1):
        sym = True
        diff = 0
        for k in range(min(i + 1, size - i - 1)):
            diff += sum(p1 != p2 for p1, p2 in zip(col(pat, i - k), col(pat, i + k + 1)))
            if diff > smudges:
                sym = False
                break
        if sym and diff == smudges:
            return i + 1

    size = len(pat)
    for i in range(size - 1):
        sym = True
        diff = 0
        for k in range(min(i + 1, size - i - 1)):
            diff += sum(p1 != p2 for p1, p2 in zip(pat[i - k], pat[i + k + 1]))
            if diff > smudges:
                sym = False
                break
        if sym and diff == smudges:
            return (i + 1) * 100

    return 0


def part1():
    return sum(sym(pattern, 0) for pattern in pattern_gen())


def part2():
    return sum(sym(pattern, 1) for pattern in pattern_gen())


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
