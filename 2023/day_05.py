def get_almanach():
    with open("2023/data/day_05.txt") as f:
        cats = f.read().split("\n\n")

    seeds = [int(el) for el in cats[0].split()[1:]]
    maps = [
        [[int(el) for el in line.split()] for line in map.split("\n") if "map" not in line and line != ""]
        for map in cats[1:]
    ]
    return seeds, maps


def lookup(source: int, table: list[list[int]]) -> int:
    for dest_start, source_start, length in table:
        if not source_start <= source <= source_start + length:
            continue
        return dest_start + source - source_start
    return source


def intersec(r1: list[int], r2: list[int]) -> list[int]:
    """Return the range intersection between r1 and r2.
    The range format is [start, len]"""
    (r1_s, r1_l), (r2_s, r2_l) = r1, r2
    r1_e, r2_e = r1_s + r1_l, r2_s + r2_l

    if r1_s > r2_e or r2_s > r1_e:
        return None
    r_s = max(r1_s, r2_s)
    r_l = min(r1_e, r2_e) - r_s
    return [r_s, r_l]


def exclude(r1: list[int], r2: list[int]) -> list[int]:
    """Return ranges in r1 not in r2.
    The range format is [start, len]"""
    (r1_s, r1_l), (r2_s, r2_l) = r1, r2
    r1_e, r2_e = r1_s + r1_l - 1, r2_s + r2_l - 1

    # non overlapping
    if r1_s > r2_e or r2_s > r1_e:
        return [r1]
    # r2 overlapps on the left
    if r2_s < r1_s and r1_s <= r2_e < r1_e:
        return [[r2_e, r1_e - r2_e]]
    # r2 overlapps on the right
    if r1_e < r2_e and r1_s < r2_s <= r1_e:
        return [[r1_s, r2_s - r1_s]]
    # r2 in r1
    if r2_s >= r1_s and r2_e <= r1_e:
        ret = []
        if r2_s - r1_s > 0:
            ret.append([r1_s, r2_s - r1_s])
        if r1_e - r2_e > 0:
            ret.append([r2_e + 1, r1_e - r2_e])
        return ret
    # r1 in r2
    if r2_s <= r1_s and r2_e >= r1_e:
        return [[]]


def lookup_range(sources: list[int], table: list[list[int]]) -> list[list[int]]:
    in_ranges = []
    out_ranges = []
    for dest_start, source_start, length in table:
        if r := intersec(sources, [source_start, length]):
            r_start, r_len = r
            in_ranges.append([r_start, r_len])
            out_ranges.append([dest_start + r_start - source_start, r_len])

    sections = [sources]
    for exclusion in in_ranges:
        new_sections = []
        for section in sections:
            new_sections.extend(exclude(section, exclusion))
        sections = new_sections

    out_ranges.extend(sections)

    return out_ranges


def part1():
    seeds, maps = get_almanach()
    for map in maps:
        for index, seed in enumerate(seeds):
            seeds[index] = lookup(seed, map)
    return min(seeds)


def part2():
    seeds, maps = get_almanach()

    conversion = [seeds[k : k + 2] for k in range(0, len(seeds), 2)]
    for map in maps:
        converted = []
        for index in range(len(conversion)):
            converted.extend(lookup_range(conversion[index], map))
        conversion = converted
    return min(conversion)[0]


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
