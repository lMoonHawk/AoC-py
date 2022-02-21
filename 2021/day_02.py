def part1():

    counter = {
        "forward": 0,
        "down": 0,
        "up": 0}

    with open("data/2021_2.txt") as f:
        for line in f:
            instruction = line.split()
            counter[instruction[0]] += int(instruction[1])

        horizontal = counter["forward"]
        depth = counter["down"] - counter["up"]

        print(horizontal * depth)

def part2():

    depth = 0

    counter = {
        "forward": 0,
        "down": 0,
        "up": 0}

    with open("data/2021_2.txt") as f:
        for line in f:
            instruction = line.split()
            counter[direction := instruction[0]] += (amount := int(instruction[1]))

            if direction == "forward":
                depth += amount * (counter["down"] - counter["up"])

        horizontal = counter["forward"]

        print(horizontal * depth)


if __name__ == '__main__':
    part1()
    part2()