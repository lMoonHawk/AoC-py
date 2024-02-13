with open("2020/data/day_09.txt") as f:
    numbers = [int(number.strip()) for number in f.readlines()]


def can_sum(k: int, numbers: list[int]) -> bool:
    for i, n1 in enumerate(numbers[:-1]):
        for n2 in numbers[i + 1 :]:
            if n1 != n2 and n1 + n2 == k:
                return True
    return False


def find_invalid():
    for idx in range(len(numbers) - 25):
        if not can_sum(numbers[idx + 25], numbers[idx : idx + 25]):
            return numbers[idx + 25]


def find_set_sum(k: int) -> int:
    for i_min in range(len(numbers) - 1):
        for i_max in range(i_min + 1, len(numbers)):
            cont_set = numbers[i_min : i_max + 1]
            res = sum(cont_set)
            if res == k:
                return max(cont_set) + min(cont_set)
            if res > k:
                break


def part1():
    return find_invalid()


def part2():
    return find_set_sum(find_invalid())


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
