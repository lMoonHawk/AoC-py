with open("2021/data/day_01.txt") as f:
    report = [int(val.strip()) for val in f]


def part1():
    return sum(report[k + 1] - report[k] > 0 for k in range(len(report) - 1))


def part2():
    return sum(report[k + 3] - report[k] > 0 for k in range(len(report) - 3))


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
