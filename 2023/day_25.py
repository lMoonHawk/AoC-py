def get_components():
    components = dict()
    with open("2023/data/day_25.txt") as f:
        for line in f:
            k, *v = line.strip().replace(":", "").split()
            if k not in components:
                components[k] = []
            components[k].extend(v)
            for comp in v:
                if comp not in components:
                    components[comp] = []
                components[comp].append(k)
    return components


def random(seed=42):
    """Lehmer random number generator"""
    while True:
        seed = (7**5 * seed) % ((2**31) - 1)
        yield seed


def ceil(n):
    return int(n) + ((n - int(n)) > 0)


def contract(graph, t, rand):
    """Return a contracted graph with t vertices"""
    graph_out = {k: v[:] for k, v in graph.items()}
    while len(graph_out) > t:
        v1 = list(graph_out)[next(rand) % len(graph_out)]
        v2 = graph_out[v1][next(rand) % len(graph_out[v1])]
        v12 = f"{v1}+{v2}"

        graph_out[v12] = [
            *[g for g in graph_out[v1] if g not in [v1, v2]],
            *[g for g in graph_out[v2] if g not in [v1, v2]],
        ]
        del graph_out[v1]
        del graph_out[v2]

        for k in graph_out:
            while v1 in graph_out[k]:
                graph_out[k][graph_out[k].index(v1)] = f"{v1}+{v2}"
            while v2 in graph_out[k]:
                graph_out[k][graph_out[k].index(v2)] = f"{v1}+{v2}"
    return graph_out


def fastmincut(components, rand):
    """Karger-Stein implementation of the minimum cut problem.
    Contract the graph until we have t vertices, then pick the best cuts.
    The idea is that two randomly selected two vertices have a high probablity of being in the same group.
    https://en.wikipedia.org/wiki/Karger%27s_algorithm"""
    t = ceil(1 + len(components) / (2**0.5))
    if len(components) <= 6:
        return contract(components, 2, rand)
    else:
        components1 = contract(components, t, rand)
        components2 = contract(components, t, rand)
        if len(list(components1.values())[0]) < len(list(components2.values())[0]):
            return fastmincut(components1, rand)
        return fastmincut(components2, rand)


def part1():
    rand = random()
    components_ini = get_components()
    while True:
        components = fastmincut(components_ini, rand)
        if len(list(components.values())[0]) == 3:
            groups = [len(k.split("+")) for k in components]
            return groups[0] * groups[1]


def part2():
    return None


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
