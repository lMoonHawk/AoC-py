with open("2018/data/day_13.txt") as f:
    tracks = [list(line) for line in f.readlines()]

FACE = {"^": 0, ">": 1, "v": 2, "<": 3}
DIR = {0: [-1, 0], 1: [0, 1], 2: [1, 0], 3: [0, -1]}
CARTS_INI = [(y, x, FACE[sq], 0) for y, r in enumerate(tracks) for x, sq in enumerate(r) if sq in ["v", "^", ">", "<"]]


def get_new_facing(tile, f, t):
    if (tile == "/" and f in [0, 2]) or (tile == "\\" and f in [1, 3]):
        f = (f + 1) % 4
    elif (tile == "/" and f in [1, 3]) or (tile == "\\" and f in [0, 2]):
        f = (f - 1) % 4
    elif tile == "+":
        if t == 0:
            f = (f - 1) % 4
        elif t == 2:
            f = (f + 1) % 4
        t = (t + 1) % 3
    return f, t


def part1():
    carts = CARTS_INI[:]
    while True:
        carts.sort()
        for i, (y, x, f, t) in enumerate(carts):
            my, mx = DIR[f]
            ny, nx = y + my, x + mx
            tile = tracks[ny][nx]

            if any((ny, nx) == (cy, cx) for cy, cx, _, _ in carts):
                return str(nx) + "," + str(ny)
            f, t = get_new_facing(tile, f, t)
            carts[i] = ny, nx, f, t


def part2():
    carts = CARTS_INI[:]
    while True:
        to_remove = set()
        carts.sort()
        for i, (y, x, f, t) in enumerate(carts):
            if i in to_remove:
                continue
            my, mx = DIR[f]
            ny, nx = y + my, x + mx
            tile = tracks[ny][nx]
            if k := [k for k, (cy, cx, _, _) in enumerate(carts) if (ny, nx) == (cy, cx) and k not in to_remove]:
                to_remove.update({k[0], i})
                continue
            f, t = get_new_facing(tile, f, t)
            carts[i] = ny, nx, f, t

        carts = [cart for i, cart in enumerate(carts) if i not in to_remove]
        if len(carts) == 1:
            return str(carts[0][1]) + "," + str(carts[0][0])


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
