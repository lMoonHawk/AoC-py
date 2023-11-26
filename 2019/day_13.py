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
    with open("2019/data/day_13.txt") as f:
        return {addr: int(value) for addr, value in enumerate(f.readline().split(","))}


def get_instruction(instruction: int) -> tuple[int, str]:
    opcode, modes = int(str(instruction)[-2:]), str(instruction)[:-2]
    return opcode, modes.zfill(3)[::-1]


def get_params(program, param_count, pointer, base, modes, writes: bool):
    params = []
    for k in range(param_count):
        param = get_from(program, pointer + k + 1)

        # Write addresses are the last parameters and are always returned as indexes
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


def run_intcode(program: list[int], inputs: list[int], asynch: bool = False, state: dict = None) -> tuple[int]:
    """Interprets intcode.

    Args:
        program (list[int]): Intcode
        inputs (list[int]): Payload
        asynch (bool, optional): In "asynchronous" mode the interpreter stops after producing an output. Defaults to False.
        state (dict, optional): Contains a dictionary that will be mutated with the code state when it returns.
                                state["pointer"] and state["base"]. A pointer of -1 signifies the program has halted. Defaults to None.

    Returns:
        int: output. This allows the program to be ran again with its state saved.
    """
    # If the program halts in asynchronous mode, its last outpout was already provided (previous return). Otherwise the output will be overwritten.
    if asynch and inputs:
        output = inputs[-1]

    p, base = 0, 0
    if asynch and state:
        base = state["base"]
        p = state["pointer"]
        if p == -1:
            return None

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
                if asynch and state:
                    state["pointer"], state["base"] = p, base
                    return output

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
                if asynch and state:
                    state["pointer"], state["base"] = -1, None
                    return None
                return output


def part1():
    program = get_program()
    state = {"pointer": 0, "base": 0}
    blocks = 0

    while True:
        _, _, tile_id = [run_intcode(program, [], True, state) for _ in range(3)]
        if state["pointer"] == -1:
            break
        if tile_id == 2:
            blocks += 1

    return blocks


def part2():
    program = get_program()
    program[0] = 2

    state = {"pointer": 0, "base": 0}
    inputs = None
    ball_x = paddle_x = 0

    while True:
        inputs = max(-1, min(1, ball_x - paddle_x))

        x, y, output = [run_intcode(program, [inputs], True, state) for _ in range(3)]
        if state["pointer"] == -1:
            break

        if x == -1 and y == 0:
            score = output
        elif output == 3:
            paddle_x = x
        elif output == 4:
            ball_x = x

    return score


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
