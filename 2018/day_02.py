def box_ids():
    with open("2018/data/day_02.txt") as f:
        yield from (line.strip() for line in f.readlines())


def part1():
    twice = thrice = 0
    for box_id in box_ids():
        dups = [box_id.count(a) for a in box_id]
        if 2 in dups:
            twice += 1
        if 3 in dups:
            thrice += 1
    return twice * thrice


def part2():
    for box_id1 in box_ids():
        for box_id2 in box_ids():
            if box_id1 == box_id2:
                continue
            res = "".join(b1 for b1, b2 in zip(box_id1, box_id2) if b1 == b2)
            if len(res) == len(box_id1) - 1:
                return res


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
