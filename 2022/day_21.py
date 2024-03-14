with open("2022/data/day_21.txt") as f:
    monkeys = {k: int(v) if v.strip().isnumeric() else v.split() for k, v in (line.split(": ") for line in f)}

ops = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x // y,
}
inverted_ops = {
    "+": lambda x, y, _: x - y,
    "-": lambda x, y, z: x + y if z else y - x,
    "*": lambda x, y, _: x // y,
    "/": lambda x, y, z: x * y if z else y // x,
}


def contains_humn(monkey, monkeys):
    val = monkeys[monkey]
    if monkey == "humn":
        return True
    if isinstance(val, int):
        return False
    if "humn" in val:
        return True
    m1, _, m2 = val
    return contains_humn(m1, monkeys) or contains_humn(m2, monkeys)


def yell(monkey, monkeys):
    val = monkeys[monkey]
    if isinstance(val, int):
        return val
    m1, op, m2 = val
    return ops[op](yell(m1, monkeys), yell(m2, monkeys))


def solve(monkey, monkeys):
    m1, op, m2 = monkeys[monkey]
    humn_branch, eval_branch = (m1, m2) if contains_humn(m1, monkeys) else (m2, m1)
    value = yell(eval_branch, monkeys)

    while humn_branch != "humn":
        m1, op, m2 = monkeys[humn_branch]
        humn_branch, eval_branch = (m1, m2) if contains_humn(m1, monkeys) else (m2, m1)

        evaled_branch = yell(eval_branch, monkeys)
        value = inverted_ops[op](value, evaled_branch, humn_branch == m1)
    return value


def part1():
    return yell("root", monkeys)


def part2():
    return solve("root", monkeys)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
