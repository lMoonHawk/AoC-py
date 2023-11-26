def part1():
    answer = 0
    grp_set = set()
    with open("2020/data/day_06.txt") as f:
        for line in f:
            if line == "\n":
                answer += len(grp_set)
                grp_set = set()

            grp_set.update({question for question in line.strip()})

    print(answer + len(grp_set))


def part2():
    answer = 0
    flag_first = True
    grp_set = set()
    with open("2020/data/day_06.txt") as f:
        for line in f:
            if line == "\n":
                answer += len(grp_set)
                flag_first = True
                continue
            if flag_first:
                grp_set = {question for question in line.strip()}
                flag_first = False
            else:
                grp_set.intersection_update({question for question in line.strip()})

    print(answer + len(grp_set))


if __name__ == "__main__":
    part1()
    part2()
