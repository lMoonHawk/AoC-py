def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def parse_sn_number(char_sn_number):
    result = []
    # Instead of evaluating the str to a list, final object is a list
    #   of the str 'elements', e.g.: [  '[',  10,   ',',   3,   ']'   ]
    # This makes the searches for splits and explosions faster
    for i, char in enumerate(char_sn_number):
        to_append = int(char) if is_int(char) else char
        result.append(to_append)
    return result


def explode(sn_number):
    exploded = False
    nest = 0
    # Find a pair with a nest level of 4 (counter at 5 "[")
    for pos, el in enumerate(sn_number):
        if el == "[":
            nest += 1
        elif el == "]":
            nest -= 1
        if nest == 5:
            # Left and right number in the exploding pair
            explode_left = sn_number[pos + 1]
            explode_right = sn_number[pos + 3]
            # Find first element to the left
            left_pos = 0
            for i, el in enumerate(sn_number[: pos + 1]):
                if is_int(el):
                    left_pos = i
            if left_pos:
                sn_number[left_pos] += explode_left
                exploded = True
            # Find first element to the right
            right_pos = 0
            for i, el in enumerate(sn_number[pos + 5 :]):
                if is_int(el):
                    right_pos = i + len(sn_number[: pos + 5])
                    break
            if right_pos:
                sn_number[right_pos] += explode_right
                exploded = True

            # Delete the pair and replace with a 0
            del sn_number[pos : pos + 5]
            sn_number.insert(pos, 0)
            break

    return exploded


def split(sn_number):
    # Find the first occurrence of a number higher than 9 and split it
    for pos, el in enumerate(sn_number):
        if is_int(el) and el > 9:
            del sn_number[pos]
            sn_number[pos:pos] = ["[", el // 2, ",", (el + 1) // 2, "]"]
            break


def reduce(sn_number):
    previous = []
    while sn_number != previous:
        previous = sn_number.copy()

        continue_explosion = True
        while continue_explosion:
            continue_explosion = explode(sn_number)

        split(sn_number)


def magnitude(sn_number):
    nest_lvl = [0]
    for el in sn_number:
        nest = 0
        if el == "[":
            nest = 1
        elif el == "]":
            nest -= 1
        nest_lvl.append(nest_lvl[-1] + nest)

    # Still faster than evaluating and using a recursive function on a list
    while len(sn_number) > 1:
        current_nest = max(nest_lvl)
        ind = nest_lvl.index(current_nest)
        left, right = sn_number[ind], sn_number[ind + 2]

        del sn_number[ind - 1 : ind + 4]
        del nest_lvl[ind : ind + 5]

        sn_number.insert(ind - 1, left * 3 + right * 2)
        nest_lvl.insert(ind, current_nest - 1)

    return sn_number[0]


def part1():

    with open("2021/data/day_18.txt") as f:
        # Parsing
        first = True
        for line in f:
            sn_number = parse_sn_number(line.strip())

            if first:
                first = False
                reduced_sn_number = sn_number
                continue

            sn_number = ["["] + reduced_sn_number + [","] + sn_number + ["]"]
            # Call explode and split until stabilized
            reduce(sn_number)

            reduced_sn_number = sn_number

    print(magnitude(sn_number))


def part2():
    with open("2021/data/day_18.txt") as f:
        # Parsing
        sn_numbers = []
        for line in f:
            sn_numbers.append(parse_sn_number(line.strip()))

        magnitude_max = 0
        for sn_number_i in sn_numbers:
            for sn_number_j in sn_numbers:
                sn_number = ["["] + sn_number_i + [","] + sn_number_j + ["]"]
                reduce(sn_number)
                current_magnitude = magnitude(sn_number)
                magnitude_max = max(magnitude_max, current_magnitude)

    print(magnitude_max)


if __name__ == "__main__":
    part1()
    part2()
