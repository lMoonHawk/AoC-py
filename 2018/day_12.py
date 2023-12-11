with open("2018/data/day_12.txt") as f:
    ini = list(f.readline().strip().split(": ")[1])
    cases = {line.strip().split(" => ")[0]: line.strip().split(" => ")[1] for line in f.readlines() if "=>" in line}


def next_state(state):
    return [cases["".join(state[k : k + 5])] for k in range(len(state) - 4)]


def part1():
    plants, index = ini, 0
    for _ in range(20):
        plants, index = next_state(["."] * 4 + plants + ["."] * 4), index + 2
    return sum((i - index) * (p == "#") for i, p in enumerate(plants))


def part2():
    # Each cycle has 3 steps:
    # 1- add padding (first plant index 0 becomes index 4)
    # 2- calculate next step (index 4 becomes index 2)
    # 3- cut empty pots on the edge to save space (index 2 becomes index - index of first plant)
    # We reach an equilibrium at some point, where plants stay or drift
    plants, index = ini, 0
    prev_plants, prev_index = [], None
    k = 0
    while plants != prev_plants:
        prev_plants[:], prev_index = plants, index
        plants, index = next_state(["."] * 4 + plants + ["."] * 4), index + 2
        first_plant = plants.index("#")
        index -= first_plant
        plants = plants[first_plant : -list(reversed(plants)).index("#")]
        k += 1

    index += (index - prev_index) * (50_000_000_000 - k)
    return sum((i - index) * (p == "#") for i, p in enumerate(plants))


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
