def gen_packets(divisor=False):
    with open("2022/data/day_13.txt") as f:
        for line in f:
            packet = line.strip()
            if packet == "":
                continue
            # Please look the other way...
            yield eval(packet)
    if divisor:
        yield [[2]]
        yield [[6]]


def gen_packet_pairs():
    pair = []
    for packet in gen_packets():
        pair.append(packet)
        if len(pair) == 2:
            yield pair
            pair = []


def compare(l1, l2):
    for el1, el2 in zip(l1, l2):
        el1_list = isinstance(el1, list)
        el2_list = isinstance(el2, list)

        # If both integers, check inequality
        if not (el1_list or el2_list):
            if el1 < el2:
                return True
            elif el1 > el2:
                return False
            else:
                continue

        # If one is not a list, convert to list
        el1 = [el1] if not el1_list else el1
        el2 = [el2] if not el2_list else el2

        # Call "compare" to find integers inside
        result = compare(el1, el2)
        # None if int in both lists are identical: continue,
        # Else go back up stack
        if result is not None:
            return result

    # If all items the same, compare list size
    if len(l1) < len(l2):
        return True
    elif len(l1) > len(l2):
        return False


# Quick sort for packets, assuming transitivity of "compare"
def sort_packets(ps):
    if ps == []:
        return []
    pivot = ps[0]
    left = sort_packets([x for x in ps[1:] if compare(x, pivot)])
    right = sort_packets([x for x in ps[1:] if not compare(x, pivot)])
    return left + [pivot] + right


def part1():
    answer = sum(
        i + 1
        for i, (left, right) in enumerate(gen_packet_pairs())
        if compare(left, right)
    )
    print(answer)


def part2():
    packets = list(gen_packets(divisor=True))
    packets = sort_packets(packets)

    print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))


if __name__ == "__main__":
    part1()
    part2()
