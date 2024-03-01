with open("2022/data/day_03.txt") as f:
    sacks = [line.strip() for line in f]


def priority(char):
    return ord(char) - (96 if char.islower() else 38)


def part1():
    return sum(priority(*set(sack[: len(sack) // 2]).intersection(sack[len(sack) // 2 :])) for sack in sacks)


def part2():
    return sum(priority(*(set(sacks[k]) & set(sacks[k + 1]) & set(sacks[k + 2]))) for k in range(0, len(sacks), 3))


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
