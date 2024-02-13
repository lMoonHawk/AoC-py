with open("2020/data/day_14.txt") as f:
    instructions = [
        (mask, list(ops)) for mask, *ops in (grp.strip().split("\n") for grp in f.read().split("mask = ")[1:])
    ]


def addr_floating(binary: list[str]):
    """Generates all possible addresses from an address whith floating bits"""
    stack = [binary]
    while stack:
        address = stack.pop()
        if "X" in address:
            k = address.index("X")
            stack.append(address[:k] + "0" + address[k + 1 :])
            stack.append(address[:k] + "1" + address[k + 1 :])
        else:
            yield address


def part1():
    mem = dict()
    for mask, ops in instructions:
        and_mask = int(mask.replace("X", "1"), 2)
        or_mask = int(mask.replace("X", "0"), 2)
        for op in ops:
            address = int(op[op.index("[") + 1 : op.index("]")])
            value = int(op.split(" = ")[-1])
            mem[address] = value & and_mask | or_mask
    return sum(mem.values())


def part2():
    mem = dict()
    for mask, ops in instructions:
        for op in ops:
            floating_address = int(op[op.index("[") + 1 : op.index("]")])
            value = int(op.split(" = ")[-1])
            floating_address = [a if m == "0" else m for m, a in zip(mask, f"{floating_address:0>36b}")]
            for address in addr_floating("".join(floating_address)):
                mem[address] = value
    return sum(mem.values())


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
