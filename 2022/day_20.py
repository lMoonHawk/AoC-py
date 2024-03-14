with open("2022/data/day_20.txt") as f:
    nums_init = [int(line) for line in f]
index_zero = nums_init.index(0)


def mix(numbers, key=1, times=1):
    mixed = [(num * key, order) for order, num in enumerate(numbers)]
    for i in range(len(numbers) * times):
        i %= len(numbers)
        index = mixed.index((numbers[i] * key, i))
        mixed.insert((index + mixed[index][0]) % (len(numbers) - 1), mixed.pop(index))
    return mixed


def get_coord(nums, index_zero):
    zero = nums.index((0, index_zero))
    return [nums[(zero + el) % len(nums)][0] for el in (1_000, 2_000, 3_000)]


def part1():
    return sum(get_coord(mix(nums_init), index_zero))


def part2():
    return sum(get_coord(mix(nums_init, key=811589153, times=10), index_zero))


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
