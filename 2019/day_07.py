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
    with open("2019/data/day_07.txt") as f:
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
                program[write_addr] = inputs.pop(0)
                p += 2

            case Op.OUTPUT:
                (output,) = get_params(program, p, 1, modes, False)
                p += 2
                if asynch:
                    return output, p

            case Op.JMP:
                param_1, param_2 = get_params(program, p, 2, modes, False)
                p = param_2 if param_1 != 0 else p + 3

            case Op.NJMP:
                param_1, param_2 = get_params(program, p, 2, modes, False)
                p = param_2 if param_1 == 0 else p + 3

            case Op.HALT:
                return output, -1


def part1():
    settings = (
        (a, b, c, d, e)
        for a in range(5)
        for b in range(5)
        for c in range(5)
        for d in range(5)
        for e in range(5)
        if len({a, b, c, d, e}) == 5
    )

    max_output = 0
    for setting in settings:
        signal = 0
        for amp in range(5):
            signal, _ = run_intcode(get_program(), [setting[amp], signal])
        max_output = max(signal, max_output)
    return max_output


def part2():
    settings = (
        (a, b, c, d, e)
        for a in range(5, 10)
        for b in range(5, 10)
        for c in range(5, 10)
        for d in range(5, 10)
        for e in range(5, 10)
        if len({a, b, c, d, e}) == 5
    )

    max_output = 0
    for setting in settings:
        programs = [get_program() for _ in range(5)]
        pointer = [0] * 5

        first_cycle = True
        signal = 0
        while pointer[4] != -1:
            for amp in range(5):
                if first_cycle:
                    payload = [setting[amp], signal]
                else:
                    payload = [signal]

                signal, pointer[amp] = run_intcode(programs[amp], payload, p=pointer[amp], asynch=True)
            first_cycle = False

        max_output = max(signal, max_output)
    return max_output


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
