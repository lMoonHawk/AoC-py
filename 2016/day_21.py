def parse_instruction(line):
    inst = line.strip().split()
    if "swap position" in line:
        return swap_pos, int(inst[2]), int(inst[-1])
    elif "swap letter" in line:
        return swap_letter, inst[2], inst[-1]
    elif "rotate based on position" in line:
        return rotate_pos, inst[-1]
    elif "rotate" in line:
        return rotate_steps, inst[1] == "right", int(inst[-2])
    elif "reverse positions" in line:
        return reverse_pos, int(inst[-3]), int(inst[-1])
    elif "move position" in line:
        return move_pos, int(inst[2]), int(inst[-1])


def instructions():
    with open("2016/data/day_21.txt") as f:
        return [parse_instruction(line) for line in f]


def swap_pos(pw, x, y):
    out = list(pw)
    x, y = sorted((x, y))
    out[x], out[y] = out[y], out[x]
    return "".join(out)


def swap_letter(pw, a, b):
    return swap_pos(pw, pw.index(a), pw.index(b))


def rotate_steps(pw, right, steps):
    n = len(pw)
    pw *= 3
    return pw[2 * n - steps : 3 * n - steps] if right else pw[steps : n + steps]


def rotate_pos(pw, a):
    index = pw.index(a)
    add = 1 if index >= 4 else 0
    return rotate_steps(pw, True, 1 + index + add)


def rev_rotate_pos(pw, a):
    for k in range(len(pw)):
        pw = rotate_steps(pw, False, 1)
        if k == 4:
            pw = rotate_steps(pw, False, 1)
        if pw.index(a) == k:
            return pw


def reverse_pos(pw, x, y):
    return pw[:x] + pw[x : y + 1][::-1] + pw[y + 1 :]


def move_pos(pw, x, y):
    out = list(pw)
    out.insert(y, out.pop(x))
    return "".join(out)


def part1():
    pw = "abcdefgh"
    for op, *args in instructions():
        pw = op(pw, *args)
    return pw


def part2():
    pw = "fbgdceah"
    for op, *args in reversed(instructions()):
        if op.__name__ == "rotate_steps":
            args[0] = not args[0]
        elif op.__name__ == "rotate_pos":
            op = rev_rotate_pos
        elif op.__name__ == "move_pos":
            args[0], args[1] = args[1], args[0]
        pw = op(pw, *args)
    return pw


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
