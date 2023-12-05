def polymer():
    with open("2018/data/day_05.txt") as f:
        while True:
            c = f.read(1)
            if not c or c == "\n":
                break
            yield c


def part1():
    stack = []
    for molecule in polymer():
        if len(stack) >= 1 and abs(ord(stack[-1]) - ord(molecule)) == 32:
            del stack[-1]
            continue
        stack.append(molecule)
    return len(stack)


def part2():
    delete_tests = [chr(k) for k in range(65, 91)]  # [A,...,Z]
    min_len = None

    for delete in delete_tests:
        stack = []
        for molecule in polymer():
            if molecule in [delete, delete.lower()]:
                continue
            if len(stack) >= 1 and abs(ord(stack[-1]) - ord(molecule)) == 32:
                del stack[-1]
                continue
            stack.append(molecule)
        min_len = len(stack) if not min_len or len(stack) < min_len else min_len
    return min_len


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
