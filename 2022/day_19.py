def get_bluprints():
    blueprints = []
    with open("2022/data/day_19.txt") as f:
        for line in f:
            line = line.strip(".\n").split(": ")[1].split(". ")
            test = [(el.split()[1], el.split("costs ")[1].split(" and ")) for el in line]
            for robot_type, ressources in test:
                ore = clay = obsidian = 0
                for needed in ressources:
                    cnt, ressource = needed.split()
                    if ressource == "ore":
                        ore = int(cnt)
                    elif ressource == "clay":
                        clay = int(cnt)
                    elif ressource == "obsidian":
                        obsidian = int(cnt)
                cost = (ore, clay, obsidian, 0)
                if robot_type == "ore":
                    ore_cost = cost
                elif robot_type == "clay":
                    clay_cost = cost
                elif robot_type == "obsidian":
                    obsidian_cost = cost
                elif robot_type == "geode":
                    geode_cost = cost
            blueprints.append((ore_cost, clay_cost, obsidian_cost, geode_cost))
    return blueprints


blueprints = get_bluprints()


class Res:
    ORE = 0
    CLAY = 1
    OBSIDIAN = 2
    GEODE = 3
    count = 3


def ceil(n):
    d, m = divmod(n, 1)
    return int(d) + (m > 0)


def add(v1, v2):
    return tuple([a + b for a, b in zip(v1, v2)])


def sub(v1, v2):
    return tuple([a - b for a, b in zip(v1, v2)])


def mult_scal(a, v):
    return tuple([a * vi for vi in v])


def eta_cost(inv, robots, robot_cost):
    """Returns the amount of time necessary to gather enough for robot_cost given current robots and inventory"""
    time_wait = 0
    for k in range(Res.count):
        if robot_cost[k] > 0:
            if robots[k] == 0:
                return float("inf")
            else:
                time_wait = max(time_wait, ceil((robot_cost[k] - inv[k]) / robots[k]))
    return time_wait


def max_geodes(blueprints, time):
    for blueprint in blueprints:
        ressources_max = [max(blueprint, key=lambda x: x[k])[k] for k in range(4)]
        best = 0
        cache = dict()
        stack = [(time, 0, (0, 0, 0, 0), (1, 0, 0, 0))]
        while stack:
            timer, geodes, inv, robots = stack.pop()
            best = max(best, geodes)
            # Prune if current permutation is not optimal
            if robots in cache and cache[robots] > timer:
                continue
            cache[robots] = timer
            # Prune if max possible geode < best:
            max_geode_robot = timer - 1
            if inv[Res.GEODE] + robots[Res.GEODE] * timer + max_geode_robot * (max_geode_robot + 1) / 2 < best:
                continue
            # Prune if there is no time to benefit from building anything
            if timer <= 1:
                continue
            for res, robot_cost in enumerate(reversed(blueprint)):
                res = Res.count - res
                # Prune if the ore robot does not have time to be profitable (costs more than what it will eventually make):
                if res == Res.ORE and timer < robot_cost[Res.ORE]:
                    continue
                # Prune if the number of robots of that type is already enough to cover all builds:
                if res != Res.GEODE and robots[res] >= ressources_max[res]:
                    continue
                wait = eta_cost(inv, robots, robot_cost)
                if timer - wait > 0:
                    new_robots = robots[:res] + (robots[res] + 1,) + robots[res + 1 :]
                    new_inventory = sub(add(mult_scal(wait + 1, robots), inv), robot_cost)
                    new_geodes = geodes + (timer - wait - 1) * (res == Res.GEODE)
                    stack.append((timer - wait - 1, new_geodes, new_inventory, new_robots))
        yield best


def part1():
    return sum(id_num * best for id_num, best in enumerate(max_geodes(blueprints, 24), 1))


def part2():
    prod = 1
    for best in max_geodes(blueprints[:3], 32):
        prod *= best
    return prod


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
