with open("2017/data/day_09.txt") as f:
    stream = f.readline().strip()


def parse_stream(stream):
    depth = score = garbage = 0
    ignore_group = ignore_next = False
    for char in stream:
        if ignore_next:
            ignore_next = False
            continue
        elif char == "!":
            ignore_next = True
        elif char == ">":
            ignore_group = False
        elif ignore_group:
            garbage += 1
            continue
        elif char == "<":
            ignore_group = True
        elif char == "{":
            depth += 1
        elif char == "}":
            score += depth
            depth -= 1
    return score, garbage


def part1():
    score, _ = parse_stream(stream)
    return score


def part2():
    _, garbage = parse_stream(stream)
    return garbage


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
