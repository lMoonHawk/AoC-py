with open("2016/data/day_18.txt") as f:
    row_init = [tile == "^" for tile in f.read().strip()]
    row_size, row_init = len(row_init), sum(tile << i for i, tile in enumerate(row_init))


def pprint(row):
    return f"{bin(row)[2:]:0>10}"


def count_safe_tiles(row, n):
    # trap if A & B & ~C | ~A & B & C | ~A & ~B & C | A & ~B & ~C
    # <=> trap if A & ~C | ~A & C
    # <=> trap if A^C
    mask = 2**row_size - 1
    row = row_init
    total = row_size - row.bit_count()
    for _ in range(n - 1):
        row = ((row << 1) ^ (row >> 1)) & mask
        total += row_size - row.bit_count()
    return total


def part1():
    return count_safe_tiles(row_init, 40)


def part2():
    return count_safe_tiles(row_init, 400_000)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
