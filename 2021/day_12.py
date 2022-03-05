def part1():

    def create_cave(a, b):
        if a in graph:
            graph[a].append(b)
        else:
            graph[a] = [b]

    def search(vertex: str, path_so_far=None):
        if path_so_far is None:
            path_so_far = []

        # Visit cave
        path_so_far += [vertex]
        # If end reached, append to the list of paths
        if vertex == "end":
            paths.append(list(path_so_far))

        for next_vertex in graph[vertex]:
            # Don't visit the same small cave twice
            if not (next_vertex.islower() and next_vertex in path_so_far):
                search(next_vertex, list(path_so_far))

    graph: dict[str, str] = {}
    paths: list[list[str]] = []

    with open("2021/data/day_12.txt") as f:
        for line in f:
            connection = line.strip().split("-")
            # Graph construction
            create_cave(connection[0], connection[1])
            create_cave(connection[1], connection[0])

        # Depth search
        search("start")

    print(len(paths))


def part2():
    def create_cave(a, b):
        if a in graph:
            graph[a].append(b)
        else:
            graph[a] = [b]

    def search(vertex: str, path_so_far=None):
        if path_so_far is None:
            path_so_far = []

        # Visit cave
        path_so_far += [vertex]
        # If end reached, append to the list of paths
        if vertex == "end":
            paths.append(list(path_so_far))
            # print(paths)

        for next_vertex in graph[vertex]:
            # Count nb of small cave visited
            nb_small = {
                cave: path_so_far.count(cave)
                for cave in path_so_far if cave.islower()}
            # list all visited more than once
            visited = [value for value in nb_small.values() if value > 1]
            # Nb visited more than once
            multi_visited = len(visited)

            single_visited = 0
            if visited:
                # Max time a small cave has been visited
                single_visited = max(visited)

            if (multi_visited < 2 and single_visited < 3 and
                    "end" not in path_so_far and next_vertex != "start"):
                search(next_vertex, list(path_so_far))

    graph: dict[str, str] = {}
    paths: list[list[str]] = []

    with open("2021/data/day_12.txt") as f:
        for line in f:
            connection = line.strip().split("-")
            # Graph construction
            create_cave(connection[0], connection[1])
            create_cave(connection[1], connection[0])

        # Depth search
        search("start")

    print(len(paths))


if __name__ == '__main__':
    part1()
    part2()
