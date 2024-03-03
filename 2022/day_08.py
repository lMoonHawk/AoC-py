with open("2022/data/day_08.txt") as f:
    forest = [[int(height) for height in row.strip()] for row in f]


def seights(forest, i, j):
    yield forest[i][:j][::-1]
    yield forest[i][j + 1 :]
    yield [forest[k][j] for k in range(i)][::-1]
    yield [forest[k][j] for k in range(i + 1, len(forest))]


def is_visible(forest, i, j):
    for line in seights(forest, i, j):
        if not line or forest[i][j] > max(line):
            return True
    return False


def view_dist(height, line):
    if not line:
        return 0
    for k, other_height in enumerate(line):
        if other_height >= height:
            return k + 1
    return k + 1


def scenic_score(forest, i, j):
    prod = 1
    for line in seights(forest, i, j):
        prod *= view_dist(forest[i][j], line)
    return prod


def part1():
    return sum(is_visible(forest, i, j) for i in range(len(forest)) for j in range(len(forest[0])))


def part2():
    return max(scenic_score(forest, i, j) for i in range(len(forest)) for j in range(len(forest[0])))


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
