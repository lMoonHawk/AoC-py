def lengths(parse_ascii=False):
    with open("2017/data/day_10.txt") as f:
        if parse_ascii:
            return [ord(char) for char in f.readline().strip()] + [17, 31, 73, 47, 23]

        else:
            return [int(length) for length in f.readline().strip().split(",")]


def knot_hash(lengths, count):
    index = skip = 0
    nums = [k for k in range(256)]
    for _ in range(count):
        for length in lengths:
            start = index % len(nums)
            end = (index + length) % len(nums)
            if length == 0:
                pass
            elif end == 0:
                nums[start:] = reversed(nums[start:])
            elif end > start:
                nums[start:end] = reversed(nums[start:end])
            else:
                selected = nums[start:] + nums[:end]
                selected.reverse()
                nums[start:] = selected[: len(nums[start:])]
                nums[:end] = selected[-len(nums[:end]) :]
            index += length + skip
            skip += 1
    return nums


def part1():
    nums = knot_hash(lengths(), 1)
    return nums[0] * nums[1]


def part2():
    nums = knot_hash(lengths(True), 64)
    xored = [0 for _ in range(16)]
    for i in range(16):
        for j in range(16):
            xored[i] ^= nums[16 * i + j]
    return "".join(f"{hex(code)[2:]:0>2}" for code in xored)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
