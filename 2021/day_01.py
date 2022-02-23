def part1():

    larger = 0

    with open("2021/data/day_01.txt") as f:
        for i, line in enumerate(f):
            if i == 0:
                measure = int(line.strip())
            else:
                next_measure = int(line.strip())
                if int(line.strip()) > measure:
                    larger += 1
                measure = next_measure

    print(larger)


def part2():
    # Counter for rolling 3 increasing
    larger = 0
    # Keep tracks of only current and last 3 numbers
    measures = []

    with open("2021/data/day_01.txt") as f:
        for i, line in enumerate(f):

            if i < 3:
                measures.append(int(line.strip()))

            else:
                next_measure = int(line.strip())
                measures.append(next_measure)
                # Comparing rolling 3s is equivalent to
                # comparing the set difference
                if measures[3] > measures[0]:
                    larger += 1
                del measures[0]

    print(larger)


if __name__ == '__main__':
    part1()
    part2()
