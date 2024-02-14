traversal = {"e": (1, 0), "se": (0, 1), "sw": (-1, 1), "w": (-1, 0), "nw": (0, -1), "ne": (1, -1)}


def get_input() -> dict:
    tiles = dict()
    with open("2020/data/day_24.txt") as f:
        for line in f:
            buffer = ""
            coordinates = (0, 0)

            for direction in line.strip():
                if direction in ["s", "n"]:
                    buffer = direction
                    continue
                direction, buffer = buffer + direction, ""
                coordinates = tuple([c + t for c, t, in zip(coordinates, traversal[direction])])

            tiles[coordinates] = 1 if coordinates not in tiles else 1 - tiles[coordinates]

    return tiles


def get_black_neigh(tiles, coord: tuple[int]) -> int:
    neighbors = [(coord[0] + t[0], coord[1] + t[1]) for t in traversal.values()]
    return sum(tiles[neighbor] for neighbor in neighbors if neighbor in tiles)


def part1():
    return sum(get_input().values())


def part2():
    tiles = get_input()

    for _ in range(100):
        for coord, color in tiles.copy().items():
            if color == 0:
                continue
            neighbors = [(coord[0] + t[0], coord[1] + t[1]) for t in traversal.values()]
            tiles.update({neighbor: 0 for neighbor in neighbors if neighbor not in tiles})

        snapshot = tiles.copy()

        for coord, color in snapshot.items():
            black_neig_count = get_black_neigh(tiles, coord)
            if color == 1 and (black_neig_count == 0 or black_neig_count > 2):
                snapshot[coord] = 0
            elif color == 0 and black_neig_count == 2:
                snapshot[coord] = 1

        tiles = snapshot

    return sum(tiles.values())


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
