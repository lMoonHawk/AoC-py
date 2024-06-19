with open("2018/data/day_10.txt") as f:
    POINTS = [
        [
            int(el.strip())
            for d in line.strip().replace("> velocity", "").replace(">", "").split("=<")[1:]
            for el in d.split(",")
        ]
        for line in f
    ]


def points_repr(s, min_x, max_x, min_y, max_y):
    points = [[x + vx * s, y + vy * s] for x, y, vx, vy in POINTS]
    buffer = "\n"
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if [x, y] in points:
                buffer += "# "
            else:
                buffer += ". "
        buffer += "\n"
    return buffer[:-1]


def find_sec():
    prev_size = None
    k = 0
    while True:
        min_x = min(x + vx * k for x, _, vx, _ in POINTS)
        max_x = max(x + vx * k for x, _, vx, _ in POINTS)
        min_y = min(y + vy * k for _, y, _, vy in POINTS)
        max_y = max(y + vy * k for _, y, _, vy in POINTS)
        size = (max_x - min_x) * (max_y - min_y)

        if prev_size is not None and size > prev_size:
            break
        prev_size = size
        best_range = min_x, max_x, min_y, max_y
        k += 1
    return k, best_range


def part1():
    k, best_range = find_sec()
    return points_repr(k - 1, *best_range)


def part2():
    k, _ = find_sec()
    return k -1


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
