def get_signal():
    with open("2019/data/day_16.txt") as f:
        return [int(d) for d in f.readline().strip()]


def run_fft(signal, n):
    return [
        abs(
            sum(sum(signal[i : i + k]) for i in range(k - 1, n, 4 * k))
            - sum(sum(signal[i : i + k]) for i in range(3 * k - 1, n, 4 * k))
        )
        % 10
        for k in range(1, n + 1)
    ]


def part1():
    signal = get_signal()
    n = len(signal)

    for _ in range(100):
        signal = run_fft(signal, n)

    return "".join([str(d) for d in signal][:8])


def part2():
    signal = get_signal()
    n = len(signal)

    offset = int("".join([str(d) for d in signal[:7]]))

    m = n * 10_000 - offset  # length needed
    copy_needed = m // n + 1

    relevant = (signal * copy_needed)[-m:]

    for _ in range(100):
        for k, _ in enumerate(relevant):
            if k == 0:
                continue
            relevant[m - 1 - k] += relevant[m - 1 - k + 1]
            relevant[m - 1 - k] %= 10

    return "".join(str(d) for d in relevant[:8])


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
