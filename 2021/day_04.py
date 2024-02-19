with open("2021/data/day_04.txt") as f:
    rands, *boards = f.read().split("\n\n")
    rands = [int(rand) for rand in rands.split(",")]
    boards = [[[int(n) for n in row.split()] for row in board.split("\n")] for board in boards]


def board_win(board, drawn):
    for k in range(5):
        if len(set(board[k]).intersection(drawn)) == 5:
            return True
        if len({board[i][k] for i in range(5)}.intersection(drawn)) == 5:
            return True
    return False


def sum_unmarked(board, drawn):
    return sum(sum(val for val in row if val not in drawn) for row in board)


def part1():
    drawn = set(rands[:5])
    for k in range(5, len(rands)):
        drawn.add(rands[k])
        for board in boards:
            if board_win(board, drawn):
                return rands[k] * sum_unmarked(board, drawn)


def part2():
    drawn = set(rands[:5])
    won = set()
    for k in range(5, len(rands)):
        drawn.add(rands[k])
        for b, board in enumerate(boards):
            if b in won:
                continue
            if board_win(board, drawn):
                won.add(b)
                if len(won) == len(boards):
                    return rands[k] * sum_unmarked(board, drawn)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
