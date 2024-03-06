def get_cave():
    with open("2022/data/day_16.txt") as f:
        cave = dict()
        flows = dict()
        with open("2022/data/day_16.txt") as f:
            for line in f:
                flow, tunnels = line.strip().split("; ")
                valve = line.split()[1]
                cave[valve] = tunnels.replace("valves", "valve").split("valve ")[1].split(", ")
                flows[valve] = int(flow.split("=")[1])
        # Rename the valves with flow > 0 to specific set bits
        names = dict()
        for valve in list(cave):
            if flows[valve] > 0:
                name = 2 ** len(names)
                names[valve] = name
                flows[name] = flows.pop(valve)
                cave[name] = cave.pop(valve)
        for start, ends in cave.items():
            cave[start] = [names[end] if end in names else end for end in ends]

        return cave, flows


def shortest_dist(graph, start, end):
    visited = set()
    queue = [(start, 0)]
    while queue:
        visit, dist = queue.pop(0)
        if visit == end:
            return dist
        for tunnel in graph[visit]:
            if tunnel not in visited:
                visited.add(tunnel)
                queue.append((tunnel, dist + 1))


def get_distances(cave, flows):
    return {
        start: {end: shortest_dist(cave, start, end) for end in cave if flows[end] > 0 and end != start}
        for start in cave
        if start == "AA" or flows[start] > 0
    }


def simulate(current, timer, distances, flows):
    cache = dict()
    pruning = dict()
    best = 0
    stack = []
    stack.append((current, timer, 0, 0))
    while stack:
        current, timer, opened, total_flow = stack.pop()
        best = max(best, total_flow)
        if opened not in cache or total_flow > cache[opened]:
            cache[opened] = total_flow
        if (current, opened) in pruning and pruning[(current, opened)] > total_flow:
            continue
        pruning[(current, opened)] = total_flow

        for valve, distance in distances[current].items():
            if valve & opened:
                continue
            if (total_time := timer - distance - 1) < 0:
                continue
            stack.append((valve, total_time, opened + valve, total_flow + total_time * flows[valve]))
    return best, cache


def part1():
    cave, flows = get_cave()
    dist = get_distances(cave, flows)
    best_dist, _ = simulate("AA", 30, dist, flows)
    return best_dist


def part2():
    cave, flows = get_cave()
    dist = get_distances(cave, flows)
    _, cache = simulate("AA", 26, dist, flows)

    # Search for the best disjointed combo of valve in the cache
    return max(
        own_flow + elephant_flow
        for own, own_flow in cache.items()
        for elephant, elephant_flow in cache.items()
        if not own & elephant
    )


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
