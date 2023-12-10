with open("2023/data/day_10.txt") as f:
    area = [list(line.strip()) for line in f.readlines()]
(start,) = [(x, y) for y, row in enumerate(area) for x, sq in enumerate(row) if sq == "S"]
directions = {
    "|": [(0, -1), (0, 1)],
    "-": [(-1, 0), (1, 0)],
    "L": [(0, -1), (1, 0)],
    "J": [(0, -1), (-1, 0)],
    "7": [(-1, 0), (0, 1)],
    "F": [(1, 0), (0, 1)],
    "S": [(1, 0), (0, 1), (-1, 0), (0, -1)],
    ".": [],
}


def get_pipes():
    path, (px, py) = [start], (None, None)
    while True:
        (x, y) = path[-1]
        if area[y][x] == "S" and (px, py) != (None, None):
            return path[:-1]

        for mx, my in directions[area[y][x]]:
            nx, ny = x + mx, y + my
            if not (0 <= nx < len(area[0]) and 0 <= ny < len(area)):
                continue
            if (nx, ny) == (px, py):
                continue
            if (-mx, -my) not in directions[area[ny][nx]]:
                continue
            path, (px, py) = path + [(nx, ny)], (x, y)
            break


def connected_group(x, y, border):
    """Collects all orthogonally connected cells starting from position x, y"""
    tiles = set([(x, y)])
    queue = [(x, y)]
    while queue:
        cx, cy = queue.pop(0)
        for nx, ny in [(cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)]:
            if (nx, ny) in tiles or (nx, ny) in border:
                continue
            if not (0 <= nx < len(area[0]) and 0 <= ny < len(area)):
                continue
            tiles.add((nx, ny))
            queue.append((nx, ny))
    return tiles


def is_inside(x, y, border):
    """Raycasting algorithm implementation. Detects if the position x, y is inside the borders"""
    # The ray is 45° to avoid alignment with edges.
    return (
        sum(
            (c, r) in border
            for r, c in zip(range(y, len(area)), range(x, len(area[0])))
            if area[r][c] not in ["7", "L"]
        )
        % 2
    )


def part1():
    return len(get_pipes()) // 2


def part2():
    path, inside, outside = set(get_pipes()), set(), set()
    for y, row in enumerate(area):
        for x, _ in enumerate(row):
            if (x, y) in inside or (x, y) in outside or (x, y) in path:
                continue
            tiles = connected_group(x, y, path)
            if is_inside(x, y, path):
                inside.update(tiles)
            else:
                outside.update(tiles)
    return len(inside)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
