def init_flat_pairs():
    materials = dict()
    with open("2016/data/day_11.txt") as f:
        for floor, line in enumerate(f):
            if "nothing" in line:
                continue
            items = (
                item.split()
                for item in line.strip()
                .strip(".")
                .replace("contains", ",")
                .replace(" a ", " ")
                .replace("-compatible", "")
                .replace(", and", " and")
                .replace(" and", ",")
                .split(", ")[1:]
            )
            for material, item in items:
                if material not in materials:
                    materials[material] = [None, None]
                materials[material][item == "generator"] = floor + 1
    return [floor for pair in materials.values() for floor in pair]


def is_valid_state(state):
    gen_floors = [gen_floor for _, gen_floor, _ in state]
    return not any(chip_floor != gen_floor and chip_floor in gen_floors for chip_floor, gen_floor, _ in state)


def get_state(d):
    """Returns the current state from a flatten list of pairs.
    {(floor chip, floor gen, # pairs), ...}"""
    pairs = [tuple([d[k], d[k + 1]]) for k in range(0, len(d) - 1, 2)]
    return frozenset([tuple([chip, gen, pairs.count((chip, gen))]) for chip, gen in set(pairs)])


def flatten_state(state):
    """Returns the flatten list of pairs from a state.
    [floor chip type 1, floor gen type 1, floor chip type 2, floor gen type 2, ...]"""
    pairs = []
    for floor_chip, floor_gen, count in state:
        for _ in range(count):
            pairs.extend([floor_chip, floor_gen])
    return pairs


def possible_floors(elevator):
    if elevator != 4:
        yield elevator + 1
    if elevator != 1:
        yield elevator - 1


def possible_moves(elevator, state):
    """Generates possible moves from an elevator position given a state."""
    flat_pairs = flatten_state(state)
    seen = set()
    for i in range(len(flat_pairs) - 1):
        if flat_pairs[i] != elevator:
            continue
        for floor in possible_floors(elevator):
            move = flat_pairs.copy()
            move[i] = floor
            new_state = get_state(move)
            if new_state not in seen and is_valid_state(new_state):
                yield floor, new_state
                seen.add(new_state)
        for j in range(i, len(flat_pairs)):
            if flat_pairs[j] != elevator:
                continue
            for floor in possible_floors(elevator):
                move = flat_pairs.copy()
                move[i] = move[j] = floor
                new_state = get_state(move)
                if new_state not in seen and is_valid_state(new_state):
                    yield floor, new_state
                    seen.add(new_state)


def is_goal(state):
    if len(state) == 1:
        ((floor_chip, floor_gen, _),) = state
        if floor_chip == floor_gen == 4:
            return True
    return False


def get_min_steps(state):
    elevator, steps = 1, 0
    queue = [(elevator, state, steps)]
    seen = set([(elevator, state)])
    while queue:
        elevator, state, steps = queue.pop(0)
        if is_goal(state):
            return steps
        for floor, new_state in possible_moves(elevator, state):
            if (floor, new_state) in seen:
                continue
            seen.add((floor, new_state))
            queue.append((floor, new_state, steps + 1))


def part1():
    state = get_state(init_flat_pairs())
    return get_min_steps(state)


def part2():
    state = get_state(init_flat_pairs() + [1, 1] + [1, 1])
    return get_min_steps(state)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
