with open("2019/data/day_10.txt") as f:
    asteroids = []
    for y, line in enumerate(f):
        asteroids.extend([(x, y) for x, asteroid in enumerate(line.strip()) if asteroid == "#"])


def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)


def is_seeable(asteroid: tuple[int], station: tuple[int], asteroids: list[tuple[int]]) -> bool:
    x_station, y_station = station
    x_ast, y_ast = asteroid

    if (x_station, y_station) == (x_ast, y_ast):
        return False

    x_step, y_step = x_ast - x_station, y_ast - y_station
    unit_step = gcd(x_step, y_step)
    # Normalization of the vector station -> asteroid in int space
    x_step, y_step = x_step / unit_step, y_step / unit_step

    x_check, y_check = x_station + x_step, y_station + y_step
    # We check each scalar for an asteroid that is not the one we test
    while (x_check, y_check) != (x_ast, y_ast):
        if (x_check, y_check) in asteroids:
            return False
        x_check += x_step
        y_check += y_step
    # Line of sight is clear
    return True


def get_best_station() -> tuple[tuple[int], int]:
    best_count = 0
    for station in asteroids:
        station_count = sum(is_seeable(asteroid, station, asteroids) for asteroid in asteroids)
        if station_count > best_count:
            best_count, best_station = station_count, station

    return best_station, best_count


def dist(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5


def part1():
    _, best_count = get_best_station()
    return best_count


def part2():
    station, _ = get_best_station()
    x_s, y_s = station

    ast_order = []
    for asteroid in asteroids:
        if asteroid == station:
            continue
        x_a, y_a = asteroid

        slope = None
        if x_a != x_s:
            slope = (y_s - y_a) / (x_s - x_a)
        # Priority for each quadrant + axis
        if x_a == x_s and y_s > y_a:  # up
            quad = 0
        if x_a > x_s and y_s > y_a:  # top right quadrant
            quad = 1
        if x_a > x_s and y_s == y_a:  # right
            quad = 2
        if x_a > x_s and y_s < y_a:  # bottom right quadrant
            quad = 3
        if x_a == x_s and y_s < y_a:  # down
            quad = 4
        if x_a < x_s and y_s < y_a:  # bottom left quadrant
            quad = 5
        if x_a < x_s and y_s == y_a:  # left
            quad = 6
        if x_a < x_s and y_s > y_a:  # top left quadrant
            quad = 7

        ast_order.append({"coord": asteroid, "quad": quad, "slope": slope, "dist": dist(station, asteroid)})

    # Each asteroid is ordered by (in order) its quadrant, slope and distance
    ast_order = sorted(ast_order, key=lambda k: (k["quad"], k["slope"], k["dist"]))

    k = 0
    destroyed = 0
    prev_prio, prev_slope = None, None
    while destroyed != 200:
        # This asteroid is hidden behind the one we destroyed (same quadrant, same slope, higher distance)
        if ast_order[k]["quad"] == prev_prio and ast_order[k]["slope"] == prev_slope:
            # Move to the next
            k += 1
            # We completed a whole cycle
            if k >= len(ast_order):
                # Start another cycle
                k = k % len(ast_order)
                prev_prio, prev_slope = None, None
            continue

        out = ast_order.pop(k)
        prev_prio, prev_slope = out["quad"], out["slope"]
        destroyed += 1

    x, y = out["coord"]
    return x * 100 + y


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
