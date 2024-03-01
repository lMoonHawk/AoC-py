with open("2022/data/day_01.txt") as f:
    calories = sorted(sum(int(cal) for cal in elf.splitlines()) for elf in f.read().split("\n\n"))


def part1():
    return calories[-1]


def part2():
    return sum(sorted(calories)[-3:])


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
