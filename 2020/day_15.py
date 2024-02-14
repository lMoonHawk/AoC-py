with open("2020/data/day_15.txt") as f:
    numbers = [int(n) for n in f.readline().strip().split(",")]


def run_game(rounds):
    previous_numbers = [None for _ in range(rounds)]
    for turn, num in enumerate(numbers[:-1], 1):
        previous_numbers[num] = turn
    previous_number = numbers[-1]
    for k in range(len(numbers), rounds):
        if previous_numbers[previous_number] is None:
            number = 0
        else:
            number = k - previous_numbers[previous_number]
        previous_numbers[previous_number] = k
        previous_number = number
    return number


def part1():
    return run_game(2020)


def part2():
    return run_game(30_000_000)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
