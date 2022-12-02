def part1():

    answer = 0
    elf_cal = 0
    with open("2022/data/day_01.txt") as f:
        for line in f:
            cal = line.strip()
            if cal == "":
                answer = elf_cal if elf_cal > answer else answer
                elf_cal = 0
                continue
            elf_cal += int(cal)

    answer = elf_cal if elf_cal > answer else answer
    print(answer)


def part2():

    top = [0, 0, 0]
    elf_cal = 0
    with open("2022/data/day_01.txt") as f:
        for line in f:
            cal = line.strip()
            if cal == "":
                top[0] = elf_cal if elf_cal > top[0] else top[0]
                top.sort()
                elf_cal = 0
                continue
            elf_cal += int(cal)

    top[0] = elf_cal if elf_cal > top[0] else top[0]
    print(sum(top))


if __name__ == "__main__":
    part1()
    part2()
