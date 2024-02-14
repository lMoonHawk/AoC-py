with open("2020/data/day_16.txt") as f:
    rules, own, nearby = f.read().split("\n\n")
own = [int(field) for field in own.split("\n")[1].split(",")]
nearby = [[int(field) for field in ticket.split(",")] for ticket in nearby.strip().split("\n")[1:]]
rules = {
    key: [[int(bound) for bound in span.split("-")] for span in spans.split(" or ")]
    for key, spans in (field.split(": ") for field in rules.split("\n"))
}


def valid_fields(value):
    return {field for field, rule in rules.items() for bounds in rule if bounds[0] <= value <= bounds[1]}


def part1():
    return sum(value for ticket in nearby for value in ticket if not valid_fields(value))


def part2():
    blueprint = [set(rules) for _ in range(len(own))]
    positions = [None for _ in range(len(own))]

    for ticket in nearby:
        for position, value in enumerate(ticket):
            fields = valid_fields(value)
            if not fields:
                break
            blueprint[position].intersection_update(fields)

    while any(field is None for field in positions):
        for position, field in enumerate(blueprint):
            if len(field) == 1:
                (positions[position],) = field
            else:
                blueprint[position].difference_update({field for field in positions})

    answer = 1
    for position, field in enumerate(positions):
        if field.startswith("departure"):
            answer *= own[position]
    return answer


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
