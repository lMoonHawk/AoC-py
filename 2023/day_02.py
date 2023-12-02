def is_poss(nb, col):
    nb = int(nb)
    if (col == "red" and nb > 12) or (col == "green" and nb > 13) or (col == "blue" and nb > 14):
        return False
    return True


def part1():
    with open("2023/data/day_02.txt") as f:
        return sum(
            (game + 1)
            * all(is_poss(*c.split()) for lot in line.strip().split(": ")[1].split("; ") for c in lot.split(", "))
            for game, line in enumerate(f)
        )


def part2():
    answer = 0
    with open("2023/data/day_02.txt") as f:
        for line in f:
            colors = {"red": 0, "green": 0, "blue": 0}
            for lot in line.strip().split(": ")[1].split("; "):
                for cube in lot.split(", "):
                    nb, col = cube.split()
                    nb = int(nb)
                    if colors[col] < nb:
                        colors[col] = nb
            answer += colors["red"] * colors["green"] * colors["blue"]
    return answer


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
