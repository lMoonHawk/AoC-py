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
    pass


if __name__ == '__main__':
    part1()
    part2()
