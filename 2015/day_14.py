class Reindeer:
    def __init__(self, desc):
        desc = desc.split()
        self.speed = int(desc[3])
        self.time = int(desc[6])
        self.rest = int(desc[-2])

    def dist(self, secs):
        cycles, add = divmod(secs, self.rest + self.time)
        return self.speed * (cycles * self.time + min(self.time, add))


with open("2015/data/day_14.txt") as f:
    reindeers = [Reindeer(line.strip()) for line in f.readlines()]


def part1():
    return max(reindeer.dist(2503) for reindeer in reindeers)


def part2():
    points = [0 for _ in range(len(reindeers))]
    for s in range(1, 2504):
        dists = [reindeer.dist(s) for reindeer in reindeers]
        max_dist = max(dists)
        for r, dist in enumerate(dists):
            if dist == max_dist:
                points[r] += 1
    return max(points)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
