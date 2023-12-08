def get_map():
    with open("2023/data/day_08.txt") as f:
        return [d == "R" for d in f.readline().strip()], {
            line[:3]: [line[7:10], line[12:15]] for line in f if "=" in line
        }


def get_steps(c, ins, nodes, single=True):
    step = 0
    while (single and c != "ZZZ") or (not single and c[-1] != "Z"):
        c = nodes[c][ins[step % len(ins)]]
        step += 1
    return step


def part1():
    return get_steps("AAA", *get_map())


def part2():
    # For each node XXA it takes b_i steps to get to XXZ, and a_i steps to get to XXZ again.
    # This means that there exists an x_i such that k = b_i + a_i*x_i for each i.
    # In other words, we have the system of equations:∀i, k ≡ b_i (mod a_i)

    # The puzzle makes it so steps(XXA,XXZ) = steps(XXZ,XXZ), thus ∀i, k ≡ 0 (mod a_i)
    # Integrating this assumption, let's denote n = instruction length,
    #   we can simply return n*Π(a_i/n), no need for LCM!

    # An alternative general solution is available in day_08_general.
    ins, nodes = get_map()
    answer = len(ins)
    for el in [get_steps(c, ins, nodes, False) for c in [k for k in nodes if k[-1] == "A"]]:
        answer *= el // len(ins)
    return answer


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
