def part1():

    nb_stacks = 0
    stacksmap_flag = True

    with open("2022/data/day_05.txt") as f:
        for line in f:

            if not nb_stacks:
                # 3 chars per crates + space between - newline char
                nb_stacks = (len(line)) // 4
                # Prepare the data structure
                stacks = [[] for i in range(nb_stacks)]

            if line == "\n" or line.strip().startswith("1"):
                stacksmap_flag = False
                # Wait for instructions
                continue

            if stacksmap_flag:
                # Parse stacks of crates
                for i in range(nb_stacks):
                    # 3 chars long + space in between
                    crate = line[i * 4 : i * 4 + 3]
                    # Remove brackets and spaces
                    crate = crate.translate({ord(i): None for i in " []"})
                    if crate:
                        stacks[i].append(crate)
            else:
                # Instructions parsing & processing
                count, start, end = [
                    int(el) for el in line.split() if el.isdigit()
                ]
                for i in range(count):
                    stacks[end - 1].insert(0, stacks[start - 1].pop(0))

    # Show top of stacks
    print("".join([el[0] for el in stacks]))


def part2():
    nb_stacks = 0
    stacksmap_flag = True

    with open("2022/data/day_05.txt") as f:
        for line in f:

            if not nb_stacks:
                # 3 chars per crates + space between - newline char
                nb_stacks = (len(line)) // 4
                # Prepare the data structure
                stacks = [[] for i in range(nb_stacks)]

            if line == "\n" or line.strip().startswith("1"):
                stacksmap_flag = False
                # Wait for instructions
                continue

            if stacksmap_flag:
                # Parse stacks of crates
                for i in range(nb_stacks):
                    # 3 chars long + space in between
                    crate = line[i * 4 : i * 4 + 3]
                    # Remove brackets and spaces
                    crate = crate.translate({ord(i): None for i in " []"})
                    if crate:
                        stacks[i].append(crate)
            else:
                # Instructions parsing & processing
                count, start, end = [
                    int(el) for el in line.split() if el.isdigit()
                ]
                # Reverse crates
                stacks[start - 1][:count] = stacks[start - 1][:count][::-1]
                for i in range(count):
                    stacks[end - 1].insert(0, stacks[start - 1].pop(0))

    # Show top of stacks
    print("".join([el[0] for el in stacks]))


if __name__ == "__main__":
    part1()
    part2()
