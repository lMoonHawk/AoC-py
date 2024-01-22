def get_file():
    with open("2016/data/day_09.txt") as f:
        return f.readline().strip()


def decomp_len(file, recurse=False):
    decompressed = 0
    while True:
        marker_start = None
        for k, c in enumerate(file):
            if c == "(":
                marker_start = k
                break
        if marker_start is None:
            decompressed += len(file)
            return decompressed

        decompressed += len(file[:marker_start])
        file = file[marker_start:]
        marker_end = file.index(")")
        size, rep = [int(el) for el in file[1:marker_end].split("x")]
        file = file[marker_end + 1 :]
        if recurse:
            decompressed += decomp_len(file[:size], recurse=True) * rep
        else:
            decompressed += len(file[:size]) * rep
        file = file[size:]


def part1():
    return decomp_len(get_file())


def part2():
    return decomp_len(get_file(), recurse=True)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
