def get_seq():
    with open("2017/data/day_05.txt") as f:
        return [int(line) for line in f.readlines()]


def part1():
    seq = get_seq()
    index = step = 0
    while 0 <= index < len(seq):
        jump, seq[index] = seq[index], seq[index] + 1
        index, step = index + jump, step + 1
    return step


def part2():
    seq = get_seq()
    index = step = 0
    while 0 <= index < len(seq):
        jump, seq[index] = seq[index], seq[index] + (1 if seq[index] < 3 else -1)
        index, step = index + jump, step + 1
    return step


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
