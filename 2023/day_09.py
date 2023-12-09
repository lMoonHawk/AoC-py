with open("2023/data/day_09.txt") as f:
    seqs = [[int(el) for el in line.strip().split()] for line in f.readlines()]


def extrapolate(seq, forward=True):
    if all(k == 0 for k in seq):
        return 0
    return seq[-forward] + (2 * forward - 1) * extrapolate([seq[i + 1] - seq[i] for i in range(len(seq) - 1)], forward)


def part1():
    return sum(extrapolate(seq) for seq in seqs)


def part2():
    return sum(extrapolate(seq, forward=False) for seq in seqs)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
