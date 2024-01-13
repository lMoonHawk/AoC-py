with open("2017/data/day_04.txt") as f:
    phrases = [line.split() for line in f.readlines()]


def part1():
    return sum(all([phrase.count(word) == 1 for word in phrase]) for phrase in phrases)


def part2():
    phrases_sets = [[{k: word.count(k) for k in word} for word in phrase] for phrase in phrases]
    return sum(all([phrase.count(word) == 1 for word in phrase]) for phrase in phrases_sets)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
