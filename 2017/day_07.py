supports = dict()
weights = dict()
with open("2017/data/day_07.txt") as f:
    for line in f:
        name, weight = line.strip().split(" ")[:2]
        weights[name] = int(weight[1:-1])
        if "->" in line:
            supports[name] = line.strip().split("-> ")[1].split(", ")


def get_bottom(supports):
    supported = {el for v in supports.values() for el in v}
    (out,) = set(supports) - supported
    return out


def check_weights(program, supports, weights):
    if program not in supports:
        return True, weights[program], 0

    sub_total_weights = []
    sub_program_weights = []
    for sub_program in supports[program]:
        matching, sub_weight, sub_carry = check_weights(sub_program, supports, weights)
        if not matching:
            return False, sub_weight, 0
        sub_total_weights.append(sub_weight + sub_carry)
        sub_program_weights.append(sub_weight)

    if len(set(sub_total_weights)) == 1:
        return True, weights[program], sum(sub_total_weights)

    wrong_tot_weigth = [sub_weight for sub_weight in sub_total_weights if sub_total_weights.count(sub_weight) == 1][0]
    correct_tot_weigth = [sub_weight for sub_weight in sub_total_weights if sub_total_weights.count(sub_weight) > 1][0]
    correct = sub_program_weights[sub_total_weights.index(wrong_tot_weigth)] + correct_tot_weigth - wrong_tot_weigth
    return False, correct, 0


def part1():
    return get_bottom(supports)


def part2():
    _, answer, _ = check_weights(get_bottom(supports), supports, weights)
    return answer


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
