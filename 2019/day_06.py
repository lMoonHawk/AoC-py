with open("2019/data/day_06.txt") as f:
    orbits = {o[1]: o[0] for o in [line.strip().split(")") for line in f.readlines()]}


def part1():
    answer = 0
    for _, around in orbits.items():
        answer += 1
        while around != "COM":
            around = orbits[around]
            answer += 1
    return answer


def traverse(graph: dict, start="YOU", end="SAN"):
    start_obj = graph[start][0]
    queue = [(start_obj, 0)]
    visited = set()

    while queue:
        obj, steps = queue.pop(0)
        for next_obj in graph[obj]:
            if next_obj == end:
                return steps
            if next_obj not in visited:
                queue.append((next_obj, steps + 1))
                visited.add(next_obj)


def part2():
    orbit_graph = dict()
    for obj1, obj2 in orbits.items():
        if obj1 not in orbit_graph:
            orbit_graph[obj1] = []
        if obj2 not in orbit_graph:
            orbit_graph[obj2] = []

        orbit_graph[obj1].append(obj2)
        orbit_graph[obj2].append(obj1)
    return traverse(orbit_graph)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
