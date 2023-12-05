def claims():
    with open("2018/data/day_03.txt") as f:
        for line in f:
            line = line.strip()
            s1 = line.index("@")
            s2 = line.index(":")
            claim_nb = line[1 : s1 - 1]
            pos = [int(el) for el in line[s1 + 2 : s2].split(",")]
            rect = [int(el) for el in line[s2 + 2 :].split("x")]
            yield claim_nb, pos, rect


def get_fabric():
    fabric_size = 1_000
    fabric = [[0] * fabric_size for _ in range(fabric_size)]
    for _, (x, y), (w, h) in claims():
        for xp, yp in ((xp, yp) for yp in range(y, y + h) for xp in range(x, x + w)):
            fabric[yp][xp] += 1
    return fabric


def part1():
    return sum(sum(1 for el in row if el > 1) for row in get_fabric())


def part2():
    fabric = get_fabric()
    for claim_id, (x, y), (w, h) in claims():
        if all(fabric[yp][xp] == 1 for yp in range(y, y + h) for xp in range(x, x + w)):
            return claim_id


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
