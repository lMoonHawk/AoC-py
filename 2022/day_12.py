height_map: list[list[int]] = []

with open("2022/data/day_12.txt") as f:
    for i, line in enumerate(f):
        row = []
        for j, elevation in enumerate(line.strip()):
            if elevation == "S":
                start = (i, j)
                row.append(1)
            elif elevation == "E":
                end = (i, j)
                row.append(26)
            else:
                # Convert letter a - z to 1 - 26
                elevation_int = ord(elevation) - 96
                row.append(int(elevation_int))
        height_map.append(row)

nb_rows = len(height_map)
nb_cols = len(height_map[0])


def get_elevation(coord):
    i, j = coord
    return height_map[i][j]


def search(coord):
    visited = set([coord])
    queue = [[coord, 0]]

    while queue:
        current, distance = queue.pop(0)
        if current == end:
            return distance
        i, j = current
        neighbors = [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]
        for neighbor in neighbors:
            n_i, n_j = neighbor
            if neighbor in visited:
                continue
            if n_i < 0 or n_i >= nb_rows or n_j < 0 or n_j >= nb_cols:
                continue
            if height_map[n_i][n_j] > height_map[i][j] + 1:
                continue
            visited.add(neighbor)
            queue.append([neighbor, distance + 1])


def part1():
    print(search(start))


def part2():

    min_path = None
    for i, row in enumerate(height_map):
        for j, elevation in enumerate(row):
            if elevation != 1:
                continue

            # None if no path
            steps = search(tuple([i, j]))

            if steps is not None and (min_path is None or steps < min_path):
                min_path = steps

    print(min_path)


if __name__ == "__main__":
    part1()
    part2()
