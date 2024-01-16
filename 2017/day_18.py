with open("2017/data/day_18.txt") as f:
    instructions = [line.strip().split() for line in f.readlines()]


class Program:
    def __init__(self, pid=0):
        self.pid = pid
        self.pointer = 0
        self.registers = {"p": pid}
        self.queue = []
        self.sent_cnt = 0

    def access(self, register):
        if register not in self.registers:
            self.registers[register] = 0
        return self.registers[register]

    def evaluate(self, args):
        r = args[0]
        values = []
        for value in args:
            if not value.strip("-").isnumeric():
                values.append(self.access(value))
            else:
                values.append(int(value))
        return r, values[0], values[1] if len(values) == 2 else None

    def send(self):
        registers = self.registers
        send_queue = []

        while 0 <= self.pointer < len(instructions):
            op, *args = instructions[self.pointer]
            r, val1, val2 = self.evaluate(args)

            if op == "set":
                registers[r] = val2
            elif op == "add":
                registers[r] = val1 + val2
            elif op == "mul":
                registers[r] = val1 * val2
            elif op == "mod":
                registers[r] = val1 % val2
            elif op == "jgz" and val1 > 0:
                self.pointer += val2 - 1
            elif op == "snd":
                send_queue.append(val1)
                self.sent_cnt += 1
            elif op == "rcv":
                if not self.queue:
                    return send_queue
                registers[r] = self.queue.pop(0)
            self.pointer += 1
        self.pointer = -1
        return send_queue


def part1():
    return Program().send()[-1]


def part2():
    p0, p1 = Program(pid=0), Program(pid=1)
    while True:
        p0.queue.extend(p1.send())
        p1.queue.extend(p0.send())
        if not p0.queue and not p1.queue:
            return p1.sent_cnt


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
