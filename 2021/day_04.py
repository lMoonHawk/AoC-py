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
    def check_win(array, nb_in):
        # Transpose to also get cols
        array_cols = [[row[i] for row in array]
                      for i in range(0, len(array[0]))]

        for row, col in zip(array, array_cols):
            # If set difference for either row or col is 0, return array
            if not ((set(row) - set(nb_in))
                    and (set(col) - set(nb_in))):
                return array
        return 0

    def sum_unmarked(array, nb_in):
        total = 0
        for row in array:
            total += sum([int(nb) for nb in row
                          if nb not in nb_in])

        return total

    count = 4  # We start at 5 numbers, bingo cant happen before
    board_check = 0

    while not board_check:
        rand_so_far = rand_nbs[:count]
        count += 1

        for card in cards:
            board_check = check_win(card, rand_so_far)
            if board_check:
                score_card = sum_unmarked(board_check, rand_so_far)
                print(int(rand_so_far[-1]) * score_card)
                break


def part2():
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
    def check_win(array, nb_in):
        array_cols = [[row[i] for row in array]
                      for i in range(0, len(array[0]))]

        for row, col in zip(array, array_cols):
            if not ((set(row) - set(nb_in))
                    and (set(col) - set(nb_in))):
                return 1
        return 0

    def sum_unmarked(array, nb_in):
        total = 0
        for row in array:
            total += sum(
                [int(nb) for nb in row
                 if nb not in nb_in])
        return total

    card_won = [0] * len(cards)
    win_counter = 1
    last_numbers = []

    for i in range(4, len(rand_nbs) + 1):
        rand_so_far = rand_nbs[0:i+1]

        for i, card in enumerate(cards):
            if not card_won[i]:
                card_won[i] = check_win(card, rand_so_far) * win_counter
                if card_won[i]:
                    win_counter += 1
                    last_numbers = rand_so_far

    last_card_idx = card_won.index(max(card_won))
    last_card = cards[last_card_idx]
    print(sum_unmarked(last_card, last_numbers) * int(last_numbers[-1]))


if __name__ == '__main__':
    part1()
    part2()
