def get_elves_pos_ini():
    with open("2022/data/day_23.txt") as f:
        return {(col, row) for row, line in enumerate(f) for col, char in enumerate(line) if char == "#"}


CHECKS = [
    [(x, -1) for x in range(-1, 2)],
    [(x, 1) for x in range(-1, 2)],
    [(-1, y) for y in range(-1, 2)],
    [(1, y) for y in range(-1, 2)],
]


def dict_append(d, k, v):
    if k not in d:
        d[k] = []
    d[k].append(v)


def move_elves(elves, checks):
    moved = False
    staging = dict()
    for x, y in elves:
        available = 0
        for adjacents in checks:
            empty_line = True
            for mx, my in adjacents:
                if (x + mx, y + my) in elves:
                    empty_line = False
                    break
            if empty_line:
                available += 1
                if available == 1:
                    mx, my = adjacents[1]
                    move = x + mx, y + my
            elif available > 0:
                break
        if 0 < available < 4:
            dict_append(staging, move, (x, y))

    for proposed, positions in staging.items():
        if len(positions) == 1:
            elves.remove(*positions)
            elves.add(proposed)
            moved = True
    checks.append(checks.pop(0))
    return moved


def part1():
    elves = get_elves_pos_ini()
    checks = CHECKS.copy()
    for _ in range(10):
        move_elves(elves, checks)

    xs, ys = [x for x, _ in elves], [y for _, y in elves]
    return (max(xs) - min(xs) + 1) * (max(ys) - min(ys) + 1) - len(elves)


def part2():
    elves = get_elves_pos_ini()
    checks = CHECKS.copy()
    cnt = 0
    while move_elves(elves, checks):
        cnt += 1
    return cnt + 1


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
