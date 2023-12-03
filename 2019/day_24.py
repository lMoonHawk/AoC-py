def get_ini_state():
    with open("2019/data/day_24.txt") as f:
        return {(x, y, 0) for y, l in enumerate(f.readlines()) for x, cell in enumerate(l.strip()) if cell == "#"}


def hash_state(grid: set[tuple]) -> int:
    return sum(1 << (y * 5 + x) for y in range(5) for x in range(5) if (x, y, 0) in grid)


def get_neighbors(pos):
    x, y, _ = pos
    n = [(x - 1, y), (x, y - 1), (x, y + 1), (x + 1, y)]
    return ((n_x, n_y, 0) for n_x, n_y in n if 0 <= n_y < 5 and 0 <= n_x < 5)


def get_neighbors_rec(pos):
    x, y, z = pos
    for n_x, n_y in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if (x, y) == (n_x, n_y):
            continue

        if n_x == -1:
            yield 1, 2, z - 1
        elif n_x == 5:
            yield 3, 2, z - 1
        elif n_y == -1:
            yield 2, 1, z - 1
        elif n_y == 5:
            yield 2, 3, z - 1

        elif (n_x, n_y) == (2, 2):
            if (x, y) == (2, 1):
                yield from ((k, 0, z + 1) for k in range(5))
            elif (x, y) == (3, 2):
                yield from ((4, k, z + 1) for k in range(5))
            elif (x, y) == (2, 3):
                yield from ((k, 4, z + 1) for k in range(5))
            elif (x, y) == (1, 2):
                yield from ((0, k, z + 1) for k in range(5))

        else:
            yield n_x, n_y, z


def part1():
    bugs = get_ini_state()
    seen = set()

    while True:
        next_bugs = bugs.copy()
        for cell in ((x, y, 0) for y in range(5) for x in range(5)):
            nb = sum(n in bugs for n in get_neighbors(cell))

            if cell not in bugs and nb in [1, 2]:
                next_bugs.add(cell)
            elif cell in bugs and nb != 1:
                next_bugs.remove(cell)

        if (h := hash_state(next_bugs)) in seen:
            return h
        seen.add(h)

        bugs = next_bugs


def part2():
    bugs = get_ini_state()
    min_z = max_z = 0

    for _ in range(200):
        grid = ((x, y, z) for z in range(min_z - 1, max_z + 2) for y in range(5) for x in range(5) if (x, y) != (2, 2))
        next_bugs = bugs.copy()

        for cell in grid:
            nb = sum(n in bugs for n in get_neighbors_rec(cell))

            if cell not in bugs and nb in [1, 2]:
                next_bugs.add(cell)
                min_z = cell[2] if cell[2] < min_z else min_z
                max_z = cell[2] if cell[2] > max_z else max_z
            elif cell in bugs and nb != 1:
                next_bugs.remove(cell)

        bugs = next_bugs

    return len(bugs)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
