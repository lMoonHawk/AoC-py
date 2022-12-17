def path(start, end):
    visited = set()
    queue = [[start, 0]]

    while queue:
        visit, dist = queue.pop(0)
        if visit == end:
            return dist
        for tunnel in cave[visit]:
            if tunnel not in visited:
                visited.add(tunnel)
                queue.append([tunnel, dist + 1])


cave = dict()
flows = dict()
with open("2022/data/day_16.txt") as f:
    for line in f:
        flow, tunnels = line.strip().split("; ")
        valve = line[6:8]
        flow = int(flow.split("=")[1])
        tunnels = (
            tunnels.replace("valves", "valve").split("valve ")[1].split(", ")
        )
        cave[valve] = tunnels
        flows[valve] = flow

# Distances from all valve to all other
distances = dict()
for start in cave:
    distances[start] = dict()
    for end in cave:
        distances[start][end] = path(start, end)


def part1():
    def simulate(current, opened=None, time=0):
        if opened is None:
            opened = set()

        best_total = 0
        total = 0
        for valve, distance in distances[current].items():
            if valve in opened or flows[valve] == 0:
                continue
            total_time = distance + 1 + time
            if total_time <= 30:
                current_opened = opened.union([valve])
                flow = (30 - total_time) * flows[valve]
                total = flow + simulate(valve, current_opened, total_time)
                if total > best_total:
                    best_total = total

        return best_total

    print(simulate("AA"))


def part2():
    pass


if __name__ == "__main__":
    part1()
    part2()
