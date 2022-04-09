def parse():
    with open("2021/data/day_21.txt") as f:
        for line in f:
            player, pos = line.strip().split(" starting position: ")
            if player == "Player 1":
                p1_pos = int(pos)
            else:
                p2_pos = int(pos)

        return p1_pos, p2_pos


def deter_rolls():
    i = 0
    while True:
        yield i % 100 + (i + 1) % 100 + (i + 2) % 100 + 3
        i += 3


def dirac_rolls():
    for i in range(1, 4):
        for j in range(1, 4):
            for k in range(1, 4):
                yield i + j + k


def play_turn(pos, score, dice):
    pos = (pos + next(dice) - 1) % 10 + 1
    score += pos
    return pos, score


def play_game(p1_pos, p2_pos):
    p1_score, p2_score = 0, 0

    dice = deter_rolls()
    dice_rolls = 0
    while True:
        p1_pos, p1_score = play_turn(p1_pos, p1_score, dice)
        dice_rolls += 3

        if p1_score >= 1000:
            return p2_score, dice_rolls

        p2_pos, p2_score = play_turn(p2_pos, p2_score, dice)
        dice_rolls += 3

        if p2_score >= 1000:
            return p2_score, dice_rolls


def part1():
    p1_pos, p2_pos = parse()
    loser_score, dice_rolls = play_game(p1_pos, p2_pos)
    print(loser_score * dice_rolls)


def board(pos):
    return (pos - 1) % 10 + 1


def wins(p1_score, p2_score, p1_pos, p2_pos, turn, memo={}):
    # Memoization, return early if answer already known
    key = f"{p1_score},{p2_score},{p1_pos},{p2_pos},{turn}"
    if key in memo:
        return memo[key]

    if p1_score >= 21:
        return 1, 0
    if p2_score >= 21:
        return 0, 1

    tot_p1_wins = 0
    tot_p2_wins = 0
    # No need to arg memo as dict is mutable
    for roll in dirac_rolls():
        if turn == "p1":
            new_pos = board(p1_pos + roll)
            win_cnt = wins(p1_score + new_pos, p2_score, new_pos, p2_pos, "p2")
        else:
            new_pos = board(p2_pos + roll)
            win_cnt = wins(p1_score, p2_score + new_pos, p1_pos, new_pos, "p1")

        tot_p1_wins += win_cnt[0]
        tot_p2_wins += win_cnt[1]

    memo[key] = tot_p1_wins, tot_p2_wins
    return memo[key]


def part2():
    p1_pos, p2_pos = parse()
    answer = wins(0, 0, p1_pos, p2_pos, "p1")
    print(max(answer))


if __name__ == "__main__":
    part1()
    part2()
