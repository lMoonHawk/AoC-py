class Cuboid:
    def __init__(self, switch, coords):
        self.switch = switch
        self.coords = coords

    def volume(self):
        w, h, l = [hi - lo + 1 for lo, hi in self.coords]
        return w * h * l

    def intersection(self, other):
        return Cuboid(
            other.switch,
            [
                [lo, hi] if lo <= hi else [1, 0]
                for lo, hi in ([max(s[0], o[0]), min(s[1], o[1])] for s, o in zip(self.coords, other.coords))
            ],
        )


with open("2021/data/day_22.txt") as f:
    cuboids = [
        Cuboid(switch == "on", [[int(c) for c in ax.split("=")[1].split("..")] for ax in cuboid.split(",")])
        for switch, cuboid in (line.split() for line in f)
    ]


def unique_volume(cuboid, i, cuboids):
    intersections = [
        intersection for other in cuboids[i + 1 :] if (intersection := cuboid.intersection(other)).volume() > 0
    ]
    return cuboid.volume() - sum(unique_volume(conflict, j, intersections) for j, conflict in enumerate(intersections))


def part1():
    bounds = Cuboid(None, [[-50, 50] for _ in range(3)])
    bounded_cuboids = [bounds.intersection(cuboid) for cuboid in cuboids]
    return sum(unique_volume(cuboid, k, bounded_cuboids) for k, cuboid in enumerate(bounded_cuboids) if cuboid.switch)


def part2():
    return sum(unique_volume(cuboid, k, cuboids) for k, cuboid in enumerate(cuboids) if cuboid.switch)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
