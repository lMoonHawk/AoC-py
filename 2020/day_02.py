def part1():
    answer = 0
    with open("2020/data/day_02.txt") as f:
        for line in f:
            span, letter, password = line.strip().split(" ")

            rule_min, rule_max = [int(rule) for rule in span.split("-")]
            letter = letter[0]

            if rule_min <= password.count(letter) <= rule_max:
                answer += 1
    print(answer)


def part2():
    answer = 0
    with open("2020/data/day_02.txt") as f:
        for line in f:
            span, letter, password = line.strip().split(" ")

            pos1, pos2 = [int(rule) for rule in span.split("-")]
            letter = letter[0]
            # Only valid if position 1 XOR position 2 is equal to the letter
            answer += (password[pos1 - 1] == letter) ^ (password[pos2 - 1] == letter)
    print(answer)


if __name__ == "__main__":
    part1()
    part2()
