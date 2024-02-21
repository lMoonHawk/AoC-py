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


with open("2021/data/day_15.txt") as f:
    cave = [[int(risk) for risk in line.strip()] for line in f]


def a_star(grid) -> int:
    """A* Algorithm, returns total cost of the best path"""
    size = len(grid)
    pqueue = Heap()
    pqueue.push((0, 0, 0))
    cache_best = {(0, 0): 0}

    while pqueue:
        exp_tot_risk, x, y = pqueue.pop()
        if (x, y) == (size - 1, size - 1):
            return exp_tot_risk

        for nx, ny in [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]:
            if not (0 <= nx < size and 0 <= ny < size):
                continue
            total_risk = cache_best[(x, y)] + grid[nx][ny]
            if (nx, ny) in cache_best and cache_best[(nx, ny)] <= total_risk:
                continue
            cache_best[(nx, ny)] = total_risk
            heuristic = 2 * (size - 1) - nx - ny
            pqueue.append((total_risk + heuristic, nx, ny))


def part1():
    return a_star(cave)


def part2():
    big_cave = [[0 for _ in range(len(cave[0]) * 5)] for _ in range(len(cave) * 5)]
    for i, row in enumerate(big_cave):
        for j, _ in enumerate(row):
            grid_y, cave_y = divmod(i, len(cave))
            grid_x, cave_x = divmod(j, len(cave[0]))
            big_cave[i][j] = (cave[cave_y][cave_x] + grid_x + grid_y - 1) % 9 + 1
    return a_star(big_cave)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
