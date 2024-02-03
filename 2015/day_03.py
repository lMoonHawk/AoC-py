with open("2015/data/day_03.txt") as f:
    instructions = f.read().strip()
directions = {"^": (0, -1), "v": (0, 1), ">": (1, 0), "<": (-1, 0)}


def add_vec2(a, b):
    return a[0] + b[0], a[1] + b[1]


def part1():
    position = 0, 0
    visited = {position}
    for instruction in instructions:
        position = add_vec2(position, directions[instruction])
        visited.add(position)
    return len(visited)


def part2():
    positions = [(0, 0), (0, 0)]
    visited = {(0, 0)}
    for turn, instruction in enumerate(instructions):
        index = turn % 2
        positions[index] = add_vec2(positions[index], directions[instruction])
        visited.add(positions[index])
    return len(visited)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
