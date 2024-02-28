div, add1, add2 = [], [], []
with open("2021/data/day_24.txt") as f:
    for i, line in enumerate(f):
        arg2 = line.split()[-1]
        if i % 18 == 4:
            div.append(int(arg2))
        elif i % 18 == 5:
            add1.append(int(arg2))
        elif i % 18 == 15:
            add2.append(int(arg2))


def run(k=0, z=0, fun=lambda x: x):
    if k == 14:
        return 0 if z == 0 else None

    z_b = z // div[k]

    if add1[k] < 0:
        forced = z % 26 + add1[k]
        if 1 <= forced <= 9:
            rest = run(k + 1, z_b, fun)
            if rest is not None:
                return forced * 10 ** (13 - k) + rest
        else:
            return None
    else:
        for num in fun(range(1, 10)):
            rest = run(k + 1, z_b * 26 + num + add2[k], fun)
            if rest is not None:
                return num * 10 ** (13 - k) + rest
    return None


def part1():
    # The program consists of 14 blocks of 18 lines, with only 3 operations different between them
    # This is captured in globals "div", "add1" and "add2".
    # There is a branch for each block depending on the value of z and the number
    # On blocks where add1 is positive, the program multiplies z by 26 everytime (+ some other values)
    # On other blocks we could divide by 26 or mutiply by 26 (+ some other values)
    # Since the number of these rows is half the number of blocks,
    #   in order to reach 0 we need to divide for all the possible blocks (when add1 is negative)
    # To reduce the search space we force half the digits
    return run(fun=reversed)


def part2():
    return run()


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
