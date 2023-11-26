players = dict()
with open("2020/data/day_22.txt") as f:
    lines = [line.strip() if line == "\n" else int(line.strip()) for line in f.readlines() if "Player" not in line]
s = lines.index("")
players[1], players[2] = lines[:s], lines[s + 1 :]


def part1():
    states = {k: v[:] for k, v in players.items()}
    winner = None
    while all(states.values()):
        card1 = states[1].pop(0)
        card2 = states[2].pop(0)
        if card1 > card2:
            winner = 1
            states[1].extend([card1, card2])
        else:
            winner = 2
            states[2].extend([card2, card1])

    print(sum(card * height for card, height in zip(states[winner], range(len(states[winner]), 0, -1))))


def game(states):
    """Before either player deals a card, if there was a previous round in this game that had exactly the same
        cards in the same order in the same players' decks, the game instantly ends in a win for player 1.
        Previous rounds from other games are not considered. (avoid infinite recursion)
    Otherwise, this round's cards must be in a new configuration; the players begin the round by each drawing the top card of their deck as normal.
    """
    states = {k: v[:] for k, v in states.items()}

    winner = None
    previous_rounds = []

    while all(states.values()):
        sub_game_winner = None

        if list(states.values()) in previous_rounds:
            return 1, states
        previous_rounds.append([cards[:] for cards in states.values()])

        card1 = states[1].pop(0)
        card2 = states[2].pop(0)

        if card1 <= len(states[1]) and card2 <= len(states[2]):
            sub_game_winner, _ = game({1: states[1][:card1], 2: states[2][:card2]})

        if (sub_game_winner == 1) or (not sub_game_winner and card1 > card2):
            winner = 1
            states[1].extend([card1, card2])
        else:
            winner = 2
            states[2].extend([card2, card1])

    return winner, states


def part2():
    winner, states = game(players)
    print(sum(card * height for card, height in zip(states[winner], range(len(states[winner]), 0, -1))))


if __name__ == "__main__":
    part1()
    part2()
