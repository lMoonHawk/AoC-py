with open("2023/data/day_15.txt") as f:
    seq = f.read().strip().split(",")


def hash(s, out=0):
    for c in s:
        out = ((out + ord(c)) * 17) % 256
    return out


def part1():
    return sum(hash(step) for step in seq)


def part2():
    boxes = [[] for _ in range(256)]
    for step in seq:
        if "=" in step:
            label, fl = step.split("=")
            replace = False
            for lens, (box_label, _) in enumerate(boxes[hash(label)]):
                if label == box_label:
                    boxes[hash(label)][lens] = (label, fl)
                    replace = True
                    break
            if not replace:
                boxes[hash(label)].append((label, fl))
        else:
            label, _ = step.split("-")
            for lens, (box_label, _) in enumerate(boxes[hash(label)]):
                if label == box_label:
                    del boxes[hash(label)][lens]
                    break

    return sum((1 + nb) * (slot + 1) * int(fl) for nb, box in enumerate(boxes) for slot, (_, fl) in enumerate(box))


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
