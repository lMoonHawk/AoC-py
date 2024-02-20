with open("2021/data/day_07.txt") as f:
    positions = [int(pos) for pos in f.read().split(",")]


def part1():
    ordered = sorted(positions)
    n = len(positions)
    median = ordered[n // 2] if n % 2 else (ordered[n // 2 - 1] + ordered[n // 2]) // 2
    return sum(abs(median - position) for position in positions)


def part2():
    lo_coord = hi_coord = sum(positions) // len(positions)
    lo_fuel = hi_fuel = None
    min_fuel = None

    while True:
        lo_fuel = sum((1 + abs(position - lo_coord)) * abs(position - lo_coord) // 2 for position in positions)
        hi_fuel = sum((1 + abs(position - hi_coord)) * abs(position - hi_coord) // 2 for position in positions)
        current_min = min(lo_fuel, hi_fuel)
        min_fuel = current_min if min_fuel is None or current_min < min_fuel else min_fuel
        # Test for global minimum (current minimum is lower than bounds)
        if min_fuel < lo_fuel and min_fuel < hi_fuel:
            return min_fuel
        lo_coord -= 1
        hi_coord += 1


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
