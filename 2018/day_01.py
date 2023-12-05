def display():
    with open("2018/data/day_01.txt") as f:
        yield from (int(line.strip()) for line in f.readlines())


def part1():
    return sum(freq for freq in display())


def part2():
    seen = {0}
    total_freq = 0
    while True:
        for freq in display():
            total_freq += freq
            if total_freq in seen:
                return total_freq
            seen.add(total_freq)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
