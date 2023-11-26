def read_input():
    with open("2020/data/day_23.txt") as f:
        return [int(c) for c in f.read()]


def part1():
    cups = read_input()
    cup_count = len(cups)

    current_cup_index = 0

    for _ in range(100):
        current_cup_label = cups[current_cup_index % cup_count]
        picked_labels = [*cups, *cups][current_cup_index + 1 : current_cup_index + 4]
        cups = [cup for cup in cups if cup not in picked_labels]

        destination_label = None
        k = 1
        while not destination_label or destination_label in picked_labels:
            destination_label = (current_cup_label - k - 1) % cup_count + 1
            k += 1

        destination_index = cups.index(destination_label)

        cups = cups[: destination_index + 1] + picked_labels + cups[destination_index + 1 :]

        current_cup_index = (cups.index(current_cup_label) + 1) % cup_count

    answer = [*cups, *cups][cups.index(1) + 1 : cups.index(1) + cup_count]
    print("".join(str(a) for a in answer))


def part2():
    class Cup:
        def __init__(self, label, next):
            self.label = label
            self.next = next

    def jump(addr, k):
        """Jump from the given address to the next k cup index"""
        for _ in range(k):
            addr = cups[addr].next
        return addr

    input_cups = read_input()
    input_count = len(input_cups)
    cup_count = 1_000_000

    cups = [Cup(input_cups[k], k + 1) for k in range(input_count)]
    cups.extend([Cup(k, k) for k in range(input_count + 1, cup_count + 1)])
    cups[-1].next = 0

    addresses = [None] * (cup_count + 1)
    for i in range(cup_count):
        addresses[cups[i].label] = i

    current = 0

    for _ in range(10_000_000):
        picked_indexes = [jump(cups[current].next, k) for k in range(3)]

        # Current cup "next" skips the 3 picks (detaches the 3 picked cups)
        cups[current].next = jump(current, 4)

        destination_index = None
        k = 1
        while destination_index in [None, *picked_indexes]:
            destination_cup = (cups[current].label - k - 1) % cup_count + 1
            destination_index = addresses[destination_cup]
            k += 1

        # Swap the picked cup

        after_destination = cups[destination_index].next
        # Point the destination cup to the first picked cup
        cups[destination_index].next = picked_indexes[0]
        # Point the last picked cup to where the destination cup pointed to
        cups[picked_indexes[2]].next = after_destination

        current = cups[current].next

    print(cups[jump(addresses[1], 1)].label * cups[jump(addresses[1], 2)].label)


if __name__ == "__main__":
    part1()
    part2()
