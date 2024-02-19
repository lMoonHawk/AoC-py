with open("2021/data/day_03.txt") as f:
    diag = [n.strip() for n in f]


def get_rating(nums, mode, col=0):
    if len(nums) == 1:
        return nums[0]
    value = int(sum(bits[col] == "1" for bits in nums) >= len(nums) / 2)
    if mode == "co2":
        value = 1 - value
    return get_rating([bits for bits in nums if bits[col] == str(value)], mode, col + 1)


def part1():
    counter = [0] * len(diag[0])
    for bits in diag:
        for i, bit in enumerate(bits):
            counter[i] += 1 if bit == "1" else -1
    gamma = int("".join(["1" if i > 0 else "0" for i in counter]), 2)
    return gamma * ((1 << gamma.bit_length()) - 1 - gamma)


def part2():
    return int(get_rating(diag, "oxygen"), 2) * int(get_rating(diag, "co2"), 2)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
