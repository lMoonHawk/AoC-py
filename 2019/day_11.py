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
    with open("2019/data/day_11.txt") as f:
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
                return output


def get_color(panel, panels):
    if panel not in panels:
        return 0
    return panels[panel]


def get_repr_panels(panels):
    xs = [x for x, _ in panels]
    ys = [y for _, y in panels]

    panels_str = "\n"
    for y in range(max(ys), min(ys) - 1, -1):
        for x in range(min(xs), max(xs) + 1):
            color = 0
            if (x, y) in panels:
                color = panels[(x, y)]
            panels_str += "##" if color == 1 else "  "
        panels_str += "\n"
    return panels_str[:-1]


def part1():
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    panels = dict()
    program = get_program()
    state = {"pointer": 0, "base": 0}
    facing, position = 0, (0, 0)

    answer = 0
    while True:
        ini_color = get_color(position, panels)
        paint_color = run_intcode(program, [ini_color], True, state)

        if state["pointer"] == -1:
            break

        # Only count as painted if a new tile goes from black to white
        if position not in panels and paint_color == 1:
            answer += 1
        panels[position] = paint_color

        turn = run_intcode(program, [], True, state)

        rot = 1 if turn == 1 else -1
        facing = (facing + rot) % 4
        position = tuple([p + d for p, d in zip(position, directions[facing])])

    return answer


def part2():
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    program = get_program()
    state = {"pointer": 0, "base": 0}
    facing, position = 0, (0, 0)
    panels = {position: 1}

    while True:
        ini_color = get_color(position, panels)
        paint_color = run_intcode(program, [ini_color], True, state)

        if state["pointer"] == -1:
            break
        panels[position] = paint_color

        turn = run_intcode(program, [], True, state)

        rot = 1 if turn == 1 else -1
        facing = (facing + rot) % 4
        position = tuple([p + d for p, d in zip(position, directions[facing])])

    return get_repr_panels(panels)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
