with open("2015/data/day_24.txt") as f:
    nums = tuple([int(line) for line in f])


def min_sum(k, use, memo={}):
    if k == 0:
        return tuple()
    if not use or k < 0:
        return None
    if (k, use) in memo:
        return memo[(k, use)]

    num, rest = use[0], use[1:]
    w = min_sum(k - num, rest)
    wo = min_sum(k, rest)

    if w is None and wo is None:
        memo[(k, use)] = None
    elif w is None:
        memo[(k, use)] = wo
    elif wo is None:
        memo[(k, use)] = (num,) + w
    else:
        memo[(k, use)] = min([(num,) + w, wo], key=lambda x: (len(x), qe(x)))
    return memo[(k, use)]


def qe(weights):
    prod = 1
    for weight in weights:
        prod *= weight
    return prod


def part1():
    return qe(min_sum(sum(nums) // 3, nums))


def part2():
    return qe(min_sum(sum(nums) // 4, nums))


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
