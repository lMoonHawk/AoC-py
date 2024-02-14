with open("2020/data/day_19.txt") as f:
    lines = [line.strip() for line in f.readlines()]
s = lines.index("")
rules_part, messages = lines[:s], lines[s + 1 :]

rules = dict()
for rule_line in rules_part:
    rule, pattern = rule_line.split(": ")
    pattern = pattern.replace('"', "").split(" ")
    if "|" in pattern:
        s = pattern.index("|")
        pattern = [pattern[:s], pattern[s + 1 :]]
    elif pattern in [["a"], ["b"]]:
        pattern = pattern[0]
    else:
        pattern = [pattern]
    rules[rule] = pattern


def is_matching(message):
    return len(message) in rec_match(message, "0")


def rec_match(message, rule, index=0):
    if index == len(message):
        return []
    patterns = rules[rule]
    if patterns in ["a", "b"]:
        if message[index] == patterns:
            return [index + 1]
        return []
    matches = []
    for pattern in patterns:
        sub_matches = [index]
        for sub_rule in pattern:
            new_matches = []
            for idx in sub_matches:
                new_matches += rec_match(message, sub_rule, idx)
            sub_matches = new_matches
        matches += sub_matches
    return matches


def part1():
    return sum(is_matching(message) for message in messages)


def part2():
    rules["8"] = [["42"], ["42", "8"]]
    rules["11"] = [["42", "31"], ["42", "11", "31"]]
    return sum(is_matching(message) for message in messages)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
