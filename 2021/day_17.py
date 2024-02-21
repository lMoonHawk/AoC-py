with open("2021/data/day_17.txt") as f:
    (x_lo, x_hi), (y_lo, y_hi) = [
        [int(el) for el in a.split("..")] for a in (el.split("=")[1] for el in f.read().split(","))
    ]


def sim_throw(x_vel, y_vel):
    x = y = 0
    while True:
        x += x_vel
        y += y_vel
        x_vel = max(0, x_vel - 1)
        y_vel -= 1
        if x > x_hi or y < y_lo or (x_vel == 0 and x < x_lo):
            return False
        if x_lo <= x <= x_hi and y_lo <= y <= y_hi:
            return True


def part1():
    # After y_pos = 0, next step will be:
    #     y_pos = - v_0 - 1
    # <=> v_0 = - y_pos - 1
    # To max v_0 we make sure to reach the target's lower boundary in one go
    max_vel = -(y_lo + 1)
    # To get max heigh reached, sum v_0 + v_1 + ... 0, i.e. 1 to max_vel
    return max_vel * (max_vel + 1) // 2


def part2():
    return sum(1 for x_vel in range(x_hi + 1) for y_vel in range(y_lo, 1 - y_lo) if sim_throw(x_vel, y_vel))


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
