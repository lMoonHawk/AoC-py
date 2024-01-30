with open("2016/data/day_19.txt") as f:
    n = int(f.read().strip())


def part1():
    # https://en.wikipedia.org/wiki/Josephus_problem#Solution
    p = 1
    while p <= n:
        p *= 2
    return (2 * n) - p + 1


def part2():
    # Get winner for n using n-1
    # Winner of round i+1 is next index if before the index of the gift, else next+1 since that number left a gap.
    index = 1
    for i in range(1, n):
        index = index % i + 1
        if index > (i + 1) // 2:
            index += 1
    return index


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
