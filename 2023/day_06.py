def get_races():
    with open("2023/data/day_06.txt") as f:
        return [[int(el) for i, el in enumerate(line.strip().split()) if i > 0] for line in f.readlines()]


def part1():
    # dist = speed * time
    # time = max_time - button_held
    # speed = button_held
    # => dist = button_held * (max_time - button_held)
    answer = 1
    times, bests = get_races()
    for time, best in zip(times, bests):
        answer *= sum(hold * (time - hold) > best for hold in range(time))
    return answer


def part2():
    time, best = [int("".join(str(el) for el in table)) for table in get_races()]
    # Find the two solutions b1, b2 such that: b^2 - Tb + d = 0
    # All integers between b1 and b2 are above the record distance d
    det = (time**2 - 4 * best) ** 0.5
    return int((time + det) // 2 - (time - det) // 2)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
