with open("2015/data/day_22.txt") as f:
    boss_hp, boss_dmg = [int(line.strip().split(": ")[-1]) for line in f]


class Heap(list):
    def push(self, item):
        self.append(item)
        self.sift_up(len(self) - 1)

    def pop(self):
        self[-1], self[0] = self[0], self[-1]
        out = super().pop()
        if self:
            self.sift_down()
        return out

    def sift_up(self, pos):
        item = self[pos]
        while pos:
            parentpos = (pos - 1) // 2
            parent = self[parentpos]
            if item < parent:
                self[pos], pos = parent, parentpos
                continue
            break
        self[pos] = item

    def sift_down(self):
        n = len(self)
        pos = 0
        l_child_pos = min_child_pos = 1
        item = self[0]
        while l_child_pos < n:
            min_child_pos, r_child_pos = l_child_pos, l_child_pos + 1
            if r_child_pos < n and self[l_child_pos] > self[r_child_pos]:
                min_child_pos = r_child_pos
            self[pos] = self[min_child_pos]
            pos = min_child_pos
            l_child_pos = 2 * pos + 1
        self[pos] = item
        self.sift_up(pos)


spells = {"missile": (53, 0), "drain": (73, 0), "shield": (113, 6), "poison": (173, 6), "recharge": (229, 5)}


class State:
    def __init__(self, spent, hp, mana, armor, boss_hp, effects):
        self.spent = spent
        self.hp = hp
        self.mana = mana
        self.armor = armor
        self.boss_hp = boss_hp
        self.effects = effects

    def __lt__(self, other):
        return (self.spent, self.boss_hp, -self.hp) < (other.spent, other.boss_hp, -other.hp)


def trigger_effects(state):
    for effect, timer in state.effects:
        match effect:
            case "shield":
                if timer > 1:
                    state.armor = 7
                else:
                    state.armor = 0
            case "poison":
                state.boss_hp -= 3
            case "recharge":
                state.mana += 101
    state.effects = [(effect, timer - 1) for effect, timer in state.effects if timer - 1 > 0]
    return state.boss_hp


def is_killed(hp):
    return hp <= 0


def cast(spell, cost, timer, state):
    match spell:
        case "missile":
            state.boss_hp -= 4
        case "drain":
            state.boss_hp -= 2
            state.hp += 2
        case "shield" | "poison" | "recharge":
            state.effects.append((spell, timer))
    state.mana -= cost
    state.spent += cost
    return state.boss_hp


def win_least_mana(hard=False):
    state = State(0, 50, 500, 0, boss_hp, [])
    pq = Heap([state])
    while pq:
        state = pq.pop()
        if hard:
            state.hp -= 1
            if state.hp <= 0:
                continue
        if is_killed(trigger_effects(state)):
            return state.spent
        for spell, (cost, timer) in spells.items():
            if any(spell == effect for effect, _ in state.effects) or cost > state.mana:
                continue
            new_state = State(state.spent, state.hp, state.mana, state.armor, state.boss_hp, state.effects.copy())
            if is_killed(cast(spell, cost, timer, new_state)):
                return new_state.spent
            if is_killed(trigger_effects(new_state)):
                return new_state.spent
            if is_killed(new_hp := (new_state.hp - max(1, boss_dmg - new_state.armor))):
                continue
            new_state.hp = new_hp
            pq.push(new_state)


def part1():
    return win_least_mana()


def part2():
    return win_least_mana(hard=True)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
