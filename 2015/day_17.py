with open("2015/data/day_17.txt") as f:
    containers = [int(line) for line in f]


def combinations(target, minimise=False):
    stack = [(containers, 0, 0)]
    counter = dict()
    while stack:
        remaining, capacity, used = stack.pop()
        if capacity == target:
            if used not in counter:
                counter[used] = 0
            counter[used] += 1
            continue
        if remaining:
            if capacity + remaining[0] <= target:
                stack.append((remaining[1:], capacity + remaining[0], used + 1))
            stack.append((remaining[1:], capacity, used))
    return counter[min(counter)] if minimise else sum(counter.values())


def part1():
    return combinations(150)


def part2():
    return combinations(150, minimise=True)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
