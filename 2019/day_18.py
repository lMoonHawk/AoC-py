class Heap(list):
    def push(self, item):
        self.append(item)
        self.sift_up(len(self) - 1)

    def pop(self):
        self[-1], self[0] = self[0], self[-1]
        out = super().pop()
        if self:
            self.sift_down()
        return out

    def sift_up(self, pos):
        item = self[pos]
        while pos:
            parentpos = (pos - 1) // 2
            parent = self[parentpos]
            if item < parent:
                self[pos], pos = parent, parentpos
                continue
            break
        self[pos] = item

    def sift_down(self):
        n = len(self)
        pos = 0
        l_child_pos = min_child_pos = 1

        item = self[0]

        while l_child_pos < n:
            min_child_pos, r_child_pos = l_child_pos, l_child_pos + 1
            if r_child_pos < n and self[l_child_pos] > self[r_child_pos]:
                min_child_pos = r_child_pos

            self[pos] = self[min_child_pos]
            pos = min_child_pos
            l_child_pos = 2 * pos + 1

        self[pos] = item
        self.sift_up(pos)


def add_coord(v1, v2):
    return tuple([a1 + a2 for a1, a2 in zip(v1, v2)])


def mask(c):
    return 1 << (ord("z") - ord(c))


def get_vault():
    vault = {}
    with open("2019/data/day_18.txt") as f:
        for y, line in enumerate(f):
            vault.update({(x, y): sq for x, sq in enumerate(line.strip())})
    return vault


def get_reachable(vault, start):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    queue = [(start, 0, 0)]
    visited, reachable = set(), dict()
    while queue:
        pos, steps, doors = queue.pop(0)
        if pos in visited:
            continue
        visited.add(pos)
        if vault[pos].islower():
            reachable[vault[pos]] = (steps, doors)

        for direction in directions:
            new_pos = add_coord(pos, direction)
            if vault[new_pos] == "#":
                continue
            new_doors = doors
            if vault[new_pos].isupper():
                new_doors |= mask(vault[new_pos].lower())

            queue.append((new_pos, steps + 1, new_doors))
    return reachable


def search_min_steps(vault, robots, nodes, all_keys):
    graph = {c: {k: v for k, v in get_reachable(vault, nodes[c]).items()} for c in nodes}

    pqueue = Heap([(0, robots, 0)])
    visited = set()

    while pqueue:
        steps, positions, keys = pqueue.pop()

        if (positions, keys) in visited:
            continue
        visited.add((positions, keys))

        if keys == all_keys:
            return steps

        for robot_i, position in enumerate(positions):
            for new_position, (path_steps, path_doors) in graph[position].items():
                if ~keys & path_doors or keys & mask(new_position):
                    continue
                new_positions = (*positions[:robot_i], new_position, *positions[robot_i + 1 :])
                pqueue.push((steps + path_steps, new_positions, keys | mask(new_position)))


def part1():
    vault = get_vault()
    nodes = {node: pos for pos, node in vault.items() if node.islower() or node == "@"}
    all_keys = sum(mask(key) for key in nodes if key != "@")
    robots = ("@",)
    return search_min_steps(vault, robots, nodes, all_keys)


def part2():
    vault = get_vault()
    nodes = {node: pos for pos, node in vault.items() if node.islower() or node == "@"}

    wall = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    robot = [(-1, -1), (1, -1), (-1, 1), (1, 1)]
    for count, (pos_wall, pos_robot) in enumerate(zip(wall, robot)):
        vault[add_coord(nodes["@"], pos_wall)] = "#"
        robot_pos = add_coord(nodes["@"], pos_robot)
        vault[robot_pos] = str(count)
        nodes[str(count)] = robot_pos

    vault[nodes["@"]] = "#"
    del nodes["@"]

    all_keys = sum(mask(key) for key in nodes if key not in ["0", "1", "2", "3"])

    robots = ("0", "1", "2", "3")
    return search_min_steps(vault, robots, nodes, all_keys)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
