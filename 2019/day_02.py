def get_program(noun, verb):
    with open("2019/data/day_02.txt") as f:
        program = [int(value) for value in f.readline().split(",")]
        program[1], program[2] = noun, verb
        return program


def part1():
    program = get_program(12, 2)

    index = 0
    while True:
        value = program[index]
        if value == 99:
            return program[0]
        if value == 1:
            program[program[index + 3]] = program[program[index + 1]] + program[program[index + 2]]
        elif value == 2:
            program[program[index + 3]] = program[program[index + 1]] * program[program[index + 2]]
        index += 4


def part2():
    count_mem = len(get_program(12, 2))
    tests = ((noun, verb) for noun in range(count_mem) for verb in range(count_mem))

    for noun, verb in tests:
        program = get_program(noun, verb)

        index = 0
        while True:
            value = program[index]
            if value == 99:
                if program[0] == 19690720:
                    return 100 * noun + verb
                break
            if value == 1:
                program[program[index + 3]] = program[program[index + 1]] + program[program[index + 2]]
            elif value == 2:
                program[program[index + 3]] = program[program[index + 1]] * program[program[index + 2]]
            index += 4


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
