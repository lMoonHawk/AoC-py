def part1():
    with open("2019/data/day_01.txt") as f:
        return sum(int(line.strip()) // 3 - 2 for line in f.readlines())


def part2():
    with open("2019/data/day_01.txt") as f:
        total_fuel = 0
        for line in f:
            module_fuel = int(line.strip()) // 3 - 2
            while module_fuel > 0:
                total_fuel += module_fuel
                module_fuel = module_fuel // 3 - 2
    return total_fuel


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
