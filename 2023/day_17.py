with open("2023/data/day_17.txt") as f:
    city = [[int(el) for el in line.strip()] for line in f.readlines()]


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


def traverse_city(min_steps, max_steps):
    directions = {0: (0, -1), 1: (1, 0), 2: (0, 1), 3: (-1, 0)}

    visited = set()
    start = (0, 0)
    end = (len(city[0]) - 1, len(city) - 1)
    pqueue = Heap([(0, start, None, None)])

    while pqueue:
        loss, (x, y), prev_rot, straight = pqueue.pop()
        if (x, y) == end:
            if min_steps <= straight <= max_steps:
                return loss
            else:
                continue

        if (x, y, straight, prev_rot) in visited:
            continue
        visited.add((x, y, straight, prev_rot))

        for rot, (mx, my) in directions.items():
            nstraight = 1
            if straight is not None:
                if rot == prev_rot:
                    nstraight += straight
                    if nstraight > max_steps:
                        continue
                else:
                    if straight < min_steps:
                        continue

            if (rot + 2) % 4 == prev_rot:
                continue

            nx, ny = x + mx, y + my
            if not (0 <= nx < len(city[0]) and (0 <= ny < len(city))):
                continue
            pqueue.push((loss + city[ny][nx], (nx, ny), rot, nstraight))


def part1():
    return traverse_city(0, 3)


def part2():
    return traverse_city(4, 10)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
