def part1():

    dots: list[list[int]] = []
    folds: list[list[str, int]] = []
    folds_next = False

    # Parsing
    with open("2021/data/day_13.txt") as f:
        for line in f:
            if line != "\n" and not folds_next:
                coords = line.strip().split(",")
                dots.append([int(coord) for coord in coords])

            elif line == "\n":
                folds_next = True

            else:
                axis, coord = line.strip().split("=")
                axis = axis[-1:]
                folds.append([axis, int(coord)])

    new_dots = set()
    instruction = folds[0]
    index = 0 if instruction[0] == "x" else 1

    for dot in dots:
        fold_dot = instruction[1] * 2 - dot[index]
        dot[index] = dot[index] if dot[index] < instruction[1] else fold_dot

        new_dots.add(tuple(dot))

    print(len(new_dots))


def part2():
    pass


if __name__ == "__main__":
    part1()
    part2()
