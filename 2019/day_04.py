with open("2019/data/day_04.txt") as f:
    BOUND_MIN, BOUND_MAX = [int(val) for val in f.readline().split("-")]


def two_consec(s: str) -> bool:
    """Returns True if there a string of exactly 2 consecutive chars.
    Faster than ORing each case:
    d[0] == d[1] != d[2]
    or any(d[i] != d[i + 1] == d[i + 2] != d[i + 3] for i in range(len(d) - 3))
    or d[-3] != d[-2] == d[-1]"""
    prev_digit, count = None, 0
    for digit in s:
        if digit == prev_digit:
            count += 1
        elif prev_digit is not None:
            if count == 1:
                return True
            count = 0
        prev_digit = digit
    return True if count == 1 else False


def part1():
    answer = 0
    k = BOUND_MIN
    while k <= BOUND_MAX:
        test = str(k)

        if not any(test[i] == test[i + 1] for i in range(len(test) - 1)):
            k += 1
            continue
        is_inc = [test[i] <= test[i + 1] for i in range(len(test) - 1)]
        if False in is_inc:
            index_sup = is_inc.index(False)
            # If a digit is more than the next one, we can directly increase k so that these digit are equal
            k += (int(test[index_sup]) - int(test[index_sup + 1])) * 10 ** (len(test) - 2 - index_sup)
        else:
            answer += 1
            k += 1

    return answer


def part2():
    answer = 0
    k = BOUND_MIN
    while k <= BOUND_MAX:
        test = str(k)

        if not two_consec(test):
            k += 1
            continue

        if False in (is_inc := [test[i] <= test[i + 1] for i in range(len(test) - 1)]):
            index_sup = is_inc.index(False)
            # If a digit is more than the next one, we can directly increase k so that these digit are equal
            k += (int(test[index_sup]) - int(test[index_sup + 1])) * 10 ** (len(test) - 2 - index_sup)
        else:
            answer += 1
            k += 1

    return answer


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
