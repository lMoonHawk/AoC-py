def resolve(monkeys, monkey):
    # Solve the tree by recursively solving branches until we find a leaf
    maths = monkeys[monkey]

    if maths[0].isdigit():
        return int(maths[0])

    monkey1, operation, monkey2 = maths
    monkey1 = resolve(monkeys, monkey1)
    monkey2 = resolve(monkeys, monkey2)

    if operation == "+":
        return monkey1 + monkey2
    if operation == "-":
        return monkey1 - monkey2
    if operation == "*":
        return monkey1 * monkey2
    if operation == "/":
        return monkey1 // monkey2


def is_branch(monkeys, monkey):
    # Recursive function to determine if humn is in the branch "monkey"
    if monkey.isdigit():
        return False
    if monkey == "humn":
        return True

    maths = monkeys[monkey]
    if maths[0].isdigit():
        return False
    if "humn" in maths:
        return True
    if is_branch(monkeys, maths[0]) or is_branch(monkeys, maths[2]):
        return True
    return False


def humn(monkeys, humn_branch, value):
    # Recursive function to pass the value down until arriving at humn
    if humn_branch == "humn":
        return value

    maths = monkeys[humn_branch]

    if is_branch(monkeys, maths[0]):
        humn_branch, other_branch = maths[0], maths[2]
    else:
        humn_branch, other_branch = maths[2], maths[0]

    # Value of the branch not containing humn
    subvalue = resolve(monkeys, other_branch)
    # Depending on the operator, modify the value to know what the
    #   current humn branch has to evaluate to
    if maths[1] == "+":
        value -= subvalue
    elif maths[1] == "*":
        value //= subvalue
    elif maths[1] == "/":
        if maths[0] == humn_branch:
            value *= subvalue
        else:
            value = subvalue // value
    elif maths[1] == "-":
        if maths[0] == humn_branch:
            value += subvalue
        else:
            value = subvalue - value

    return humn(monkeys, humn_branch, value)


def part1():
    monkeys = dict()

    with open("2022/data/day_21.txt") as f:
        for line in f:
            monkey, maths = line.split(":")
            maths = maths.strip().split()
            monkeys[monkey] = maths

    print(resolve(monkeys, "root"))


def part2():
    monkeys = dict()

    with open("2022/data/day_21.txt") as f:
        for line in f:
            monkey, maths = line.split(":")
            maths = maths.strip().split()
            monkeys[monkey] = maths

    maths = monkeys["root"]
    if is_branch(monkeys, maths[0]):
        humn_branch, other_branch = maths[0], maths[2]
    else:
        humn_branch, other_branch = maths[2], maths[0]

    # Humn branch has to evaluate to "value"
    value = resolve(monkeys, other_branch)

    print(humn(monkeys, humn_branch, value))


if __name__ == "__main__":
    part1()
    part2()
