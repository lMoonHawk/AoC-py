with open("2015/data/day_11.txt") as f:
    pw = f.read().strip()


def increment(li):
    for k in range(len(li)):
        li[k] += 1
        if li[k] % 26 != 0:
            return li
        li[k] %= 26
    return li


def jump(li, index):
    return [0] * index + increment(li[index:])


def pw_int(pw):
    return [ord(c) - 97 for c in pw][::-1]


def int_pw(li):
    return "".join(chr(el + 97) for el in li[::-1])


def valid(pw):
    pw_k = increment(pw_int(pw))
    while True:
        straight = False
        pair_cnt, pair_check = 0, True
        for i, _ in enumerate(pw_k):
            if pw_k[i] in [8, 11, 14]:
                pw_k = jump(pw_k, i)
                break
            if i < len(pw_k) - 3 and (pw_k[i]) == (pw_k[i + 1]) + 1 == pw_k[i + 2] + 2:
                straight = True
            if i < len(pw_k) - 1 and pair_check and pw_k[i] == pw_k[i + 1]:
                pair_check, pair_cnt = False, pair_cnt + 1
                continue
            pair_check = True
            if straight and pair_cnt >= 2:
                yield int_pw(pw_k)
                pw_k = increment(pw_k)
                break
        else:
            pw_k = increment(pw_k)


valid_gen = valid(pw)


def part1():
    return next(valid_gen)


def part2():
    return next(valid_gen)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
