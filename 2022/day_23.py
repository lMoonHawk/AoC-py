def adjacent(lat=None, lon=None):
    if lat:
        return [[lat, j] for j in range(-1, 2)]
    return [[i, lon] for i in range(-1, 2)]


# Check North, South, West and East cells
checks = [
    adjacent(lat=-1),
    adjacent(lat=1),
    adjacent(lon=-1),
    adjacent(lon=1),
]


def parse_elves():
    elves = set()
    with open("2022/data/day_23.txt") as f:
        for row, line in enumerate(f):
            for col, char in enumerate(line):
                if char == "#":
                    elves.add(tuple([row, col]))
    return elves


def move_elves(elves, priority):
    stage = dict()
    for elf in elves:
        # Checks in order of priority for the round
        round_check = checks[priority:] + checks[:priority]
        not_blocked = 0
        for direction in round_check:
            to_check = [
                (elf[0] + direction_i[0], elf[1] + direction_i[1]) in elves
                for direction_i in direction
            ]
            # Not blocked
            if not any(to_check):
                not_blocked += 1
                # Propose move
                if not_blocked == 1:
                    stage[elf] = (
                        elf[0] + direction[1][0],
                        elf[1] + direction[1][1],
                    )
        # If not elves around, remove move
        if not_blocked == 4:
            del stage[elf]

    # Go through proposed moves
    for elf, move in stage.items():
        # Only allow elves with unique moves to move
        if list(stage.values()).count(move) == 1:
            elves.remove(elf)
            elves.add(move)

    # Return True if no moves were done
    return len(stage) == 0


def part1():
    elves = parse_elves()
    priority = 0

    for _ in range(10):
        move_elves(elves, priority)
        priority = (priority + 1) % 4

    min_y, max_y, min_x, max_x = None, None, None, None
    for elf in elves:
        min_y = elf[0] if min_y is None or min_y > elf[0] else min_y
        max_y = elf[0] if max_y is None or max_y < elf[0] else max_y
        min_x = elf[1] if min_x is None or min_x > elf[1] else min_x
        max_x = elf[1] if max_x is None or max_x < elf[1] else max_x

    answer = (max_y - min_y + 1) * (max_x - min_x + 1) - len(elves)

    print(answer)


def part2():
    elves = parse_elves()
    priority = 0
    stage_count = 0
    done = False

    while not done:
        if move_elves(elves, priority):
            done = True
        priority = (priority + 1) % 4
        stage_count += 1

    print(stage_count)


if __name__ == "__main__":
    part1()
    part2()
