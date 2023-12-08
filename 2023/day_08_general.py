def get_map():
    with open("2023/data/day_08.txt") as f:
        return [d == "R" for d in f.readline().strip()], {
            line[:3]: [line[7:10], line[12:15]] for line in f if "=" in line
        }


def ext_euclide(a: int, b: int) -> tuple[int, int]:
    """Extended euclide algorithm, returning u, v from the Bézout's identity a*u + b*v = gcd(a,b)"""
    if a == 0:
        return 0, 1
    x1, y1 = ext_euclide(b % a, a)
    x, y = y1 - (b // a) * x1, x1
    return x, y


def crt(congruences, moduli):
    m_tot = 1
    for i in moduli:
        m_tot *= i
    t = 0
    for c_i, n_i in zip(congruences, moduli):
        n_hat_i = m_tot // n_i
        t += (c_i * n_hat_i * ext_euclide(n_i, n_hat_i)[1]) % m_tot
    return t if t else m_tot


def get_steps(current_node, nodes, instructions, single=True):
    step = 0
    while (single and current_node != "ZZZ") or (not single and current_node[-1] != "Z"):
        current_node = nodes[current_node][instructions[step % len(instructions)]]
        step += 1
    return current_node, step


def part1():
    instructions, nodes = get_map()
    _, steps = get_steps("AAA", nodes, instructions)
    return steps


def part2():
    # For each node XXA it takes b_i steps to get to XXZ, and a_i steps to get to XXZ again.
    # This means that there exists an x_i such that k = b_i + a_i*x_i for each i.
    # In other words, we have the system of equations:∀i, k ≡ b_i (mod a_i)

    # Sure, the puzzle makes it so steps(XXA,XXZ) = steps(XXZ,XXZ), thus ∀i, k ≡ 0 (mod a_i)
    #   but we have a general* solution below *(as long as each a_i/instruction length are coprime)
    # Integrating this assumption, let's denote n = instruction length,
    #   we can simply return n*Π(a_i/n), no need for LCM!
    # This alternative solution is available in the function part2_simple()

    # We use the Chinese remainder theorem to answer the general case. This is overkill for our
    #   input since it returns the product of the modulus anyway.
    # The division by the length of instruction is necessary: pairs of a_i have to be coprime.
    # The number of steps to reach each end node has to be a full multiple of the instructions.

    instructions, nodes = get_map()
    current_nodes = [k for k in nodes if k[-1] == "A"]
    moduli, congruences = [], []
    for current_node in current_nodes:
        current_node, steps = get_steps(current_node, nodes, instructions, False)
        moduli.append(steps // len(instructions))
        congruences.append(steps + get_steps(current_node, nodes, instructions, False)[1])
    return crt(congruences, moduli) * len(instructions)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
    # print(f"Part 2 simple: {part2_simple()}")
