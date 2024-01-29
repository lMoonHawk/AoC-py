# Breaking the challenge... I am not going to create my own MD5 hash function, especially without access to math.
from hashlib import md5


with open("2016/data/day_17.txt") as f:
    code = f.read().strip()


def traverse(longest=False):
    remaining = [(0, 0, "", 0)]
    directions = "UDLR"
    best = 0
    while remaining:
        x, y, path, steps = remaining.pop(-longest)
        doors = md5(str.encode(code + path)).hexdigest()[:4]
        for direction, door, (nx, ny) in zip(directions, doors, [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]):
            if not (0 <= nx < 4 and (0 <= ny < 4)):
                continue
            if door in "bcdef":
                if (nx, ny) == (3, 3):
                    if not longest:
                        return path + direction
                    best = steps + 1 if steps + 1 > best else best
                    continue
                remaining.append((nx, ny, path + direction, steps + 1))
    return best


def part1():
    return traverse()


def part2():
    return traverse(longest=True)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
