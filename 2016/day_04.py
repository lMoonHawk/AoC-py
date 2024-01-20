with open("2016/data/day_04.txt") as f:
    rooms = [line.strip().strip("]").split("[") for line in f]


def part1():
    valid = 0
    for room, checksum in rooms:
        order = sorted([(c, room.count(c)) for c in set(room) if c.isalpha()], key=lambda x: (-x[1], x[0]))
        valid += ("".join(c[0] for c in order[:5]) == checksum) * int(room.split("-")[-1])
    return valid


def part2():
    for room, _ in rooms:
        rid = int(room.split("-")[-1])
        if "object" in "".join(chr((ord(c) - 97 + rid) % 26 + 97) if c.isalpha() else " " for c in room):
            return rid


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
