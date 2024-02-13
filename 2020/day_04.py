def passeports():
    with open("2020/data/day_04.txt") as f:
        yield from (
            {k: v for k, v in (el.split(":") for el in line.replace("\n", " ").split())}
            for line in f.read().split("\n\n")
        )


required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
validation = {
    "byr": lambda x: 1920 <= int(x) <= 2002,
    "iyr": lambda x: 2010 <= int(x) <= 2020,
    "eyr": lambda x: 2020 <= int(x) <= 2030,
    "hgt": lambda x: ("in" in x and 59 <= int(x.rstrip("in")) <= 76)
    or ("cm" in x and 150 <= int(x.rstrip("cm")) <= 193),
    "hcl": lambda x: x[0] == "#" and len(x) == 7 and all(char in "abcdef0123456789" for char in x[1:]),
    "ecl": lambda x: x in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
    "pid": lambda x: len(x) == 9 and all(el.isdigit() for el in x),
    "cid": lambda _: True,
}


def part1():
    return sum(all(field in passeport for field in required_fields) for passeport in passeports())


def part2():
    return sum(
        all(validation[field](value) for field, value in passeport.items())
        for passeport in passeports()
        if all(field in passeport for field in required_fields)
    )


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
