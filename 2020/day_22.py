def get_cards():
    with open("2020/data/day_22.txt") as f:
        return [
            [int(card) for card in player.split("\n") if "Player" not in card]
            for player in f.read().strip().split("\n\n")
        ]


def part1():
    states = get_cards()
    while all(states):
        card1, card2 = states[0].pop(0), states[1].pop(0)
        winner = card1 < card2
        states[winner].extend(sorted([card1, card2], reverse=True))
    return sum(card * height for card, height in zip(states[winner], range(len(states[winner]), 0, -1)))


def game(states):
    """Before either player deals a card, if there was a previous round in this game that had exactly the same
        cards in the same order in the same players' decks, the game instantly ends in a win for player 1.
        Previous rounds from other games are not considered. (avoid infinite recursion)
    Otherwise, this round's cards must be in a new configuration; the players begin the round by each drawing the top card of their deck as normal.
    """
    winner = None
    previous_rounds = set()

    while all(states):
        sub_game_winner = None
        frozen_states = tuple([tuple(state) for state in states])
        if frozen_states in previous_rounds:
            return 0, states
        previous_rounds.add(frozen_states)

        card1 = states[0].pop(0)
        card2 = states[1].pop(0)

        if card1 <= len(states[0]) and card2 <= len(states[1]):
            sub_game_winner, _ = game([states[0][:card1], states[1][:card2]])

        if (sub_game_winner == 0) or (not sub_game_winner and card1 > card2):
            winner = 0
            states[0].extend([card1, card2])
        else:
            winner = 1
            states[1].extend([card2, card1])

    return winner, states


def part2():
    winner, states = game(get_cards())
    return sum(card * height for card, height in zip(states[winner], range(len(states[winner]), 0, -1)))


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
