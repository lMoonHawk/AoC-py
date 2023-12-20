class Pulse:
    def __init__(self, source, destination, high):
        self.source = source
        self.destination = destination
        self.high = high


class Broadcaster:
    def __init__(self, name, destinations):
        self.name = name
        self.destinations = destinations

    def relay(self, _, high):
        return [Pulse(self.name, dest, high) for dest in self.destinations]

    def __repr__(self):
        return f"{self.name}"


class Flipflop:
    def __init__(self, name, status, destinations):
        self.name = name
        self.status = status
        self.destinations = destinations

    def relay(self, _, high):
        if high:
            return ()
        self.status = not self.status
        return [Pulse(self.name, dest, self.status) for dest in self.destinations]

    def __repr__(self):
        return f"%{self.name}"


class Conjunction:
    def __init__(self, name, destinations=[], sources=None):
        self.name = name
        self.destinations = destinations
        self.sources = {} if sources is None else sources

    def relay(self, source, high):
        self.sources[source] = high
        sent_high = True
        if all(self.sources.values()):
            sent_high = False
        return [Pulse(self.name, dest, sent_high) for dest in self.destinations]

    def __repr__(self):
        return f"&{self.name}"


class Output:
    def __init__(self, name):
        self.name = name

    def relay(self, *_):
        return ()


modules = {}
with open("2023/data/day_20.txt") as f:
    for line in f:
        name, dest = line.strip().split(" -> ")
        if "rx" in dest:
            modules["rx"] = Output(dest)
            last_module = name[1:]
        if "broadcaster" in name:
            modules["broadcaster"] = Broadcaster("broadcaster", dest.split(", "))
        if "%" in name:
            name = name.replace("%", "")
            modules[name] = Flipflop(name, 0, dest.split(", "))
        if "&" in name:
            name = name.replace("&", "")
            modules[name] = Conjunction(name, dest.split(", "))

last_layer = {}
for name, module in modules.items():
    if isinstance(module, Output):
        continue
    for dest in module.destinations:
        if dest == last_module:
            last_layer[name] = []
        if isinstance(modules[dest], Conjunction):
            modules[dest].sources[name] = 0


def part1():
    low_cnt, high_cnt = 0, 0
    for _ in range(1000):
        queue = [Pulse(source="button", destination="broadcaster", high=False)]
        while queue:
            pulse = queue.pop(0)
            low_cnt += not pulse.high
            high_cnt += pulse.high
            queue.extend(modules[pulse.destination].relay(pulse.source, pulse.high))

    return low_cnt * high_cnt


def part2():
    presses = 0
    while True:
        queue = [Pulse(source="button", destination="broadcaster", high=False)]
        while queue:
            pulse = queue.pop(0)

            queue.extend(modules[pulse.destination].relay(pulse.source, pulse.high))

            if pulse.destination == last_module and pulse.high:
                last_layer[pulse.source].append(presses)
                if all(len(v) > 1 for v in last_layer.values()):
                    out = 1
                    for prev_module in last_layer.values():
                        out *= prev_module[1] - prev_module[0]
                    return out

        presses += 1


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
