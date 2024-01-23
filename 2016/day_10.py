class Bot:
    def __init__(self, id, low_to, low_to_id, high_to, high_to_id, held):
        self.id = id
        self.low_to = low_to
        self.low_to_id = low_to_id
        self.high_to = high_to
        self.high_to_id = high_to_id
        self.held = held


def init():
    bots = []
    values = []
    with open("2016/data/day_10.txt") as f:
        for line in f:
            line = line.strip().split()
            if "value" in line:
                values.append((int(line[1]), int(line[-1])))
            else:
                bot_id = int(line[1])
                bot = Bot(bot_id, line[5], int(line[6]), line[10], int(line[11]), [])
                if bot_id >= len(bots):
                    bots.extend([None] * (bot_id - len(bots) + 1))
                bots[bot_id] = bot
    queue = []
    for value, bot in values:
        bots[bot].held.append(value)
        if len(bots[bot].held) == 2:
            queue.append(bot)
    return bots, queue


def chip_handling(compares=None):
    bots, queue = init()
    output = [None, None, None]
    while queue:
        bot_id = queue.pop()
        bot = bots[bot_id]

        if compares and compares[0] in bot.held and compares[1] in bot.held:
            return bot.id

        m1, m2 = bot.held.pop(), bot.held.pop()
        if m1 > m2:
            m1, m2 = m2, m1

        if bot.low_to == "output" and bot.low_to_id in [0, 1, 2]:
            output[bot.low_to_id] = m1
        else:
            bots[bot.low_to_id].held.append(m1)
            if len(bots[bot.low_to_id].held) == 2:
                queue.append(bot.low_to_id)

        if bot.high_to == "output" and bot.high_to_id in [0, 1, 2]:
            output[bot.high_to_id] = m2
        else:
            bots[bot.high_to_id].held.append(m2)
            if len(bots[bot.high_to_id].held) == 2:
                queue.append(bot.high_to_id)

    return output[0] * output[1] * output[2]


def part1():
    return chip_handling(compares=(61, 17))


def part2():
    return chip_handling()


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
