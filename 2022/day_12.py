with open("2022/data/day_12.txt") as f:
    area = [[ord(elevation) - 97 for elevation in line.strip()] for line in f]
for i, row in enumerate(area):
    for j, height in enumerate(row):
        if height == ord("S") - 97:
            si, sj = i, j
            area[si][sj] = ord("a") - 97
        elif height == ord("E") - 97:
            ei, ej = i, j
            area[ei][ej] = ord("a") - 97


def min_steps_from(i, j, area):
    queue = [(i, j, 0)]
    visited = {queue[0]}
    while queue:
        i, j, steps = queue.pop(0)
        if (i, j) == (ei, ej):
            return steps
        for ni, nj in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
            if not (0 <= ni < len(area) and 0 <= nj < len(area[0])):
                continue
            if area[ni][nj] - 1 > area[i][j]:
                continue
            if (ni, nj) in visited:
                continue
            visited.add((ni, nj))
            queue.append((ni, nj, steps + 1))


def part1():
    return min_steps_from(si, sj, area)


def part2():
    min_steps = None
    for i, row in enumerate(area):
        for j, height in enumerate(row):
            if height == 0:
                if result := min_steps_from(i, j, area):
                    if min_steps is None or result < min_steps:
                        min_steps = result
    return min_steps


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
