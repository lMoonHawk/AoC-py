def get_instructions():
    with open("2022/data/day_05.txt") as f:
        stacks_txt, inst_txt = [el.splitlines() for el in f.read().split("\n\n")]
        nb_stacks = (len(stacks_txt[0]) + 1) // 4
        stacks = [[] for _ in range(nb_stacks)]
        for line in reversed(stacks_txt[:-1]):
            for k in range(nb_stacks):
                crate = line[k * 4 + 1]
                if crate != " ":
                    stacks[k].append(crate)
        instructions = ((int(el[1]), int(el[3]) - 1, int(el[5]) - 1) for el in (line.split() for line in inst_txt))
    return stacks, instructions


def op(count, ver):
    if ver == 9000:
        return slice(None, -count - 1, -1)
    elif ver == 9001:
        return slice(-count, None, None)


def peek_rearrange(stacks, instructions, ver=9000):
    for count, start, end in instructions:
        stacks[end].extend(stacks[start][op(count, ver)])
        stacks[start] = stacks[start][:-count]
    return "".join(stack[-1] for stack in stacks)


def part1():
    return peek_rearrange(*get_instructions(), ver=9000)


def part2():
    return peek_rearrange(*get_instructions(), ver=9001)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
