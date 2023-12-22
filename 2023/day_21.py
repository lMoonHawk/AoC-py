with open("2023/data/day_21.txt") as f:
    plots = [list(line.strip()) for line in f.readlines()]
(start,) = [(x, y) for y, row in enumerate(plots) for x, sq in enumerate(row) if sq == "S"]


def traverse(start, plots, stop):
    parity = stop % 2
    counter = 0
    visited = set()
    queue = [(start, 0)]
    while queue:
        (x, y), steps = queue.pop(0)
        if (x, y) in visited:
            continue
        visited.add((x, y))
        if steps > stop:
            return counter
        if steps % 2 == parity:
            counter += 1
        for mx, my in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + mx, y + my
            if plots[ny % len(plots[0])][nx % len(plots)] == "#":
                continue
            queue.append(((nx, ny), steps + 1))


def part1():
    return traverse(start, plots, 64)


def part2():
    length = len(plots)
    # n is the number of full tiles traversed in a straigh line.
    # In the input, there are straight lines from the start to the edges.
    n = 26501365 // length
    # We calculate the number of tiles of the correct parity for three full lenghts since this is a quadratic result.
    a, b, c = [traverse(start, plots, s * length + (length // 2)) for s in range(3)]
    return a + n * (b - a + (n - 1) * (c - 2 * b + a) // 2)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
