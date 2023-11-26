class Sides:
    top = 0
    right = 1
    left = 2
    bottom = 3
    sides = [top, right, left, bottom]

    def opposite(side):
        return 3 - side


with open("2020/data/day_20.txt") as f:
    tiles_txt = f.read().split("\n\n")
tiles_txt[-1] = tiles_txt[-1].rstrip("\n")

tiles = dict()
for t, tile_txt in enumerate(tiles_txt):
    tile = dict()
    tile_list = tile_txt.split("\n")
    for y, line in enumerate(tile_list):
        if t == 0 and y == 0:
            tile_size = len(line)
        if y == 0:
            tile_id = line.split("Tile ")[1][:-1]
        else:
            for x, square in enumerate(line):
                tile[(x, y - 1)] = square

    tiles[tile_id] = tile


def transform(tile: dict, size, rot: int, flip: int) -> dict:
    for _ in range(rot):
        tile = {(y, size - 1 - x): sq for (x, y), sq in tile.items()}

    if flip in [1, 3]:
        tile = {(x, size - 1 - y): sq for (x, y), sq in tile.items()}
    if flip in [2, 3]:
        tile = {(size - 1 - x, y): sq for (x, y), sq in tile.items()}
    return tile


def sides(tile: dict):
    left = [tile[(0, y)] for y in range(tile_size)]
    right = [tile[(tile_size - 1, y)] for y in range(tile_size)]
    top = [tile[(x, 0)] for x in range(tile_size)]
    bottom = [tile[(x, tile_size - 1)] for x in range(tile_size)]

    return {0: top, 1: right, 2: left, 3: bottom}


def matched(tile_cand, sides_comp) -> tuple[dict, int]:
    """Test the candidate tile against the sides of a tile.
    Returns the transformed tile and the side of the matched tile if found"""
    rot = flip = [0, 1, 2, 3]
    for t in ((r, f) for r in rot for f in flip):
        test = transform(tile_cand, tile_size, *t)

        for s in Sides.sides:
            if sides_comp[s] == sides(test)[Sides.opposite(s)]:
                return test, s
    return None, None


def is_matching(tile_1, tile_2):
    return any(side in tile_2.values() or side[::-1] in tile_2.values() for side in tile_1.values())


def part1():
    answer = 1
    for tile_id_1, tile_1 in tiles.items():
        # Corner tiles only match 2 other tiles
        if sum(is_matching(sides(tile_1), sides(tile_2)) for tile_2 in tiles.values() if tile_1 != tile_2) == 2:
            answer *= int(tile_id_1)

    print(answer)


def part2():
    edge = [0, tile_size - 1]
    image = dict()
    placed = set()

    tile_ini = list(tiles.items())[0]
    stack = [(tile_ini, (0, 0))]
    while stack:
        (tile_id, tile), c = stack.pop()
        placed.add(tile_id)
        image.update(
            {
                (x - 1 + c[0], y - 1 + c[1]): square
                for (x, y), square in tile.items()
                if x not in edge and y not in edge
            }
        )

        for tile_2_id, tile_2 in tiles.items():
            if tile_2_id in placed or tile_2_id == tile_id:
                continue

            tile_2, side = matched(tile_2, sides(tile))
            if not tile_2:
                continue

            if side == Sides.top:
                new_c = c[0], c[1] - (tile_size - 2)
            elif side == Sides.right:
                new_c = (c[0] + (tile_size - 2), c[1])
            elif side == Sides.bottom:
                new_c = (c[0], c[1] + (tile_size - 2))
            elif side == Sides.left:
                new_c = (c[0] - (tile_size - 2), c[1])

            stack.append(((tile_2_id, tile_2), new_c))

    x_offset = min(x for x, _ in image)
    y_offset = min(y for _, y in image)
    image = {(x - x_offset, y - y_offset): square for (x, y), square in image.items()}

    see_monster_txt = """
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
"""
    see_monster = [
        (x, y - 1)
        for y, row in enumerate(see_monster_txt.split("\n"))
        for x, square in enumerate(row)
        if square == "#"
    ]

    see_monster_size = max(x for x, _ in see_monster), max(y for _, y in see_monster)
    image_size = int((len(tiles) ** 0.5) * (tile_size - 2))

    found = False
    rot = flip = [0, 1, 2, 3]
    for t in ((r, f) for r in rot for f in flip):
        test = transform(image, image_size, *t)

        for j in range(image_size):
            for i in range(image_size):
                if j + see_monster_size[0] >= image_size:
                    continue
                if i + see_monster_size[1] >= image_size:
                    continue

                if all(test[x + j, y + i] == "#" for x, y in see_monster):
                    found = True
                    test.update({(x + j, y + i): "0" for x, y in see_monster})
        if found:
            answer = list(test.values()).count("#")
            break

    print(answer)


if __name__ == "__main__":
    part1()
    part2()
