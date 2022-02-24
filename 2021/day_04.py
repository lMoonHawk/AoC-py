def part1():
    # list of all bingo cards [card[row[int]]]
    cards: list[list[list[int]]] = []
    card_count = -1

    with open("2021/data/day_04.txt") as f:
        for i, line in enumerate(f):
            if not i:
                rand_nbs = line.strip().split(",")
            else:
                # Cards are separated by newline, set up next card
                if line == "\n":
                    card_count += 1
                    cards.insert(card_count, [])
                else:
                    cards[card_count].append(line.strip().split())

    # Check cols or rows for bingo
    def check_row(arrays, nb_in):
        for array in arrays:
            for row in array:
                if not set(row) - set(nb_in):
                    return array
        return False

    def check_col(arrays, nb_in):
        for array in arrays:
            # Transpose
            cols = [[row[i] for row in array]
                    for i in range(0, len(array[0]))]
            for col in cols:
                if not set(col) - set(nb_in):
                    return array
        return False

    def sum_unmarked(array, nb_in):
        total = 0
        for row in array:
            total += sum(
                [int(nb) for nb in row
                 if nb not in nb_in])

        return total

    for i in range(0, len(rand_nbs) + 1):
        if i > 3:  # No bingos possible at that stage
            rand_so_far = rand_nbs[0:i+1]

            check = check_row(cards, rand_so_far)
            if not check:
                check = check_col(cards, rand_so_far)
            if check:
                print(int(rand_so_far[-1]) * sum_unmarked(check, rand_so_far))
                break


def part2():
    pass


if __name__ == '__main__':
    part1()
    # part2()
