def part1():

    distinct_streak = 4
    window = []
    cursor = 0

    with open("2022/data/day_06.txt") as f:
        while True:
            c = f.read(1)
            if not c:
                break

            window.append(c)
            if cursor >= distinct_streak - 1:
                if len(set(window)) == distinct_streak:
                    print(cursor + 1)
                    break
                del window[0]
            cursor += 1


def part2():

    distinct_streak = 14
    window = []
    cursor = 0

    with open("2022/data/day_06.txt") as f:
        while True:
            c = f.read(1)
            if not c:
                break

            window.append(c)
            if cursor >= distinct_streak - 1:
                if len(set(window)) == distinct_streak:
                    print(cursor + 1)
                    break
                del window[0]
            cursor += 1


if __name__ == "__main__":
    part1()
    part2()
