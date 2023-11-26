def part1():
    answer = 0
    with open("2020/data/day_05.txt") as f:
        for line in f:
            line = line.strip()
            row_bin, col_bin = line.strip()[:7], line.strip()[7:]
            #
            row = int(row_bin.replace("B", "1").replace("F", "0"), 2)
            col = int(col_bin.replace("R", "1").replace("L", "0"), 2)
            current_id = row * 8 + col

            answer = current_id if current_id > answer else answer
    print(answer)


def part2():
    ids = []
    with open("2020/data/day_05.txt") as f:
        for line in f:
            line = line.strip()
            row_bin, col_bin = line.strip()[:7], line.strip()[7:]

            row = int(row_bin.replace("B", "1").replace("F", "0"), 2)
            col = int(col_bin.replace("R", "1").replace("L", "0"), 2)
            ids.append(row * 8 + col)

    # The first missing id found in the sorted list will be our seat
    # if we start from the first existing id
    ids.sort()
    for i, seat_id in enumerate(ids):
        expected = i + ids[0]
        if seat_id != expected:
            print(expected)
            break


if __name__ == "__main__":
    part1()
    part2()
