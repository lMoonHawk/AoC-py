with open("2022/data/day_17.txt") as f:
    jets_file = f.read()


def gen_jets():
    while True:
        for jet in jets_file:
            yield jet


def gen_rocks():
    # Coordinates of each rocks, starting at [0,0] bottom-left
    rocks = [
        [(0, 0), (1, 0), (2, 0), (3, 0)],
        [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
        [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
        [(0, 0), (0, 1), (0, 2), (0, 3)],
        [(0, 0), (1, 0), (0, 1), (1, 1)],
    ]
    while True:
        for rock in rocks:
            # Wait for "send" instruction with spawn_y coordinates
            lowest = yield
            out = []
            for point in rock:
                out.append(tuple([point[0] + 2, point[1] + lowest]))
            yield out


def check_rock(rock, mouv, obstacles):
    for point in rock:
        check = tuple([point[0] + mouv[0], point[1] + mouv[1]])
        if check in obstacles or check[1] < 0 or not (0 <= check[0] <= 6):
            return False
    return True


def move_rock(rock, mouv, obstacles):
    if not check_rock(rock, mouv, obstacles):
        return False
    for index, point in enumerate(rock):
        rock[index] = tuple([point[0] + mouv[0], point[1] + mouv[1]])
    return True


def rock_fall(rock, jets, obstacles):
    while True:
        jet = next(jets)
        offset = (-1, 0) if jet == "<" else (1, 0)
        move_rock(rock, offset, obstacles)
        offset = (0, -1)
        if not move_rock(rock, offset, obstacles):
            return rock


def part1():
    rocks = gen_rocks()
    jets = gen_jets()
    obstacles = set()

    spawn_y = 3
    count = 0
    done = False

    while not done:
        next(rocks)
        # Get coordinates of the rock
        rock = rocks.send(spawn_y)

        rest_position = rock_fall(rock, jets, obstacles)

        count += 1
        for point in rest_position:
            obstacles.add(point)

        rock_max = max(point[1] for point in rest_position) + 4
        spawn_y = rock_max if rock_max > spawn_y else spawn_y

        if count == 2022:
            done = True

    print(spawn_y - 3)


def part2():
    pass


if __name__ == "__main__":
    part1()
    part2()
