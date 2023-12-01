DIGITS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def get_digit(line, front):
    for i in range(1, len(line) + 1):
        inspect = line[:i] if front else line[-i:]
        for digit_name, digit in DIGITS.items():
            if digit_name in inspect or digit in inspect:
                return digit


def part1():
    with open("2023/data/day_01.txt") as f:
        digits = [[c for c in line.strip() if c.isdigit()] for line in f.readlines()]
        return sum(int(c[0] + c[-1]) for c in digits)


def part2():
    with open("2023/data/day_01.txt") as f:
        lines = [line.strip() for line in f.readlines()]
    return sum(int(get_digit(line, True) + get_digit(line, False)) for line in lines)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
