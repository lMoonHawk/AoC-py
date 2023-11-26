with open("2020/data/day_15.txt") as f:
    numbers = [int(n) for n in f.readline().strip().split(",")]


def run_game(rounds):
    previous_numbers = dict()
    for k in range(rounds):
        if k < len(numbers):
            number = numbers[k]
        else:
            number = 0 if previous_number not in previous_numbers else k - previous_numbers[previous_number]

        if k > 0:
            previous_numbers[previous_number] = k

        previous_number = number

    return number


def part1():
    print(run_game(2020))


def part2():
    print(run_game(30_000_000))


if __name__ == "__main__":
    part1()
    part2()
