class Node:
    def __init__(self, file, size, used, avail, _):
        x, y = [int(el) for el in file.replace("x", "").replace("y", "").split("-")[-2:]]
        self.x, self.y = x, y
        self.size = int(size[:-1])
        self.used = int(used[:-1])
        self.avail = int(avail[:-1])


with open("2016/data/day_22.txt") as f:
    nodes = [Node(*line.split()) for line in f if "/dev/" in line]


def part1():
    return sum(
        (a.used and a.used <= b.avail) + (b.used and b.used <= a.avail)
        for k, a in enumerate(nodes[:-1])
        for b in nodes[k + 1 :]
    )


def part2():
    # Fist, move the hole from it position to being in front of the data.
    # Then, swap position of hole and data (1 step) and get back in front (4 steps)
    hole = min(nodes, key=lambda node: node.used)
    goal = (nodes[-1].x - 1, 0)
    return move_hole(hole, goal) + 5 * (nodes[-1].x - 1) + 1


def move_hole(hole, goal):
    stride = nodes[-1].y + 1
    len_x = nodes[-1].x
    queue = [(hole, 0)]
    visited = {(hole.x, hole.y)}
    while queue:
        hole, steps = queue.pop(0)
        x, y = hole.x, hole.y
        if (x, y) == goal:
            return steps
        for nx, ny in [(x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1)]:
            index = nx * stride + ny
            if not (0 <= nx <= len_x and 0 <= ny < stride) or (nx, ny) in visited:
                continue
            visited.add((nx, ny))
            if nodes[index].used <= hole.size:
                queue.append((nodes[index], steps + 1))


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
