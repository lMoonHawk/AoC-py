with open("2016/data/day_01.txt") as f:
    instructions = f.readline().strip().split(", ")


def part1():
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    x, y, facing = 0, 0, 0
    for instruction in instructions:
        turn, steps = instruction[0], instruction[1:]
        steps = int(steps)
        if turn == "R":
            facing = (facing + 1) % 4
        elif turn == "L":
            facing = (facing - 1) % 4
        mx, my = directions[facing]
        x, y = x + steps * mx, y + steps * my
    return abs(x) + abs(y)


def part2():
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    visited = set((0, 0))
    x, y, facing = 0, 0, 0
    for instruction in instructions:
        turn, steps = instruction[0], instruction[1:]
        steps = int(steps)
        if turn == "R":
            facing = (facing + 1) % 4
        elif turn == "L":
            facing = (facing - 1) % 4
        mx, my = directions[facing]
        for _ in range(steps):
            x, y = x + mx, y + my
            if (x, y) in visited:
                return abs(x) + abs(y)
            visited.add((x, y))


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
