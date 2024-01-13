with open("2017/data/day_01.txt") as f:
    n = f.readline().strip()


def matches(n, after):
    return sum(int(n[k]) for k in range(len(n)) if n[k] == n[(k + after) % len(n)])


def part1():
    return matches(n, 1)


def part2():
    return matches(n, len(n) // 2)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
