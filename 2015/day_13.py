with open("2015/data/day_13.txt") as f:
    ref = {
        tuple([line[0], line[-1][:-1]]): (2 * (line[2] == "gain") - 1) * int(line[3])
        for line in (line.split() for line in f.readlines())
    }
    guests = {guest for pair in ref for guest in pair}


def get_max_hap(ref, guests):
    stack = [(guest, 0, {guest}, guest) for guest in guests]
    max_hap = None
    while stack:
        guest, tot_hap, table, first = stack.pop()
        remaining = [guest for guest in guests if guest not in table]
        if not remaining:
            tot_hap += ref[(guest, first)] + ref[(first, guest)]
            max_hap = max(max_hap, tot_hap) if max_hap is not None else tot_hap
        for n_guest in remaining:
            n_tot_hap = tot_hap + ref[(guest, n_guest)] + ref[(n_guest, guest)]
            stack.append((n_guest, n_tot_hap, table | {n_guest}, first))
    return max_hap


def part1():
    return get_max_hap(ref, guests)


def part2():
    for guest in guests:
        ref[("", guest)] = ref[(guest, "")] = 0
    guests.add("")
    return get_max_hap(ref, guests)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
