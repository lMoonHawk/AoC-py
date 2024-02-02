with open("2016/data/day_24.txt") as f:
    layout = [line.strip() for line in f]
    poi = {sq: (x, y) for y, row in enumerate(layout) for x, sq in enumerate(row) if sq.isdigit()}


def traverse(go_back=False):
    x, y = poi["0"]
    goal = 2 ** len(poi) - 1
    state = 1 if not go_back else 0
    queue = [(x, y, state, 0)]
    visited = {(x, y, 0)}
    while queue:
        x, y, state, steps = queue.pop(0)
        for nx, ny in [(x, y + 1), (x + 1, y), (x - 1, y), (x, y - 1)]:
            if not (0 <= nx < len(layout[0]) and 0 <= ny < len(layout)) or layout[ny][nx] == "#":
                continue
            if (nx, ny, state) in visited:
                continue
            visited.add((nx, ny, state))
            new_state = state
            if layout[ny][nx] in poi:
                if go_back and layout[ny][nx] == "0" and state != goal - 1:
                    continue
                new_state |= 1 << (int(layout[ny][nx]))
                if new_state == goal:
                    return steps + 1
            queue.append((nx, ny, new_state, steps + 1))


def part1():
    return traverse()


def part2():
    return traverse(go_back=True)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
