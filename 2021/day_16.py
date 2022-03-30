def part1():
    def l_bin2dec(l_bin: list[str]):
        return int("".join(l_bin), 2)

    def parse(k, convert=False):
        out = bin_line[:k]
        del bin_line[:k]
        if convert:
            out = l_bin2dec(out)
        return out

    def parse_literal():
        out = []
        stop = False
        while not stop:
            if bin_line[0] == "0":
                stop = True
            # header
            del bin_line[0]
            # group
            out += parse(4)
        return l_bin2dec(out)

    def parse_packet():
        version = parse(3, convert=True)
        type_id = parse(3, convert=True)

        version_sum = version

        if type_id == 4:
            parse_literal()
        else:
            if parse(1, convert=True):
                nb_subpackets = parse(11, convert=True)
                for _ in range(nb_subpackets):
                    version_sum += parse_packet()

            else:
                size_subpackets = parse(15, convert=True)
                current_size = len(bin_line)
                while current_size - len(bin_line) < size_subpackets:
                    version_sum += parse_packet()
        return version_sum

    # Parsing
    with open("2021/data/day_16.txt") as f:
        hex_line = f.readline()

    bin_line = []
    for hex_num in hex_line:
        # Convert hex to 4 bit binary
        bin_line.extend(format(int(hex_num, 16), "0>4b"))

    print(parse_packet())


def part2():
    def l_bin2dec(l_bin: list[str]):
        """Joins a list of bit to a decimal"""
        return int("".join(l_bin), 2)

    def parse(k, convert=False):
        """Parses k elements from the line and removes from the stack.\n
        If convert=True, returns a decimal"""
        out = bin_line[:k]
        del bin_line[:k]
        if convert:
            out = l_bin2dec(out)
        return out

    def parse_literal():
        out = []
        stop = False
        while not stop:
            if bin_line[0] == "0":
                stop = True
            # header
            del bin_line[0]
            # group
            out += parse(4)
        return l_bin2dec(out)

    def packet_prod(l_in: list):
        out = 1
        for x in l_in:
            out *= x
        return out

    def packet_gt(l_in: list):
        if l_in[0] > l_in[1]:
            return 1
        else:
            return 0

    def packet_lt(l_in: list):
        if l_in[0] < l_in[1]:
            return 1
        else:
            return 0

    def packet_eq(l_in: list):
        if l_in[0] == l_in[1]:
            return 1
        else:
            return 0

    operators = {
        0: sum,
        1: packet_prod,
        2: min,
        3: max,
        5: packet_gt,
        6: packet_lt,
        7: packet_eq,
    }

    def parse_packet():
        _ = parse(3, convert=True)  # Version
        type_id = parse(3, convert=True)

        if type_id == 4:
            return parse_literal()
        else:
            operation = operators[type_id]

            # Control flow for type of length type ID
            if parse(1, convert=True):
                nb_subpackets = parse(11, convert=True)
                subpacket = []
                for _ in range(nb_subpackets):
                    subpacket.append(parse_packet())
            else:
                size_subpackets = parse(15, convert=True)
                current_size = len(bin_line)
                subpacket = []
                while current_size - len(bin_line) < size_subpackets:
                    subpacket.append(parse_packet())

            return operation(subpacket)

    # Parsing
    with open("2021/data/day_16.txt") as f:
        hex_line = f.readline()

    bin_line = []
    for hex_num in hex_line:
        # Convert hex to 4 bit binary
        bin_line.extend(format(int(hex_num, 16), "0>4b"))

    print(parse_packet())


if __name__ == "__main__":
    part1()
    part2()
