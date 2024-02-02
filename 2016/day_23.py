class Program:
    def __init__(self, inst, r):
        self.inst = inst
        self.r = r

    def evaluate(self, arg):
        if arg.strip("-").isnumeric():
            return int(arg)
        return self.r[arg]

    def run(self, optimisation=None):
        ip = 0
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
            elif op == "tgl":
                toggled_index = ip + self.evaluate(args[0])
                if 0 <= toggled_index < len(self.inst):
                    self.inst[toggled_index][0] = toggles[self.inst[toggled_index][0]]
            ip += 1
        return self.r


def get_program():
    with open("2016/data/day_23.txt") as f:
        return [line.strip().split() for line in f.readlines()]


toggles = {
    "dec": "inc",
    "inc": "dec",
    "tgl": "inc",
    "cpy": "jnz",
    "jnz": "cpy",
}


def part1():
    return Program(get_program(), {"a": 7, "b": 0, "c": 0, "d": 0}).run()["a"]


def part2():
    def optimisation(ip, r):
        # 4: cpy b c
        # 5: inc a
        # 6: dec c
        # 7: jnz c -2
        # 8: dec d
        # 9: jnz d -5
        if ip == 4:
            r["a"] += r["b"] * r["d"]
            r["d"] = 0
            ip = 9
        return ip, r

    return Program(get_program(), {"a": 12, "b": 0, "c": 0, "d": 0}).run(optimisation)["a"]


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
