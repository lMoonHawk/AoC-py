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


def modinv(x, p):
    return pow(x, -1, p)


def rev_cut(deck_n: list, amt: int, index: int):
    return (index + deck_n + amt) % deck_n


def rev_deal_inc(deck_n: list, inc: int, index):
    return modinv(inc, deck_n) * index % deck_n


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


def reverse_shuffle(index, deck_n):
    for inst, arg in reversed(list(shuffle())):
        index = rev_shuffles[inst](deck_n, arg, index)
    return index


def part1():
    index, n = 2019, 10007
    for inst, arg in shuffle():
        index = shuffles[inst](n, arg, index)
    return index


def part2():
    k = 101741582076661
    n = 119315717514047

    # reverse_shuffle(index) = a*index + b

    x = 2020
    # y = a*x+b
    y = reverse_shuffle(x, n)
    # z = a*y+b
    z = reverse_shuffle(y, n)
    # y - z = a*(x - y)
    # => a = (y-z)/(x-y)
    a = (y - z) * modinv(x - y + n, n) % n
    # => b = y-a*x
    b = (y - a * x) % n

    # f^k(x) = a^k*x + a^(k-1)*b + a^(k-2)*b + ... + b
    #        = a^k*x + b * [a^(k-1) + a^(k-2) + ... + 1]
    #        = a^k*x + b*(a^k-1)/(a-1)

    return (pow(a, k, n) * x + b * (pow(a, k, n) - 1) * modinv(a - 1, n)) % n


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
