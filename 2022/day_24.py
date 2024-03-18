def init():
    with open("2022/data/day_24.txt") as f:
        lines = f.readlines()
        start = (lines[0].index("."), 0)
        end = (lines[-1].index("."), len(lines) - 1)
        blizzards = [set(), set(), set(), set()]
        order = [">", "v", "<", "^"]
        for y, row in enumerate(lines):
            for x, tile in enumerate(row.strip()):
                if tile in order:
                    index = order.index(tile)
                    blizzards[index].add((x, y))
        row_max = y
        col_max = x
    return blizzards, start, end, row_max, col_max


def update_blizzards(blizzards, col_max, row_max):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    blizzards[:] = [
        {((x - 1 + mx) % (col_max - 1) + 1, (y - 1 + my) % (row_max - 1) + 1) for (x, y) in blizzard}
        for blizzard, (mx, my) in zip(blizzards, directions)
    ]


def is_safe(x, y, blizzards):
    for b in blizzards:
        if (x, y) in b:
            return False
    return True


def fastest_traverse(blizzards, start, end, row_max, col_max):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (0, 0)]
    minute = [(*start,)]
    time = 0
    while True:
        next_minute = []
        visited = set()
        update_blizzards(blizzards, col_max, row_max)
        while minute:
            x, y = minute.pop()
            if (x, y) in visited:
                continue
            visited.add((x, y))

            for mx, my in directions:
                nx, ny = x + mx, y + my
                if (nx, ny) == end:
                    return time + 1
                if (mx, my) != (0, 0) and not (0 < nx < col_max and 0 < ny < row_max):
                    continue
                if is_safe(nx, ny, blizzards):
                    next_minute.append((nx, ny))
        minute = next_minute
        time += 1


def part1():
    return fastest_traverse(*init())


def part2():
    blizzards, start, end, row_max, col_max = init()
    t0 = fastest_traverse(blizzards, start, end, row_max, col_max)
    t1 = fastest_traverse(blizzards, end, start, row_max, col_max)
    t2 = fastest_traverse(blizzards, start, end, row_max, col_max)
    return t0 + t1 + t2


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
