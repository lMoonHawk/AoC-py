with open("2023/data/day_11.txt") as f:
    stars = {(x, y) for y, line in enumerate(f.readlines()) for x, s in enumerate(line.strip()) if s == "#"}
xs, ys = [x for x, _ in stars], [y for _, y in stars]
empty_cols = {col for col in range(max(xs)) if col not in xs}
empty_rows = {row for row in range(max(ys)) if row not in ys}


def count_dist(stars, exp):
    dist, done = 0, set()
    for (xs1, ys1), (xs2, ys2) in ((s1, s2) for s1 in stars for s2 in stars if s1 != s2):
        if ((xs2, ys2), (xs1, ys1)) in done:
            continue
        done.add(((xs1, ys1), (xs2, ys2)))
        dist += abs(xs2 - xs1) + abs(ys2 - ys1)
        dist += (exp - 1) * sum(min(xs1, xs2) < ec < max(xs1, xs2) for ec in empty_cols)
        dist += (exp - 1) * sum(min(ys1, ys2) < er < max(ys1, ys2) for er in empty_rows)
    return dist


def part1():
    return count_dist(stars, 2)


def part2():
    return count_dist(stars, 1_000_000)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
