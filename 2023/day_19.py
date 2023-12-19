wfs = dict()
parts = []
with open("2023/data/day_19.txt") as f:
    parts_part = False
    for line in f:
        if line == "\n":
            parts_part = True
            continue
        if not parts_part:
            label, inst = line.strip().replace("}", "").split("{")
            wfs[label] = [
                (s[0][0], s[0][1], int(s[0][2:]), s[1]) if any(var in s[0] for var in "<>") else (s[0],)
                for s in [cond.split(":") for cond in inst.split(",")]
            ]
        else:
            parts.append(
                {
                    s.split("=")[0]: int(s.split("=")[1])
                    for s in line.strip().replace("{", "").replace("}", "").split(",")
                }
            )
            pass


def is_accepted(part, wfs):
    label = "in"
    while True:
        for rule in wfs[label]:
            if len(rule) == 1:
                (dest,) = rule
            else:
                var, op, num, dest = rule
                if not ((op == "<" and part[var] < num) or (op == ">" and part[var] > num)):
                    continue
            if dest in ["A", "R"]:
                return dest == "A"
            else:
                label = dest
                break


def count_set(bounds):
    out = 1
    for lo, hi in bounds.values():
        out *= hi - lo + 1
    return out


def part1():
    return sum(sum(part.values()) for part in parts if is_accepted(part, wfs))


def part2():
    process = [("in", {var: (1, 4000) for var in "xmas"})]
    accepted = 0

    while process:
        label, bounds = process.pop()

        if label in ["A", "R"]:
            accepted += (label == "A") * count_set(bounds)
            continue

        for rule in wfs[label]:
            if len(rule) == 1:
                (dest,) = rule
                process.append((dest, bounds))
                break
            var, op, num, dest = rule
            lo, hi = bounds[var]
            if (op == "<" and hi < num) or (op == ">" and lo > num):
                process.append((dest, bounds))
                break
            elif op == "<":
                process.append((dest, dict(bounds, **{var: (lo, num - 1)})))
                bounds[var] = num, hi
            elif op == ">":
                process.append((dest, dict(bounds, **{var: (num + 1, hi)})))
                bounds[var] = lo, num

    return accepted


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
