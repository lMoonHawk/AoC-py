# Breaking the challenge... I am not going to create my own MD5 hash function, especially without access to math.
from hashlib import md5

with open("2016/data/day_14.txt") as f:
    salt = f.read().strip()


def in_a_row(s):
    counter, streak, char = 1, None, None
    for k in range(1, len(s)):
        if s[k] == s[k - 1]:
            counter += 1
            if (counter == 3 and not streak) or (counter == 5 and streak == 3):
                streak = counter
                char = s[k]
                if streak == 5:
                    return streak, char
        else:
            counter = 1
    return streak, char


def add(d, k, v):
    if k not in d:
        d[k] = []
    d[k].append(v)


def md5_stretch(s, times):
    for _ in range(times):
        s = md5(str.encode(s)).hexdigest()
    return s


def get_last_index(hash_times):
    index = 0
    candidates = dict()
    keys_cnt = 0
    while True:
        streak, c = in_a_row(md5_stretch(f"{salt}{index}", hash_times))
        if streak:
            add(candidates, c, index)
            if streak == 5:
                if c not in candidates:
                    continue
                while candidates[c]:
                    if candidates[c][0] >= index - 1000:
                        if candidates[c][0] == index:
                            break
                        key = candidates[c].pop(0)
                        keys_cnt += 1
                        if keys_cnt == 64:
                            return key
                    else:
                        candidates[c].pop(0)
        index += 1


def part1():
    return get_last_index(1)


def part2():
    return get_last_index(2017)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
