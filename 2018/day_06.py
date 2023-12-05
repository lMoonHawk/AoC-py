with open("2018/data/day_06.txt") as f:
    POINTS = [tuple([int(el) for el in line.strip().split(", ")]) for line in f]


def part1():
    xs = [x for x, _ in POINTS]
    ys = [y for _, y in POINTS]
    min_x, max_x, min_y, max_y = min(xs), max(xs), min(ys), max(ys)

    census = {point: 0 for point in POINTS}
    infinite = set()

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            best_point, best_dist = None, None
            for px, py in POINTS:
                dist = abs(x - px) + abs(y - py)
                if best_dist is None or best_dist > dist:
                    best_dist, best_point = dist, (px, py)
                elif best_dist == dist:
                    best_point = None
            if best_point:
                census[best_point] += 1
                if x == min_x or x == max_x or y == min_y or y == max_y:
                    infinite.add(best_point)

    return max(v for k, v in census.items() if k not in infinite)


def part2():
    SIZE = 10_000
    xs = [x for x, _ in POINTS]
    ys = [y for _, y in POINTS]
    min_x, max_x, min_y, max_y = min(xs), max(xs), min(ys), max(ys)
    answer = 0

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            dist = 0
            for px, py in POINTS:
                dist += abs(x - px) + abs(y - py)
                if dist >= SIZE:
                    break
            if dist < SIZE:
                answer += 1
    return answer


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
