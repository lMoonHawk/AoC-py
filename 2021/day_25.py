with open("2021/data/day_25.txt") as f:
    herd_init = [list(line.strip()) for line in f]


def part1():
    herd = herd_init
    steps = 0
    while True:
        movement = False
        for group in [">", "v"]:
            new_herd = [row[:] for row in herd]
            for i, row in enumerate(herd):
                for j, loc in enumerate(row):
                    if loc not in group:
                        continue
                    new_i, new_j = i, j
                    if group == ">":
                        new_j = (j + 1) % len(herd[0])
                    elif group == "v":
                        new_i = (i + 1) % len(herd)
                    if herd[new_i][new_j] != ".":
                        continue
                    new_herd[new_i][new_j] = group
                    new_herd[i][j] = "."
                    movement = True
            herd = new_herd
        steps += 1
        if not movement:
            return steps


def part2():
    return


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
