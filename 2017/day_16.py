with open("2017/data/day_16.txt") as f:
    dance = f.readline().strip().split(",")


def dance_round(programs):
    for move in dance:
        if move[0] == "s":
            val = int(move[1:])
            programs[:-val:], programs[-val:] = programs[-val:], programs[:-val]
        elif move[0] == "x":
            p1, p2 = [int(el) for el in move[1:].split("/")]
            programs[p1], programs[p2] = programs[p2], programs[p1]
        elif move[0] == "p":
            p1, p2 = [programs.index(el) for el in move[1:].split("/")]
            programs[p1], programs[p2] = programs[p2], programs[p1]
    return "".join(programs)


def part1():
    return dance_round([chr(97 + k) for k in range(112 - 97 + 1)])


def part2():
    programs = [chr(97 + k) for k in range(112 - 97 + 1)]
    cycles = ["".join(programs)]
    for _ in range(1_000_000_000):
        order = dance_round(programs)
        if order == cycles[0]:
            return cycles[(1_000_000_000 - len(cycles)) % len(cycles)]
        cycles.append(order)
    return order


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
