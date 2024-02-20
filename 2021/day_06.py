def get_school_ini():
    with open("2021/data/day_06.txt") as f:
        fishes = (int(age) for age in f.read().strip().split(","))
    school = [0 for _ in range(9)]
    for timer in fishes:
        school[timer] += 1
    return school


def count_fishes(sc, days):
    for _ in range(1, days + 1):
        sc = [sc[1], sc[2], sc[3], sc[4], sc[5], sc[6], sc[0] + sc[7], sc[8], sc[0]]
    return sum(sc)


def part1():
    return count_fishes(get_school_ini(), 80)


def part2():
    return count_fishes(get_school_ini(), 256)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
