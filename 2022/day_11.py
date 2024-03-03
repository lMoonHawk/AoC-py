def monkey_from_desc(desc):
    descs = desc.split("\n")
    items = [int(item) for item in descs[1].split(": ")[1].split(", ")]
    operation = descs[2].split("= ")[1].split()
    div_test = int(descs[3].split()[-1])
    targets = [int(descs[k].split()[-1]) for k in [5, 4]]
    return Monkey(items, operation, div_test, targets)


class Monkey:
    def __init__(self, items, operation, div_test, targets):
        self.items = items
        self.operation = operation
        self.div_test = div_test
        self.targets = targets
        self.inspected = 0

    def inspect(self, item, relief, simplify):
        a, op, b = self.operation
        a = item if a == "old" else int(a)
        b = item if b == "old" else int(b)
        if op == "*":
            result = a * b
        elif op == "+":
            result = a + b
        return (result // relief) % simplify

    def test(self, item):
        return (item % self.div_test) == 0

    def throw_items(self, monkeys, relief, simplify):
        while self.items:
            item = self.items.pop(0)
            item = self.inspect(item, relief, simplify)
            target = self.targets[self.test(item)]
            monkeys[target].items.append(item)
            self.inspected += 1


def prod_largest(k, it):
    largest = [0 for _ in range(k)]
    for cnt in it:
        for i, nb in enumerate(largest):
            if cnt > nb:
                largest.insert(i, cnt)
                del largest[-1]
                break
    prod = 1
    for nb in largest:
        prod *= nb
    return prod


def monkeys_init():
    with open("2022/data/day_11.txt") as f:
        return [monkey_from_desc(desc) for desc in f.read().split("\n\n")]


def get_monkey_business(rounds, monkeys, relief):
    simplify = 1
    for monkey in monkeys:
        simplify *= monkey.div_test
    for _ in range(rounds):
        for monkey in monkeys:
            monkey.throw_items(monkeys, relief, simplify)
    return prod_largest(2, (monkey.inspected for monkey in monkeys))


def part1():
    return get_monkey_business(rounds=20, monkeys=monkeys_init(), relief=3)


def part2():
    return get_monkey_business(rounds=10_000, monkeys=monkeys_init(), relief=1)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
