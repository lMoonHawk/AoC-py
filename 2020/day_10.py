with open("2020/data/day_10.txt") as f:
    jolts = [int(jolt.strip()) for jolt in f.readlines()]
jolts.sort()


def part1():
    # To go through each adapter, we only need to iterate over the sorted list
    # and count the difference between each joltage
    # diff: [diff1, diff2, diff3]
    diff = [0, 0, 1]
    for i, jolt in enumerate(jolts):
        if i == 0:
            current_adapter = 0
        diff[jolt - current_adapter - 1] += 1
        current_adapter = jolt
    return diff[0] * diff[2]


def part2():
    # Initialize the tabulation [(joltage, number of ways to get this joltage)]
    tab = [(0, 1)]
    for jolt in jolts:
        # At any point in the adapter list, the number of ways to get to it is:
        # sum(num of ways for each adapter that can reach it)
        ways = sum([j_ways for j, j_ways in tab if jolt - j <= 3])
        tab.append(tuple([jolt, ways]))
        if len(tab) > 3:
            del tab[0]
    return tab[-1][1]


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
