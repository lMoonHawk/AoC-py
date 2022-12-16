ROW = 2000000
RANGE_MIN = 0
RANGE_MAX = 4_000_000


def distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


def part1():
    ranges_row = []
    beacons_row = set()
    with open("2022/data/day_15.txt") as f:
        for line in f:
            # Isolate numbers and extract them
            numbers = [
                int(c)
                for c in line.replace(",", " ")
                .replace("=", " ")
                .replace(":", " ")
                .split()
                if c.lstrip("-").isdigit()
            ]
            sensor = tuple([numbers[0], numbers[1]])
            beacon = tuple([numbers[2], numbers[3]])
            if beacon[1] == ROW:
                beacons_row.add(beacon)
            reach = distance(sensor, beacon)
            # Distance left when reaching ROW directly
            left_row = reach - abs(sensor[1] - ROW)
            # Range of reach on row ROW
            if left_row > 0:
                range_row = [sensor[0] - left_row, sensor[0] + left_row]
                ranges_row.append(range_row)

    # Merge ranges
    ranges_row.sort()
    interval = [ranges_row.pop(0)]

    for i in ranges_row:
        if interval[-1][0] <= i[0] <= interval[-1][1]:
            interval[-1][1] = max(interval[-1][1], i[1])
        else:
            interval.append(i)
    # Sum of all intervals covered by sensors minus beacons on the row
    answer = sum(i[1] - i[0] + 1 for i in interval) - len(beacons_row)
    print(answer)


def part2():
    diags_up = set()
    diags_down = set()
    sensors = []
    with open("2022/data/day_15.txt") as f:
        for line in f:
            # Isolate numbers and extract them
            numbers = [
                int(c)
                for c in line.replace(",", " ")
                .replace("=", " ")
                .replace(":", " ")
                .split()
                if c.lstrip("-").isdigit()
            ]
            sensor = tuple([numbers[0], numbers[1]])

            beacon = tuple([numbers[2], numbers[3]])
            outside = distance(sensor, beacon) + 1

            sensors.append([sensor, outside - 1])

            # Store x-axis coord of the 4 lines outside the sensor's range
            # /
            diags_up.add(outside + sensor[1] - sensor[0])
            diags_up.add(-outside + sensor[1] - sensor[0])
            # \
            diags_down.add(outside + sensor[1] + sensor[0])
            diags_down.add(-outside + sensor[1] + sensor[0])

    def search_empty():
        # Missing beacon must lie just 1 out of reach
        # Let's check for shared spots like this
        # i.e. intersection of all diagonals forming the scanner's diamond
        for up in diags_up:
            for down in diags_down:
                intersection = tuple([(down - up) // 2, (down + up) // 2])
                if all(RANGE_MIN <= p <= RANGE_MAX for p in intersection):
                    if all(
                        distance(sensor[0], intersection) > sensor[1]
                        for sensor in sensors
                    ):
                        return intersection

    intersection = search_empty()
    print(4_000_000 * intersection[0] + intersection[1])


if __name__ == "__main__":
    part1()
    part2()
