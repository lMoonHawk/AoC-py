with open("2017/data/day_24.txt") as f:
    components = [tuple([int(el) for el in line.strip().split("/")]) for line in f]


def max_strength(port, strength, components):
    best = 0
    none_left = True
    for c, component in enumerate(components):
        if port in component:
            none_left = False
            next_port = component[1 - component.index(port)]
            branch = max_strength(next_port, sum(component), components[:c] + components[c + 1 :])
            if branch > best:
                best = branch
    if none_left:
        return strength
    return best + strength


def longest(port, strength, components):
    best = 0, 0
    none_left = True
    for c, component in enumerate(components):
        if port in component:
            none_left = False
            next_port = component[1 - component.index(port)]
            branch = longest(next_port, sum(component), components[:c] + components[c + 1 :])
            best = max(best, branch)
    if none_left:
        return 0, strength
    best_len, best_str = best
    return best_len + 1, best_str + strength


def part1():
    return max_strength(0, 0, components)


def part2():
    _, strength = longest(0, 0, components)
    return strength


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
