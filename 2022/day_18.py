class Vec3:
    def __init__(self, x=0, y=0, z=0):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)

    def __eq__(self, other):
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __add__(self, other):
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y and self.z <= other.z

    def __ge__(self, other):
        return self.x >= other.x and self.y >= other.y and self.z >= other.z

    def adjacents(self):
        yield from (self + Vec3(*o) for o in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)])

    @staticmethod
    def comp_min(it):
        return Vec3(min(it, key=lambda v: v.x).x, min(it, key=lambda v: v.y).y, min(it, key=lambda v: v.z).z)

    @staticmethod
    def comp_max(it):
        return Vec3(max(it, key=lambda v: v.x).x, max(it, key=lambda v: v.y).y, max(it, key=lambda v: v.z).z)


with open("2022/data/day_18.txt") as f:
    cubes = {Vec3(*cube.strip().split(",")) for cube in f}


def part1():
    return sum(adj not in cubes for cube in cubes for adj in cube.adjacents())


def part2():
    lo = Vec3.comp_min(cubes) + Vec3(-1, -1, -1)
    hi = Vec3.comp_max(cubes) + Vec3(1, 1, 1)

    visited = set()
    perimeter = 0
    stack = [(hi)]
    while stack:
        cube = stack.pop()
        for adj in cube.adjacents():
            if adj in cubes:
                perimeter += 1
            elif adj not in visited and lo <= adj <= hi:
                visited.add(adj)
                stack.append(adj)
    return perimeter


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
