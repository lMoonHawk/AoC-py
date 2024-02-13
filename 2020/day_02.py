def pws():
    with open("2020/data/day_02.txt") as f:
        for line in f:
            span, letter, pw = line.strip().split(" ")
            pos1, pos2 = [int(rule) for rule in span.split("-")]
            letter = letter[0]
            yield pw, pos1, pos2, letter


def part1():
    return sum(pos1 <= pw.count(letter) <= pos2 for pw, pos1, pos2, letter in pws())


def part2():
    return sum((pw[pos1 - 1] == letter) ^ (pw[pos2 - 1] == letter) for pw, pos1, pos2, letter in pws())


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
