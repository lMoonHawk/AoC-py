def get_strength(hand):
    max_val = 13**5
    dups = [hand.count(lab) for lab in hand]
    nb_dups = [dups.count(k + 1) // (k + 1) for k in range(5)]

    if nb_dups[5 - 1] == 1:
        return max_val * 6
    elif nb_dups[4 - 1] == 1:
        return max_val * 5
    elif nb_dups[3 - 1] == 1 and nb_dups[2 - 1] == 1:
        return max_val * 4
    elif nb_dups[3 - 1] == 1:
        return max_val * 3
    elif nb_dups[2 - 1] == 2:
        return max_val * 2
    elif nb_dups[2 - 1] == 1:
        return max_val * 1
    else:
        return 0


def hand_hash(hand, joker_rule):
    """Return a perfect hash of the hand, that represents the hand's power."""
    # Hash the card values based on ordering, converting base 13 to 10
    # lab   base 13 base 10
    # 22223 00001   1
    # AKQJT CBA98   368714
    # Then add hand strength*100000_13 (0 for high card up to 6 for five of a kind)

    if not joker_rule:
        values = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    else:
        values = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]

    value = sum(values.index(lab) * 13 ** (4 - k) for k, lab in enumerate(hand))
    if not joker_rule or "J" not in hand:
        strength = get_strength(hand)
    else:
        strength = max(get_strength(hand.replace("J", joker)) for joker in values)

    return strength + value


def cards(joker=False):
    with open("2023/data/day_07.txt") as f:
        return [(hand_hash(line.split()[0], joker), int(line.split()[1])) for line in f.readlines()]


def part1():
    return sum(bid * (rank + 1) for rank, (_, bid) in enumerate(sorted(cards())))


def part2():
    return sum(bid * (rank + 1) for rank, (_, bid) in enumerate(sorted(cards(joker=True))))


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
