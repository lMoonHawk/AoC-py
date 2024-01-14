class Instruction:
    def __init__(self, reg, inc, val, cond_reg, cond_op, cond_val):
        self.reg = reg
        self.val = int(val) if inc == "inc" else -int(val)
        self.cond_reg = cond_reg
        self.cond_op = cond_op
        self.cond_val = int(cond_val)

    def check_condition(self, cond_reg_val):
        if self.cond_op == ">" and cond_reg_val > self.cond_val:
            return True
        elif self.cond_op == ">=" and cond_reg_val >= self.cond_val:
            return True
        elif self.cond_op == "<" and cond_reg_val < self.cond_val:
            return True
        elif self.cond_op == "<=" and cond_reg_val <= self.cond_val:
            return True
        elif self.cond_op == "==" and cond_reg_val == self.cond_val:
            return True
        elif self.cond_op == "!=" and cond_reg_val != self.cond_val:
            return True
        return False

    def evaluate(self, registers):
        if self.reg not in registers:
            registers[self.reg] = 0
        if self.cond_reg not in registers:
            registers[self.cond_reg] = 0
        if self.check_condition(registers[self.cond_reg]):
            registers[self.reg] += self.val


def evaluate_instructions(instructions):
    max_reg_ever, registers = 0, dict()
    for instruction in instructions:
        instruction.evaluate(registers)
        max_reg = max(registers.values())
        max_reg_ever = max_reg if max_reg > max_reg_ever else max_reg_ever
    return max_reg_ever, max_reg


def instructions():
    with open("2017/data/day_08.txt") as f:
        for line in f:
            yield Instruction(*line.strip().replace(" if", "").split())


def part1():
    max_reg, _ = evaluate_instructions(instructions())
    return max_reg


def part2():
    _, max_reg_ever = evaluate_instructions(instructions())
    return max_reg_ever


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
