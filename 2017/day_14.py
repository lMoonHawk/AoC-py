with open("2017/data/day_14.txt") as f:
    key = f.readline().strip()


def knot_hash(key):
    lengths = [ord(c) for c in key] + [17, 31, 73, 47, 23]
    index = skip = 0
    nums = [k for k in range(256)]
    for _ in range(64):
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

    xored = [0 for _ in range(16)]
    for i in range(16):
        for j in range(16):
            xored[i] ^= nums[16 * i + j]
    return "".join(f"{hex(code)[2:]:0>2}" for code in xored)


def build_disk():
    return [[el for c in knot_hash(f"{key}-{n}") for el in f"{bin(int(c, 16))[2:]:0>4}"] for n in range(128)]


def count_group(disk, i, j, visited=set()):
    visited.add((i, j))
    return 1 + sum(
        count_group(disk, i, j, visited)
        for i, j in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
        if (i, j) not in visited and (0 <= i < 128 and 0 <= j < 128) and disk[i][j] == "1"
    )


def part1():
    return sum(row.count("1") for row in build_disk())


def part2():
    disk = build_disk()
    visited = set()
    return len(
        [
            count_group(disk, i, j, visited)
            for i, row in enumerate(disk)
            for j, _ in enumerate(row)
            if (i, j) not in visited and disk[i][j] == "1"
        ]
    )


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
