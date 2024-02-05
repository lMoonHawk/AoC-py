with open("2015/data/day_08.txt") as f:
    strings = [line.strip() for line in f]


def part1():
    return sum(len(string) - len(eval(string)) for string in strings)


def part2():
    return sum(2 + string.count('"') + string.count("\\") for string in strings)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
