def parse_json(s, i):
    first_char = s[i]
    if first_char == "{":
        return parse_dict(s, i)
    elif first_char == "[":
        return parse_list(s, i)
    elif first_char == '"':
        return parse_str(s, i)
    else:
        return parse_int(s, i)


def parse_dict(s, i):
    i += 1
    python_dict = {}
    while s[i] != "}":
        key, i = parse_str(s, i)
        value, i = parse_json(s, i + 1)
        python_dict[key] = value
        if s[i] == ",":
            i += 1
    return python_dict, i + 1


def parse_list(s, i):
    i += 1
    python_list = []
    while s[i] != "]":
        python_element, i = parse_json(s, i)
        python_list.append(python_element)
        if s[i] == ",":
            i += 1
    return python_list, i + 1


def parse_str(s, i):
    i += 1
    i0 = i
    while s[i] != '"':
        i += 1
    python_string = s[i0:i]
    return python_string, i + 1


def parse_int(s, i):
    i0 = i
    while s[i].isdigit() or s[i] == "-":
        i += 1
    return int(s[i0:i]), i


with open("2015/data/day_12.txt") as f:
    book_str = f.read().strip()
book, _ = parse_json(book_str, 0)


def sum_node(node, ban_prop=None):
    match node:
        case str():
            return 0
        case int():
            return node
        case list():
            return sum(sum_node(subnode, ban_prop) for subnode in node)
        case dict():
            if ban_prop and ban_prop in node.values():
                return 0
            return sum(sum_node(subnode, ban_prop) for subnode in node.values())


def part1():
    return sum_node(book)


def part2():
    return sum_node(book, "red")


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
