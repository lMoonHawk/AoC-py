original_nums = []
with open("2022/data/day_20.txt") as f:
    for line in f:
        original_nums.append(int(line.strip()))

n = len(original_nums)


def mix(numbers, key=1, times=1):
    mixed = [[num * key, order] for order, num in enumerate(numbers)]
    for i in range(n * times):
        i %= n

        index = mixed.index([numbers[i] * key, i])
        new_pos = index + mixed[index][0]

        if new_pos < -n:
            new_pos = -(-new_pos % (n - 1))
        if new_pos > n:
            new_pos = new_pos % (n - 1)

        mixed.insert(new_pos, mixed.pop(index))

    return mixed


def part1():

    nums = mix(original_nums)

    zero = nums.index([0, original_nums.index(0)])
    answer = 0
    for el in [1_000, 2_000, 3_000]:
        index_wrapped = (zero + el) % n
        answer += nums[index_wrapped][0]

    print(answer)


def part2():
    nums = mix(original_nums, key=811589153, times=10)

    zero = nums.index([0, original_nums.index(0)])
    answer = 0
    for el in [1_000, 2_000, 3_000]:
        index_wrapped = (zero + el) % n
        answer += nums[index_wrapped][0]

    print(answer)


if __name__ == "__main__":
    part1()
    part2()
