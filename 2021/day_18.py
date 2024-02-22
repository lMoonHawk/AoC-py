class Value:
    def __init__(self, num, depth):
        self.num = int(num)
        self.depth = depth


class SnailfishNumber(list):
    def explode(self):
        for k, value in enumerate(self):
            if value.depth < 4:
                continue
            if k > 0:
                self[k - 1].num += value.num
            if k < len(self) - 2:
                self[k + 2].num += self[k + 1].num
            self[k : k + 2] = [Value(0, value.depth - 1)]
            return True
        return False

    def split(self):
        for k, value in enumerate(self):
            if value.num >= 10:
                left = value.num // 2
                right = value.num - left
                self[k : k + 1] = [Value(left, value.depth + 1), Value(right, value.depth + 1)]
                return True
        return False

    def __add__(self, other):
        out = SnailfishNumber([Value(v.num, v.depth + 1) for v in self] + [Value(v.num, v.depth + 1) for v in other])
        while out.explode() or out.split():
            pass
        return out

    def magnitude(self):
        out = SnailfishNumber([Value(v.num, v.depth) for v in self])
        while len(out) > 1:
            max_depth = max(out, key=lambda x: x.depth).depth
            for k, value in enumerate(out):
                if value.depth == max_depth:
                    out[k : k + 2] = [Value(3 * out[k].num + 2 * out[k + 1].num, value.depth - 1)]
        return out[0].num


def str_to_sfn(s):
    depth = -1
    sn = []
    for char in s:
        if char == "[":
            depth += 1
        elif char == "]":
            depth -= 1
        elif char.isdigit():
            sn.append(Value(char, depth))
    return SnailfishNumber(sn)


with open("2021/data/day_18.txt") as f:
    nums = [str_to_sfn(s) for s in f.readlines()]


def part1():
    return sum(nums[1:], nums[0]).magnitude()


def part2():
    return max(max((a + b).magnitude(), (b + a).magnitude()) for k, a in enumerate(nums[:-1]) for b in nums[k + 1 :])


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
