def part1():

    answer = 0

    def is_included(a: list[str], b: list[str]):
        if (int(a[0]) >= int(b[0]) and int(a[1]) <= int(b[1])) or (
            int(a[0]) <= int(b[0]) and int(a[1]) >= int(b[1])
        ):
            return True
        return False

    with open("2022/data/day_04.txt") as f:
        for line in f:
            sectors = [el.split("-") for el in line.strip().split(",")]
            if is_included(sectors[0], sectors[1]):
                answer += 1

    print(answer)


def part2():
    answer = 0

    def is_overlapping(a: list[str], b: list[str]):
        if (
            (int(b[0]) <= int(a[0]) <= int(b[1]))
            or (int(b[0]) <= int(a[1]) <= int(b[1]))
            or (int(a[0]) <= int(b[0]) <= int(a[1]))
            or (int(a[0]) <= int(b[1]) <= int(a[1]))
        ):
            return True
        return False

    with open("2022/data/day_04.txt") as f:
        for line in f:
            sectors = [el.split("-") for el in line.strip().split(",")]
            if is_overlapping(sectors[0], sectors[1]):
                answer += 1

    print(answer)


if __name__ == "__main__":
    part1()
    part2()
