def get_banks():
    with open("2017/data/day_06.txt") as f:
        return [int(bank) for bank in f.readline().split()]


def run_until_dups(banks):
    seen = set([tuple(banks)])
    steps = 0
    while True:
        index = banks.index(max(banks))
        blocks, banks[index] = banks[index], 0
        for k in range(blocks):
            banks[(index + k + 1) % len(banks)] += 1
        steps += 1
        if tuple(banks) in seen:
            return steps, banks
        seen.add(tuple(banks))


def part1():
    steps, _ = run_until_dups(get_banks())
    return steps


def part2():
    steps, banks = run_until_dups(get_banks())
    steps, _ = run_until_dups(banks)
    return steps


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
