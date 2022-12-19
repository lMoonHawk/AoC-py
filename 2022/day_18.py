def part1():
    drops = []
    ranges = [None, None, None]
    with open("2022/data/day_18.txt") as f:
        for line in f:
            drop = tuple([int(drop) for drop in line.strip().split(",")])
            drops.append(drop)

            for i in range(len(ranges)):
                ranges[i] = (
                    drop[i] + 1
                    if ranges[i] is None or drop[i] + 1 > ranges[i]
                    else ranges[i]
                )

    grid = [
        [[0 for _ in range(ranges[2])] for _ in range(ranges[1])]
        for _ in range(ranges[0])
    ]

    for drop in drops:
        grid[drop[0]][drop[1]][drop[2]] = 1

    perimeter = 0
    for i in range(ranges[0]):
        for j in range(ranges[1]):
            for k in range(ranges[2]):

                if grid[i][j][k] == 0:
                    continue
                if i - 1 < 0 or grid[i - 1][j][k] == 0:
                    perimeter += 1
                if i + 1 >= ranges[0] or grid[i + 1][j][k] == 0:
                    perimeter += 1
                if j - 1 < 0 or grid[i][j - 1][k] == 0:
                    perimeter += 1
                if j + 1 >= ranges[1] or grid[i][j + 1][k] == 0:
                    perimeter += 1
                if k - 1 < 0 or grid[i][j][k - 1] == 0:
                    perimeter += 1
                if k + 1 >= ranges[2] or grid[i][j][k + 1] == 0:
                    perimeter += 1

    print(perimeter)


def part2():
    pass


if __name__ == "__main__":
    part1()
    part2()
