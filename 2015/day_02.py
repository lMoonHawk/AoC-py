with open("2015/data/day_02.txt") as f:
    gifts = [[int(el) for el in line.strip().split("x")] for line in f]


def part1():
    paper = 0
    for l, w, h in gifts:
        areas = l * w, l * h, w * h
        paper += 2 * sum(areas) + min(areas)
    return paper


def part2():
    return sum(2 * sum(sorted(dim)[:2]) + dim[0] * dim[1] * dim[2] for dim in gifts)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
