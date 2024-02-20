with open("2021/data/day_09.txt") as f:
    hmap = [[int(height) for height in row.strip()] for row in f]


def is_low(hmap, i, j):
    height = hmap[i][j]
    for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
        if 0 <= ni < len(hmap) and 0 <= nj < len(hmap[0]):
            if hmap[ni][nj] <= height:
                return False
    return True


def part1():
    return sum(1 + height for i, row in enumerate(hmap) for j, height in enumerate(row) if is_low(hmap, i, j))


def part2():
    visited = set()
    basins_sizes = []

    for i, row in enumerate(hmap):
        for j, height in enumerate(row):
            if (i, j) in visited or height == 9:
                continue
            visited.add((i, j))
            queue = [(i, j)]
            size = 0
            while queue:
                y, x = queue.pop(0)
                size += 1
                for ny, nx in [(y, x + 1), (y, x - 1), (y + 1, x), (y - 1, x)]:
                    if (ny, nx) in visited:
                        continue
                    if not (0 <= nx < len(hmap[0]) and 0 <= ny < len(hmap)) or hmap[ny][nx] == 9:
                        continue
                    visited.add((ny, nx))
                    queue.append((ny, nx))
            basins_sizes.append(size)

    mult = 1
    for size in sorted(basins_sizes)[-3:]:
        mult *= size
    return mult


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
