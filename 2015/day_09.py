with open("2015/data/day_09.txt") as f:
    dists = {frozenset(k.split(" to ")): int(v) for k, v in (line.split(" = ") for line in f)}
    locs = {loc for pair in dists for loc in pair}


def get_steps(dists, locs, fun):
    stack = [(loc, 0, {loc}) for loc in locs]
    out_dist = None
    while stack:
        loc, dist, path = stack.pop()
        remaining = [loc for loc in locs if loc not in path]
        if not remaining:
            out_dist = fun(out_dist, dist) if out_dist is not None else dist
        for n_loc in remaining:
            stack.append((n_loc, dist + dists[frozenset([loc, n_loc])], path | {n_loc}))
    return out_dist


def part1():
    return get_steps(dists, locs, min)


def part2():
    return get_steps(dists, locs, max)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
