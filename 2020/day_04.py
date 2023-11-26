def part1():
    required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    current_fields = {field: False for field in required_fields}

    answer = 0
    with open("2020/data/day_04.txt") as f:
        for line in f:
            field_names = [field.split(":")[0] for field in line.split(" ")]

            for field_name in field_names:
                if field_name in current_fields:
                    current_fields[field_name] = True

            if line == "\n":
                if sum(current_fields.values()) == len(required_fields):
                    answer += 1
                current_fields = {field: False for field in required_fields}

    if sum(current_fields.values()) == len(required_fields):
        answer += 1
    print(answer)


def check_passeport(fields):
    if "byr" not in fields or int(fields["byr"]) < 1920 or int(fields["byr"]) > 2002:
        return False
    if "iyr" not in fields or int(fields["iyr"]) < 2010 or int(fields["iyr"]) > 2020:
        return False
    if "eyr" not in fields or int(fields["eyr"]) < 2020 or int(fields["eyr"]) > 2030:
        return False
    if "hgt" not in fields:
        return False
    if "in" in fields["hgt"]:
        hgt = fields["hgt"].replace("in", "")
        if not hgt.isdigit() or int(hgt) < 59 or int(hgt) > 76:
            return False
    elif "cm" in fields["hgt"]:
        hgt = fields["hgt"].replace("cm", "")
        if not hgt.isdigit() or int(hgt) < 150 or int(hgt) > 193:
            return False
    else:
        return False
    if (
        "hcl" not in fields
        or fields["hcl"][0] != "#"
        or not all(
            hexa in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
            for hexa in fields["hcl"][1:]
        )
    ):
        return False
    if "ecl" not in fields or fields["ecl"] not in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
        return False
    if "pid" not in fields or len(fields["pid"]) != 9 or not all(num.isdigit() for num in fields["pid"]):
        return False

    return True


def part2():
    answer = 0
    idx = 1
    with open("2020/data/day_04.txt") as f:
        current_fields = dict()
        for line in f:
            if line == "\n":
                # Check if passeport is valid
                answer += check_passeport(current_fields)
                # answer += check_passeport(current_fields)
                # Setup next passeport
                current_fields = dict()
                idx += 1
                continue

            # Parse current row into the field dict
            line = line.strip()
            current_fields.update({field.split(":")[0]: field.split(":")[1] for field in line.split(" ")})

    # Check last passeport
    answer += check_passeport(current_fields)
    print(answer)


if __name__ == "__main__":
    part1()
    part2()
