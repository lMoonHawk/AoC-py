class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def in_bounds(self, bounds):
        return bounds.x <= self.x <= bounds.y and bounds.x <= self.y <= bounds.y

    def distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)


def merge_intervals(intervals):
    intervals.sort(reverse=True)
    unique_intervals = [intervals.pop()]
    while intervals:
        lo, hi = intervals.pop()
        prev_lo, prev_hi = unique_intervals.pop()
        if prev_lo <= lo <= prev_hi:
            unique_intervals.append((prev_lo, max(prev_hi, hi)))
        else:
            unique_intervals.append((lo, hi))
            unique_intervals.append((prev_lo, prev_hi))
    return unique_intervals


with open("2022/data/day_15.txt") as f:
    coords = [[Vec2(*[int(el.split("=")[1]) for el in axis.split(", ")]) for axis in line.split(": ")] for line in f]


def part1():
    row = 2_000_000
    intervals = []
    beacons_in_row = set()
    for sensor, beacon in coords:
        if beacon.y == row:
            beacons_in_row.add((beacon.x, beacon.y))
        radius = sensor.distance(beacon)
        if (reach := radius - abs(sensor.y - row)) > 0:
            intervals.append((sensor.x - reach, sensor.x + reach))
    return sum(hi - lo + 1 for lo, hi in merge_intervals(intervals)) - len(beacons_in_row)


def part2():
    bounds = Vec2(0, 4_000_000)
    pos_diag_intercepts = []
    neg_diag_intercepts = []
    for sensor, beacon in coords:
        # The gap has to be on the edge of a detection range, otherwise the gap would be greater than one cell wide.
        # Collect the 4 outside lines of each diamond shape
        # Since all slopes are either 1 or -1 we can store only the intercept
        # b = y₁ +/- x₁
        radius = sensor.distance(beacon)
        pos_diag_intercepts.append(sensor.y - sensor.x + radius + 1)
        pos_diag_intercepts.append(sensor.y - sensor.x - radius - 1)
        neg_diag_intercepts.append(sensor.y + sensor.x + radius + 1)
        neg_diag_intercepts.append(sensor.y + sensor.x - radius - 1)

    for up in pos_diag_intercepts:
        for down in neg_diag_intercepts:
            # Check each intersections of these lines for a point outside all ranges
            intersection = Vec2((down - up) // 2, (down + up) // 2)
            if not intersection.in_bounds(bounds):
                continue
            if all(sensor.distance(intersection) > sensor.distance(beacon) for sensor, beacon in coords):
                return 4_000_000 * intersection.x + intersection.y


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
