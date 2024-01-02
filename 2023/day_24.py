class Hailstone:
    def __init__(self, x, y, z, vx, vy, vz):
        self.pos = x, y, z
        self.vel = vx, vy, vz
        self.xy_slope = self.vel[1] / self.vel[0]
        self.xy_intercept = self.pos[1] - self.xy_slope * self.pos[0]

    def intersect(self, other):
        if self.xy_slope == other.xy_slope:
            return False
        x_int = (other.xy_intercept - self.xy_intercept) / (self.xy_slope - other.xy_slope)
        y_int = self.xy_slope * x_int + self.xy_intercept
        in_bounds = (BOUNDS[0] <= x_int <= BOUNDS[1]) and (BOUNDS[0] <= y_int <= BOUNDS[1])
        self_in_future = (self.vel[0] > 0) == (x_int > self.pos[0])
        other_in_future = (other.vel[0] > 0) == (x_int > other.pos[0])
        return in_bounds and self_in_future and other_in_future


with open("2023/data/day_24.txt") as f:
    hail = [Hailstone(*[int(el) for l in line.strip().split(" @ ") for el in l.split(", ")]) for line in f.readlines()]

BOUNDS = (200_000_000_000_000, 400_000_000_000_000)


def find_plane(p1, v1, p2, v2):
    p12 = sub(p1, p2)
    v12 = sub(v1, v2)
    vv = cross(v1, v2)
    return (cross(p12, v12), dot(p12, vv))


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def lin(r, a, s, b, t, c):
    x = r * a[0] + s * b[0] + t * c[0]
    y = r * a[1] + s * b[1] + t * c[1]
    z = r * a[2] + s * b[2] + t * c[2]
    return (x, y, z)


def part1():
    return sum(hail[s1].intersect(hail[s2]) for s1 in range(len(hail) - 1) for s2 in range(s1 + 1, len(hail)))


def part2():
    p1, v1 = hail[0].pos, hail[0].vel
    p2, v2 = hail[1].pos, hail[1].vel
    p3, v3 = hail[2].pos, hail[2].vel

    a, A = find_plane(p1, v1, p2, v2)
    b, B = find_plane(p1, v1, p3, v3)
    c, C = find_plane(p2, v2, p3, v3)

    w = lin(A, cross(b, c), B, cross(c, a), C, cross(a, b))
    t = dot(a, cross(b, c))
    w = w[0] // t, w[1] // t, w[2] // t

    w1 = sub(v1, w)
    w2 = sub(v2, w)
    ww = cross(w1, w2)

    E = dot(ww, cross(p2, w2))
    F = dot(ww, cross(p1, w1))
    G = dot(p1, ww)
    S = dot(ww, ww)

    rock = lin(E, w1, -F, w2, G, ww)
    return sum(rock) // S


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
