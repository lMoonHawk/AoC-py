class Vec2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def scalar_mul(self, a):
        return Vec2(a * self.x, a * self.y)

    def add(self, other):
        return Vec2(self.x + other.x, self.y + other.y)

    def rotate(self, degrees):
        rotated = self
        for _ in range((degrees // 90) % 4):
            rotated = Vec2(rotated.y, -rotated.x)
        return rotated


directions = {"N": Vec2(0, 1), "E": Vec2(1, 0), "S": Vec2(0, -1), "W": Vec2(-1, 0)}


def instructions():
    with open("2020/data/day_12.txt") as f:
        yield from ((el[0], int(el[1:])) for el in (line.strip() for line in f))


def part1():
    ship, facing = Vec2(), 1
    for action, value in instructions():
        if action in "NESW":
            ship = ship.add(directions[action].scalar_mul(value))
        elif action == "F":
            ship = ship.add(directions["NESW"[facing]].scalar_mul(value))
        elif action in "LR":
            value = -value if action == "L" else value
            facing = (facing + value // 90) % 4
    return abs(ship.x) + abs(ship.y)


def part2():
    ship = Vec2()
    waypoint = Vec2(10, 1)
    for action, value in instructions():
        if action == "F":
            ship = ship.add(waypoint.scalar_mul(value))
        elif action in directions:
            waypoint = waypoint.add(directions[action].scalar_mul(value))
        elif action in "RL":
            value = -value if action == "L" else value
            waypoint = waypoint.rotate(value)
    return abs(ship.x) + abs(ship.y)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
