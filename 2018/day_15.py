def initialize_combat(elf_attack=3):
    with open("2018/data/day_15.txt") as f:
        area = [list(line.strip()) for line in f.readlines()]
    units = []
    for y, row in enumerate(area):
        for x, sq in enumerate(row):
            if sq in ["E", "G"]:
                unit = Unit(y, x, team=sq == "E", hp=200, attack=elf_attack if sq == "E" else 3)
                units.append(unit)
                area[y][x] = unit
    return area, units


class Unit:
    def __init__(self, y, x, team, hp, attack):
        self.y = y
        self.x = x
        self.team = team
        self.hp = hp
        self.attack = attack

    def __lt__(self, other):
        return (self.y, self.x) < (other.y, other.x)

    def target_in_reach(self, area):
        chosen = None
        for my, mx in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            ny, nx = self.y + my, self.x + mx
            if isinstance(area[ny][nx], Unit):
                target = area[ny][nx]
                if target.team != self.team and target.hp > 0:
                    if not chosen or target.hp < chosen.hp:
                        chosen = target
        return None if not chosen else chosen

    def move_to_target(self, area):
        visited = set()
        queue = [(self.y, self.x, 0, ())]
        candidates = []
        min_steps = None
        while queue:
            y, x, steps, first_step = queue.pop(0)
            if min_steps is not None and steps > min_steps - 1:
                return min_steps - 1, min(candidates)[1]

            for my, mx in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                ny, nx = y + my, x + mx

                if (ny, nx) in visited:
                    continue
                visited.add((ny, nx))

                nfirst_step = first_step
                if not first_step:
                    nfirst_step = my, mx

                if area[ny][nx] == "#":
                    continue

                if isinstance(area[ny][nx], Unit) and area[ny][nx].hp > 0:
                    if area[ny][nx].team != self.team:
                        candidates.append(((y, x), first_step))
                        if min_steps is None:
                            min_steps = steps + 1
                    else:
                        continue
                queue.append((ny, nx, steps + 1, nfirst_step))
        return None, None


def move_unit(area, unit, my, mx):
    area[unit.y][unit.x] = "."
    unit.y += my
    unit.x += mx
    area[unit.y][unit.x] = unit


def simulate_battle(area, units, no_elf_death=False):
    rounds = 0
    while True:
        for unit in units:
            if unit.hp <= 0:
                if no_elf_death and unit.team:
                    return None
                continue

            if all(enemy.hp <= 0 for enemy in units if enemy.team != unit.team):
                return rounds * sum(alive.hp for alive in units if alive.hp > 0)

            if target := unit.target_in_reach(area):
                target.hp -= unit.attack
            else:
                steps, first_step = unit.move_to_target(area)
                if not steps:
                    continue
                move_unit(area, unit, *first_step)
                if steps == 1:
                    unit.target_in_reach(area).hp -= unit.attack

        units.sort()
        rounds += 1


def part1():
    return simulate_battle(*initialize_combat())


def part2():
    elf_attack = 4
    while True:
        outcome = simulate_battle(*initialize_combat(elf_attack), no_elf_death=True)
        if not outcome:
            elf_attack += 1
        else:
            return elf_attack, outcome


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
