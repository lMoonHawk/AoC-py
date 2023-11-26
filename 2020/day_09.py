SLIDING_WINDOW_SIZE = 25

with open("2020/data/day_09.txt") as f:
    numbers = [int(number.strip()) for number in f.readlines()]


def can_sum(k: int, numbers: list[int]) -> bool:
    for number_1 in numbers:
        for number_2 in numbers:
            if number_1 != number_2 and number_1 + number_2 == k:
                return True
    return False


def find_invalid():
    window = []

    for number in numbers:
        if len(window) == SLIDING_WINDOW_SIZE:
            if not can_sum(number, window):
                return number

            del window[0]
        window.append(number)


def find_set_sum(k: int) -> int:
    for i_min in range(len(numbers) - 1):
        for i_max in range(i_min + 1, len(numbers)):
            cont_set = numbers[i_min : (i_max + 1)]
            res = sum(cont_set)

            if res == k:
                return max(cont_set) + min(cont_set)
            if res > k:
                break


def part1():
    print(find_invalid())


def part2():
    target = find_invalid()
    print(find_set_sum(target))


if __name__ == "__main__":
    part1()
    part2()
