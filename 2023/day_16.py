with open("2023/data/day_16.txt") as f:
    grid = [list(line.strip()) for line in f.readlines()]


def send_light(grid, start):
    directions = {0: (0, -1), 1: (1, 0), 2: (0, 1), 3: (-1, 0)}
    visited = set()
    beams = [start]
    while beams:
        x, y, rot = beams.pop()
        if (x, y, rot) in visited:
            continue
        visited.add((x, y, rot))

        mx, my = directions[rot]
        nx, ny = x + mx, y + my
        if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
            sq = grid[ny][nx]
            if sq == ".":
                beams.append((nx, ny, rot))
            elif sq in ["-", "|"]:
                if (sq == "-" and rot in [1, 3]) or (sq == "|" and rot in [0, 2]):
                    beams.append((nx, ny, rot))
                else:
                    beams.append((nx, ny, (rot + 1) % 4))
                    beams.append((nx, ny, (rot - 1) % 4))
            elif (sq == "\\" and rot in [1, 3]) or (sq == "/" and rot in [0, 2]):
                beams.append((nx, ny, (rot + 1) % 4))
            elif (sq == "\\" and rot in [0, 2]) or (sq == "/" and rot in [1, 3]):
                beams.append((nx, ny, (rot - 1) % 4))

    return len(set((x, y) for x, y, _ in visited)) - 1


def part1():
    return send_light(grid, (-1, 0, 1))


def part2():
    max_v = max(max(send_light(grid, (-1, y, 1)), send_light(grid, (len(grid[0]), y, 3))) for y in range(len(grid)))
    max_h = max(max(send_light(grid, (x, -1, 2)), send_light(grid, (x, len(grid), 0))) for x in range(len(grid[0])))
    return max(max_v, max_h)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
