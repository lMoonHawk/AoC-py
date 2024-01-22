with open("2016/data/day_07.txt") as f:
    ips = [line.strip() for line in f.readlines()]


def has_abba(s):
    for k in range(len(s) - 3):
        if s[k : k + 2] == s[k + 3] + s[k + 2] and s[k] != s[k + 1]:
            return True
    return False


def supports_tls(ip):
    ip = ip.replace("]", "[").split("[")
    supernets, hypernets = ip[::2], ip[1::2]
    for h in hypernets:
        if has_abba(h):
            return False
    for s in supernets:
        if has_abba(s):
            return True
    return False


def supports_ssl(ip):
    ip = ip.replace("]", "[").split("[")
    supernets, hypernets = ip[::2], ip[1::2]
    for s in supernets:
        for k in range(len(s) - 2):
            if s[k] == s[k + 2] and s[k] != s[k + 1]:
                if any(s[k + 1] + s[k] + s[k + 1] in h for h in hypernets):
                    return True
    return False


def part1():
    return sum(supports_tls(ip) for ip in ips)


def part2():
    return sum(supports_ssl(ip) for ip in ips)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
