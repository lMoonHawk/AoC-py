with open("2018/data/day_20.txt") as f:
    regex = f.readline().strip()[1:-1]
directions = {"N": (0, -1), "E": (1, 0), "S": (0, 1), "W": (-1, 0)}


def add_node(d, k, v):
    if k not in d:
        d[k] = set()
    if v not in d:
        d[v] = set()
    d[k].add(v)
    d[v].add(k)


def add_vec2(a, b):
    return a[0] + b[0], a[1] + b[1]


def regex_to_graph():
    graph = dict()
    positions = {(0, 0)}
    starts, ends = {(0, 0)}, set()
    stack = []
    for char in regex:
        if char in "NESW":
            direction = directions[char]
            new_positions = set()
            for position in positions:
                new_position = add_vec2(position, direction)
                add_node(graph, position, new_position)
                new_positions.add(new_position)
            positions = new_positions
        elif char == "(":
            stack.append((starts, ends))
            starts, ends = positions, set()
        elif char == ")":
            positions.update(ends)
            starts, ends = stack.pop()
        elif char == "|":
            ends.update(positions)
            positions = starts
    return graph


def traverse(graph, doors=None):
    visited = set()
    queue = [((0, 0), 0)]
    out = 0
    while queue:
        (x, y), steps = queue.pop(0)
        visited.add((x, y))
        if doors and steps >= doors:
            out += 1
        elif not doors and steps > out:
            out = steps
        for nx, ny in graph[(x, y)]:
            if (nx, ny) not in visited:
                queue.append(((nx, ny), steps + 1))
    return out


def part1():
    return traverse(regex_to_graph())


def part2():
    return traverse(regex_to_graph(), doors=1_000)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
