with open("2020/data/day_05.txt") as f:
    seats = [
        int(el[:7], 2) * 8 + int(el[7:], 2)
        for el in (line.strip().translate(str.maketrans("BRFL", "1100")) for line in f)
    ]


def part1():
    return max(seats)


def part2():
    min_seat = min(seats)
    for i, seat_id in enumerate(sorted(seats)):
        expected = i + min_seat
        if seat_id != expected:
            return expected


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
