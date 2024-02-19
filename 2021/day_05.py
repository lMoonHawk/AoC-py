with open("2021/data/day_05.txt") as f:
    lines = [[int(n) for line in row.split(" -> ") for n in line.split(",")] for row in f]


def sign(a: int) -> int:
    return 1 if a > 0 else -1 if a < 0 else 0


def count_overlaps(diags):
    grid = dict()
    for line in lines:
        x1, y1, x2, y2 = line
        if not diags and x1 != x2 and y1 != y2:
            continue
        length = max(abs(x2 - x1), abs(y2 - y1)) + 1
        for k in range(length):
            point = (x1 + k * sign(x2 - x1), y1 + k * sign(y2 - y1))
            if point not in grid:
                grid[point] = 0
            grid[point] += 1
    return sum(intersection > 1 for intersection in grid.values())


def part1():
    return count_overlaps(diags=False)


def part2():
    return count_overlaps(diags=True)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
