def get_rocks():
    with open("2022/data/day_14.txt") as f:
        rocks = set()
        lowest = None
        for line in f:
            path = [[int(coord) for coord in vert.split(",")] for vert in line.split(" -> ")]
            for k in range(1, len(path)):
                (sx, sy), (ex, ey) = path[k - 1 : k + 1]
                sy, ey = (ey, sy) if ey < sy else (sy, ey)
                sx, ex = (ex, sx) if ex < sx else (sx, ex)
                lowest = ey if lowest is None or ey > lowest else lowest
                rocks.update([(x, y) for y in range(sy, ey + 1) for x in range(sx, ex + 1)])
    return rocks, lowest


def sand_fall(obstacles, lowest, ground):
    still_sand = 0
    while True:
        x, y = 500, 0
        while True:
            if (500, 0) in obstacles or y >= lowest + 2:
                return still_sand
            if y == 1 + lowest and ground:
                obstacles.add((x, y))
                still_sand += 1
                break
            elif (x, y + 1) not in obstacles:
                y += 1
            elif (x - 1, y + 1) not in obstacles:
                y += 1
                x -= 1
            elif (x + 1, y + 1) not in obstacles:
                y += 1
                x += 1
            else:
                obstacles.add((x, y))
                still_sand += 1
                break


def part1():
    return sand_fall(*get_rocks(), ground=False)


def part2():
    return sand_fall(*get_rocks(), ground=True)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
