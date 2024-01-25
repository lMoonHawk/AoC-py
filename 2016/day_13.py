with open("2016/data/day_13.txt") as f:
    num = int(f.readline())


def is_open(x, y):
    return not (x * x + 3 * x + 2 * x * y + y + y * y + num).bit_count() % 2


def traverse(reach=None, max_steps=None):
    queue = [(1, 1, 0)]
    tried = set([(1, 1)])
    visited = 1
    while queue:
        x, y, steps = queue.pop(0)
        if max_steps and steps == max_steps:
            return visited
        elif reach and (x, y) == reach:
            return steps
        for nx, ny in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
            if nx < 0 or ny < 0 or (nx, ny) in tried:
                continue
            tried.add((nx, ny))
            if is_open(nx, ny):
                visited += 1
                queue.append((nx, ny, steps + 1))


def part1():
    return traverse(reach=(31, 39))


def part2():
    return traverse(max_steps=50)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
