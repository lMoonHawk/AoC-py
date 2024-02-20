def signals():
    with open("2021/data/day_08.txt") as f:
        yield from ([section.split() for section in signal.split(" | ")] for signal in f)


# Digits with a unique number of segments, easily identifiable
uniques = {1: 2, 4: 4, 7: 3, 8: 7}
# Each other digits can be uniquely represented by the number of intersections with the "uniques"
# digit: [#common segments with 1, #common segments with 4, ...]
representations = {
    0: [2, 3, 3, 6],
    2: [1, 2, 2, 5],
    3: [2, 3, 3, 5],
    5: [1, 3, 2, 5],
    6: [1, 3, 2, 6],
    9: [2, 4, 3, 6],
}


def get_output(patterns, output):
    lookup = [None for _ in range(10)]
    # Find "uniques" and add to lookup
    for signal in patterns:
        for digit, segments in uniques.items():
            if len(signal) == segments:
                lookup[digit] = set(signal)
    # Find the other based on their intersection map and add to lookup
    for signal in patterns:
        identifier = [len(lookup[k].intersection(set(signal))) for k in uniques]
        for digit, representation in representations.items():
            if identifier == representation:
                lookup[digit] = set(signal)
    return int("".join(str(lookup.index(set(signal))) for signal in output))


def part1():
    return sum(sum(len(signal) in [2, 3, 4, 7] for signal in output) for _, output in signals())


def part2():
    return sum(get_output(patterns, output) for patterns, output in signals())


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
