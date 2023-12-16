def spring_gen():
    with open("2023/data/day_12.txt") as f:
        yield from ((s, tuple(int(el) for el in b.split(","))) for s, b in (l.strip().split() for l in f.readlines()))


def combin(spr, grps, memo={}):
    if (spr, grps) in memo:
        return memo[(spr, grps)]
    if not spr:
        return 1 if not grps else 0
    if not grps:
        return 1 if "#" not in spr else 0

    result = 0

    if spr[0] in [".", "?"]:
        result += combin(spr[1:], grps)
    if spr[0] in ["#", "?"]:
        can_grp = grps[0] <= len(spr) and "." not in spr[: grps[0]]
        if can_grp and (grps[0] == len(spr) or spr[grps[0]] != "#"):
            result += combin(spr[grps[0] + 1 :], grps[1:])

    memo[(spr, grps)] = result
    return result


def part1():
    return sum(combin(row, grp) for row, grp in spring_gen())


def part2():
    return sum(combin("?".join(row for _ in range(5)), grp * 5) for row, grp in spring_gen())


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
