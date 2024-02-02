with open("2016/data/day_12.txt") as f:
    instructions = [line.strip().split() for line in f.readlines()]


def evaluate(arg, registers):
    if arg.strip("-").isnumeric():
        return int(arg)
    return registers[arg]


def run(instructions, registers):
    ip = 0
    while 0 <= ip < len(instructions):
        op, *args = instructions[ip]

        if op == "cpy":
            registers[args[1]] = evaluate(args[0], registers)
        elif op == "inc":
            registers[args[0]] += 1
        elif op == "dec":
            registers[args[0]] -= 1
        elif op == "jnz":
            ip += -1 + evaluate(args[1], registers) if evaluate(args[0], registers) else 0
        ip += 1
    return registers


def part1():
    return run(instructions, {"a": 0, "b": 0, "c": 0, "d": 0})["a"]


def part2():
    return run(instructions, {"a": 0, "b": 0, "c": 1, "d": 0})["a"]


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
