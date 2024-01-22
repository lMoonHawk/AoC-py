with open("2016/data/day_06.txt") as f:
    messages = [line.strip() for line in f.readlines()]


def count(d, c):
    if c not in d:
        d[c] = 0
    d[c] += 1


def error_correct(messages, func):
    positions = [dict() for _ in range(len(messages[0]))]
    for message in messages:
        for pos, char in enumerate(message):
            count(positions[pos], char)
    return "".join(func(position, key=position.get) for position in positions)


def part1():
    return error_correct(messages, max)


def part2():
    return error_correct(messages, min)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
