with open("2022/data/day_25.txt") as f:
    snafus = [line.strip() for line in f]


def snafu_to_dec(snafu):
    char = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
    return sum(char[c] * (5 ** (len(snafu) - n - 1)) for n, c in enumerate(snafu))


def dec_to_snafu(dec):
    char = {-2: "=", -1: "-", 0: "0", 1: "1", 2: "2"}
    max_digit = 0
    cumsum = [0]
    while dec > 2 * 5**max_digit:
        cumsum.append(cumsum[-1] + 5**max_digit)
        max_digit += 1
    buffer = ""
    for i in range(max_digit, -1, -1):
        current = 5**i
        for d in char:
            num = d * current
            # We apply this most significant digit "d"
            # If this is lower than target, check if we can compensate with all lower digits = 2
            # If this is higher than target, check if we can compensate with all lower digits = -2
            if (dec - 2 * cumsum[i] <= num < dec) or (dec < num <= dec + 2 * cumsum[i]):
                buffer += char[d]
                dec -= num
                break
    return buffer + char[dec]


def part1():
    return dec_to_snafu(sum(snafu_to_dec(snafu) for snafu in snafus))


def part2():
    return


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
