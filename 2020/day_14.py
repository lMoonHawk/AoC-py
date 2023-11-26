def part1():
    mem = dict()

    with open("2020/data/day_14.txt") as f:
        for line in f:
            instruction, value = line.strip().split(" = ")
            if "mask = " in line:
                erase_mask = ["1" if bit == "X" else "0" for bit in value]
                or_mask = ["0" if bit == "X" else bit for bit in value]

                erase_mask = int("".join(erase_mask), 2)
                or_mask = int("".join(or_mask), 2)

            else:
                address = int(instruction[instruction.index("[") + 1 : instruction.index("]")])
                value = int(value)

                mem[address] = (value & erase_mask) | or_mask

    print(sum(mem.values()))


def part2():
    mem = dict()

    def get_floating(binary: list[str]) -> list[tuple[str]]:
        """Returns all possible addresses from an address whith floating bits"""
        out = []
        stack = [binary]
        while stack:
            to_split = stack.pop()
            if "X" in to_split:
                k = to_split.index("X")
                stack.append(to_split[:k] + ["0"] + to_split[k + 1 :])
                stack.append(to_split[:k] + ["1"] + to_split[k + 1 :])
            else:
                out.append(tuple(to_split))
        return out

    with open("2020/data/day_14.txt") as f:
        for line in f:
            instruction, value = line.strip().split(" = ")
            if "mask = " in line:
                mask = value
            else:
                addresses = []

                # Isolate decimal address
                floating_address = instruction[instruction.index("[") + 1 : instruction.index("]")]
                # Convert to 36-bit
                floating_address = f"{int(floating_address):0>36b}"
                # Apply mask
                floating_address = [a if m == "0" else m for m, a in zip(mask, floating_address)]
                # Get all addresses
                addresses = get_floating(floating_address)
                for address in addresses:
                    mem[address] = int(value)

    print(sum(mem.values()))


if __name__ == "__main__":
    part1()
    part2()
