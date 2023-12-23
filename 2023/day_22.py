def get_state():
    bricks = []
    state = set()
    with open("2023/data/day_22.txt") as f:
        for line in f:
            (xs, ys, zs), (xe, ye, ze) = [[int(c) for c in end.split(",")] for end in line.strip().split("~")]
            brick = [(x, y, z) for x in range(xs, xe + 1) for y in range(ys, ye + 1) for z in range(zs, ze + 1)]
            bricks.append(brick)
            state.update(brick)
    return bricks, state


def is_supported_by(a, b):
    return any(c in b for c in [(x, y, z - 1) for x, y, z in a])


def get_supports(bricks, state):
    bricks.sort(key=lambda x: x[0][2])
    for k, _ in enumerate(bricks):
        while True:
            if any(z == 1 for _, _, z in bricks[k]):
                break
            down_brick = [(x, y, z - 1) for x, y, z in bricks[k]]
            state.difference_update(bricks[k])
            if any(c in state for c in down_brick):
                state.update(bricks[k])
                break
            bricks[k] = down_brick
            state.update(down_brick)
    supports = [[] for _ in range(len(bricks))]
    for b1 in range(len(bricks) - 1):
        for b2 in range(b1 + 1, len(bricks)):
            # Since bricks are sorted by z, b2.z >= b1.z
            if is_supported_by(bricks[b2], bricks[b1]):
                supports[b2].append(b1)
    return supports


def count_fall(index, supports):
    indices = set([index])
    prev_count = None
    count = 0
    while prev_count != count:
        prev_count = count
        for k, support in enumerate(supports):
            if k not in indices and support and all(s in indices for s in support):
                count += 1
                indices.add(k)
    return count


def part1():
    supports = get_supports(*get_state())
    single_supports = {s[0] for s in supports if len(s) == 1}
    return len(supports) - len(single_supports)


def part2():
    supports = get_supports(*get_state())
    return sum(count_fall(i, supports) for i in range(len(supports)))


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
