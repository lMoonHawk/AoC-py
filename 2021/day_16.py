with open("2021/data/day_16.txt") as f:
    bits = "".join(f"{int(h, 16):0>4b}" for h in f.readline().strip())


def prod(lst):
    out = 1
    for n in lst:
        out *= n
    return out


op = {
    0: sum,
    1: prod,
    2: min,
    3: max,
    4: lambda x: x,
    5: lambda x: x[0] > x[1],
    6: lambda x: x[0] < x[1],
    7: lambda x: x[0] == x[1],
}


def chop_int(n, bits, k):
    return int(bits[k : k + n], 2), k + n


def parse_literal(bits, k):
    value, prefix = 0, 1
    while prefix:
        group, k = chop_int(5, bits, k)
        prefix = group >> 4
        value = (value << 4) + (group & 0xF)
    return value, k


def parse_operator(bits, k, get_version):
    length_id, k = chop_int(1, bits, k)
    values = []

    if length_id == 0:
        sub_length, k = chop_int(15, bits, k)
        start = k
        while k < start + sub_length:
            value, k = parse_packet(bits, k, get_version)
            values.append(value)

    elif length_id == 1:
        sub_count, k = chop_int(11, bits, k)
        for _ in range(sub_count):
            value, k = parse_packet(bits, k, get_version)
            values.append(value)

    return values, k


def parse_packet(bits, k, get_version):
    version, k = chop_int(3, bits, k)
    type_id, k = chop_int(3, bits, k)

    if type_id == 4:
        value, k = parse_literal(bits, k)
        sub_packets = value if not get_version else []
    else:
        sub_packets, k = parse_operator(bits, k, get_version)

    if get_version:
        return sum(sub_packets) + version, k
    return op[type_id](sub_packets), k


def parse_transmission(bits, get_version=False):
    out, _ = parse_packet(bits, 0, get_version)
    return out


def part1():
    return parse_transmission(bits, get_version=True)


def part2():
    return parse_transmission(bits)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
