with open("2015/data/day_05.txt") as f:
    strings = [line.strip() for line in f]


def part1():
    def is_nice(s):
        vowel, twice = 0, False
        for k, char in enumerate(s):
            if char in "aeiou":
                vowel += 1
            if k < len(s) - 1 and char == s[k + 1]:
                twice = True
        return vowel >= 3 and twice and not any(banned in s for banned in ["ab", "cd", "pq", "xy"])

    return sum(is_nice(string) for string in strings)


def part2():
    def is_nice(s):
        cond1 = cond2 = False
        for k, char in enumerate(s):
            cond1 |= k < len(s) - 1 and s[k : k + 2] in s[k + 2 :]
            cond2 |= k < len(s) - 2 and char == s[k + 2]
            if cond1 and cond2:
                return True
        return False

    return sum(is_nice(string) for string in strings)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
