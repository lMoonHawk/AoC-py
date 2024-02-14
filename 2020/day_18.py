operation = {"+": lambda a, b: int(a) + int(b), "*": lambda a, b: int(a) * int(b)}


def expressions():
    with open("2020/data/day_18.txt") as f:
        yield from (list(line.strip().replace(" ", "")) for line in f)


def evaluate(expr: list[str], prec: dict[str, int]):
    """Shunting yard algorithm implementation with built-in evaluation."""
    # out builds a RPN from the infix expression and evaluates the stack inplace when given an operator
    out = []
    op = []
    while expr:
        token = expr.pop(0)
        if token.isdigit():
            out.append(token)
        else:
            while op and "(" not in [op[-1], token] and (token not in prec or prec[op[-1]] >= prec[token]):
                out.append(operation[op.pop()](out.pop(), out.pop()))
            if token == ")":
                op.pop()
            else:
                op.append(token)
    while op:
        out.append(operation[op.pop()](out.pop(), out.pop()))
    return out[0]


def part1():
    return sum(evaluate(expression, {"+": 0, "*": 0}) for expression in expressions())


def part2():
    return sum(evaluate(expression, {"+": 1, "*": 0}) for expression in expressions())


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
