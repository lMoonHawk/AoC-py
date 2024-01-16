def get_starting_values():
    with open("2017/data/day_15.txt") as f:
        return [int(line.split()[-1]) for line in f.readlines()]


def generator(val, fact, mult=1):
    while True:
        val = (val * fact) % 2147483647
        if val % mult == 0:
            yield val


def part1():
    start_a, start_b = get_starting_values()
    gen_a, gen_b = generator(start_a, 16807), generator(start_b, 48271)
    return sum((next(gen_a) & 0xFFFF) == (next(gen_b) & 0xFFFF) for _ in range(40_000_000))


def part2():
    start_a, start_b = get_starting_values()
    gen_a, gen_b = generator(start_a, 16807, 4), generator(start_b, 48271, 8)
    return sum((next(gen_a) & 0xFFFF) == (next(gen_b) & 0xFFFF) for _ in range(5_000_000))


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
