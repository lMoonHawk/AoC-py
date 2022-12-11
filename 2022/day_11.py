class Monkey:
    business = 0

    def inspects(self, relief, simplify):
        self.business += 1

        if self.operator == "*":
            if self.amount == "old":
                new = self.items[0] ** 2
            else:
                new = self.items[0] * int(self.amount)
        else:
            if self.amount == "old":
                new = self.items[0] * 2
            else:
                new = self.items[0] + int(self.amount)

        self.items[0] = (new // relief) % simplify

    def tests(self):
        if (self.items[0] % self.test) == 0:
            return self.throw[0]
        return self.throw[1]


def parse_file():
    # List of instances of class Monkey
    monkeys = []
    # Product of divisibility tests numbers.
    # Tests with "(worry_level) mod (simplify)" will be equivalent
    simplify = 1
    with open("2022/data/day_11.txt") as f:
        for line in f:
            line = line.strip()
            if line.startswith("Monkey"):
                monkeys.append(Monkey())
            if line.startswith("Starting items"):
                items = line.split(": ")[1].split(", ")
                monkeys[-1].items = [int(item) for item in items]
            if line.startswith("Operation"):
                operator, amount = line.split("old ")[1].split()
                monkeys[-1].operator = operator
                monkeys[-1].amount = amount
            if line.startswith("Test"):
                test = int(line.split("by ")[1])
                simplify *= test
                monkeys[-1].test = int(line.split("by ")[1])
            if line.startswith("If true"):
                monkeys[-1].throw = [int(line.split("monkey ")[1])]
            if line.startswith("If false"):
                monkeys[-1].throw.append(int(line.split("monkey ")[1]))

    return monkeys, simplify


def part1():
    monkeys, simplify = parse_file()

    for _ in range(20):
        for monkey in monkeys:
            for _ in range(len(monkey.items)):
                monkey.inspects(relief=3, simplify=simplify)
                throw_to = monkey.tests()
                monkeys[throw_to].items.append(monkey.items.pop(0))

    most_active = sorted([monkey.business for monkey in monkeys])[-2:]
    print(most_active[0] * most_active[1])


def part2():
    monkeys, simplify = parse_file()

    for i in range(10_000):
        for monkey in monkeys:
            for _ in range(len(monkey.items)):
                monkey.inspects(relief=1, simplify=simplify)
                throw_to = monkey.tests()
                monkeys[throw_to].items.append(monkey.items.pop(0))

    most_active = sorted([monkey.business for monkey in monkeys])[-2:]
    print(most_active[0] * most_active[1])


if __name__ == "__main__":
    part1()
    part2()
