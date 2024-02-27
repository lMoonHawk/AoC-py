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


with open("2021/data/day_23.txt") as f:
    siderooms = [[ord(line[k]) - 65 for k in [3, 5, 7, 9]] for line in f.readlines()[2:4]]
    siderooms = tuple(zip(*reversed(siderooms)))


def path_blocked(pos, target, hallway):
    if hallway[target] != -1:
        return True
    if pos > target:
        pos, target = target, pos
    for sq in hallway[pos + 1 : target]:
        if sq != -1:
            return True
    return False


def is_end_state(siderooms, rooms_size):
    for i, room in enumerate(siderooms):
        if len(room) != rooms_size:
            return False
        for amphipod in room:
            if amphipod != i:
                return False
    return True


def room_done(k, room):
    for amphipod in room:
        if amphipod != k:
            return False
    return True


def move_to_room(amphipod, siderooms, k, hallway):
    # Cannot enter if sideroom has another amphipod type
    for other in siderooms[amphipod]:
        if other != amphipod:
            return None
    # Room entrances are hallway 2, 4, 6, 8
    target = 2 * (amphipod + 1)
    # Cannot enter if path is blocked
    if path_blocked(k, target, hallway):
        return None
    return target


def sort_energy(siderooms):
    rooms_size = len(siderooms[0])
    pqueue = Heap()
    seen = set()
    hallway = tuple([-1 for _ in range(11)])
    state = 0, siderooms, hallway
    pqueue.push(state)

    while pqueue:
        total_energy, siderooms, hallway = pqueue.pop()
        if (siderooms, hallway) in seen:
            continue
        seen.add((siderooms, hallway))

        if is_end_state(siderooms, rooms_size):
            return total_energy

        # For each amphipod in the hallway, reach its room. Best possible move.
        moved_to_room = False
        for k, amphipod in enumerate(hallway):
            if amphipod == -1:
                continue
            if (target := move_to_room(amphipod, siderooms, k, hallway)) is None:
                continue
            # Energy spent to move to the room entrance
            energy = abs(target - k)
            # Energy spent to go to the back of the room
            energy += rooms_size - len(siderooms[amphipod])

            energy *= 10**amphipod
            moved_to_room = True
            new_hallway = hallway[:k] + (-1,) + hallway[k + 1 :]
            new_siderooms = siderooms[:amphipod] + (siderooms[amphipod] + (amphipod,),) + siderooms[amphipod + 1 :]
            pqueue.push((total_energy + energy, new_siderooms, new_hallway))
            break

        if moved_to_room:
            continue

        # for each siderooms, amphipod on top can move to hallway 0,1,3,5,7,9,10 if not occupied or moving past another amphipod
        for k, room in enumerate(siderooms):
            if not room:
                continue
            if room_done(k, room):
                continue
            amphipod = room[-1]
            if amphipod == k and len(room) == 1:
                continue
            new_room = room[:-1]
            new_siderooms = siderooms[:k] + (new_room,) + siderooms[k + 1 :]
            pos = 2 * (k + 1)
            for target in [0, 1, 3, 5, 7, 9, 10]:
                if path_blocked(pos, target, hallway):
                    continue
                # Energy spent to move to the room entrance
                energy = rooms_size - len(new_room)
                # Energy spent to reach target
                energy += abs(target - pos)
                energy *= 10**amphipod
                new_hallway = hallway[:target] + (amphipod,) + hallway[target + 1 :]
                pqueue.push((total_energy + energy, new_siderooms, new_hallway))


def part1():
    return sort_energy(siderooms)


def part2():
    extras = [(3, 3), (1, 2), (0, 1), (2, 0)]
    ext_siderooms = tuple([(room[0],) + extra + (room[1],) for room, extra in zip(siderooms, extras)])
    return sort_energy(ext_siderooms)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
