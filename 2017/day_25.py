def parse_states():
    with open("2017/data/day_25.txt") as f:
        init, *states_txt = f.read().split("\n\n")
    init_state, end_steps = init.split("\n")
    init_state = init_state[-2]
    end_steps = int(end_steps.split()[-2])

    states = dict()
    for state in states_txt:
        label, *conditions = state.split("If")
        label = label.strip()[-2]
        for condition in conditions:
            for line in condition.split("\n"):
                if "current" in line:
                    value = int(line[-2])
                elif "Write" in line:
                    write = int(line[-2])
                elif "Move" in line:
                    move = 2 * ("right" in line) - 1
                elif "Continue" in line:
                    next_state = line[-2]
            states[(label, value)] = write, move, next_state
    return init_state, end_steps, states


def part1():
    state, end_steps, states = parse_states()
    tape_ones = set()
    pointer = 0
    for _ in range(end_steps):
        value = pointer in tape_ones
        write, move, next_state = states[(state, value)]
        if value == 0 and write == 1:
            tape_ones.add(pointer)
        elif value == 1 and write == 0:
            tape_ones.remove(pointer)
        pointer += move
        state = next_state
    return len(tape_ones)


def part2():
    return


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
