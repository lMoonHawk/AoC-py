with open("2018/data/day_21.txt") as f:
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
    # Register 0 is only accessed once in the elfcode.
    # 28: eqrr 1 0 5 (r5 = r1==r0)
    # 29: addr 5 3 3 (if r5: r3/ip += 1 which halts)
    # We run the code until we hit instruction 28 for the first time. The lowest number of instructions which halts must be when A == current B.
    registers = [0, 0, 0, 0, 0, 0]
    while 0 <= registers[bound] < len(instructions):
        name, a, b, c = instructions[registers[bound]]
        registers = opcodes[name](a, b, c, registers)
        registers[bound] += 1
        if registers[bound] == 28:
            return registers[1]


def part2():
    # We run the elfcode until we see a repeat in r1 and provide the last unique r1 stored.
    # The main optimisation can be implemented by noticing that the loop from instruction 17 to 27
    #   is an integer division of r2 with 256, which then goes back to instruction 8.
    registers = [0, 0, 0, 0, 0, 0]
    seen = set()
    while 0 <= registers[bound] < len(instructions):
        if registers[bound] == 17:
            registers[2] //= 256
            registers[bound] = 8
            continue
        elif registers[bound] == 28:
            if registers[1] in seen:
                return last
            seen.add(registers[1])
            last = registers[1]

        name, a, b, c = instructions[registers[bound]]
        registers = opcodes[name](a, b, c, registers)
        registers[bound] += 1


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
