class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def fold(self, axis, line):
        if axis == "x":
            if self.x <= line:
                return self
            return Vec2(line * 2 - self.x, self.y)
        elif axis == "y":
            if self.y <= line:
                return self
            return Vec2(self.x, line * 2 - self.y)


with open("2021/data/day_13.txt") as f:
    dots, folds = f.read().strip().split("\n\n")
    dots = [Vec2(*[int(n) for n in dot.split(",")]) for dot in dots.split("\n")]
    folds = [(axis[-1], int(val)) for axis, val in (fold.split("=") for fold in folds.split("\n"))]


def part1():
    folded_dots = set()
    axis, line = folds[0]
    for dot in dots:
        folded_dots.add(dot.fold(axis, line))
    return len(folded_dots)


def part2():
    unique_dots = set(dots)
    for axis, line in folds:
        folded_dots = set()
        for dot in unique_dots:
            folded_dots.add(dot.fold(axis, line))
        unique_dots = folded_dots

    buffer = "\n"
    for i in range(max(dot.y for dot in unique_dots) + 1):
        for j in range(max(dot.x for dot in unique_dots) + 1):
            buffer += "##" if Vec2(j, i) in unique_dots else "  "
        buffer += "\n"
    return buffer


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
