def part1():

    ref = {"(": ")", "[": "]", "{": "}", "<": ">"}
    openings = list(ref)
    closings = list(ref.values())
    score_table = {")": 3, "]": 57, "}": 1197, ">": 25137}
    score = 0

    def next_close(level, i_min, operations, levels):
        """ Returns the next closing statement at the same nest level"""
        value = [matched for i, (matched, same_lvl)
                 in enumerate(zip(operations, levels))
                 if (matched in closings and same_lvl == level
                     and i > i_min)]
        if value:
            return value[0]

    with open("2021/data/day_10.txt") as f:
        for line in f:
            line = line.strip()
            operations = [operation for operation in line]

            levels = [0]
            for i, operation in enumerate(operations):

                if i == 0:
                    continue

                # Create list of nest level after each statement
                if operation in openings and operations[i - 1] in openings:
                    levels.append(levels[i - 1] + 1)
                elif operation in closings and operations[i - 1] in closings:
                    levels.append(levels[i - 1] - 1)
                else:
                    levels.append(levels[i - 1])

            # Count the number of statement per level
            table = {k: levels.count(k) for k in range(max(levels) + 1)}

            for i, (level, operation) in enumerate(zip(levels, operations)):
                if table[level] > 1 and operation in openings:

                    closing = next_close(level, i, operations, levels)
                    # If the next closing statement at the same level does
                    # not correspond, this is a corrupt line
                    if closing and closing != ref[operation]:
                        # print(f"{line} - ",
                        #       f"Expected {ref[operations[i]]}",
                        #       f"but found {closing}")
                        score += score_table[closing]
                        break
        print(score)


def part2():
    pass


if __name__ == '__main__':
    part1()
    part2()
