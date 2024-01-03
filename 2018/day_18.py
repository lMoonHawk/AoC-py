GRID = 50


def get_area_ini():
    with open("2018/data/day_18.txt") as f:
        return [el for line in f.readlines() for el in list(line.strip())]


def count_neigh(area, x, y):
    neighbors = {".": 0, "#": 0, "|": 0}
    for nx, ny in ((x + i, y + j) for i in range(-1, 2) for j in range(-1, 2) if (i, j) != (0, 0)):
        if not (0 <= nx < GRID and 0 <= ny < GRID):
            continue
        neighbors[area[GRID * ny + nx]] += 1
    return neighbors


def change(area):
    next_area = [row[:] for row in area]
    for y in range(GRID):
        for x in range(GRID):
            acre = area[GRID * y + x]
            neigh = count_neigh(area, x, y)
            if acre == "." and neigh["|"] >= 3:
                next_area[GRID * y + x] = "|"
            elif acre == "|" and neigh["#"] >= 3:
                next_area[GRID * y + x] = "#"
            elif acre == "#" and (neigh["#"] == 0 or neigh["|"] == 0):
                next_area[GRID * y + x] = "."
    return next_area


def find_seq(arr):
    for i in range(2, len(arr) // 3):
        if arr[-1] == arr[-1 - i] == arr[-1 - 2 * i]:
            return i
    return 0


def get_val(area):
    trees = yards = 0
    for cell in area:
        if cell == "|":
            trees += 1
        if cell == "#":
            yards += 1
    return yards * trees


def part1():
    area = get_area_ini()
    for _ in range(10):
        area = change(area)
    return area.count("|") * area.count("#")


def part2():
    area = get_area_ini()
    values = []
    k = 0
    while True:
        k += 1
        area = change(area)
        values.append(area.count("|") * area.count("#"))
        if cycle_size := find_seq(values):
            return values[-cycle_size:][(1_000_000_000 - k - 1) % cycle_size]


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
