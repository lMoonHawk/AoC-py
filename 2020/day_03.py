def gen_rows():
    with open("2020/data/day_03.txt") as f:
        yield from (row.strip() for row in f)


def part1():
    return sum(row[i * 3 % len(row)] == "#" for i, row in enumerate(gen_rows()))


def part2():
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    trees = [0] * len(slopes)
    for i, row in enumerate(gen_rows()):
        for k, slope in enumerate(slopes):
            right, down = slope
            if i % down != 0:
                continue
            trees[k] += row[i * right // down % len(row)] == "#"

    answer = 1
    for i in trees:
        answer *= i
    return answer


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
