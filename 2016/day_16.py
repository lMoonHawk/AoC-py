with open("2016/data/day_16.txt") as f:
    init = f.read().strip()


def expand(s):
    return s + "0" + "".join("1" if c == "0" else "0" for c in s[::-1])


def curve(n):
    return str(1 - (((n // (n & -n)) % 4) == 1))


def part1():
    n = init
    while len(n) < 272:
        n = expand(n)
    n = n[:272]
    while True:
        buffer = ""
        for k in range(0, len(n), 2):
            buffer += str(int(n[k] == n[k + 1]))
        if len(buffer) % 2:
            return buffer
        n = buffer


def resolve_cs(n, memo={}):
    """Returns the final '1' or '0' given 2^k elements"""
    if n in memo:
        return memo[n]
    size = len(n)
    if size == 2:
        return str(int(n[0] == n[1]))
    else:
        memo[n] = str(int(resolve_cs(n[: size // 2]) == resolve_cs(n[size // 2 :])))
        return memo[n]


def part2():
    size_init = len(init)
    size = 35_651_584
    # size of the final checksum
    # n = k // (k&k) get n such that k = n*2^x
    cs_size = size // (size & -size)
    # amount of digits compared for each digit in the final checksum
    chunk_size = size // cs_size

    a = init
    b = "".join("1" if c == "0" else "0" for c in a[::-1])

    data = [a + curve(index) + b + curve(index + 1) for index in range(1, size // size_init, 2)]
    data = "".join(data)[:size]
    return "".join(resolve_cs(chunk) for chunk in (data[k : k + chunk_size] for k in range(0, size, chunk_size)))


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
