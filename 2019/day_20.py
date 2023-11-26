def get_maze():
    with open("2019/data/day_20.txt") as f:
        maze = {(x, y): sq for y, line in enumerate(f) for x, sq in enumerate(line)}

    xs = [x for (x, _), sq in maze.items() if sq in ["#", "."]]
    ys = [y for (_, y), sq in maze.items() if sq in ["#", "."]]
    minx, maxx, miny, maxy = min(xs), max(xs), min(ys), max(ys)

    inner_portals, outer_portals = dict(), dict()
    for (x, y), sq in maze.items():
        if sq.isupper():
            portal_label = None
            if (x, y - 1) in maze and maze[(x, y - 1)].isupper():
                portal_label = maze[(x, y - 1)] + sq
                if (x, y - 2) in maze and maze[(x, y - 2)] == ".":
                    portal_pos = x, y - 2
                if (x, y + 1) in maze and maze[(x, y + 1)] == ".":
                    portal_pos = x, y + 1

            if (x - 1, y) in maze and maze[(x - 1, y)].isupper():
                portal_label = maze[(x - 1, y)] + sq
                if (x - 2, y) in maze and maze[(x - 2, y)] == ".":
                    portal_pos = x - 2, y
                if (x + 1, y) in maze and maze[(x + 1, y)] == ".":
                    portal_pos = x + 1, y

            if not portal_label:
                continue

            if not minx <= x <= maxx or not miny <= y <= maxy:
                outer_portals[portal_label] = portal_pos
            else:
                inner_portals[portal_label] = portal_pos

    maze = {pos: sq for pos, sq in maze.items() if sq in [".", "#"]}

    start = outer_portals.pop("AA")
    end = outer_portals.pop("ZZ")

    outer_portals = {pos: inner_portals[label] for label, pos in outer_portals.items()}
    inner_portals = {v: k for k, v in outer_portals.items()}
    return maze, outer_portals, inner_portals, start, end


def add_coord(v1, v2):
    return tuple([a1 + a2 for a1, a2 in zip(v1, v2)])


def part1():
    maze, outer_portals, inner_portals, start, end = get_maze()
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    visited = set()
    queue = [(start, 0)]
    while queue:
        pos, steps = queue.pop(0)
        if pos == end:
            return steps
        if pos in visited:
            continue
        visited.add(pos)

        for direction in directions:
            new_pos = add_coord(pos, direction)
            if new_pos not in maze:
                if pos in inner_portals:
                    new_pos = inner_portals[pos]
                elif pos in outer_portals:
                    new_pos = outer_portals[pos]
                else:
                    continue
            if maze[new_pos] == "#":
                continue

            queue.append((new_pos, steps + 1))


def part2():
    maze, outer_portals, inner_portals, start, end = get_maze()
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    visited = set()
    queue = [(start, 0, 0)]
    while queue:
        pos, level, steps = queue.pop(0)
        if pos == end and level == 0:
            return steps
        if (pos, level) in visited:
            continue
        visited.add((pos, level))

        for direction in directions:
            new_pos = add_coord(pos, direction)
            new_level = level

            if new_pos not in maze:
                if pos in inner_portals:
                    new_pos = inner_portals[pos]
                    new_level = level + 1
                elif pos in outer_portals and level > 0:
                    new_pos = outer_portals[pos]
                    new_level = level - 1
                else:
                    continue
            if maze[new_pos] == "#":
                continue

            queue.append((new_pos, new_level, steps + 1))


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
