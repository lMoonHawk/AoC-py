with open("2017/data/day_19.txt") as f:
    diagram = f.readlines()


def routing(diagram):
    x, y = diagram[0].index("|"), 0
    steps, mx, my = 0, 0, 1
    letters = ""
    while diagram[y][x] != " ":
        letters += diagram[y][x] if diagram[y][x].isalpha() else ""
        if diagram[y][x] == "+":
            turns = [(1 - abs(mx), 1 - abs(my)), (abs(mx) - 1, abs(my) - 1)]
            for mx, my in turns:
                if diagram[y + my][x + mx] != " ":
                    break
        x, y = x + mx, y + my
        steps += 1
    return steps, letters


def part1():
    _, letters = routing(diagram)
    return letters


def part2():
    steps, _ = routing(diagram)
    return steps


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
