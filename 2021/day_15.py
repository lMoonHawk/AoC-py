def array_get(array: list[list], t: tuple[int, int]):
    return array[t[0]][t[1]]


def array_set(array: list[list], t: tuple[int, int], v):
    array[t[0]][t[1]] = v


def a_star(grid, start, end) -> int:
    """A* Algorithm, returns total cost of the best path"""
    # G: Cost so far
    # H: Heuristic, estimation of cost from current to end
    # F: G + H, current estimation for positions value

    size = len(grid)

    # initialize F, G, H
    g_array = [[float("inf")] * size for i in range(size)]
    array_set(g_array, start, 0)
    # H is the number of cells from i, j to the end
    h_array = [
        [2 * size - i - j - 2 for j in range(size)] for i in range(size)
    ]
    f_array = [[float("inf")] * size for i in range(size)]
    array_set(f_array, start, array_get(h_array, start))

    opened = [start]
    closed = []

    while opened:
        current = opened[0]
        # Select current best position (minimize F)
        for position in opened:
            if array_get(f_array, position) < array_get(f_array, current):
                current = position

        # Close it
        opened.remove(current)
        closed.append(position)

        # If best is "end", solution found
        if current == end:
            return array_get(g_array, end)

        # Add neighbors to the "opened" list
        for offset in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            neighbor = (current[0] + offset[0], current[1] + offset[1])

            # If outside grid, stop current neighbor
            underflow = any([pos < 0 for pos in neighbor])
            overflow = any([pos > size - 1 for pos in neighbor])
            if underflow or overflow:
                continue

            # G of neighbor is G of current + grid value
            g = array_get(g_array, current) + array_get(grid, neighbor)
            # If this G is better than previous one
            # (better path to neighbor found)
            if g < array_get(g_array, neighbor):
                # Update G array
                array_set(g_array, neighbor, g)
                # Update F array
                h = array_get(h_array, neighbor)
                array_set(f_array, neighbor, g + h)

                opened.append(neighbor)


def part1():

    cave: list[list[int]] = []

    # Parsing
    with open("2021/data/day_15.txt") as f:
        for line in f:
            row = [int(risk) for risk in list(line.strip())]
            cave.append(row)

    size = len(cave)
    result = a_star(cave, (0, 0), (size - 1, size - 1))
    print(result)


def part2():

    cave: list[list[int]] = []

    # Parsing
    with open("2021/data/day_15.txt") as f:
        for line in f:
            row = [int(risk) for risk in list(line.strip())]
            cave.append(row)

    size = len(cave)

    for row in cave:
        row.extend([(el + i) % 9 + 1 for i in range(4) for el in row])
    for k in range(4):
        for j in range(size):
            new_row = [(el + k) % 9 + 1 for el in cave[j]]
            cave.append(new_row)

    size = len(cave)
    result = a_star(cave, (0, 0), (size - 1, size - 1))
    print(result)


if __name__ == "__main__":
    part1()
    part2()
