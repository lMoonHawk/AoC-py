def parse_rocks():
    rock_paths = []
    with open("2022/data/day_14.txt") as f:
        for line in f:
            line = line.strip()
            rock_paths.append(
                [
                    tuple([int(el) for el in point.split(",")])
                    for point in line.split(" -> ")
                ]
            )

    # Set of all obstacles
    blocks = set()
    lowest_rock = 0

    for rock_path in rock_paths:
        for i in range(len(rock_path)):

            prev_rock_x, prev_rock_y = rock_path[i - 1]
            rock_x, rock_y = rock_path[i]

            # Find lowest rock for the finish condition
            lowest_rock = rock_y if rock_y > lowest_rock else lowest_rock

            if i == 0:
                continue
            # Creates a tuple for each point on the segment
            path = [
                tuple([x, y])
                for y in range(
                    min(rock_y, prev_rock_y),
                    max(rock_y, prev_rock_y) + 1,
                )
                for x in range(
                    min(rock_x, prev_rock_x),
                    max(rock_x, prev_rock_x) + 1,
                )
            ]

            blocks.update(path)
    return blocks, lowest_rock


def sand_fall(blocks, lowest, ground):
    sand_x, sand_y = (500, 0)
    while True:
        # Sand is reaching source
        if (sand_x, sand_y) in blocks:
            return False
        # Sand is falling of the edge
        if not ground and sand_y > lowest:
            return False

        ground_condition = sand_y < lowest - 1 if ground else True

        if (sand_x, sand_y + 1) not in blocks and ground_condition:
            sand_y += 1
        elif (sand_x - 1, sand_y + 1) not in blocks and ground_condition:
            sand_x -= 1
            sand_y += 1
        elif (sand_x + 1, sand_y + 1) not in blocks and ground_condition:
            sand_x += 1
            sand_y += 1
        else:
            # Cannot fall anymore
            return sand_x, sand_y


def part1():
    blocks, lowest_rock = parse_rocks()

    done = False
    still_sand = 0
    while not done:
        # Spawn sand, receive coordinates when it is at rest
        rest_position = sand_fall(blocks, lowest_rock, False)
        if not rest_position:
            done = True
        else:
            # If end condition is not met, add it to the list of obstacles
            blocks.add(rest_position)
            still_sand += 1

    print(still_sand)


def part2():
    blocks, lowest_rock = parse_rocks()

    done = False
    still_sand = 0
    while not done:
        # Spawn sand
        rest_position = sand_fall(blocks, lowest_rock + 2, True)
        if not rest_position:
            done = True
        else:
            blocks.add(rest_position)
            still_sand += 1

    print(still_sand)


if __name__ == "__main__":
    part1()
    part2()
