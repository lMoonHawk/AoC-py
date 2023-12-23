with open("2023/data/day_23.txt") as f:
    trail = [line.strip() for line in f.readlines()]
start = trail[0].index("."), 0
end = trail[-1].index("."), len(trail) - 1


def part1():
    queue = [(start, set(), 0)]
    max_steps = 0
    while queue:
        (x, y), visited, steps = queue.pop()
        if (x, y) == end:
            max_steps = steps if steps > max_steps else max_steps
            continue
        for slope, (mx, my) in zip(["^", "<", ">", "v"], [(0, 1), (1, 0), (-1, 0), (0, -1)]):
            nx, ny = x + mx, y + my
            if not ((0 <= nx < len(trail[0])) and (0 <= ny < len(trail))):
                continue
            if trail[ny][nx] in ["#", slope]:
                continue
            if (nx, ny) in visited:
                continue
            queue.append(((nx, ny), visited | {(nx, ny)}, steps + 1))

    return max_steps


def connecting_nodes(trail, start):
    visited = set()
    paths = [(start, 0)]
    nodes = []
    while paths:
        (x, y), steps = paths.pop()
        visited.add((x, y))
        path = []
        for mx, my in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nx, ny = x + mx, y + my
            if (nx, ny) in visited:
                continue
            if not ((0 <= nx < len(trail[0])) and (0 <= ny < len(trail))):
                if (x, y) != start:
                    nodes.append(((x, y), steps))
                continue
            if trail[ny][nx] == "#":
                continue
            path.append(((nx, ny), steps + 1))

        if len(path) > 1 and (x, y) != start:
            nodes.append(((x, y), steps))
        else:
            paths.extend(path)
    return nodes


def connecting_nodes2(trail, start):
    visited = set()
    paths = [(start, 0)]
    nodes = dict()
    while paths:
        (x, y), steps = paths.pop()
        visited.add((x, y))
        path = []
        for mx, my in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nx, ny = x + mx, y + my
            if (nx, ny) in visited:
                continue
            if not ((0 <= nx < len(trail[0])) and (0 <= ny < len(trail))):
                if (x, y) != start:
                    nodes[(x, y)] = steps
                continue
            if trail[ny][nx] == "#":
                continue
            path.append(((nx, ny), steps + 1))

        if len(path) > 1 and (x, y) != start:
            nodes[(x, y)] = steps
        else:
            paths.extend(path)
    return nodes


def is_node(x, y, trail):
    if trail[y][x] == "#":
        return False
    paths = 0
    for nx, ny in [(x, y + 1), (x + 1, y), (x - 1, y), (x, y - 1)]:
        if not ((0 <= nx < len(trail[0])) and (0 <= ny < len(trail))):
            return True
        if trail[ny][nx] != "#":
            paths += 1
    if paths > 2:
        return True
    return False


def part2():
    nodes = {
        node: connecting_nodes2(trail, node)
        for node in [(x, y) for y, row in enumerate(trail) for x, _ in enumerate(row) if is_node(x, y, trail)]
    }
    last_node = {node_from: node_to[end] for node_from, node_to in nodes.items() if end in node_to}

    queue = [(0, start, set())]
    max_steps = 0
    while queue:
        steps, node, visited = queue.pop()
        if node == end:
            max_steps = steps if steps > max_steps else max_steps
            continue
        if node in last_node:
            max_steps = steps + last_node[node] if steps + last_node[node] > max_steps else max_steps
            continue
        for end_node, end_steps in nodes[node].items():
            if end_node in visited:
                continue
            queue.append((steps + end_steps, end_node, visited | {end_node}))
    return max_steps


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
