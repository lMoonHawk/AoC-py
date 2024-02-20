with open("2021/data/day_10.txt") as f:
    lines = [line.strip() for line in f]

ref = {")": "(", "]": "[", "}": "{", ">": "<"}
score_corrupt = {")": 3, "]": 57, "}": 1197, ">": 25137}
score_incomplete = {"(": 1, "[": 2, "{": 3, "<": 4}


def check(line):
    stack = []
    for operation in line:
        if operation in ref.values():
            stack.insert(0, operation)
        elif ref[operation] == stack[0]:
            stack.pop(0)
        else:
            return "corrupt", score_corrupt[operation]
    score = 0
    for operation in stack:
        score = score * 5 + score_incomplete[operation]
    return "incomplete", score


def part1():
    return sum(score for error, score in (check(line) for line in lines) if error == "corrupt")


def part2():
    scores = [score for error, score in (check(line) for line in lines) if error == "incomplete"]
    return sorted(scores)[len(scores) // 2]


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
