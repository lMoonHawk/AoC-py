with open("2023/data/day_03.txt") as f:
    schematic = [line.strip() for line in f.readlines()]

SYMBOLS = {"-", "/", "*", "+", "$", "@", "#", "=", "&", "%"}


def key_append(d, k, v):
    if k not in d:
        d[k] = []
    d[k].append(v)


def get_symb_adj(grid, i, j):
    directions = [
        [i - 1, j - 1],
        [i - 1, j],
        [i - 1, j + 1],
        [i, j - 1],
        [i, j + 1],
        [i + 1, j - 1],
        [i + 1, j],
        [i + 1, j + 1],
    ]
    for n_i, n_j in directions:
        if 0 <= n_i < len(grid) and 0 < n_j < len(grid[0]):
            if grid[n_i][n_j] in SYMBOLS:
                return [grid[n_i][n_j], (n_i, n_j)]
    return False


def part1():
    answer = 0
    buffer = ""
    part_nb = False

    for i, row in enumerate(schematic):
        for j, cell in enumerate(row):
            if cell.isdigit():
                buffer += cell
                if not part_nb and get_symb_adj(schematic, i, j):
                    part_nb = True
            elif buffer:
                if part_nb:
                    answer += int(buffer)
                    part_nb = False
                buffer = ""

    return answer


def part2():
    answer = 0
    buffer = ""
    part_nb = False
    poss_gears = dict()

    for i, row in enumerate(schematic):
        for j, cell in enumerate(row):
            if cell.isdigit():
                buffer += cell

                if not part_nb and (s := get_symb_adj(schematic, i, j)):
                    part_nb = True

            elif buffer:
                if part_nb:
                    part = int(buffer)
                    symb, symb_pos = s
                    if symb == "*":
                        key_append(poss_gears, symb_pos, part)
                    answer += part
                    part_nb = False

                buffer = ""

    return sum(v[0] * v[1] for v in poss_gears.values() if len(v) == 2)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
