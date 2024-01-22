with open("2016/data/day_08.txt") as f:
    instructions = [line.strip() for line in f.readlines()]


def draw(instructions):
    screen = [[0 for _ in range(50)] for _ in range(6)]
    for instruction in instructions:
        if "rect" in instruction:
            wide, tall = instruction.split()[1].split("x")
            for i in range(int(tall)):
                screen[i][: int(wide)] = [1] * int(wide)
        elif "rotate row" in instruction:
            row, step = [int(el) for el in instruction.split("=")[1].split(" by ")]
            screen[row] = screen[row][-step:] + screen[row][:-step]
        elif "rotate column" in instruction:
            col, step = [int(el) for el in instruction.split("=")[1].split(" by ")]
            pixels = [row[col] for row in screen]
            pixels = pixels[-step:] + pixels[:-step]
            for k in range(len(screen)):
                screen[k][col] = pixels[k]
    return screen


def display(screen):
    buffer = "\n"
    for row in screen:
        for pixel in row:
            buffer += "##" if pixel else "  "
        buffer += "\n"
    return buffer


def part1():
    return sum(sum(row) for row in draw(instructions))


def part2():
    return display(draw(instructions))


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
