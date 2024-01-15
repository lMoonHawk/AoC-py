graph = dict()
with open("2017/data/day_12.txt") as f:
    for line in f:
        program, connections = line.strip().split(" <-> ")
        graph[program] = connections.split(", ")


def count_nodes(node, visited=set()):
    visited.add(node)
    return 1 + sum(count_nodes(program, visited) for program in graph[node] if program not in visited)


def part1():
    return count_nodes("0")


def part2():
    visited = set()
    return len([count_nodes(program, visited) for program in graph if program not in visited])


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
