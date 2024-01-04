with open("2018/data/day_19.txt") as f:
    instructions = [line.strip().split(" ") for line in f.readlines()]
    bound, instructions = int(instructions[0][1]), [(op, int(a), int(b), int(c)) for op, a, b, c in instructions[1:]]


opcodes = {
    "addr": lambda a, b, c, reg: [reg[a] + reg[b] if k == c else r for k, r in enumerate(reg)],
    "addi": lambda a, b, c, reg: [reg[a] + b if k == c else r for k, r in enumerate(reg)],
    "mulr": lambda a, b, c, reg: [reg[a] * reg[b] if k == c else r for k, r in enumerate(reg)],
    "muli": lambda a, b, c, reg: [reg[a] * b if k == c else r for k, r in enumerate(reg)],
    "banr": lambda a, b, c, reg: [reg[a] & reg[b] if k == c else r for k, r in enumerate(reg)],
    "bani": lambda a, b, c, reg: [reg[a] & b if k == c else r for k, r in enumerate(reg)],
    "borr": lambda a, b, c, reg: [reg[a] | reg[b] if k == c else r for k, r in enumerate(reg)],
    "bori": lambda a, b, c, reg: [reg[a] | b if k == c else r for k, r in enumerate(reg)],
    "setr": lambda a, _, c, reg: [reg[a] if k == c else r for k, r in enumerate(reg)],
    "seti": lambda a, _, c, reg: [a if k == c else r for k, r in enumerate(reg)],
    "gtir": lambda a, b, c, reg: [a > reg[b] if k == c else r for k, r in enumerate(reg)],
    "gtri": lambda a, b, c, reg: [reg[a] > b if k == c else r for k, r in enumerate(reg)],
    "gtrr": lambda a, b, c, reg: [reg[a] > reg[b] if k == c else r for k, r in enumerate(reg)],
    "eqir": lambda a, b, c, reg: [a == reg[b] if k == c else r for k, r in enumerate(reg)],
    "eqri": lambda a, b, c, reg: [reg[a] == b if k == c else r for k, r in enumerate(reg)],
    "eqrr": lambda a, b, c, reg: [reg[a] == reg[b] if k == c else r for k, r in enumerate(reg)],
}


def part1():
    registers = [0, 0, 0, 0, 0, 0]
    while 0 <= registers[bound] < len(instructions):
        name, a, b, c = instructions[registers[bound]]
        registers = opcodes[name](a, b, c, registers)
        registers[bound] += 1
    return registers[0]


def part2():
    # Small attempt at generalising the solution by looking at the biggest register after 100 steps.
    # Through dissassembly using this specific input, one can note that the program tries to calculate
    #   the sum of factors of whatever is in register 4 after some amount of steps.
    registers = [1, 0, 0, 0, 0, 0]
    for _ in range(100):
        name, a, b, c = instructions[registers[bound]]
        registers = opcodes[name](a, b, c, registers)
        registers[bound] += 1
    return sum([n for n in range(1, max(registers) + 1) if max(registers) % n == 0])


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
