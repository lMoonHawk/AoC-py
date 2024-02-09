with open("2015/data/day_23.txt") as f:
    program = [line.strip().replace(",", "").split() for line in f]


def run(r):
    ip = 0
    while 0 <= ip < len(program):
        op, *args = program[ip]
        match op:
            case "hlf":
                r[args[0]] //= 2
            case "tpl":
                r[args[0]] *= 3
            case "inc":
                r[args[0]] += 1
            case "jmp":
                ip += int(args[0])
                continue
            case "jie" if r[args[0]] % 2 == 0:
                ip += int(args[1])
                continue
            case "jio" if r[args[0]] == 1:
                ip += int(args[1])
                continue
        ip += 1
    return r["b"]


def part1():
    return run({"a": 0, "b": 0})


def part2():
    return run({"a": 1, "b": 0})


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
