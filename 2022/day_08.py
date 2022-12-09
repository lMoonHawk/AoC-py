field = []
with open("2022/data/day_08.txt") as f:
    for line in f:
        field.append([int(tree) for tree in line.strip()])
nb_rows = len(field)
nb_cols = len(field[0])


def part1():
    def is_visible(n, m):

        top = [field[i][m] for i in range(n)]
        if field[i][m] > max(top):
            return 1
        bottom = [field[i][m] for i in range(n + 1, nb_rows)]
        if field[i][m] > max(bottom):
            return 1
        left = field[n][:m]
        if field[i][m] > max(left):
            return 1
        right = field[n][m + 1 : nb_cols]
        if field[i][m] > max(right):
            return 1

        return 0

    visible = nb_rows * 2 + nb_cols * 2 - 4
    for i in range(1, nb_rows - 1):
        for j in range(1, nb_cols - 1):
            visible += is_visible(i, j)
    print(visible)


def part2():
    def scenic_score(n, m):
        tree = field[n][m]

        top = 1 if n != 0 else 0
        for i in range(n - 1, -1, -1):
            if tree <= field[i][m]:
                break
            if i != 0:
                top += 1

        bottom = 1 if n != nb_rows - 1 else 0
        for i in range(n + 1, nb_rows):
            if tree <= field[i][m]:
                break
            if i != nb_rows - 1:
                bottom += 1

        left = 1 if m != 0 else 0
        for j in range(m - 1, -1, -1):
            if tree <= field[n][j]:
                break
            if j != 0:
                left += 1

        right = 1 if m != nb_cols - 1 else 0
        for j in range(m + 1, nb_cols):
            if tree <= field[n][j]:
                break
            if j != nb_cols - 1:
                right += 1

        return top * bottom * left * right

    score = 0
    for i in range(nb_rows):
        for j in range(nb_cols):
            pass
            score_ij = scenic_score(i, j)
            score = score_ij if score_ij > score else score
    print(score)


if __name__ == "__main__":
    part1()
    part2()
