with open("2017/data/day_23.txt") as f:
    instructions = [line.strip().split() for line in f.readlines()]


def access(registers, register):
    if register not in registers:
        registers[register] = 0
    return registers[register]


def evaluate(registers, args):
    r = args[0]
    values = []
    for value in args:
        if not value.strip("-").isnumeric():
            values.append(access(registers, value))
        else:
            values.append(int(value))
    return r, values[0], values[1] if len(values) == 2 else None


def is_prime(n):
    if n == 2:
        return True
    if n == 1 or n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def part1():
    registers = dict()
    ip = 0
    mul_cnt = 0
    while 0 <= ip < len(instructions):
        op, *args = instructions[ip]
        r, val1, val2 = evaluate(registers, args)
        if op == "set":
            registers[r] = val2
        elif op == "sub":
            registers[r] = val1 - val2
        elif op == "mul":
            registers[r] = val1 * val2
            mul_cnt += 1
        elif op == "jnz" and val1 != 0:
            ip += val2 - 1
        ip += 1
    return mul_cnt


def part2():
    # The instructions can be rewritten as:
    # h = 0
    # b = 65 * 100 + 100_000
    # c = b + 17_000
    # while True:
    #     f = 1
    #     d = 2
    #     while True:
    #         e = 2
    #         while True:
    #             if b == d * e:
    #                 f = 0
    #             e += 1
    #             if e == b:
    #                 break
    #         d += 1
    #         if d == b:
    #             break
    #     if f == 0:
    #         h += 1
    #     if c == b:
    #         break
    #     b += 17

    # When b can be written as the factor of d and e, f is set to 0 which ultimately increments h.
    # This process is done for the starting b up to c
    b = 65 * 100 + 100_000
    c = b + 17_000
    return sum(not is_prime(p) for p in range(b, c + 1, 17))


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
