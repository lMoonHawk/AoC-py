class Vect3(tuple):
    def __init__(self, it):
        x, y, z = it
        self.x = x
        self.y = y
        self.z = z

    def dist(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    def __add__(self, other):
        return Vect3((self.x + other.x, self.y + other.y, self.z + other.z))

    def __str__(self):
        return f"(x={self.x}, y={self.y}, z={self.z})"

    def __repr__(self):
        return f"(x={self.x}, y={self.y}, z={self.z})"


class Particule:
    def __init__(self, p, v, a):
        self.p = Vect3(p)
        self.v = Vect3(v)
        self.a = Vect3(a)

    def update(self):
        self.v += self.a
        self.p += self.v
        return self.p

    def escaping(self):
        return (
            sign(self.p.x, self.v.x, self.a.x)
            and sign(self.p.y, self.v.y, self.a.y)
            and sign(self.p.z, self.v.z, self.a.z)
        )

    def __str__(self):
        return f"(p={self.p}, v={self.v}, a={self.a})"

    def __repr__(self):
        return f"(p={self.p}, v={self.v}, a={self.a})"


def particules_init():
    particules = []
    with open("2017/data/day_20.txt") as f:
        for particule in f.readlines():
            vects = [[int(v) for v in vect[3:-1].split(",")] for vect in particule.strip().split(", ")]
            particules.append(Particule(*vects))
    return particules


def sign(p, v, a):
    same_sign = (p > 0) == (v > 0) == (a > 0)
    same_sign |= (p > 0) == (v > 0) == (a == 0)
    same_sign |= (p > 0) == (v == 0) == (a == 0)
    return same_sign


def part1():
    close_dist = None
    for p, particule in enumerate(particules_init()):
        current = particule.a.dist()
        if close_dist is None or current < close_dist:
            close_dist = current
            close_part = p
    return close_part


def part2():
    particules = particules_init()
    stop = False
    while not stop:
        stop = True
        positions = set()
        collisions = set()
        for particule in particules:
            position = particule.update()
            if not particule.escaping():
                stop = False
            if position in positions:
                collisions.add(position)
            positions.add(position)
        particules = [particule for particule in particules if particule.p not in collisions]
    return len(particules)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
