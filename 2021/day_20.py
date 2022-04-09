def parse():
    with open("2021/data/day_20.txt") as f:
        # Parsing
        input_image = []
        for row, content in enumerate(f):
            content = content.strip()

            if not row:
                algo = content
                continue

            if content != "":
                input_image.append(list(content))

    return algo, input_image


def get_index(image, i, j, inf="."):
    neighbors = [
        (ni, nj) for ni in range(i - 1, i + 2) for nj in range(j - 1, j + 2)
    ]
    pixels = []
    for ni, nj in neighbors:
        if 0 <= ni <= len(image) - 1 and 0 <= nj <= len(image[0]) - 1:
            pixels.append(image[ni][nj])
        else:
            pixels.append(inf)

    number = "".join(["1" if pixel == "#" else "0" for pixel in pixels])
    return int(number, 2)


def enhance(input_image, algo, inf):
    output_image = []
    for i in range(-1, len(input_image) + 1):
        output_image.append([])
        for j in range(-1, len(input_image[0]) + 1):
            index = get_index(input_image, i, j, inf)
            output_image[i + 1].append(algo[index])
    return output_image


def enhance_times(k):
    algo, input_image = parse()

    inf = "."
    for k in range(k):
        output_image = enhance(input_image, algo, inf)

        if inf == ".":
            inf = algo[0]
        else:
            inf = algo[-1]

        input_image = output_image

    return sum([sum([pixel == "#" for pixel in row]) for row in output_image])


def part1():
    print(enhance_times(2))


def part2():
    print(enhance_times(50))


if __name__ == "__main__":
    part1()
    part2()
