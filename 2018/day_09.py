with open("2018/data/day_09.txt") as f:
    line = f.readline().split()
    PLAYERS, LAST_MARBLE = int(line[0]), int(line[-2])


class Marble:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def jump(self, group, k):
        out = self
        if k >= 0:
            for _ in range(k):
                out = group[out.next]
        else:
            for _ in range(-k):
                out = group[out.prev]
        return out

    def attach_after(self, group, left_marble):
        right_marble = left_marble.jump(group, 1)
        self.prev = right_marble.prev
        self.next = left_marble.next
        group.append(self)
        left_marble.next = len(group) - 1
        right_marble.prev = len(group) - 1

    def detach(self, group):
        left_marble_idx = self.prev
        right_marble_idx = self.next
        group[left_marble_idx].next = right_marble_idx
        group[right_marble_idx].prev = left_marble_idx


def play(players, last_marble):
    current_player = 0
    scores = [0] * players

    current_marble = Marble(0, 0, 0)
    marbles = [current_marble]

    for marble_value in range(1, last_marble + 1):
        if marble_value % 23 != 0:
            new_marble = Marble(marble_value, marbles)
            new_marble.attach_after(marbles, current_marble.jump(marbles, 1))
            current_marble = new_marble
        else:
            removed = current_marble.jump(marbles, -7)
            scores[current_player] += marble_value + removed.value
            current_marble = removed.jump(marbles, 1)
            removed.detach(marbles)

        current_player = (current_player + 1) % players

    return max(scores)


def part1():
    return play(PLAYERS, LAST_MARBLE)


def part2():
    return play(PLAYERS, LAST_MARBLE * 100)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
