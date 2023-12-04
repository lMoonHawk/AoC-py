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
    with open("2019/data/day_25.txt") as f:
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
                if not inputs:
                    state["pointer"], state["base"] = p, base
                    return None

                (write_addr,) = get_params(program, 1, p, base, modes, True)
                write_to(program, write_addr, inputs.pop(0))
                if asynch:
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
                state["pointer"], state["base"] = -1, None
                return None


def asciify(inst):
    return [el for line in [[ord(c) for c in line] + [ord("\n")] for line in inst] for el in line]


def asciify(asc):
    return [ord(a) for a in asc] + [ord("\n")]


def parse_output(text):
    if "==" not in text:
        return None
    place = text.split("==")[1].strip()
    doors = [direction for direction in ["north", "east", "south", "west"] if direction in text]
    items = []
    if "Items here:" in text:
        items = text.split("Items here:\n")[1].split("\n\n")[0].replace("- ", "").split("\n")
    return place, doors, items


def take_all_objects(program, state):
    banned = ["escape pod", "photons", "giant electromagnet", "molten lava", "infinite loop"]
    buffer = ""
    inputs = []

    directions = {0: "north", 1: "east", 2: "south", 3: "west"}
    facing = 0
    visited = dict()
    inventory = []

    while True:
        output = run_intcode(program, inputs, True, state)

        if not output:
            out = parse_output(buffer)

            if out:
                place, doors, items = out

                if place not in visited:
                    visited[place] = 1
                else:
                    visited[place] += 1
                if visited[place] > 4:
                    return doors, inventory

                if place == "Security Checkpoint":
                    facing = (facing - 2) % 4
                elif directions[(facing + 1) % 4] in doors:
                    facing = (facing + 1) % 4
                elif directions[facing] in doors:
                    pass
                elif directions[(facing - 1) % 4] in doors:
                    facing = (facing - 1) % 4
                else:
                    facing = (facing - 2) % 4

            if items and (item := items.pop(0)) not in banned:
                inputs = asciify(f"take {item}")
                inventory.append(item)
            else:
                inputs = asciify(directions[facing])

            buffer = ""
        else:
            buffer += chr(output)


def go_to(end, start_doors, program, state):
    buffer = ""
    inputs = []

    directions = {0: "north", 1: "east", 2: "south", 3: "west"}
    facing = 0
    start = True

    while True:
        output = run_intcode(program, inputs, True, state)

        if not output:
            out = parse_output(buffer)

            if out or start:
                if start:
                    place, doors = "", start_doors
                    start = False
                else:
                    place, doors, _ = out

                if place == end:
                    return facing
                elif directions[(facing + 1) % 4] in doors:
                    facing = (facing + 1) % 4
                elif directions[facing] in doors:
                    pass
                elif directions[(facing - 1) % 4] in doors:
                    facing = (facing - 1) % 4
                else:
                    facing = (facing - 2) % 4

            inputs = asciify(directions[facing])
            buffer = ""
        else:
            buffer += chr(output)


def check_plate(to_drop, facing, program, state):
    inputs = []
    directions = {0: "north", 1: "east", 2: "south", 3: "west"}

    for dropped_item in to_drop:
        inputs = asciify(f"drop {dropped_item}")
        run_intcode(program, inputs, True, state)
        while True:
            output = run_intcode(program, inputs, True, state)
            if not output:
                break

    inputs = asciify(directions[facing])
    buffer = chr(run_intcode(program, inputs, True, state))
    while True:
        output = run_intcode(program, [], True, state)
        if not output:
            if "Alert" in buffer:
                return None
            else:
                return buffer
        buffer += chr(output)


def part1():
    program = get_program()
    state = {"pointer": 0, "base": 0, "consumed": 0}

    doors, inventory = take_all_objects(program, state)
    facing = go_to("Security Checkpoint", doors, program, state)

    for k in range(1 << len(inventory)):
        to_drop = [item for item, drop in zip(inventory, f"{bin(k)[2:]:0>{len(inventory)}}") if drop == "1"]
        if answer := check_plate(to_drop, facing, program.copy(), state.copy()):
            return answer


def part2():
    return None


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
