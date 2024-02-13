def groups():
    with open("2020/data/day_06.txt") as f:
        yield from ([{ans for ans in per} for per in grp.split("\n")] for grp in f.read().strip().split("\n\n"))


def part1():
    return sum(len(set.union(*group)) for group in groups())


def part2():
    return sum(len(set.intersection(*group)) for group in groups())


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
