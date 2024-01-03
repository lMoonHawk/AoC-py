clay = set()
min_y, max_y = None, None
with open("2018/data/day_17.txt") as f:
    for line in f:
        fixed, ranged = line.strip().replace("x=", "").replace("y=", "").split(", ")
        ranged = [int(el) for el in ranged.split("..")]
        for k in range(ranged[0], ranged[1] + 1):
            if line[0] == "x":
                x, y = int(fixed), k
            else:
                x, y = k, int(fixed)
            min_y = y if min_y is None or y < min_y else min_y
            max_y = y if max_y is None or y > max_y else max_y
            clay.add((x, y))

still = set()
water = set()
queue = [(500, 0)]
while queue:
    x, y = queue.pop(0)
    if (x, y) in still:
        continue

    y_below = y + 1
    while y_below < max_y and ((x, y_below) not in clay) and ((x, y_below) not in still):
        if y_below >= min_y:
            water.add((x, y_below))
        y_below += 1

    if y_below > max_y:
        continue

    y = y_below - 1
    x_left = x
    blocked_left = None
    while True:
        water.add((x_left, y))
        if ((x_left, y + 1) not in clay) and ((x_left, y + 1) not in still):
            queue.append((x_left, y + 1))
            water.add((x_left, y + 1))
            break
        elif (x_left - 1, y) in clay:
            blocked_left = x_left
            break
        x_left -= 1
    x_right = x
    while True:
        water.add((x_right, y))
        if ((x_right, y + 1) not in clay) and ((x_right, y + 1) not in still):
            queue.append((x_right, y + 1))
            water.add((x_right, y + 1))
            break
        elif (x_right + 1, y) in clay:
            if blocked_left:
                still.update({(k, y) for k in range(x_left, x_right + 1)})
                queue.append((x, y - 1))
            break
        x_right += 1


def part1():
    return len(water)


def part2():
    return len(still)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
