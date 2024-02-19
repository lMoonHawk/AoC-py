def course():
    with open("2021/data/day_02.txt") as f:
        yield from ((inst, int(val)) for inst, val in (line.split() for line in f))


def part1():
    counter = {"forward": 0, "down": 0, "up": 0}
    for inst, val in course():
        counter[inst] += val
    return counter["forward"] * (counter["down"] - counter["up"])


def part2():
    depth = 0
    counter = {"forward": 0, "down": 0, "up": 0}
    for inst, val in course():
        counter[inst] += val
        if inst == "forward":
            depth += val * (counter["down"] - counter["up"])
    return counter["forward"] * depth


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
