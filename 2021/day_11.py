def grid_ini():
    with open("2021/data/day_11.txt") as f:
        return [[int(energy) for energy in row.strip()] for row in f]


def flashes(grid):
    step = 0
    while True:
        step += 1
        flash_cnt = 0
        for i, row in enumerate(grid):
            for j, _ in enumerate(row):
                grid[i][j] += 1

        stabilised = False
        while not stabilised:
            stabilised = True
            for i, row in enumerate(grid):
                for j, energy in enumerate(row):
                    if grid[i][j] > 9:
                        stabilised = False
                        flash_cnt += 1
                        grid[i][j] = 0
                        for ni, nj in [(i + mi, j + mj) for mi in range(-1, 2) for mj in range(-1, 2)]:
                            if (ni, nj) == (i, j):
                                continue
                            if not (0 <= ni < len(grid) and 0 <= nj < len(grid[0])):
                                continue
                            if grid[ni][nj] == 0:
                                continue
                            grid[ni][nj] += 1
        yield flash_cnt


def part1():
    flash_counts = flashes(grid_ini())
    return sum(next(flash_counts) for _ in range(100))


def part2():
    grid = grid_ini()
    flash_counts = flashes(grid)
    step = 0
    while True:
        step += 1
        if next(flash_counts) == len(grid) * len(grid[0]):
            return step


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
