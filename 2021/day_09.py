def part1():

    heightmap: list[list[int]] = []
    risk_level = 0

    def is_low(i: int, j: int, heightmap: list[list[int]]) -> bool:
        """ Test for current value against neighbors in the array"""
        height = heightmap[i][j]
        last_row = len(heightmap) - 1
        last_col = len(heightmap[0]) - 1

        # Top
        if i - 1 >= 0 and heightmap[i - 1][j] <= height:
            return False
        # Right
        if j + 1 <= last_col and heightmap[i][j + 1] <= height:
            return False
        # Bottom
        if i + 1 <= last_row and heightmap[i + 1][j] <= height:
            return False
        # Left
        if j - 1 >= 0 and heightmap[i][j - 1] <= height:
            return False

        return True

    with open("2021/data/day_09.txt") as f:
        for row_char in f:
            row_char = row_char.strip()

            new_row = [int(height) for height in row_char]
            heightmap.append(new_row)

        for i, row in enumerate(heightmap):
            for j, height in enumerate(heightmap[i]):
                if is_low(i, j, heightmap):
                    risk_level += height + 1

        print(risk_level)


def part2():

    heightmap: list[list[str]] = []

    def calc_basin(
            heighmap: list[list[str]], visited: list[list[bool]],
            basin: list[str], i: int, j: int):
        """ Visits a location and calls itself on any non-visited neighbors.\n
        Returns (tuple): the heights in the basin so far
        and the updated visited array """
        visited[i][j] = True
        basin.append(heighmap[i][j])

        last_row = len(heightmap) - 1
        last_col = len(heightmap[0]) - 1

        # Top
        if (i - 1 >= 0 and not visited[i - 1][j] and
                heightmap[i - 1][j] != "9"):
            basin, visited = calc_basin(
                heightmap, visited, basin, i - 1, j)
        # Right
        if (j + 1 <= last_col and not visited[i][j + 1] and
                heightmap[i][j + 1] != "9"):
            basin, visited = calc_basin(
                heightmap, visited, basin, i, j + 1)
        # Bottom
        if (i + 1 <= last_row and not visited[i + 1][j] and
                heightmap[i + 1][j] != "9"):
            basin, visited = calc_basin(
                heightmap, visited, basin, i + 1, j)
        # Left
        if (j - 1 >= 0 and not visited[i][j - 1] and
                heightmap[i][j - 1] != "9"):
            basin, visited = calc_basin(
                heightmap, visited, basin, i, j - 1)

        return (basin, visited)

    with open("2021/data/day_09.txt") as f:
        for row_char in f:
            row_char = row_char.strip()

            new_row = [height for height in row_char]
            heightmap.append(new_row)

    rows_count = len(heightmap)
    cols_count = len(heightmap[0])
    visited = [[False] * cols_count for i in range(rows_count)]

    # List of basins
    basins: list[list[str]] = []

    for i, row in enumerate(heightmap):
        for j, height in enumerate(heightmap[i]):
            if not visited[i][j] and height != "9":
                # calc_basin returns (as a tuple)
                # - The length of the calculated basin
                # - The new visited array
                new_basin, visited = calc_basin(heightmap, visited, [], i, j)
                basins.append(new_basin)

    basins_len = map(len, basins)
    answer = 1
    for basin_len in sorted(basins_len)[-3:]:
        answer *= basin_len

    print(answer)


if __name__ == '__main__':
    part1()
    part2()
