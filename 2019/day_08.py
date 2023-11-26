class Img:
    WIDTH = 25
    HEIGHT = 6
    PIXELS = WIDTH * HEIGHT


def part1():
    with open("2019/data/day_08.txt") as f:
        layers = []
        while True:
            layer = f.read(Img.PIXELS).strip()
            if not layer:
                break
            layers.append(layer)

    zeros = [layer.count("0") for layer in layers]
    min_index = zeros.index(min(zeros))
    return layers[min_index].count("1") * layers[min_index].count("2")


def part2():
    with open("2019/data/day_08.txt") as f:
        layers = []
        while True:
            layer = f.read(Img.PIXELS).strip()
            if not layer:
                break
            layer = [layer[i : i + Img.WIDTH] for i in range(0, Img.PIXELS, Img.WIDTH)]
            layers.append(layer)

    image_repr = "\n"

    for row in range(Img.HEIGHT):
        for col in range(Img.WIDTH):
            for layer in layers:
                color = layer[row][col]
                if color == "2":
                    continue
                image_repr += ("." if color == "0" else "#") + " "
                break
        image_repr += "\n"

    return image_repr


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
