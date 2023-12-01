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
    with open(f"2019/data/day_23.txt") as f:
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


def run_intcode(program: list[int], inputs: list[int], state: dict = None) -> tuple[int]:
    p, base = state["pointer"], state["base"]
    output = None

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
            state["pointer"], state["base"] = -1, None

    state["pointer"], state["base"] = p, base
    return None if not output else output


def part1():
    states = [{"pointer": 0, "base": 0, "consumed": 0} for _ in range(50)]
    programs = [get_program() for _ in range(50)]
    queues = [[n] for n in range(50)]
    outputs = [[] for _ in range(50)]

    while True:
        for n in range(50):
            if output := run_intcode(programs[n], queues[n] if queues[n] else [-1], state=states[n]):
                outputs[n].append(output)
                if len(outputs[n]) == 3:
                    addr, x, y = outputs[n].pop(0), outputs[n].pop(0), outputs[n].pop(0)
                    if addr == 255:
                        return y
                    queues[addr].extend([x, y])


def part2():
    states = [{"pointer": 0, "base": 0, "consumed": 0} for _ in range(50)]
    programs = [get_program() for _ in range(50)]
    queues = [[n] for n in range(50)]
    outputs = [[] for _ in range(50)]
    idle = [False for _ in range(50)]

    nat = []
    last_y_nat = None

    while True:
        for n in range(50):
            if queues[n]:
                payload = queues[n]
                empty_payload = False
            else:
                payload = [-1]
                empty_payload = True

            if output := run_intcode(programs[n], payload, state=states[n]):
                idle[n] = False
                outputs[n].append(output)

                if len(outputs[n]) == 3:
                    addr, x, y = outputs[n].pop(0), outputs[n].pop(0), outputs[n].pop(0)
                    if addr == 255:
                        nat = [x, y]
                    else:
                        queues[addr].extend([x, y])

            elif empty_payload and not payload:
                idle[n] = True

        if all(idle) and len(nat) == 2:
            x_nat, y_nat = nat.pop(0), nat.pop(0)
            queues[0].extend([x_nat, y_nat])

            if y_nat == last_y_nat:
                return y_nat
            last_y_nat = y_nat


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
