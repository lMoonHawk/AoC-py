def part1():
    def increment_table(d: dict[str, int], key: str, step):
        if key in d:
            d[key] += step
        else:
            d[key] = step

    rules_next: bool = False
    rules: dict[str, str] = {}
    pair_count: dict[str, int] = {}
    count: dict[str:int] = {}

    # Parsing
    with open("2021/data/day_14.txt") as f:
        for line in f:
            if not rules_next and line != "\n":
                template = line.strip()
            elif line == "\n":
                rules_next = True
            else:
                pair, insert = line.strip().split(" -> ")
                rules[pair] = insert

    # Pair frequency table
    for i in range(len(template) - 1):
        key = template[i : (i + 2)]
        increment_table(pair_count, key, 1)

    # Element frequency table
    count = {elem: template.count(elem) for elem in template}

    for i in range(10):
        new_pair_count = pair_count.copy()

        for key, number in pair_count.items():
            # New element to insert
            insert = rules[key]
            # Creates as many "insert" element as there is pairs creating it
            increment_table(count, insert, number)

            # New pair count considering inserted element
            # AB -> C: AB removed and AC, BC created
            new_pair_count[key] -= number
            if not new_pair_count[key]:
                del new_pair_count[key]

            increment_table(new_pair_count, key[0] + insert, number)
            increment_table(new_pair_count, insert + key[1], number)

        pair_count = new_pair_count

    print(max(count.values()) - min(count.values()))


# Same exact function with 40 instead of 10
def part2():
    def increment_table(d: dict[str, int], key: str, step):
        if key in d:
            d[key] += step
        else:
            d[key] = step

    rules_next: bool = False
    rules: dict[str, str] = {}
    pair_count: dict[str, int] = {}
    count: dict[str:int] = {}

    # Parsing
    with open("2021/data/day_14.txt") as f:
        for line in f:
            if not rules_next and line != "\n":
                template = line.strip()
            elif line == "\n":
                rules_next = True
            else:
                pair, insert = line.strip().split(" -> ")
                rules[pair] = insert

    # Pair frequency table
    for i in range(len(template) - 1):
        key = template[i : (i + 2)]
        increment_table(pair_count, key, 1)

    # Element frequency table
    count = {elem: template.count(elem) for elem in template}

    for i in range(40):
        new_pair_count = pair_count.copy()

        for key, number in pair_count.items():
            # New element to insert
            insert = rules[key]
            # Creates as many "insert" element as there is pairs creating it
            increment_table(count, insert, number)

            # New pair count considering inserted element
            # AB -> C: AB removed and AC, BC created
            new_pair_count[key] -= number
            if not new_pair_count[key]:
                del new_pair_count[key]

            increment_table(new_pair_count, key[0] + insert, number)
            increment_table(new_pair_count, insert + key[1], number)

        pair_count = new_pair_count

    print(max(count.values()) - min(count.values()))


if __name__ == "__main__":
    part1()
    part2()
