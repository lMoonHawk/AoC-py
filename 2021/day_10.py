def part1():
    ref = {')': '(', ']': '[', '}': '{', '>': '<'}
    score_table = {")": 3, "]": 57, "}": 1197, ">": 25137}
    score = 0

    with open("2021/data/day_10.txt") as f:
        for line in f:
            operations = line.strip()

            stack = []
            for operation in operations:
                if operation in ref.values():
                    stack.insert(0, operation)
                elif ref[operation] == stack[0]:
                    stack.pop(0)
                else:
                    score += score_table[operation]
                    break
    print(score)


def part2():
    ref = {')': '(', ']': '[', '}': '{', '>': '<'}
    score_table = {"(": 1, "[": 2, "{": 3, "<": 4}
    scores = []

    with open("2021/data/day_10.txt") as f:
        for line in f:
            operations = line.strip()

            stack = []
            corrupt = False

            for operation in operations:
                if operation in ref.values():
                    stack.insert(0, operation)
                elif ref[operation] == stack[0]:
                    stack.pop(0)
                else:
                    corrupt = True
                    break

            if not corrupt:
                score = 0
                for operation in stack:
                    score = score * 5 + score_table[operation]

                scores.append(score)

    print(sorted(scores)[len(scores) // 2])


if __name__ == '__main__':
    part1()
    part2()
