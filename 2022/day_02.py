def guide():
    with open("2022/data/day_02.txt") as f:
        yield from (("ABC".index(o), "XYZ".index(p)) for o, p in (line.split() for line in f))


def part1():
    return sum(p + 1 + ((o + 1) % 3 == p) * 6 + (o == p) * 3 for o, p in guide())


def part2():
    # (outcome + 2) % 3 gives the proper shape offset for the outcome
    # (o_shape + (outcome + 2) % 3) % 3 + 1 applies the offset to the opponent shape to get the player shape
    return sum((o_shape + (outcome + 2) % 3) % 3 + 1 + outcome * 3 for o_shape, outcome in guide())


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
