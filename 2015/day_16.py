with open("2015/data/day_16.txt") as f:
    sues = [{k: int(v) for k, v in [prop.split(": ")[-2:] for prop in line.strip().split(", ")]} for line in f]

target = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


def part1():
    for i, sue in enumerate(sues):
        if all(sue[k] == v for k, v in target.items() if k in sue):
            return i + 1


def part2():
    for i, sue in enumerate(sues):
        for k, v in target.items():
            if k in sue:
                if k in ["cats", "trees"]:
                    if sue[k] <= v:
                        break
                elif k in ["pomeranians", "goldfish"]:
                    if sue[k] >= v:
                        break
                else:
                    if sue[k] != v:
                        break
        else:
            return i + 1


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
