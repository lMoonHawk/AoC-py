def get_platform():
    with open("2023/data/day_14.txt") as f:
        return [list(line.strip()) for line in f.readlines()]


def part1():
    platform = get_platform()
    answer = 0
    for i, row in enumerate(platform):
        for j, _ in enumerate(row):
            if platform[i][j] == "O":
                ni = i
                for k in range(i):
                    if platform[i - k - 1][j] != ".":
                        break
                    ni = i - k - 1
                platform[i][j], platform[ni][j] = ".", "O"
                answer += len(platform) - ni
    return answer


def cycle(platform):
    # North
    for i in range(len(platform)):
        for j in range(len(platform[0])):
            if platform[i][j] == "O":
                ni = i
                for k in range(i):
                    if platform[i - k - 1][j] != ".":
                        break
                    ni = i - k - 1
                platform[i][j], platform[ni][j] = ".", "O"

    # West
    for j in range(len(platform[0])):
        for i in range(len(platform)):
            if platform[i][j] == "O":
                nj = j
                for k in range(j):
                    if platform[i][j - k - 1] != ".":
                        break
                    nj = j - k - 1
                platform[i][j], platform[i][nj] = ".", "O"

    # South
    for i in reversed(range(len(platform))):
        for j in range(len(platform[0])):
            if platform[i][j] == "O":
                ni = i
                for k in range(len(platform) - i - 1):
                    if platform[i + k + 1][j] != ".":
                        break
                    ni = i + k + 1
                platform[i][j], platform[ni][j] = ".", "O"
    # East
    for j in reversed(range(len(platform[0]))):
        for i in range(len(platform)):
            if platform[i][j] == "O":
                nj = j
                for k in range(len(platform[0]) - j - 1):
                    if platform[i][j + k + 1] != ".":
                        break
                    nj = j + k + 1
                platform[i][j], platform[i][nj] = ".", "O"


def get_load(platform):
    answer = 0
    for i, row in enumerate(platform):
        for j, _ in enumerate(row):
            if platform[i][j] == "O":
                answer += len(platform) - i
    return answer


def find_seq(arr):
    for i in range(2, len(arr) // 3):
        if arr[-1] == arr[-1 - i] == arr[-1 - 2 * i]:
            return i
    return 0


def part2():
    platform = get_platform()
    loads = []
    k = 0
    while True:
        k += 1
        cycle(platform)
        loads.append(get_load(platform))
        if a := find_seq(loads):
            return loads[-a:][(1_000_000_000 - k - 1) % a]


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
