class Section:
    RULES = 0
    OWN_TICKET = 1
    NEARBY_TICKETS = 2


rules = dict()
nearby_tickets = []
read = Section.RULES
with open("2020/data/day_16.txt") as f:
    for line in f:
        line = line.strip()
        if read == Section.RULES:
            if line == "":
                read += 1
                continue
            key, spans = line.split(": ")
            spans = [[int(bound) for bound in span.split("-")] for span in spans.split(" or ")]
            rules[key] = spans

        elif read == Section.OWN_TICKET:
            if line == "your ticket:":
                continue
            own_ticket = [int(val) for val in line.split(",")]
            read += 1

        else:  # read == Section.NEARBY_TICKETS
            if line == "nearby tickets:" or line == "":
                continue
            nearby_tickets.append([int(val) for val in line.split(",")])


def is_valid(ticket):
    for value in ticket:
        if not any(bounds[0] <= value <= bounds[1] for rule in rules.values() for bounds in rule):
            return False
    return True


def part1():
    answer = 0
    for ticket in nearby_tickets:
        for value in ticket:
            if not any(bounds[0] <= value <= bounds[1] for rule in rules.values() for bounds in rule):
                answer += value

    print(answer)


def part2():
    # List all possible fields for each position
    possible_fields = [None] * len(rules)
    for ticket in nearby_tickets:
        if not is_valid(ticket):
            continue
        for position, value in enumerate(ticket):
            possibilities = set()
            for field, rule in rules.items():
                for bounds in rule:
                    if bounds[0] <= value <= bounds[1]:
                        possibilities.add(field)

            if not possible_fields[position]:
                possible_fields[position] = possibilities
            else:
                possible_fields[position] = possible_fields[position].intersection(possibilities)

    # Process of elimination to get a unique field per position
    # At least one position must have a unique field possible
    fields = dict()
    while len(fields) != len(rules):
        for position, possible_field in enumerate(possible_fields):
            if len(possible_field) == 1:
                fields[position] = list(possible_field)[0]
            else:
                for field in fields.values():
                    possible_fields[position].discard(field)

    answer = 1
    for position, field in fields.items():
        if field[:9] == "departure":
            answer *= own_ticket[position]

    print(answer)


if __name__ == "__main__":
    part1()
    part2()
