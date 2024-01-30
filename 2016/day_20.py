with open("2016/data/day_20.txt") as f:
    ips = sorted(tuple([int(el) for el in line.strip().split("-")]) for line in f.readlines())


def allowed_ip(count=False):
    cnt = value = 0
    for lo, hi in ips:
        if lo <= value <= hi:
            value = hi + 1
        elif value < lo:
            if not count:
                return value
            cnt += lo - value
            value = hi + 1
    return cnt


def part1():
    return allowed_ip()


def part2():
    return allowed_ip(count=True)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
