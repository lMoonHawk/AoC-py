def tokenise(s):
    out = []
    buffer = ""
    for char in s:
        if buffer and char.isupper():
            out.append(buffer)
            buffer = ""
        buffer += char
    return tuple(out + [buffer])


with open("2015/data/day_19.txt") as f:
    rep_s, base = f.read().split("\n\n")
    base = tokenise(base.strip())
    replace = dict()
    replace_rev = dict()
    for line in rep_s.split("\n"):
        before, after = line.split(" => ")
        after = tokenise(after)
        replace_rev[after] = before
        if before not in replace:
            replace[before] = []
        replace[before].append(after)


def part1():
    molecules = set()
    for k, atom in enumerate(base):
        if atom in replace:
            for replacement in replace[atom]:
                molecules.add(base[:k] + replacement + base[k + 1 :])
    return len(molecules)


def part2():
    max_size = max(len(molecule) for molecule in replace_rev)
    goal = ("e",)
    stack = [(base, 0)]
    while stack:
        molecule, steps = stack.pop()
        for start, _ in enumerate(molecule):
            for end in range(start + max_size, start, -1):
                sub = molecule[start:end]
                if sub not in replace_rev:
                    continue
                new_molecule = molecule[:start] + (replace_rev[sub],) + molecule[end:]
                if new_molecule == goal:
                    return steps + 1
                stack.append((new_molecule, steps + 1))


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
