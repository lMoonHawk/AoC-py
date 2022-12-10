directions = {"R": (0, 1), "D": (-1, 0), "L": (0, -1), "U": (1, 0)}
positions = [(0, 0) for _ in range(10)]
visited_part2 = set()
visited_part2.add(positions[-1])
visited_part1 = set()
visited_part1.add(positions[1])

with open("2022/data/day_09.txt") as f:
    for line in f:
        motion, count = line.split()
        direction = directions[motion]

        for _ in range(int(count)):
            # Update "Head" position
            positions[0] = (
                positions[0][0] + direction[0],
                positions[0][1] + direction[1],
            )

            for i in range(1, 10):
                # Relative position of knot to knot ahead
                rel_y, rel_x = (
                    positions[i][0] - positions[i - 1][0],
                    positions[i][1] - positions[i - 1][1],
                )
                # If knot not adjacent to knot ahead
                if not ((-1 <= rel_y <= 1) and (-1 <= rel_x <= 1)):
                    move_y = 1 if rel_y < 0 else -1 if rel_y > 0 else 0
                    move_x = 1 if rel_x < 0 else -1 if rel_x > 0 else 0

                    positions[i] = (
                        positions[i][0] + move_y,
                        positions[i][1] + move_x,
                    )

            # Part 1: path of 2nd knot, Part 2: path of last knot
            visited_part2.add(positions[-1])
            visited_part1.add(positions[1])


def part1():
    print(len(visited_part1))


def part2():
    print(len(visited_part2))


if __name__ == "__main__":
    part1()
    part2()
