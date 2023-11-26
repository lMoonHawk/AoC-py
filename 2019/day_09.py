class Op:
    ADD = 1
    MULT = 2
    INPUT = 3
    OUTPUT = 4
    JMP = 5
    NJMP = 6
    LT = 7
    EQ = 8
    OFFSET = 9
    HALT = 99


def get_program() -> list[int]:
    with open("2019/data/day_09.txt") as f:
        return {addr: int(value) for addr, value in enumerate(f.readline().split(","))}


def get_instruction(instruction: int) -> tuple[int, str]:
    opcode, modes = int(str(instruction)[-2:]), str(instruction)[:-2]
    return opcode, modes.zfill(3)[::-1]


def get_params(program, param_count, pointer, base, modes, writes: bool):
    params = []
    for k in range(param_count):
        param = get_from(program, pointer + k + 1)

        # Write addresses are the last parameters and are always return as indexes
        is_write_addr = writes and (k == (param_count - 1))

        if modes[k] == "0":
            param = get_from(program, param) if not is_write_addr else param
        elif modes[k] == "2":
            param = get_from(program, param + base) if not is_write_addr else param + base

        params.append(param)
    return params


def write_to(program, addr, content):
    if addr not in program:
        program[addr] = 0
    program[addr] = content


def get_from(program, addr):
    if addr not in program:
        program[addr] = 0
    return program[addr]


def run_intcode(program: list[int], inputs: list[int], p=0, asynch: bool = False) -> tuple[int]:
    """Interprets intcode.

    Args:
        program (list[int]): Intcode
        inputs (list[int]): Payload
        p (int, optional): Address of the entry point. Defaults to 0.
        asynch (bool, optional): In "asynchronous" mode the interpreter stops after producing an output. Defaults to False.

    Returns:
        tuple[int]: output, pointer. This allows the program to be ran again with its state saved. A pointer of -1 signifies the program has halted.
    """
    # If the program halts in asynchronous mode, its last outpout was already provided (previous return). Otherwise the output will be overwritten.
    if asynch:
        output = inputs[-1]
    base = 0
    output = []

    while True:
        opcode, modes = get_instruction(program[p])

        match opcode:
            case Op.ADD:
                param_1, param_2, write_addr = get_params(program, 3, p, base, modes, True)
                write_to(program, write_addr, param_1 + param_2)
                p += 4

            case Op.MULT:
                param_1, param_2, write_addr = get_params(program, 3, p, base, modes, True)
                write_to(program, write_addr, param_1 * param_2)
                p += 4

            case Op.LT:
                param_1, param_2, write_addr = get_params(program, 3, p, base, modes, True)
                write_to(program, write_addr, int(param_1 < param_2))
                p += 4

            case Op.EQ:
                param_1, param_2, write_addr = get_params(program, 3, p, base, modes, True)
                write_to(program, write_addr, int(param_1 == param_2))
                p += 4

            case Op.INPUT:
                (write_addr,) = get_params(program, 1, p, base, modes, True)
                write_to(program, write_addr, inputs.pop(0))
                p += 2

            case Op.OUTPUT:
                (output,) = get_params(program, 1, p, base, modes, False)
                p += 2
                if asynch:
                    return output, p

            case Op.JMP:
                param_1, param_2 = get_params(program, 2, p, base, modes, False)
                p = param_2 if param_1 != 0 else p + 3

            case Op.NJMP:
                param_1, param_2 = get_params(program, 2, p, base, modes, False)
                p = param_2 if param_1 == 0 else p + 3

            case Op.OFFSET:
                (base_inc,) = get_params(program, 1, p, base, modes, False)
                base += base_inc
                p += 2

            case Op.HALT:
                return output, -1


def part1():
    return run_intcode(get_program(), [1])[0]


def part2():
    return run_intcode(get_program(), [2])[0]


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
