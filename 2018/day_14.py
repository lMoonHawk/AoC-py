with open("2018/data/day_14.txt") as f:
    end = f.readline().strip()


def part1():
    seq = [3, 7]
    e1, e2 = 0, 1
    while len(seq) < int(end) + 10:
        seq.extend([int(el) for el in str(seq[e1] + seq[e2])])
        e1 = (e1 + seq[e1] + 1) % len(seq)
        e2 = (e2 + seq[e2] + 1) % len(seq)
    return "".join(str(el) for el in seq[int(end) : int(end) + 10])


def part2():
    # For some reason, comparing a buffer is faster than checking the end of the seq every turn
    seq = [3, 7]
    e1, e2 = 0, 1
    buffer, k = "", 0
    while True:
        n = [int(el) for el in str(seq[e1] + seq[e2])]
        for i, el in enumerate(n):
            if buffer == str(end):
                return k
            elif not buffer and str(el) == str(end)[0]:
                buffer, k = str(el), len(seq) + i
            elif buffer and str(end)[len(buffer)] == str(el):
                buffer += str(el)
            else:
                buffer, k = "", 0
                if str(el) == str(end)[0]:
                    buffer, k = str(el), len(seq) + i

        seq.extend(n)
        e1 = (e1 + seq[e1] + 1) % len(seq)
        e2 = (e2 + seq[e2] + 1) % len(seq)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
