def dict_append(d, k, v):
    if k not in d:
        d[k] = []
    d[k].append(v)


graph = dict()
with open("2021/data/day_12.txt") as f:
    for line in f:
        c1, c2 = line.strip().split("-")
        dict_append(graph, c1, c2)
        dict_append(graph, c2, c1)


def traverse(graph, node, small_cave_quota, visited=None):
    if visited is None:
        visited = set()
    if node == "end":
        return 1
    if node.islower():
        visited.add(node)
    paths = 0
    for subnode in graph[node]:
        new_quota = small_cave_quota
        if subnode in visited:
            if new_quota == 0 or subnode == "start":
                continue
            new_quota -= 1
        paths += traverse(graph, subnode, new_quota, visited.copy())
    return paths


def part1():
    return traverse(graph, node="start", small_cave_quota=0)


def part2():
    return traverse(graph, node="start", small_cave_quota=1)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
