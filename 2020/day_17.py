def parse_input():
    pocket_dim = dict()
    size = [[0, 0, 0, 0]]
    with open("2020/data/day_17.txt") as f:
        for row, line in enumerate(f):
            for col, state in enumerate(line.strip()):
                pocket_dim[(col, row, 0, 0)] = 0 if state == "." else 1
    size.append([col, row, 0, 0])
    return pocket_dim, size


def get_neighbors(coord, dim):
    """Returns a generator listing all the neigbors of a cube given a dimension"""
    x, y, z, w = coord
    r = [-1, 0, 1]
    r_w = r if dim == 4 else [0]
    return ((a + x, b + y, c + z, w + d) for a in r for b in r for c in r for d in r_w)


def expend(size, dim):
    """Returns the new bounding coordinates of the pocket dimension, expending by one on all sides given the dimension"""
    bound_min, bound_max = size
    inc = [1, 1, 1, 1 if dim == 4 else 0]
    return [[v - k for v, k in zip(bound_min, inc)], [v + 1 for v, k in zip(bound_max, inc)]]


def next_cycle(grid, size, dim):
    grid_cycle = grid.copy()
    (x_min, y_min, z_min, w_min), (x_max, y_max, z_max, w_max) = size

    cubes = (
        (x, y, z, w)
        for x in range(x_min, x_max + 1)
        for y in range(y_min, y_max + 1)
        for z in range(z_min, z_max + 1)
        for w in range(w_min, w_max + 1)
    )
    for cube in cubes:
        state = grid[cube] if cube in grid else 0
        nb_neigh_act = sum(grid[n] for n in get_neighbors(cube, dim) if n in grid and n != cube)
        if (state == 1 and nb_neigh_act not in [2, 3]) or (state == 0 and nb_neigh_act == 3):
            grid_cycle[cube] = 1 - state

    return grid_cycle


def part1():
    pocket_dim, size = parse_input()
    for _ in range(6):
        size = expend(size, 3)
        pocket_dim = next_cycle(pocket_dim, size, 3)
    return sum(pocket_dim.values())


def part2():
    pocket_dim, size = parse_input()
    for _ in range(6):
        size = expend(size, 4)
        pocket_dim = next_cycle(pocket_dim, size, 4)
    return sum(pocket_dim.values())


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
