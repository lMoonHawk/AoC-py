reactions = dict()
# {"A"(chem) : [10 (batch size), {"ORE":10} (recipe)],
# "C":[1,{"A":7, "B":1}]}
with open("2019/data/day_14.txt") as f:
    for line in f:
        inputs, output = line.strip().split(" => ")

        output_count, output_chem = output.split(" ")
        inputs = {reac_i[1]: int(reac_i[0]) for reac_i in [i.split() for i in inputs.split(",")]}

        reactions[output_chem] = [int(output_count), inputs]


def get(d, k):
    return d[k] if k in d else 0


def req_ore(fuel):
    surplus = {}
    queue = [[fuel, "FUEL"]]
    total_ore = 0

    while queue:
        need, chem = queue.pop(0)

        if chem == "ORE":
            total_ore += need
            continue

        per_reaction, recipe = reactions[chem]
        reaction_count, m = divmod(need - get(surplus, chem), per_reaction)
        if m > 0:
            reaction_count += 1
            surplus[chem] = per_reaction - m
        elif m == 0:
            surplus[chem] = 0

        for sub_chem, sub_need in recipe.items():
            queue.append([sub_need * reaction_count, sub_chem])

    return total_ore


def part1():
    return req_ore(1)


def part2():
    unit = req_ore(1)
    prev_candidate, candidate = 0, 1_000_000_000_000 // unit

    while True:
        diff = 1_000_000_000_000 - req_ore(candidate)

        if prev_candidate == candidate:
            break
        prev_candidate = candidate
        candidate += diff // unit

    return candidate


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
