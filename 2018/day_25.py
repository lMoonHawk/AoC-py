with open("2018/data/day_25.txt") as f:
    points = [tuple([int(c) for c in line.strip().split(",")]) for line in f.readlines()]


def traverse(graph, p1, visited):
    visited.add(p1)
    return 1 + sum(traverse(graph, p2, visited) for p2 in graph[p1] if p2 not in visited)


def part1():
    graph = {p: [] for p in points}
    for k, p1 in enumerate(points[:-1]):
        for p2 in points[k + 1 :]:
            if sum(abs(p1_i - p2_i) for p1_i, p2_i in zip(p1, p2)) <= 3:
                graph[p1].append(p2)
                graph[p2].append(p1)
    visited = set()
    return len([traverse(graph, p, visited) for p in points if p not in visited])


def part2():
    return


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
