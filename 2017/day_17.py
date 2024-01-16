with open("2017/data/day_17.txt") as f:
    steps = int(f.readline())


def part1():
    position, buffer = 0, [0]
    for k in range(2017):
        position = (position + steps) % len(buffer) + 1
        buffer.insert(position, k + 1)
    return buffer[buffer.index(2017) + 1]


def part2():
    position, len_buffer = 0, 1
    for k in range(50_000_000):
        position = (position + steps) % len_buffer + 1
        if position == 1:
            val = k + 1
        len_buffer += 1
    return val


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
