with open("2022/data/day_22.txt") as f:
    board, instructions_txt = f.read().rstrip().split("\n\n")
    board = [line for line in board.split("\n")]
    instructions = [
        ("move", int(el)) if el.isnumeric() else ("turn", 2 * (el == "R") - 1)
        for el in instructions_txt.replace("R", " R ").replace("L", " L ").split()
    ]


LENGTH = 50
cube_edges = {
    (1, 0, 2): lambda x, y: (0, 3 * LENGTH - y - 1, 0),
    (1, 0, 3): lambda x, y: (0, x + 2 * LENGTH, 0),
    (2, 0, 3): lambda x, y: (x - 2 * LENGTH, 4 * LENGTH - 1, 3),
    (2, 0, 0): lambda x, y: (x - LENGTH, 3 * LENGTH - y - 1, 2),
    (2, 0, 1): lambda x, y: (2 * LENGTH - 1, x - LENGTH, 2),
    (1, 1, 2): lambda x, y: (y - LENGTH, 2 * LENGTH, 1),
    (1, 1, 0): lambda x, y: (y + LENGTH, LENGTH - 1, 3),
    (0, 2, 3): lambda x, y: (LENGTH, LENGTH + x, 0),
    (0, 2, 2): lambda x, y: (LENGTH, 3 * LENGTH - y - 1, 0),
    (1, 2, 0): lambda x, y: (3 * LENGTH - 1, 3 * LENGTH - y - 1, 2),
    (1, 2, 1): lambda x, y: (LENGTH - 1, x + 2 * LENGTH, 2),
    (0, 3, 2): lambda x, y: (y - 2 * LENGTH, 0, 1),
    (0, 3, 0): lambda x, y: (y - 2 * LENGTH, 3 * LENGTH - 1, 3),
    (0, 3, 1): lambda x, y: (x + 2 * LENGTH, 0, 1),
}


def wrap_next_pos(x, y, mx, my, board, facing):
    nx, ny = x, y
    while True:
        nx, ny = (nx + mx) % (3 * LENGTH), (ny + my) % len(board)
        if 0 <= nx < len(board[ny]):
            if board[ny][nx] == "#":
                return x, y, facing
            elif board[ny][nx] == ".":
                return nx, ny, facing


def cube_next_pos(x, y, mx, my, board, facing):
    nx, ny, nfacing = x + mx, y + my, facing
    if not (0 <= ny < len(board) and 0 <= nx < len(board[ny])) or board[ny][nx] == " ":
        nx, ny, nfacing = cube_edges[x // LENGTH, y // LENGTH, facing](x, y)
    if board[ny][nx] == "#":
        return x, y, facing
    elif board[ny][nx] == ".":
        return nx, ny, nfacing


def traverse(move_fun):
    forward = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    x, y = [y for y, tile in enumerate(board[0]) if tile == "."][0], 0
    facing = 0
    for instruction, value in instructions:
        if instruction == "move":
            for _ in range(value):
                x, y, facing = move_fun(x, y, *forward[facing], board, facing)
        elif instruction == "turn":
            facing = (facing + value) % 4
    return 1_000 * (y + 1) + 4 * (x + 1) + facing


def part1():
    return traverse(move_fun=wrap_next_pos)


def part2():
    return traverse(move_fun=cube_next_pos)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
