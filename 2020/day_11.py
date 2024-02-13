def get_area():
    with open("2020/data/day_11.txt") as f:
        return [list(line.strip()) for line in f.readlines()]


def adjacent(grid, i, j):
    count = 0
    for ni in range(i - 1, i + 2):
        for nj in range(j - 1, j + 2):
            if (ni, nj) == (i, j) or not (0 <= ni < len(grid) and 0 <= nj < len(grid[0])):
                continue
            count += grid[ni][nj] == "#"
    return count


def see(grid, i, j, inc_i, inc_j):
    while True:
        i += inc_i
        j += inc_j
        if not (0 <= i < len(grid) and 0 <= j < len(grid[0])):
            return 0
        if grid[i][j] == "#":
            return 1
        if grid[i][j] == "L":
            return 0


def seen(grid, i, j):
    count = 0
    for ni in range(-1, 2):
        for nj in range(-1, 2):
            count += see(grid, i, j, ni, nj) if (ni, nj) != (0, 0) else 0
    return count


def next_round(grid: list[list[str]], method, threshold: int) -> list[list[str]]:
    round_grid = [row[:] for row in grid]
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == ".":
                continue
            nb_adj_occupied = method(grid, i, j)
            if nb_adj_occupied == 0:
                round_grid[i][j] = "#"
            if nb_adj_occupied >= threshold:
                round_grid[i][j] = "L"

    return round_grid


def count_stable(method, threshold):
    next_grid = None
    area = get_area()
    while next_grid != area:
        if not next_grid:
            next_grid = [row[:] for row in area]
        area = next_grid
        next_grid = next_round(area, method, threshold)
    return sum(row.count("#") for row in next_grid)


def part1():
    return count_stable(adjacent, 4)


def part2():
    return count_stable(seen, 5)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
