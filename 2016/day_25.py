def get_program():
    with open("2016/data/day_25.txt") as f:
        return [line.strip().split() for line in f.readlines()]


class Program:
    def __init__(self, inst, r):
        self.inst = inst
        self.r = r
        self.ip = 0

    def evaluate(self, arg):
        if arg.strip("-").isnumeric():
            return int(arg)
        return self.r[arg]

    def run(self, optimisation=None):
        ip = self.ip
        while 0 <= ip < len(self.inst):
            if optimisation:
                ip, self.r = optimisation(ip, self.r)
            op, *args = self.inst[ip]
            if op == "cpy":
                if args[1] in self.r:
                    self.r[args[1]] = self.evaluate(args[0])
            elif op == "inc":
                if args[0] in self.r:
                    self.r[args[0]] += 1
            elif op == "dec":
                if args[0] in self.r:
                    self.r[args[0]] -= 1
            elif op == "jnz":
                ip += -1 + self.evaluate(args[1]) if self.evaluate(args[0]) else 0
            elif op == "out":
                self.ip = ip + 1
                return self.evaluate(args[0])
            ip += 1
        return


def part1():
    def optimisation(ip, r):
        if ip == 4:
            r["a"] += r["b"] * r["c"]
            r["d"] = r["a"]
            ip = 10
        return ip, r

    a = 0
    while True:
        p = Program(get_program(), {"a": a, "b": 0, "c": 0, "d": 0})
        for k in range(10):
            if p.run(optimisation) % 2 != k % 2:
                break
        else:
            return a
        a += 1


def part2():
    return


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
