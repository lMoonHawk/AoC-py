def part1():
    answer = 0
    with open("2020/data/day_03.txt") as f:
        for row, line in enumerate(f):
            line = line.strip()
            if line[row * 3 % len(line)] == "#":
                answer += 1

    print(answer)


def part2():
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    trees = [0] * len(slopes)

    with open("2020/data/day_03.txt") as f:
        for row, line in enumerate(f):
            line = line.strip()

            for i, slope in enumerate(slopes):
                right, down = slope

                # If this slope does not hit this row
                if row % down != 0:
                    continue
                # Get correct index (right) by inverting the slope
                if line[row * right // down % len(line)] == "#":
                    trees[i] += 1
    answer = 1
    for i in trees:
        answer *= i
    print(answer)


if __name__ == "__main__":
    part1()
    part2()
