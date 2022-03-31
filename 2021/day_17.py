def part1():
    # Parsing
    with open("2021/data/day_17.txt") as f:
        line = f.readline()

    parse_between = line.index("y=")
    # Parse target's lower y boundary
    target = int(line[parse_between + 2 :].split("..")[0])
    # Max velocity that can still reach the target
    # After y_pos = 0, next step will be:
    #     y_pos = - v_0 - 1
    # <=> v_0 = - y_pos - 1
    # To max v_0 we make sure to reach the target's lower boundary in one go
    max_vel = -target - 1
    # To get max heigh reached, sum v_0 + v_1 + ... 0, i.e. 1 to max_vel
    max_height = max_vel * (max_vel + 1) // 2

    print(max_height)


def part2():
    def sim_throw(x_vel: int, y_vel: int) -> int:
        x = y = 0
        while True:
            x += x_vel
            y += y_vel
            x_vel -= 1 if x_vel > 0 else 0
            y_vel -= 1

            if (
                x > target_x[1]
                or y < target_y[0]
                or (x_vel == 0 and x < target_x[0])
            ):
                return 0

            if (
                target_x[0] <= x <= target_x[1]
                and target_y[0] <= y <= target_y[1]
            ):
                return 1

    # Parsing
    with open("2021/data/day_17.txt") as f:
        line = f.readline()

    parse_start = line.index("x=")
    parse_between = line.index("y=")

    target_x = line[parse_start + 2 : parse_between - 2].split("..")
    target_x = [int(el) for el in target_x]
    target_y = line[parse_between + 2 :].split("..")
    target_y = [int(el) for el in target_y]

    search_range_x = target_x[1] + 1
    search_range_y = [target_y[0], -target_y[0] + 1]

    counter = 0
    for x_vel in range(search_range_x):
        for y_vel in range(search_range_y[0], search_range_y[1]):
            counter += sim_throw(x_vel, y_vel)

    print(counter)


def steps():
    vx0 = 6
    vy0 = 3

    def y(n):
        return int(vy0 + n * (vy0 - (n + 1) / 2))

    def x(n):
        step_vel = max(0, vx0 - n)
        return int((vx0 + step_vel) * (vx0 - step_vel + 1) / 2)

    for i in range(0, 10):
        print(f"i={i}; x={x(i)}, y={y(i)}")


if __name__ == "__main__":
    part1()
    part2()
    # steps()
