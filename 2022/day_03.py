def part1():

    answer = 0
    with open("2022/data/day_03.txt") as f:
        for line in f:
            ks = line.strip()
            comp_1, comp_2 = ks[: len(ks) // 2], ks[len(ks) // 2 :]
            common_item = "".join(set(comp_1).intersection(comp_2))

            # Convert letter to integer unicode representation
            # "a"->"z" = 97-> 122 (-96 : 1->26)
            # "A" -> "Z" = 65-> 90 (-(64 - 26) : 27->52)
            ord_offset = 96 if common_item.islower() else 64 - 26
            answer += ord(common_item) - ord_offset

    print(answer)


def part2():

    answer = 0
    group = []

    with open("2022/data/day_03.txt") as f:
        for line in f:
            group.append(set(line.strip()))
            if len(group) == 3:
                common_item = "".join(set.intersection(*group))
                ord_offset = 96 if common_item.islower() else 64 - 26
                answer += ord(common_item) - ord_offset
                group = []
    print(answer)


if __name__ == "__main__":
    part1()
    part2()
