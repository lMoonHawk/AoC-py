with open("2018/data/day_22.txt") as f:
    depth, target = [line.strip().split()[1] for line in f.readlines()]
    depth, (tx, ty) = int(depth), [int(t) for t in target.split(",")]


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


class Tool:
    none = 0
    torch = 1
    gear = 2


def get_erosion(x, y, cache={}):
    if (x, y) not in cache:
        if (x, y) == (tx, ty):
            cache[(x, y)] = depth % 20183
        elif y == 0:
            cache[(x, y)] = (x * 16807 + depth) % 20183
        elif x == 0:
            cache[(x, y)] = (y * 48271 + depth) % 20183
        else:
            cache[(x, y)] = (get_erosion(x, y - 1) * get_erosion(x - 1, y) + depth) % 20183
    return cache[(x, y)]


def get_type(x, y):
    return get_erosion(x, y) % 3


def part1():
    return sum(get_type(x, y) for y in range(ty + 1) for x in range(tx + 1))


def part2():
    # A* implemented with a Heap.
    # f = minutes already spent + manhattan distance to target
    # We check the item in the priority queue which has the min f. The first one to get to target with a torch is the best.
    reg_tools = {
        0: {Tool.torch, Tool.gear},
        1: {Tool.none, Tool.gear},
        2: {Tool.none, Tool.torch},
    }

    pqueue = Heap([(0, 0, 0, 0, Tool.torch)])
    visited = set()
    while pqueue:
        _, m, x, y, t = pqueue.pop()
        if (x, y, t) in visited:
            continue
        visited.add((x, y, t))
        if (x, y) == (tx, ty):
            if t == Tool.torch:
                return m
            pqueue.push((0, m + 7, x, y, Tool.torch))
            continue
        for nx, ny in [(x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]:
            if nx < 0 or ny < 0:
                continue
            for nt in reg_tools[get_type(x, y)] & reg_tools[get_type(nx, ny)]:
                nm = m + 1 if nt == t else m + 8
                nf = nm + abs(tx - nx) + abs(ty - ny)
                pqueue.push((nf, nm, nx, ny, nt))


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
