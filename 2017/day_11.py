traversal = {
    "n": (0, 1),
    "ne": (1, 1),
    "se": (1, 0),
    "s": (0, -1),
    "sw": (-1, -1),
    "nw": (-1, 0),
}


def hex_l1(vect):
    a, b = vect
    if a * b > 0:
        return max(abs(a), abs(b))
    else:
        return abs(a - b)


def sum_vect2(vects):
    out = [0, 0]
    for vect in vects:
        out[0] += vect[0]
        out[1] += vect[1]
    return tuple(out)


with open("2017/data/day_11.txt") as f:
    moves = [traversal[direction] for direction in f.readline().strip().split(",")]


def part1():
    # Hexagonal tiles are mapped on a euclidian grid.
    # A side normal vector must be the sum of the adjacent sides normals i.e. ne = n + se / (1,1) = (0,1) + (1,0)
    # The L1 distance has to be modified as it is possible to reach (+1,+1) or (-1,-1) in a single step.
    return hex_l1(sum_vect2(moves))


def part2():
    position = (0, 0)
    best = 0
    for move in moves:
        position = sum_vect2([position, move])
        dist = hex_l1(position)
        best = dist if dist > best else best
    return best


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
