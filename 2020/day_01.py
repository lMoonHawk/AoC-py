with open("2020/data/day_01.txt") as f:
    nums = [int(num.strip()) for num in f]


def mult_find_sum(nums: list[int], target: int, k: int) -> int:
    if target < 0:
        return None
    if target == 0 and k == 0:
        return 1
    for num in nums:
        sum_comp = mult_find_sum(nums, target - num, k - 1)
        if sum_comp:
            return sum_comp * num
    return None


def part1():
    return mult_find_sum(nums, 2020, 2)


def part2():
    return mult_find_sum(nums, 2020, 3)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
