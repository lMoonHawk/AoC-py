with open("2015/data/day_25.txt") as f:
    row, col = [int(el.split()[-1]) for el in f.read().strip().strip(".").split(", ")[1:]]


def part1():
    y = x = 1
    code = 20151125
    while True:
        if y == 1:
            y, x = x + 1, 1
        else:
            y, x = y - 1, x + 1
        code = (code * 252533) % 33554393
        if (y, x) == (row, col):
            return code


def part2():
    return


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
