with open("2015/data/day_21.txt") as f:
    boss_hp, boss_dmg, boss_arm = [int(line.strip().split()[-1]) for line in f]

weapons = [(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)]
armors = [(0, 0, 0), (13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5)]
rings = [(0, 0, 0), (0, 0, 0), (25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3)]


def wins(hp, dmg, arm, boss_hp, boss_dmg, boss_arm):
    boss_ttk, boss_r = divmod(boss_hp, max(1, dmg - boss_arm))
    ttk, r = divmod(hp, max(1, boss_dmg - arm))
    if ttk + (r > 0) >= boss_ttk + (boss_r > 0):
        return True
    return False


def shop():
    for w_cost, w_dmg, w_arm in weapons:
        for a_cost, a_dmg, a_arm in armors:
            for r1, (r1_cost, r1_dmg, r1_arm) in enumerate(rings[:-1]):
                for r2_cost, r2_dmg, r2_arm in rings[r1 + 1 :]:
                    spent = w_cost + a_cost + r1_cost + r2_cost
                    dmg = w_dmg + a_dmg + r1_dmg + r2_dmg
                    arm = w_arm + a_arm + r1_arm + r2_arm
                    yield spent, dmg, arm


def part1():
    return min(spent for spent, dmg, arm in shop() if wins(100, dmg, arm, boss_hp, boss_dmg, boss_arm))


def part2():
    return max(spent for spent, dmg, arm in shop() if not wins(100, dmg, arm, boss_hp, boss_dmg, boss_arm))


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
