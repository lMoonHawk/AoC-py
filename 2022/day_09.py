with open("2022/data/day_09.txt") as f:
    movements = [line.split() for line in f]


def rope(size):
    directions = {"R": (0, 1), "D": (-1, 0), "L": (0, -1), "U": (1, 0)}
    visited = set()
    positions = [(0, 0) for _ in range(size)]
    for motion, count in movements:
        my, mx = directions[motion]
        for _ in range(int(count)):
            y, x = positions[0]
            positions[0] = y + my, x + mx
            for i in range(1, size):
                (y, x), (py, px) = positions[i], positions[i - 1]
                rel_y, rel_x = y - py, x - px
                if not ((-1 <= rel_y <= 1) and (-1 <= rel_x <= 1)):
                    m_y = 1 if rel_y < 0 else -1 if rel_y > 0 else 0
                    m_x = 1 if rel_x < 0 else -1 if rel_x > 0 else 0
                    positions[i] = y + m_y, x + m_x
            visited.add(positions[-1])
    return len(visited)


def part1():
    return rope(2)


def part2():
    return rope(10)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
