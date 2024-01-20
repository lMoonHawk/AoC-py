with open("2016/data/day_03.txt") as f:
    shapes = [tuple([int(el) for el in line.strip().split()]) for line in f]


def part1():
    return sum(a + b > c and a + c > b and b + c > a for a, b, c in shapes)


def part2():
    return sum(
        shapes[k][col] + shapes[k + 1][col] > shapes[k + 2][col]
        and shapes[k][col] + shapes[k + 2][col] > shapes[k + 1][col]
        and shapes[k + 1][col] + shapes[k + 2][col] > shapes[k][col]
        for k in range(0, len(shapes), 3)
        for col in range(3)
    )


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
