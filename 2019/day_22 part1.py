def shuffle():
    with open("2019/data/day_22.txt") as f:
        for line in f:
            if not line.strip():
                break
            if "increment" in line:
                inst, arg = "inc", int(line.split("deal with increment ")[1])
            elif "stack" in line:
                inst, arg = "stack", None
            else:
                inst, arg = "cut", int(line.split("cut ")[1])
            yield inst, arg


def deal_stack(deck_n: list, _, index: int):
    return deck_n - index - 1


def cut(deck_n: list, amt: int, index: int):
    return (index - amt) % deck_n


def deal_inc(deck_n: list, inc: int, index):
    return (index * inc) % deck_n


def rev_cut(deck_n: list, amt: int, index: int):
    return (index - deck_n + amt) % deck_n


def rev_deal_inc(deck_n: list, inc: int, index):
    return (index * pow(inc, -1, deck_n)) % deck_n


shuffles = {
    "stack": deal_stack,
    "cut": cut,
    "inc": deal_inc,
}
rev_shuffles = {
    "stack": deal_stack,
    "cut": rev_cut,
    "inc": rev_deal_inc,
}


def part1():
    index, n = 2019, 10007
    for inst, arg in shuffle():
        index = shuffles[inst](n, arg, index)
    return index


def part2():
    return None


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
