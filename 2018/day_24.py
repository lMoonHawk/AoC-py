class Group:
    def __init__(self, team, size, hp, atk_type, atk, initiative, weak, immune, target=None, targeted=False):
        self.team = team
        self.size = size
        self.hp = hp
        self.atk_type = atk_type
        self.atk = atk
        self.initiative = initiative
        self.weak = weak
        self.immune = immune
        self.target = target
        self.targeted = targeted

    def power(self):
        return self.size * self.atk

    def get_damage(self, defender):
        if self.atk_type in defender.immune:
            return 0
        modifier = 1 if self.atk_type not in defender.weak else 2
        return self.power() * modifier

    def get_target(self, groups):
        remaining = [group for group in groups if group.team != self.team and not group.targeted]
        if remaining:
            defender = max(remaining, key=lambda x: (self.get_damage(x), x.power(), x.initiative))
            if self.get_damage(defender) > 0:
                self.target = defender
                self.target.targeted = True


def get_groups():
    groups = []
    army = -1
    with open("2018/data/day_24.txt") as f:
        for line in f:
            if line == "\n":
                continue
            elif ":" in line:
                army += 1
                continue
            line = line.strip()
            size = int(line.split(" unit")[0])
            hp = int(line.split(" hit")[0].split("with ")[1])
            atk, atk_type = line.split(" damage")[0].split("does ")[1].split()
            atk = int(atk)
            initiative = int(line.split()[-1])
            immune, weak = [], []
            if "(" in line:
                details = line.split(")")[0].split("(")[1].split("; ")
                for detail in details:
                    if detail.split()[0] == "immune":
                        immune = detail.replace("immune to ", "").split(", ")
                    elif detail.split()[0] == "weak":
                        weak = detail.replace("weak to ", "").split(", ")
            groups.append(Group(army, size, hp, atk_type, atk, initiative, weak, immune))
    return groups


def simulate_combat(groups, boost=0):
    for group in groups:
        if group.team == 0:
            group.atk += boost
    while True:
        teams = [group.team for group in groups]

        if not (0 in teams and 1 in teams):
            return not groups[0].team, sum(group.size for group in groups)

        groups.sort(key=lambda x: (-x.power(), -x.initiative))
        for group in groups:
            group.get_target(groups)

        groups.sort(key=lambda x: -x.initiative)
        stalemate = True
        for attacker in groups:
            if attacker.size <= 0:
                continue
            if not attacker.target:
                continue
            defender = attacker.target
            damage = attacker.get_damage(defender)
            unit_lost = damage // defender.hp
            if unit_lost > 0:
                stalemate = False
            defender.size = defender.size - damage // defender.hp
            attacker.target, defender.targeted = None, False
            if defender.size <= 0:
                if defender.target:
                    defender.target.targeted = False

        groups = [group for group in groups if group.size > 0]
        if stalemate:
            return False, None


def part1():
    _, size = simulate_combat(get_groups())
    return size


def part2():
    boost = 1
    hi = None
    while True:
        win, size = simulate_combat(get_groups(), boost)

        if win:
            if boost == lo + 1:
                return size
            hi = boost
            boost = (hi + lo) // 2 + 1
        else:
            lo = boost
            if not hi:
                boost *= 2
            else:
                boost = (hi + lo) // 2 + 1


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
