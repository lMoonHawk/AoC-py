def part1():

    grid = {}

    with open("2021/data/day_05.txt") as f:
        for line in f:
            line = line.strip().replace(" ", "").split("->")

            x_1, y_1, x_2, y_2 = [
                int(pos) for coords in line for pos in coords.split(",")
            ]
            # print(f'coord 1 = {x_1}, {y_1} ; coord 2 = {x_2}, {y_2}')
            ref = []
            # Line is horizontal or vertical
            if x_1 == x_2:
                line = list(range(min(y_1, y_2), max(y_1, y_2) + 1))
                ref = [str(x_1) + "," + str(pos) for pos in line]
            elif y_1 == y_2:
                line = list(range(min(x_1, x_2), max(x_1, x_2) + 1))
                ref = [str(pos) + "," + str(y_1) for pos in line]

            for point in ref:
                if point in grid:
                    grid[point] += 1
                else:
                    grid[point] = 1
        print(grid)
        print(len([point for point in grid.values() if point > 1]))


def part2():
    pass


if __name__ == '__main__':
    part1()
    # part2()
