def part1():

    # key = player shape
    # values = shape score, equivalent, win against, lose against]
    shapes = {
        "X": [1, "A", "C", "B"],
        "Y": [2, "B", "A", "C"],
        "Z": [3, "C", "B", "A"],
    }

    answer = 0
    with open("2022/data/day_02.txt") as f:
        for line in f:
            opponent, player = line.split()
            shape_score = shapes[player][0]

            if opponent == shapes[player][1]:
                outcome_score = 3
            if opponent == shapes[player][2]:
                outcome_score = 6

            answer += shape_score + outcome_score
            shape_score, outcome_score = 0, 0

    print(answer)


def part2():
    # key = opponent move
    # values = shape score if lose, draw, win
    shapes = {
        "A": {"X": 3, "Y": 1, "Z": 2},
        "B": {"X": 1, "Y": 2, "Z": 3},
        "C": {"X": 2, "Y": 3, "Z": 1},
    }
    outcome_score = {"X": 0, "Y": 3, "Z": 6}

    answer = 0
    with open("2022/data/day_02.txt") as f:
        for line in f:
            opponent, outcome = line.split()
            answer += shapes[opponent][outcome] + outcome_score[outcome]

    print(answer)


if __name__ == "__main__":
    part1()
    part2()
