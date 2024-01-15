class Layer:
    def __init__(self, depth, range):
        self.depth = int(depth)
        self.range = int(range)
        self.cycle = 2 * self.range - 2


with open("2017/data/day_13.txt") as f:
    layers = [Layer(*line.strip().split(": ")) for line in f.readlines()]


def part1():
    # The cycle for a layer of range k is the kth even number (2*k-2)
    # We only need to check if the cycle is hit on that layer depth knowing that depth = current picosecond
    return sum(layer.depth * layer.range for layer in layers if layer.depth % layer.cycle == 0)


def part2():
    delay = 1
    while any((delay + layer.depth) % layer.cycle == 0 for layer in layers):
        delay += 1
    return delay


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
