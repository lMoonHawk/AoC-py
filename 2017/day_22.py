def state_init():
    with open("2017/data/day_22.txt") as f:
        grid = {(x, y): c for y, line in enumerate(f) for x, c in enumerate(line.strip())}
        middle = int(len(grid) ** 0.5) // 2
        return grid, (middle, middle)


directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def state(grid, x, y):
    if (x, y) not in grid:
        grid[(x, y)] = "."
    return grid[(x, y)]


def part1():
    grid, (x, y) = state_init()
    facing = 0
    count_infect = 0
    for _ in range(10_000):
        if state(grid, x, y) == "#":
            facing = (facing + 1) % 4
            grid[(x, y)] = "."
        else:
            facing = (facing - 1) % 4
            grid[(x, y)] = "#"
            count_infect += 1
        mx, my = directions[facing]
        x, y = x + mx, y + my
    return count_infect


def part2():
    grid, (x, y) = state_init()
    facing = 0
    count_infect = 0
    for _ in range(10_000_000):
        cell = state(grid, x, y)
        if cell == "#":
            facing = (facing + 1) % 4
            grid[(x, y)] = "F"
        elif cell == ".":
            facing = (facing - 1) % 4
            grid[(x, y)] = "W"
        elif cell == "W":
            grid[(x, y)] = "#"
            count_infect += 1
        elif cell == "F":
            facing = (facing + 2) % 4
            grid[(x, y)] = "."
        mx, my = directions[facing]
        x, y = x + mx, y + my
    return count_infect


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
