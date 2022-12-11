def part1():
    signal_strength = 0
    cycle = 0
    x = 1
    with open("2022/data/day_10.txt") as f:
        for line in f:
            cycle += 1
            if (cycle - 20) % 40 == 0:
                signal_strength += cycle * x

            op = line.split()
            if op[0] == "noop":
                continue

            cycle += 1
            if (cycle - 20) % 40 == 0:
                signal_strength += cycle * x

            x += int(op[1])

    print(signal_strength)


def part2():
    def draw():
        if x - 1 <= beam_x <= x + 1:
            pixel = "#"
        else:
            pixel = "."
        # Newline
        if (cycle - 1) % 40 == 0 and cycle != 1:
            print()
        print(pixel, end="")

    cycle = 0
    x = 1
    with open("2022/data/day_10.txt") as f:
        for line in f:
            # Read cycle: draw
            cycle += 1
            beam_x = (cycle - 1) % 40
            draw()

            op = line.split()
            if op[0] == "addx":
                # Start add cycle: draw
                cycle += 1
                beam_x = (cycle - 1) % 40
                draw()
                # End cycle: add
                x += int(op[1])


if __name__ == "__main__":
    part1()
    part2()
