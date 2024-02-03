with open("2015/data/day_01.txt") as f:
    instructions = f.read().strip()


def part1():
    return 2 * instructions.count("(") - len(instructions)


def part2():
    floor = 0
    for position, instruction in enumerate(instructions):
        floor += 2 * (instruction == "(") - 1
        if floor == -1:
            return position + 1


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
