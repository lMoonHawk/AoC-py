def pad(lst):
    out = [None] * (3 - len(lst)) + lst
    if out[1] is None:
        out[1] = "ASSIGN"
    return out


with open("2015/data/day_07.txt") as f:
    connections = {inst[1]: pad(inst[0].split()) for inst in (line.strip().split(" -> ") for line in f)}

ops = {
    "AND": lambda x, y: x & y,
    "OR": lambda x, y: x | y,
    "LSHIFT": lambda x, y: x << y,
    "RSHIFT": lambda x, y: x >> y,
    "NOT": lambda _, y: ~(0x10000 | y) & 0xFFFF,
    "ASSIGN": lambda _, y: y,
}


def signal(wire, connections, signals=None):
    if signals is None:
        signals = dict()
    if wire is None:
        return wire
    if wire.strip("-").isnumeric():
        return int(wire)
    if wire in signals:
        return signals[wire]

    a, op, b = connections[wire]
    signals[wire] = ops[op](signal(a, connections, signals), signal(b, connections, signals))
    return signals[wire]


def part1():
    return signal("a", connections)


def part2():
    signals = {"b": signal("a", connections)}
    return signal("a", connections, signals)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
