with open("2018/data/day_11.txt") as f:
    serial = int(f.readline().strip())


def get_power_level(x, y, serial):
    return int(str(((x + 10) * y + serial) * (x + 10))[-3]) - 5


def sqmat_cumsum(m):
    """Inplace cumulative sum for square matrices"""
    s = len(m)
    for k in range(1, s):
        m[0][k] += m[0][k - 1]
        m[k][0] += m[k - 1][0]
    for y in range(1, s):
        for x in range(1, s):
            m[y][x] += m[y - 1][x] + m[y][x - 1] - m[y - 1][x - 1]


def part1():
    size = 3
    grid = [[get_power_level(x + 1, y + 1, serial) for x in range(300)] for y in range(300)]
    largest = 0
    for y in range(0, 300 - size):
        for x in range(0, 300 - size):
            total = sum(sum(grid[r][x : x + size]) for r in range(y, y + size))
            if total > largest:
                largest = total
                b_x, b_y = x + 1, y + 1
    return f"{b_x},{b_y}"


def part2():
    grid_size = 300
    sqmat_cumsum(grid := [[get_power_level(x + 1, y + 1, serial) for x in range(grid_size)] for y in range(grid_size)])

    largest = None
    b_x = b_y = b_s = None
    for y in range(0, grid_size - 1):
        for x in range(0, grid_size - 1):
            for size in range(2, grid_size - max(x, y) + 1):
                power = grid[y + size - 1][x + size - 1]
                if x > 0:
                    power -= grid[y + size - 1][x - 1]
                if y > 0:
                    power -= grid[y - 1][x + size - 1]
                if x * y > 0:
                    power += grid[y - 1][x - 1]
                if largest is None or power > largest:
                    largest = power
                    b_x, b_y, b_s = x + 1, y + 1, size
    return f"{b_x},{b_y},{b_s}"


if __name__ == "__main__":
    print(part1())
    print(part2())
