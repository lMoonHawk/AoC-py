with open("2016/data/day_15.txt") as f:
    discs = [tuple([int(el[3]), int(el[11][:-1])]) for el in [line.split() for line in f]]


def get_timing(discs):
    t = 0
    while True:
        if all((t + ini_pos + sec + 1) % mod == 0 for sec, (mod, ini_pos) in enumerate(discs)):
            return t
        t += 1


def part1():
    return get_timing(discs)


def part2():
    new_discs = discs + [(11, 0)]
    return get_timing(new_discs)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
