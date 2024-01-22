# Breaking the challenge... I am not going to create my own MD5 hash function, especially without access to math.
from hashlib import md5

with open("2016/data/day_05.txt") as f:
    d_id = f.readline().strip()


def part1():
    index = 0
    password = ""
    while True:
        hashed = md5(str.encode(f"{d_id}{index}")).hexdigest()
        if hashed.startswith("0" * 5):
            password += hashed[5]
            if len(password) == 8:
                return password
        index += 1


def part2():
    index = 0
    password = [None] * 8
    while True:
        hashed = md5(str.encode(f"{d_id}{index}")).hexdigest()
        if hashed.startswith("0" * 5):
            pos = hashed[5]
            if pos.isdigit() and 0 <= int(pos) < 8 and not password[int(pos)]:
                password[int(pos)] = hashed[6]
                if None not in password:
                    return "".join(password)
        index += 1


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
