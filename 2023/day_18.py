def inst_gen():
    with open("2023/data/day_18.txt") as f:
        yield from (line.strip().split(" ") for line in f.readlines())


def calc_area(inverted=False):
    # We first build a list of ordered vertices to represent the trench.
    # We count every left turn, right turns will be #verticies - left_turns.
    # If we come back to the starting point with a left turn, #left_turns <=> #convex_verticies else #concave_verticies.

    # We calculate the area with a 0 line width (area_inside) using a basic trapezoid formula.
    # We then add a band of 0.5 width on the outside to get the true solution.
    # This band will be of area [sum of (side_distance -1)*0.5] + 3*concave*0.5^2 + convex*0.5^2.

    # Sample with 2 convex verticies (interior of shape is below):
    # We have 3 squares of sides 0.5x0.5 for each convex corner + (length -1)x0.5 for the actual side.
    #   ##   ###  ##
    #   #┏   ---  ┓#

    # Sample with a concave vertex (interior of shape is on the right and below):
    # the concave corner adds a single 0.5x0.5 square.
    #      |
    #     #|
    #  ‾‾‾‾

    directions = {"U": (0, -1), "R": (1, 0), "D": (0, 1), "L": (-1, 0)}
    lookup = {"0": "R", "1": "D", "2": "L", "3": "U"}
    left_turns = [("R", "U"), ("L", "D"), ("U", "L"), ("D", "R")]

    x, y = 0, 0
    trench = [(0, 0)]
    left_turns_cnt = 0

    for k, (traj, count, code) in enumerate(inst_gen()):
        if inverted:
            count, traj = int(code[2 : 2 + 5], 16), lookup[code[-2]]

        if k > 0 and (prev_traj, traj) in left_turns:
            left_turns_cnt += 1
        if k == 0:
            first_traj = traj

        mx, my = directions[traj]
        x, y = x + mx * int(count), y + my * int(count)
        trench.append((x, y))
        prev_traj = traj

    if (traj, first_traj) in left_turns:
        left_turns_cnt += 1
        conv_vert, conc_vert = left_turns_cnt, len(trench) - left_turns_cnt - 1
    else:
        conv_vert, conc_vert = len(trench) - left_turns_cnt - 1, left_turns_cnt

    area_inside = 0
    bands = 0
    for k in range(len(trench) - 1):
        area_inside += (trench[k][1] + trench[k + 1][1]) * (trench[k][0] - trench[k + 1][0])
        bands += abs(trench[k][1] - trench[k + 1][1]) + abs(trench[k][0] - trench[k + 1][0]) - 1

    return int(area_inside // 2 + bands // 2 + (conv_vert * 3) * 0.5**2 + conc_vert * 0.5**2)


def part1():
    return calc_area()


def part2():
    return calc_area(inverted=True)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
