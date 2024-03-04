with open("2015/data/day_08.txt") as f:
    strings = [line.strip() for line in f]


def eval_len(s):
    s = s[1:-1]
    count = k = 0
    while k < len(s):
        if s[k] == "\\":
            k += 4 if s[k + 1] == "x" else 2
        else:
            k += 1
        count += 1
    return count


def part1():
    return sum(len(string) - eval_len(string) for string in strings)


def part2():
    return sum(2 + string.count('"') + string.count("\\") for string in strings)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
