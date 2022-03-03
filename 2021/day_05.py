def part1():

    grid = {}

    with open("2021/data/day_05.txt") as f:
        for line in f:
            line = line.strip().replace(" ", "").split("->")

            x_1, y_1, x_2, y_2 = [
                int(pos) for coords in line for pos in coords.split(",")
            ]

            ref = []
            # Line is horizontal or vertical
            if x_1 == x_2:
                line = list(range(min(y_1, y_2), max(y_1, y_2) + 1))
                ref = [str(x_1) + "," + str(pos) for pos in line]
            elif y_1 == y_2:
                line = list(range(min(x_1, x_2), max(x_1, x_2) + 1))
                ref = [str(pos) + "," + str(y_1) for pos in line]

            # Keep points in the dict only if a line has visited
            for point in ref:
                if point in grid:
                    grid[point] += 1
                else:
                    grid[point] = 1

        print(len([point for point in grid.values() if point > 1]))


def part2():

    def sign(a: int) -> int:
        if not a:
            return 0
        if a > 0:
            return 1
        return -1

    grid = {}

    with open("2021/data/day_05.txt") as f:
        for line in f:
            line = line.strip().replace(" ", "").split("->")

            x_1, y_1, x_2, y_2 = [
                int(pos) for coords in line for pos in coords.split(",")]

            length = max(abs(x_2 - x_1), abs(y_2 - y_1)) + 1
            x_s = [x_1 + sign(x_2 - x_1) * i for i in range(length)]
            y_s = [y_1 + sign(y_2 - y_1) * i for i in range(length)]

            # List all the points visited by that line
            ref = [str(x) + "," + str(y) for x, y in zip(x_s, y_s)]

            # Keep points in the dict only if a line has visited
            for point in ref:
                if point in grid:
                    grid[point] += 1
                else:
                    grid[point] = 1

        print(len([point for point in grid.values() if point > 1]))


if __name__ == '__main__':
    part1()
    part2()
