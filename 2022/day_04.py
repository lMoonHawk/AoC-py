with open("2022/data/day_04.txt") as f:
    pairs = [[int(n) for elf in pair.split(",") for n in elf.split("-")] for pair in f]


def part1():
    return sum((b_lo >= a_lo and b_hi <= a_hi) or (a_lo >= b_lo and a_hi <= b_hi) for a_lo, a_hi, b_lo, b_hi in pairs)


def part2():
    return sum((b_lo <= a_lo <= b_hi) or (a_lo <= b_lo <= a_hi) for a_lo, a_hi, b_lo, b_hi in pairs)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
