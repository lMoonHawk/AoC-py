def get_instructions():
    with open("2015/data/day_06.txt") as f:
        for line in f:
            line = line.strip().split()
            if "toggle" in line:
                op = "toggle"
            elif "on" in line:
                op = "on"
            elif "off" in line:
                op = "off"
            start = [int(el) for el in line[-3].split(",")]
            end = [int(el) for el in line[-1].split(",")]
            yield op, start, end


def part1():
    grid = [[0 for _ in range(1_000)] for _ in range(1_000)]
    for op, start, end in get_instructions():
        if op == "off":
            row = [0 for _ in range(start[0], end[0] + 1)]
        elif op == "on":
            row = [1 for _ in range(start[0], end[0] + 1)]

        for y in range(start[1], end[1] + 1):
            if op == "toggle":
                row = [1 - l for l in grid[y][start[0] : end[0] + 1]]
            grid[y][start[0] : end[0] + 1] = row

    return sum(sum(row) for row in grid)


def part2():
    grid = [[0 for _ in range(1_000)] for _ in range(1_000)]
    for op, start, end in get_instructions():

        for y in range(start[1], end[1] + 1):
            if op == "toggle":
                row = [l + 2 for l in grid[y][start[0] : end[0] + 1]]
            elif op == "on":
                row = [l + 1 for l in grid[y][start[0] : end[0] + 1]]
            elif op == "off":
                row = [l - 1 if l >= 1 else 0 for l in grid[y][start[0] : end[0] + 1]]
            grid[y][start[0] : end[0] + 1] = row

    return sum(sum(row) for row in grid)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
