with open("2021/data/day_14.txt") as f:
    template, rules = f.read().strip().split("\n\n")
    rules = {k: v for k, v in (line.split(" -> ") for line in rules.split("\n"))}


def polymer_score(steps):
    polymer = {k: template.count(k) for k in rules}
    freq = {k: template.count(k) for k in {el for pair in rules for el in pair}}
    for _ in range(steps):
        next_polymer = polymer.copy()
        for pair, count in polymer.items():
            left, right = pair
            insert = rules[pair]
            freq[insert] += count
            next_polymer[pair] -= count
            next_polymer[left + insert] += count
            next_polymer[insert + right] += count
        polymer = next_polymer
    return max(freq.values()) - min(freq.values())


def part1():
    return polymer_score(steps=10)


def part2():
    return polymer_score(steps=40)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
