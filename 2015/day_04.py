# Breaking the challenge... I am not going to create my own MD5 hash function, especially without access to math.
from hashlib import md5

with open("2015/data/day_04.txt") as f:
    key = f.read().strip()


def mine(lead_z):
    num = 0
    while True:
        if md5(str.encode(f"{key}{num}")).hexdigest().startswith("0" * lead_z):
            return num
        num += 1


def part1():
    return mine(5)


def part2():
    return mine(6)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
