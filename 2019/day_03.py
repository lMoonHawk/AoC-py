directions = {"R": (1, 0), "D": (0, 1), "L": (-1, 0), "U": (0, -1)}
with open("2019/data/day_03.txt") as f:
    wire_paths = [line.strip().split(",") for line in f.readlines()]


def part1():
    wires = []
    for wire_path in wire_paths:
        wire = set()
        x, y = 0, 0
        for instruction in wire_path:
            direction, length = instruction[:1], int(instruction[1:])
            move_x, move_y = directions[direction]
            for _ in range(length):
                x, y = x + move_x, y + move_y
                wire.add((x, y))
        wires.append(wire)

    return min(abs(x) + abs(y) for x, y in set.intersection(*wires))


def part2():
    wires = []
    for wire_path in wire_paths:
        wire = dict()
        x, y = 0, 0
        step = 0
        for instruction in wire_path:
            direction, length = instruction[:1], int(instruction[1:])
            move_x, move_y = directions[direction]
            for _ in range(length):
                step += 1
                x, y = x + move_x, y + move_y
                if (x, y) not in wire:
                    wire[(x, y)] = step
        wires.append(wire)

    return min(wires[0][i] + wires[1][i] for i in wires[0].keys() & wires[1].keys())


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
