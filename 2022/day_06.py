with open("2022/data/day_06.txt") as f:
    buffer = f.readline().strip()


def get_marker_index(buffer, distinct):
    for k in range(len(buffer) - distinct):
        if len(set(buffer[k : k + distinct])) == distinct:
            return k + distinct


def part1():
    return get_marker_index(buffer, 4)


def part2():
    return get_marker_index(buffer, 14)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
