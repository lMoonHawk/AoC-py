with open("2015/data/day_18.txt") as f:
    lights_init = {(x, y) for y, row in enumerate(f) for x, light in enumerate(row.strip()) if light == "#"}


def cnt_neigh_lights(x, y, lights):
    count = 0
    for ny in range(y - 1, y + 2):
        for nx in range(x - 1, x + 2):
            if (nx, ny) != (x, y) and (nx, ny) in lights:
                count += 1
    return count


def animate_step(lights):
    new_lights = set()
    for x, y in ((nx, ny) for nx in range(100) for ny in range(100)):
        neigh_lights = cnt_neigh_lights(x, y, lights)
        if (x, y) in lights and 2 <= neigh_lights <= 3:
            new_lights.add((x, y))
        elif (x, y) not in lights and neigh_lights == 3:
            new_lights.add((x, y))
    return new_lights


def part1():
    lights = lights_init
    for _ in range(100):
        lights = animate_step(lights)
    return len(lights)


def part2():
    corners = {(0, 0), (0, 99), (99, 99), (99, 0)}
    lights = lights_init
    lights.update(corners)
    for _ in range(100):
        lights = animate_step(lights)
        lights.update(corners)
    return len(lights)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
