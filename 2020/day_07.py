bags = dict()
with open("2020/data/day_07.txt") as f:
    for line in f:
        key, content = line.strip().split(" bags contain ")
        bags[key] = [
            (int(num), " ".join(col)) for num, *col in (bag.split()[:-1] for bag in content.split(", ")) if num != "no"
        ]


def has_shiny_gold(bag):
    if bag == "shiny gold":
        return True
    return any(has_shiny_gold(sub_bag) for _, sub_bag in bags[bag])


def cnt_bags(bag):
    if not bags[bag]:
        return 1
    return 1 + sum(cnt * cnt_bags(sub_bag) for cnt, sub_bag in bags[bag])


def part1():
    return sum(has_shiny_gold(bag) for bag in bags if bag != "shiny gold")


def part2():
    return cnt_bags("shiny gold") - 1  # remove 1 for initial bag


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
