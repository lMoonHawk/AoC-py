def get_area():
    with open("2020/data/day_11.txt") as f:
        return [[char for char in line.strip()] for line in f.readlines()]


def adjacent(grid, i, j):
    max_rows = len(grid)
    max_cols = len(grid[0])
    count = 0

    # 3x3 square of neighbors
    for k in range(9):
        o_i = int(k / 3) - 1
        o_j = k % 3 - 1

        if o_i == 0 and o_j == 0:
            continue
        if i + o_i < 0 or i + o_i >= max_rows:
            continue
        if j + o_j < 0 or j + o_j >= max_cols:
            continue
        if grid[i + o_i][j + o_j] == "#":
            count += 1

    return count


def see(grid, i, j, inc_i, inc_j):
    max_rows = len(grid)
    max_cols = len(grid[0])
    while True:
        i += inc_i
        j += inc_j

        # Out of bounds
        if i < 0 or i >= max_rows or j < 0 or j >= max_cols:
            return 0

        cell = grid[i][j]
        if cell == "#":
            return 1
        if cell == "L":
            return 0


def seen(grid, i, j):
    count = 0
    for k in range(9):
        o_i = int(k / 3) - 1
        o_j = k % 3 - 1
        if o_i == 0 and o_j == 0:
            continue
        count += see(grid, i, j, o_i, o_j)
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


def part1():
    next_grid = None
    area = get_area()
    i = 0
    while next_grid != area:
        if not next_grid:
            next_grid = [row[:] for row in area]

        area = next_grid
        next_grid = next_round(grid=area, method=adjacent, threshold=4)
        i += 1

    answer = sum(row.count("#") for row in next_grid)
    print(answer)


def part2():
    next_grid = None
    area = get_area()
    i = 0
    while next_grid != area:
        if not next_grid:
            next_grid = [row[:] for row in area]

        area = next_grid
        next_grid = next_round(grid=area, method=seen, threshold=5)
        i += 1

    answer = sum(row.count("#") for row in next_grid)
    print(answer)


if __name__ == "__main__":
    part1()
    part2()
