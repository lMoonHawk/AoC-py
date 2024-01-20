with open("2016/data/day_02.txt") as f:
    instructions = [line.strip() for line in f.readlines()]


def part1():
    code = ""
    keypad = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    x, y = 1, 1
    directions = {"L": (-1, 0), "R": (1, 0), "U": (0, -1), "D": (0, 1)}
    for instruction in instructions:
        for direction in instruction:
            mx, my = directions[direction]
            if 0 <= y + my < len(keypad) and 0 <= x + mx < len(keypad[y + my]):
                x, y = x + mx, y + my
        code += keypad[y][x]
    return code


def part2():
    code = ""
    keypad = [
        ["", "", "1", "", ""],
        ["", "2", "3", "4", ""],
        ["5", "6", "7", "8", "9"],
        ["", "A", "B", "C", ""],
        ["", "", "D", "", ""],
    ]
    x, y = 0, 2
    directions = {"L": (-1, 0), "R": (1, 0), "U": (0, -1), "D": (0, 1)}
    for instruction in instructions:
        for direction in instruction:
            mx, my = directions[direction]
            if 0 <= y + my < len(keypad) and 0 <= x + mx < len(keypad[y + my]):
                if keypad[y + my][x + mx]:
                    x, y = x + mx, y + my
        code += keypad[y][x]
    return code


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
