class MaxHeap(list):
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
            if item > parent:
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
            if r_child_pos < n and self[l_child_pos] < self[r_child_pos]:
                min_child_pos = r_child_pos
            self[pos] = self[min_child_pos]
            pos = min_child_pos
            l_child_pos = 2 * pos + 1
        self[pos] = item
        self.sift_up(pos)


bots = []
with open("2018/data/day_23.txt") as f:
    for line in f:
        pos, r = [el.split("=")[1] for el in line.strip().replace("<", "").replace(">", "").split(", ")]
        pos, r = [int(el) for el in pos.split(",")], int(r)
        bots.append((pos, r))


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])


def scal_vect(s, v3):
    return tuple([c * s for c in v3])


def add_vect(a, b):
    return tuple([ai + bi for ai, bi in zip(a, b)])


def pot_bots_in_range(point, edge):
    """Counts the number of bots that can reach the cube (point, point + edge)"""
    bx, by, bz = point
    count = 0
    for (x, y, z), r in bots:
        # Calculate the point on the cube closest to the bot
        best_x = max(x, bx) if x < (bx + edge // 2) else min(x, bx + edge)
        best_y = max(y, by) if y < (by + edge // 2) else min(y, by + edge)
        best_z = max(z, bz) if z < (bz + edge // 2) else min(z, bz + edge)
        # The bot can reach the cube if its distance to the closest point on the cube is less than its range
        if abs(best_x - x) + abs(best_y - y) + abs(best_z - z) <= r:
            count += 1
    return count


def part1():
    (bx, by, bz), br = max(bots, key=lambda x: x[1])
    return sum(abs(x - bx) + abs(y - by) + abs(z - bz) <= br for (x, y, z), _ in bots)


def part2():
    xs, ys, zs = [x for (x, _, _), _ in bots], [y for (_, y, _), _ in bots], [z for (_, _, z), _ in bots]
    bounds = max(abs(max(xs)), abs(min(xs)), abs(max(ys)), abs(min(ys)), abs(max(zs)), abs(min(zs)))
    # Cubes are described by their min coordinates (left-bottom-back point).
    # Make a cube side length the first power of 2 that contains all bots.
    edge = 1
    while edge <= bounds:
        edge *= 2
    point = (-edge, -edge, -edge)
    edge *= 2
    # The priority queue maximises the amount of bots in the cube then the size of the cube and finally minimises the distance to origin.
    pqueue = MaxHeap([(len(bots), edge, -manhattan(point, (0, 0, 0)), point)])
    while pqueue:
        _, edge, dist, point = pqueue.pop()
        if edge == 0:
            return -dist
        edge = edge // 2
        for subpoint in [(x, y, z) for x in range(2) for y in range(2) for z in range(2)]:
            subpoint = add_vect(point, scal_vect(edge, subpoint))
            pqueue.push((pot_bots_in_range(subpoint, edge), edge, -manhattan(subpoint, (0, 0, 0)), subpoint))


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
