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

    final_dots = set()
    axis, coord = folds[0]
    index = 0 if axis == "x" else 1

    for dot in dots:
        fold_dot = coord * 2 - dot[index]
        dot[index] = dot[index] if dot[index] < coord else fold_dot

        final_dots.add(tuple(dot))

    print(len(final_dots))


def part2():
    dots: list[list[int]] = []
    folds: list[list[str, int]] = []
    folds_next = False
    page = list[list[bool]]

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

    col_count = 0
    row_count = 0

    for axis, coord in folds:
        # Last folding instruction called for each axis is the final page size
        col_count = coord if axis == "x" else col_count
        row_count = coord if axis == "y" else row_count

        index = 0 if axis == "x" else 1

        for dot in dots:
            fold_dot = coord * 2 - dot[index]
            dot[index] = dot[index] if dot[index] < coord else fold_dot

    # Unique dots
    dots = set([tuple(dot) for dot in dots])

    page = [[False] * col_count for i in range(row_count)]

    for dot in dots:
        if dot:
            page[dot[1]][dot[0]] = True

    for line in page:
        for dot in line:
            print("#" if dot else " ", end="")
        print("\n", end="")


if __name__ == "__main__":
    # part1()
    part2()
