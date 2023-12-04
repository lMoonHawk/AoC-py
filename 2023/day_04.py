def gen_scratchcards():
    with open("2023/data/day_04.txt") as f:
        yield from ([nums.split() for nums in line.strip().split(": ")[1].split(" | ")] for line in f)


def list_combin(a: list, b: list) -> list:
    """Elementwise list addition preserving the longest"""
    diff = len(a) - len(b)
    out = [a_i + b_i for a_i, b_i in zip(a, b)]
    if diff > 0:
        out.extend(a[-diff:])
    if diff < 0:
        out.extend(b[diff:])
    return out


def part1():
    return sum((1 << sum(num in winning for num in have)) >> 1 for winning, have in gen_scratchcards())


def part2():
    answer = 0
    next_copies = []
    for winning, have in gen_scratchcards():
        if next_copies:
            copies = next_copies.pop(0) + 1
        else:
            copies = 1

        answer += copies
        next_copies = list_combin(next_copies, [copies] * sum(num in winning for num in have))

    return answer


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
