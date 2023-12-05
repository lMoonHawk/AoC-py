def get_calendar():
    calendar = []
    with open("2018/data/day_04.txt") as f:
        for line in f:
            datetime, comment = line.strip().replace("[", "").split("] ")
            m = int(datetime.split()[1].split(":")[1])
            calendar.append((datetime, m, comment))
    return calendar


def get_sleep_table(calendar):
    calendar.sort()
    guards = dict()
    for _, m, comment in calendar:
        if "Guard" in comment:
            guard = comment.split("#")[1].split()[0]
            if guard not in guards:
                guards[guard] = dict()
        elif "asleep" in comment:
            starting = m
        elif "wakes" in comment:
            for k in range(starting, m):
                if k not in guards[guard]:
                    guards[guard][k] = 0
                guards[guard][k] += 1
    return guards


def part1():
    guards = get_sleep_table(get_calendar())

    max_sleep = max(sum(guard.values()) for guard in guards.values())
    (best_guard,) = [guard for guard, t in guards.items() if sum(t.values()) == max_sleep]
    (best_min,) = [m for m, tot in guards[best_guard].items() if tot == max(guards[best_guard].values())]
    return int(best_guard) * best_min


def part2():
    guards = get_sleep_table(get_calendar())

    max_sleep = max(max(guard.values()) for guard in guards.values() if len(guard.values()))
    (best_guard,) = [guard for guard, t in guards.items() if len(t.values()) and max(t.values()) == max_sleep]
    (best_min,) = [m for m, tot in guards[best_guard].items() if tot == max(guards[best_guard].values())]
    return int(best_guard) * best_min


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
