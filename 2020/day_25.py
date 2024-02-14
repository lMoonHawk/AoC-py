with open("2020/data/day_25.txt") as f:
    card_pk, door_pk = [int(pk) for pk in f.readlines()]


def get_loop_size(pk):
    value = 1
    loop_size = 0
    while True:
        loop_size += 1
        value = (value * 7) % 20201227
        if value == pk:
            return loop_size


def get_ek(subject_nb, ls):
    value = 1
    for _ in range(ls):
        value = (value * subject_nb) % 20201227
    return value


def part1():
    card_ls, door_ls = [get_loop_size(pk) for pk in (card_pk, door_pk)]
    if card_ls < door_ls:
        ek = get_ek(door_pk, card_ls)
    else:
        ek = get_ek(card_pk, door_ls)

    return ek


def part2():
    return


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
