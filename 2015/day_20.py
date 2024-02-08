with open("2015/data/day_20.txt") as f:
    num = int(f.read())


def part1():
    n = num // 10
    k = 2
    while True:
        if sum(i + k // i for i in range(1, int(k**0.5) + 1) if not k % i) >= n:
            return k
        k += 2


def part2():
    n, r = divmod(num, 11)
    n += r > 0
    k = 2
    while True:
        if sum(k // i for i in range(1, 50 + 1) if not k % i) >= n:
            return k
        k += 2


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
