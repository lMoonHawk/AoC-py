with open("2020/data/day_08.txt") as f:
    instructions = [tuple(line.strip().split(" ")) for line in f.readlines()]


def part1():
    visited = set()
    acc = 0
    current_line = 0
    while current_line not in visited:
        visited.add(current_line)
        operation, argument = instructions[current_line]

        if operation == "acc":
            acc += int(argument)
        if operation == "jmp":
            current_line += int(argument)
            continue

        current_line = current_line + 1

    print(acc)


def part2():
    def check_program(program):
        visited = set()
        acc = 0
        current_line = 0
        end_program = len(program)
        while True:
            if current_line in visited:
                return None
            visited.add(current_line)
            operation, argument = program[current_line]

            jmp_next_line = 1
            if operation == "acc":
                acc += int(argument)
            if operation == "jmp":
                jmp_next_line = int(argument)

            current_line += jmp_next_line
            if current_line > end_program:
                return None
            if current_line == end_program:
                return acc

    for line, (operation, argument) in enumerate(instructions):
        program = instructions.copy()
        if operation == "nop":
            program[line] = tuple(["jmp", argument])
        if operation == "jmp":
            program[line] = tuple(["nop", argument])

        answer = check_program(program)
        if answer is not None:
            print(answer)
            break


if __name__ == "__main__":
    part1()
    part2()
