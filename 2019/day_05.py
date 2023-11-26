class Op:
    ADD = 1
    MULT = 2
    INPUT = 3
    OUTPUT = 4
    JMP = 5
    NJMP = 6
    LT = 7
    EQ = 8
    HALT = 99


def get_program() -> list[int]:
    with open("2019/data/day_05.txt") as f:
        return [int(value) for value in f.readline().split(",")]


def get_instruction(instruction: int) -> tuple[int, str]:
    opcode, modes = int(str(instruction)[-2:]), str(instruction)[:-2]
    return opcode, modes.zfill(3)[::-1]


def get_params(program, pointer, count, modes, writes: bool):
    params = []
    for k in range(count):
        param = program[pointer + k + 1]
        # We send write addresses as indexes
        if modes[k] == "1" or (writes and (k == (count - 1))):
            params.append(param)
        else:
            params.append(program[param])
    return params


def run_intcode(program: list[int], input: int) -> int:
    p = 0
    while True:
        opcode, modes = get_instruction(program[p])

        match opcode:
            case Op.ADD:
                param_1, param_2, write_addr = get_params(program, p, 3, modes, True)
                program[write_addr] = param_1 + param_2
                p += 4

            case Op.MULT:
                param_1, param_2, write_addr = get_params(program, p, 3, modes, True)
                program[write_addr] = param_1 * param_2
                p += 4

            case Op.LT:
                param_1, param_2, write_addr = get_params(program, p, 3, modes, True)
                program[write_addr] = int(param_1 < param_2)
                p += 4

            case Op.EQ:
                param_1, param_2, write_addr = get_params(program, p, 3, modes, True)
                program[write_addr] = int(param_1 == param_2)
                p += 4

            case Op.INPUT:
                (write_addr,) = get_params(program, p, 1, modes, True)
                program[write_addr] = input
                p += 2

            case Op.OUTPUT:
                (output,) = get_params(program, p, 1, modes, False)
                p += 2

            case Op.JMP:
                param_1, param_2 = get_params(program, p, 2, modes, False)
                p = param_2 if param_1 != 0 else p + 3

            case Op.NJMP:
                param_1, param_2 = get_params(program, p, 2, modes, False)
                p = param_2 if param_1 == 0 else p + 3

            case Op.HALT:
                return output


def part1():
    return run_intcode(program=get_program(), input=1)


def part2():
    return run_intcode(program=get_program(), input=5)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
