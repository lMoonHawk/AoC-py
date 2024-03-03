with open("2022/data/day_10.txt") as f:
    instructions = [line.split() for line in f]


def draw(x, beam_x, cycle):
    buffer = "\n" if beam_x == 0 and cycle != 1 else ""
    buffer += "##" if x - 1 <= beam_x <= x + 1 else ".."
    return buffer


def part1():
    signal_strength, cycle = 0, 0
    x = 1
    for instruction in instructions:
        cycle += 1
        if (cycle - 20) % 40 == 0:
            signal_strength += cycle * x
        if instruction[0] == "addx":
            cycle += 1
            if (cycle - 20) % 40 == 0:
                signal_strength += cycle * x
            x += int(instruction[1])
    return signal_strength


def part2():
    cycle = 0
    x = 1
    buffer = "\n"
    for instruction in instructions:
        cycle += 1
        buffer += draw(x, (cycle - 1) % 40, cycle)
        if instruction[0] == "addx":
            cycle += 1
            buffer += draw(x, (cycle - 1) % 40, cycle)
            x += int(instruction[1])
    return buffer


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
