class Packet(list):
    def __lt__(self, other):
        for left, right in zip(self, other):
            lst_cmp = None
            match [left, right]:
                case [int(), int()]:
                    if left != right:
                        return left < right
                case [list(), int()]:
                    lst_cmp = Packet(left) < Packet([right])
                case [int(), list()]:
                    lst_cmp = Packet([left]) < Packet(right)
                case [list(), list()]:
                    lst_cmp = Packet(left) < Packet(right)
            if lst_cmp is not None:
                return lst_cmp

        if len(self) != len(other):
            return len(self) < len(other)

    def __gt__(self, other):
        return not self < other


def parse_list(s, i):
    first_char = s[i]
    if first_char == "[":
        i += 1
        lst = []
        while s[i] != "]":
            el, i = parse_list(s, i)
            lst.append(el)
            if s[i] == ",":
                i += 1
        return lst, i + 1
    else:
        i0 = i
        while s[i].isdigit() or s[i] == "-":
            i += 1
        return int(s[i0:i]), i


def parse_packet(s):
    content, _ = parse_list(s, 0)
    return Packet(content)


with open("2022/data/day_13.txt") as f:
    packets = [parse_packet(line.strip()) for line in f if line != "\n"]


def part1():
    return sum(i + 1 for i, k in enumerate(range(0, len(packets), 2)) if packets[k] < packets[k + 1])


def part2():
    divisors = [[[2]], [[6]]]
    key = 1
    for index, packet in enumerate(sorted(packets + divisors), 1):
        if packet in divisors:
            key *= index
    return key


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
