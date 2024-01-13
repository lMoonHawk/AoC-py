with open("2017/data/day_03.txt") as f:
    n = int(f.readline())


def sum_adjacent(memory, x, y):
    out = 0
    for nx, ny in ((nx, ny) for nx in range(x - 1, x + 2) for ny in range(y - 1, y + 2)):
        if (nx, ny) in memory:
            out += memory[(nx, ny)]
    return out


def part1():
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    k = inc = 0
    num, x, y = 1, 0, 0
    while True:
        mx, my = directions[k % 4]
        if (mx, my) in [(1, 0), (-1, 0)]:
            inc += 1
        for _ in range(inc):
            x, y = x + mx, y + my
            num += 1
            if num == n:
                return abs(x) + abs(y)
        k += 1


def part2():
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    k = inc = 0
    x, y = 0, 0
    grid = {(0, 0): 1}
    while True:
        mx, my = directions[k % 4]
        if (mx, my) in [(1, 0), (-1, 0)]:
            inc += 1
        for _ in range(inc):
            x, y = x + mx, y + my
            grid[(x, y)] = sum_adjacent(grid, x, y)
            if grid[(x, y)] >= n:
                return grid[(x, y)]
        k += 1


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
