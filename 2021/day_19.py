class Vec3:
    def __init__(self, x=0, y=0, z=0):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)

    def __eq__(self, other):
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def transform(self, transform_mat):
        ax, ay, az, a = transform_mat[0]
        bx, by, bz, b = transform_mat[1]
        cx, cy, cz, c = transform_mat[2]
        x = self.x * ax + self.y * ay + self.z * az + a
        y = self.x * bx + self.y * by + self.z * bz + b
        z = self.x * cx + self.y * cy + self.z * cz + c
        return Vec3(x, y, z)


with open("2021/data/day_19.txt") as f:
    scanners = [[Vec3(*b.split(",")) for b in scanner.split("\n")[1:]] for scanner in f.read().strip().split("\n\n")]


def get_dist(v1, v2):
    return abs(v1.x - v2.x) + abs(v1.y - v2.y) + abs(v1.z - v2.z)


def incr_counter(d, k):
    if k not in d:
        d[k] = 0
    d[k] += 1


def get_cross_dist(scanner):
    """Calculates the distance of all beacons againts all other. Returns a counter dict"""
    distances = [dict() for _ in range(len(scanner))]
    for b1, beacon1 in enumerate(scanner[:-1]):
        for b2, beacon2 in enumerate(scanner[b1 + 1 :], b1 + 1):
            dist = get_dist(beacon1, beacon2)
            incr_counter(distances[b1], dist)
            incr_counter(distances[b2], dist)
    return distances


def is_overlapping(c1, c2):
    """Check if two sets of beacons overlap by providing the cross distances counters"""
    return sum(min(c1[k], c2[k]) for k in c1 if k in c2) >= 11


def get_transform(lv):
    # Calculate T in V2*T = V1 without using matrix inverse functions and multiplications. This would be trivial in numpy.
    # The transformation matrix and vectors have 4 components to account for the intercept of the linear equation (translation).
    # This translation corresponds with the position of the scanner 2 seen from scanner 1.
    # Example:
    # To get the component x of the transformed vector V1, we test the 6 different possible axis of the starting vector V2
    # x1=x2+k, x=-x+k, x=y+k, x=-y+k, x=z+k, x=-z+k
    # We search for both the rotation (which axis correspond to which) and translation (value of k) at the same time.
    # If all vectors agree on the value of k after testing a configuration, we found the correct transformation for this specific coordinate x
    transform = []
    for axis in ["x", "y", "z"]:
        for t_axis in ["x", "y", "z"]:
            for op, op_fun in {"-": lambda x, y: x - y, "+": lambda x, y: x + y}.items():
                test = {op_fun(getattr(v1, axis), getattr(v2, t_axis)) for v1, v2 in lv}
                if len(test) != 1:
                    continue
                (trans,) = test
                sign = 1 if op == "-" else -1
                transform.append((sign * (t_axis == "x"), sign * (t_axis == "y"), sign * (t_axis == "z"), trans))
    return transform


def transform_scanners(scanners):
    scanners_c = [Vec3()]
    cross_dist = [get_cross_dist(scanner) for scanner in scanners]
    queue = [0]
    # Scanners index which have already been transformed to scanner 0 coordinate system
    transformed = {0}

    while queue:
        s1 = queue.pop(0)
        for s2, _ in enumerate(scanners):
            if s2 in transformed:
                continue
            overlaps = []
            for b1, b1_dist in enumerate(cross_dist[s1]):
                for b2, b2_dist in enumerate(cross_dist[s2]):
                    if is_overlapping(b1_dist, b2_dist):
                        overlaps.append((scanners[s1][b1], scanners[s2][b2]))
            if not overlaps:
                continue
            # Based on the overlaps, build the transformation matrix beacon_scanner_s2*T = beacon_scanner_s1
            transform_mat = get_transform(overlaps)
            # Get the position of the scanner_s2 based on the transformation intercepts
            scanners_c.append(Vec3(*[p[3] for p in transform_mat]))
            # Replaces scanner_s2 beacons with the scanner_s1 coordinates (which is in the scanner 0 coordinate system)
            scanners[s2] = [beacon.transform(transform_mat) for beacon in scanners[s2]]
            transformed.add(s2)
            queue.append(s2)
    return scanners_c, scanners


scanners_c, scanners = transform_scanners(scanners)


def part1():
    return len(set().union(*scanners))


def part2():
    return max(get_dist(s1, s2) for s1 in scanners_c for s2 in scanners_c)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
