def get_pos():
    pos = []
    with open("2019/data/day_12.txt") as f:
        for line in f:
            pos.append(
                [
                    int(c)
                    for c in line.strip()
                    .replace("<", "")
                    .replace(">", "")
                    .replace("x=", "")
                    .replace("y=", "")
                    .replace("z=", "")
                    .split(", ")
                ]
            )
    return pos


def part1():
    pos = get_pos()
    vel = [[0, 0, 0] for _ in range(4)]
    compared = set()

    for _ in range(1_000):
        for m1, pos1 in enumerate(pos):
            for m2, pos2 in enumerate(pos):
                if pos1 == pos2 or (m1, m2) in compared:
                    continue

                for axis in range(3):
                    if pos1[axis] > pos2[axis]:
                        vel[m1][axis] -= 1
                        vel[m2][axis] += 1

                    if pos1[axis] < pos2[axis]:
                        vel[m1][axis] += 1
                        vel[m2][axis] -= 1
                compared.add((m2, m1))
        compared = set()

        for m, (m_pos, m_vel) in enumerate(zip(pos, vel)):
            pos[m] = [p + v for p, v in zip(m_pos, m_vel)]

    pot = [sum(abs(c) for c in pos_m) for pos_m in pos]
    kin = [sum(abs(c) for c in vel_m) for vel_m in vel]
    return sum(p * k for p, k in zip(pot, kin))


def simulate_axis(points, vel):
    compared = set()
    for m1, pos1 in enumerate(points):
        for m2, pos2 in enumerate(points):
            if m1 == m2 or (m1, m2) in compared:
                continue

            if pos1 > pos2:
                vel[m1] -= 1
                vel[m2] += 1

            if pos1 < pos2:
                vel[m1] += 1
                vel[m2] -= 1
            compared.add((m2, m1))

    return [p + v for p, v in zip(points, vel)]


def get_cycle(pos, vel):
    pos_ini, vel_ini = pos.copy(), vel.copy()
    k = 0
    while True:
        pos = simulate_axis(pos, vel)
        k += 1
        if pos == pos_ini and vel == vel_ini:
            return k


def gcd(*args):
    gcd = 0
    for i in range(len(args)):
        a, b = gcd, args[i]
        while b:
            a, b = b, a % b
        gcd = abs(a)
    return gcd


def lcm(*args):
    num = 1
    for arg in args:
        num *= arg
    return num // gcd(*[a * b for a in args for b in args if a != b])


def part2():
    pos = get_pos()

    tpos = [[point[c] for point in pos] for c in range(3)]
    cycle = lcm(*[get_cycle(tpos[m], [0, 0, 0, 0]) for m in range(3)])

    return cycle


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
