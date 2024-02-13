with open("2020/data/day_08.txt") as f:
    instructions = [(op, int(arg)) for op, arg in (line.strip().split(" ") for line in f.readlines())]


def run(instructions):
    visited = set()
    ip = acc = 0
    while True:
        if ip in visited:
            return False, acc
        if ip == len(instructions):
            return True, acc
        visited.add(ip)
        op, arg = instructions[ip]
        if op == "acc":
            acc += arg
        elif op == "jmp":
            ip += arg - 1
        ip += 1


def part1():
    _, acc = run(instructions)
    return acc


def part2():
    swap = {"nop": "jmp", "jmp": "nop"}
    for line, (op, arg) in enumerate(instructions):
        if op not in swap:
            continue
        terminates, acc = run(instructions[:line] + [tuple([swap[op], arg])] + instructions[line + 1 :])
        if terminates:
            return acc


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
