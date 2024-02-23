with open("2021/data/day_21.txt") as f:
    pos_init = [int(line.split()[-1]) for line in f]


def deter_rolls():
    i = 0
    while True:
        value = 0
        for _ in range(3):
            i = i % 100 + 1
            value += i
        yield value


def dirac_rolls():
    return (r1 + r2 + r3 for r1 in range(1, 4) for r2 in range(1, 4) for r3 in range(1, 4))


def run_dirac(pos, scores=None, player=0, memo={}):
    if scores is None:
        scores = [0, 0]
    rid = tuple(pos + scores + [player])
    if rid in memo:
        return memo[rid]
    if scores[0] >= 21:
        return 1, 0
    if scores[1] >= 21:
        return 0, 1

    total_scores = (0, 0)
    for roll in dirac_rolls():
        new_pos = pos.copy()
        new_scores = scores.copy()
        new_pos[player] = (pos[player] + roll - 1) % 10 + 1
        new_scores[player] += new_pos[player]
        win_cnt = run_dirac(new_pos, new_scores, 1 - player)
        total_scores = total_scores[0] + win_cnt[0], total_scores[1] + win_cnt[1]
    memo[rid] = total_scores
    return total_scores


def part1():
    pos, scores = pos_init.copy(), [0, 0]
    rolls = 0
    for p, roll in enumerate(deter_rolls()):
        player = p % 2
        pos[player] = (pos[player] + roll - 1) % 10 + 1
        scores[player] += pos[player]
        rolls += 3
        if scores[player] >= 1_000:
            return scores[1 - player] * rolls


def part2():
    return max(run_dirac(pos_init))


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
