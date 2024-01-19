with open("2017/data/day_21.txt") as f:
    rules = {k: v for k, v in (line.strip().replace("/", "").split(" => ") for line in f.readlines())}


def transform(sq, flip, rot):
    size = int(len(sq) ** 0.5)
    for _ in range(rot):
        if size == 2:
            sq = sq[2] + sq[0] + sq[3] + sq[1]
        elif size == 3:
            sq = sq[6] + sq[3] + sq[0] + sq[7] + sq[4] + sq[1] + sq[8] + sq[5] + sq[2]
    if flip:
        sq = sq[-size:] + sq[size:-size] + sq[:size]
    return sq


def recombine(squares):
    """Recombine 3x3s into 2x2s in the correct order"""
    sq_per_size = int(len(squares) ** 0.5)
    big_square = ""
    for i in range(sq_per_size):
        for sq_i in range(3):
            for j in range(sq_per_size):
                big_square += squares[sq_per_size * i + j][3 * sq_i : 3 * sq_i + 3]
    size = int(len(big_square) ** 0.5)
    squares = []
    for i in range(0, size, 2):
        for j in range(0, size, 2):
            squares.append(
                big_square[size * i + j : size * i + j + 2] + big_square[size * i + j + size : size * i + j + 2 + size]
            )
    return squares


complete_rules = dict()
for key, rule in rules.items():
    for flip, rot in ((f, r) for f in range(2) for r in range(4)):
        assert not (transform(key, flip, rot) in rules and transform(key, flip, rot) != key)
        complete_rules[transform(key, flip, rot)] = rule


def generate(count):
    squares = [".#...####"]
    size = 3
    for _ in range(count):
        if size % 2 != 0:
            # 3x3s -> 4x4s -> break 4x4s into 2x2s
            new_squares = [None for _ in range(len(squares) * 4)]
            sq_per_row = 2 * size // 3
            for pos, square in enumerate(squares):
                start = 2 * pos + sq_per_row * int(2 * pos // sq_per_row)
                new_square = complete_rules[square]
                new_squares[start] = new_square[:2] + new_square[4:6]
                new_squares[start + 1] = new_square[2:4] + new_square[6:8]
                new_squares[start + sq_per_row] = new_square[8:10] + new_square[12:14]
                new_squares[start + sq_per_row + 1] = new_square[10:12] + new_square[14:16]
            squares = new_squares
            size = 4 * size // 3
        elif size % 4 == 0:
            # 2x2s -> 3x3s -> recombine into 2x2s
            squares = recombine([complete_rules[square] for square in squares])
            size = 3 * size // 2
        else:
            # 2x2s -> 3x3s -> no change
            squares = [complete_rules[square] for square in squares]
            size = 3 * size // 2
    return sum(sq.count("#") for sq in squares)


def part1():
    return generate(5)


def part2():
    return generate(18)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
