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
    with open("2019/data/day_17.txt") as f:
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
                state["consumed"] += 1
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


facings_index = {94: 0, 65: 1, 118: 2, 60: 3}
move = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def add_coord(v1, v2):
    return tuple([a1 + a2 for a1, a2 in zip(v1, v2)])


def get_scaffold():
    program = get_program()
    scaffolds = set()
    state = {"pointer": 0, "base": 0}
    x, y = (0, 0)
    while True:
        char = run_intcode(program, [], True, state)
        if not char:
            break
        if char == 35:
            scaffolds.add((x, y))
            x += 1
        elif char in [94, 62, 118, 60]:
            position, direction = (x, y), facings_index[char]
            scaffolds.add((x, y))
            x += 1
        elif char == 10:
            x = 0
            y += 1
        else:
            x += 1
    return scaffolds, position, direction


def get_instructions(world, position, direction):
    instructions = []
    while True:
        if add_coord(position, move[direction]) in world:
            instructions[-1] += 1
        elif add_coord(position, move[(direction + 1) % 4]) in world:
            instructions.extend(["R", 1])
            direction = (direction + 1) % 4
        elif add_coord(position, move[(direction - 1) % 4]) in world:
            instructions.extend(["L", 1])
            direction = (direction - 1) % 4
        else:
            break

        position = add_coord(position, move[direction])

    return instructions


def try_compress(l, fun_len):
    fun_lab = ["A", "B", "C"]
    fun = [None, None, None]

    patterns = [l]

    for f, _ in enumerate(fun):
        p = 0
        while p <= len(patterns) - 1:
            pattern = patterns[p]

            if pattern in fun_lab:
                p += 1
                continue

            if not fun[f]:
                if len(pattern) >= fun_len[f]:
                    fun[f] = pattern[: fun_len[f]]
                else:
                    return False, None, None

            for i in range(len(pattern) - fun_len[f] + 1):
                if pattern[i : i + fun_len[f]] == fun[f]:
                    before = pattern[:i]
                    after = pattern[i + fun_len[f] :]

                    del patterns[p]

                    if after:
                        patterns.insert(p, after)
                    patterns.insert(p, fun_lab[f])
                    if before:
                        patterns.insert(p, before)

                    break
            p += 1

    if all(pattern in fun_lab for pattern in patterns):
        return True, patterns, fun
    return False, None, None


def asciify(l):
    out = [ord(c) for c in ",".join(str(el) for el in l)]
    return out + [10]


def compress(l):
    fun_len_tests = ((a, b, c) for a in range(1, 11) for b in range(1, 11) for c in range(1, 11))

    for fun_len in fun_len_tests:
        success, routine, fun = try_compress(l, fun_len)

        if success:
            routine = asciify(routine)
            fun = [asciify(f) for f in fun]
            return routine, fun


def part1():
    world, _, _ = get_scaffold()

    alignment = 0
    for square in world:
        neighbors = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        alignment += square[0] * square[1] * all(add_coord(square, n) in world for n in neighbors)

    return alignment


def part2():
    instructions = get_instructions(*get_scaffold())
    routine, funs = compress(instructions)

    funs = [asc for fun in funs for asc in fun]

    program = get_program()
    program[0] = 2

    state = {"pointer": 0, "base": 0, "consumed": 0}
    payload = [*routine, *funs, ord("n"), 10]

    while True:
        output = run_intcode(program, payload[state["consumed"] :], True, state)
        if not output:
            return answer
        answer = output


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
