def read_input():
    with open("2020/data/day_23.txt") as f:
        return [int(c) for c in f.read()]


def moves(cups, steps):
    current = cups[0]
    cups = dict(zip(cups, cups[1:] + [cups[0]]))

    for _ in range(steps):
        p1 = cups[current]
        p2 = cups[p1]
        p3 = cups[p2]
        cups[current] = cups[p3]

        destination = current - 1
        while destination < 1 or destination in [p1, p2, p3]:
            destination -= 1
            if destination < 1:
                destination = len(cups)

        cups[p3] = cups[destination]
        cups[destination] = p1
        current = cups[current]
    return cups


def part1():
    cups = moves(read_input(), 100)
    buffer = ""
    current = 1
    while len(buffer) != len(cups) - 1:
        current = cups[current]
        buffer += str(current)
    return buffer


def part2():
    cups = moves(read_input() + list(range(10, 1_000_001)), 10_000_000)
    out1 = cups[1]
    out2 = cups[out1]
    return out1 * out2


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
