bags = dict()
with open("2020/data/day_07.txt") as f:
    for line in f:
        line = line.strip()
        key, content = line.split(" bags contain ")

        key = key.replace(" ", "")
        content = content.replace("bags", "bag").replace(" bag", "").replace(".", "")
        content = content.split(", ")

        inside = []
        for bag in content:
            if bag == "no other":
                continue
            number = int("".join(x for x in bag if x.isdigit()))
            colour = "".join(x for x in bag if x.isalpha())
            inside.append((number, colour))
        bags[key] = inside


def part1():
    memo = {key: False for key in bags}

    def traverse_bag(key, path=None):
        if path is None:
            path = [key]

        content = bags[key]

        if "shinygold" in [colour for _, colour in content]:
            return True

        for _, bag in content:
            new_path = path + [bag]
            if memo[bag] or traverse_bag(bag, new_path):
                for has_shinygold in new_path:
                    memo[has_shinygold] = True
                return True

        return False

    answer = 0
    for key in bags:
        answer += traverse_bag(key)
    print(answer)


def part2():
    def traverse_count(key):
        content = bags[key]
        if not content:
            return 0

        bag_count = 0
        for number, colour in content:
            bag_count += number * (traverse_count(colour) + 1)

        return bag_count

    print(traverse_count("shinygold"))


if __name__ == "__main__":
    part1()
    part2()
