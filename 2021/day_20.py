with open("2021/data/day_20.txt") as f:
    algo, input_img = f.read().strip().split("\n\n")
    ALGO = [cell == "#" for cell in algo]
    IMG = [[cell == "#" for cell in row] for row in input_img.split("\n")]


def get_pixel(input_img, i, j, algo, infinity):
    index = 0
    for ni, nj in [(i + oi, j + oj) for oi in range(-1, 2) for oj in range(-1, 2)]:
        index <<= 1
        if 0 <= ni < len(input_img) and 0 <= nj < len(input_img[0]):
            index += input_img[ni][nj]
        else:
            index += infinity
    return algo[index]


def enhance(k, input_img, algo):
    invert = infinity = algo[0]
    for _ in range(k):
        infinity = infinity if not invert else (1 - infinity)
        output_img = [
            [get_pixel(input_img, i, j, algo, infinity) for j in range(-1, len(input_img[0]) + 1)]
            for i in range(-1, len(input_img) + 1)
        ]
        input_img = output_img
    return output_img


def part1():
    return sum(sum(row) for row in enhance(2, IMG, ALGO))


def part2():
    return sum(sum(row) for row in enhance(50, IMG, ALGO))


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
