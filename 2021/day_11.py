def part1():

    def inc_neighbors(i, j):

        in_bound: bool = (0 <= i <= 9) and (0 <= j <= 9)
        # Has not flashed yet
        if in_bound and not flash_map[i][j]:
            energy_map[i][j] += 1

    def wave_step() -> int:
        """ If flashes, increment all neighbors"""
        flashes = 0
        for i, row in enumerate(energy_map):
            for j, energy in enumerate(row):
                if energy > 9:
                    flash_map[i][j] = True
                    energy_map[i][j] = 0
                    flashes += 1

                    offsets_i = [-1, -1, 0, 1, 1, 1, 0, -1]
                    offsets_j = [0, 1, 1, 1, 0, -1, -1, -1]

                    for offset_i, offset_j in zip(offsets_i, offsets_j):
                        inc_neighbors(i + offset_i, j + offset_j)

        return flashes

    energy_map: list[list[int]] = []

    with open("2021/data/day_11.txt") as f:
        for line in f:
            energy_map.append([int(char) for char in line.strip()])

    rows_count = len(energy_map)
    cols_count = len(energy_map[0])
    total_flashes = 0

    for i in range(100):
        flash_map: list[list[bool]] = [
            [False] * cols_count for i in range(rows_count)]

        for i, row in enumerate(energy_map):
            for j, energy in enumerate(row):
                energy_map[i][j] += 1

        flashes = 0
        previous_flashes = 0
        stabilized = False

        while not stabilized:
            flashes += wave_step()
            if flashes == previous_flashes:
                stabilized = True
            previous_flashes = flashes

        total_flashes += flashes

    print(total_flashes)


def part2():
    def inc_neighbors(i, j):

        in_bound: bool = (0 <= i <= 9) and (0 <= j <= 9)
        # Has not flashed yet
        if in_bound and not flash_map[i][j]:
            energy_map[i][j] += 1

    def wave_step() -> int:
        """ If flashes, increment all neighbors"""
        flashes = 0
        for i, row in enumerate(energy_map):
            for j, energy in enumerate(row):
                if energy > 9:
                    flash_map[i][j] = True
                    energy_map[i][j] = 0
                    flashes += 1

                    offsets_i = [-1, -1, 0, 1, 1, 1, 0, -1]
                    offsets_j = [0, 1, 1, 1, 0, -1, -1, -1]

                    for offset_i, offset_j in zip(offsets_i, offsets_j):
                        inc_neighbors(i + offset_i, j + offset_j)

        return flashes

    energy_map: list[list[int]] = []

    with open("2021/data/day_11.txt") as f:
        for line in f:
            energy_map.append([int(char) for char in line.strip()])

    rows_count = len(energy_map)
    cols_count = len(energy_map[0])
    synchronized = False
    step = 0

    while not synchronized:
        flash_map: list[list[bool]] = [
            [False] * cols_count for i in range(rows_count)]

        for i, row in enumerate(energy_map):
            for j, energy in enumerate(row):
                energy_map[i][j] += 1

        flashes = 0
        previous_flashes = 0
        stabilized = False

        while not stabilized:
            flashes += wave_step()
            if flashes == previous_flashes:
                stabilized = True
            previous_flashes = flashes

        step += 1

        # If all of them are 0
        if all([not any(row) for row in energy_map]):
            synchronized = True

    print(step)


if __name__ == '__main__':
    part1()
    part2()
