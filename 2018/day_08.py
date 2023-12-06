def tree():
    with open("2018/data/day_08.txt") as f:
        return [int(el) for el in f.readline().split()]


def get_metadata(node):
    """Process the node by eating the tree recursively"""
    (children_cnt, meta_cnt), node[:] = node[:2], node[2:]
    totals = sum(get_metadata(node) for _ in range(children_cnt)) + sum(node[:meta_cnt])
    node[:] = node[meta_cnt:]
    return totals


def get_value(node):
    """Process the node by eating the tree recursively"""
    (children_cnt, meta_cnt), node[:] = node[:2], node[2:]
    vals = [get_value(node) for _ in range(children_cnt)]
    out = sum(vals[k - 1] for k in node[:meta_cnt] if 0 < k <= len(vals)) + (sum(node[:meta_cnt]) if not vals else 0)
    node[:] = node[meta_cnt:]
    return out


def part1():
    return get_metadata(tree())


def part2():
    return get_value(tree())


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
