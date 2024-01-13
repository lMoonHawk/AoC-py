with open("2017/data/day_02.txt") as f:
    sheet = [[int(n) for n in line.strip().split()] for line in f.readlines()]


def part1():
    return sum(max(row) - min(row) for row in sheet)


def part2():
    out = 0
    for row in sheet:
        for n1, n2 in [(n1, n2) for k, n1 in enumerate(row[:-1]) for n2 in row[k + 1 :]]:
            div, mod = divmod(*sorted([-n1, -n2]))
            if mod == 0:
                out += div
                break
    return out


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
