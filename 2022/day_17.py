with open("2022/data/day_17.txt") as f:
    jets = f.readline().strip()


SHAPES = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(1, 2), (0, 1), (1, 1), (2, 1), (1, 0)],
    [(2, 2), (2, 1), (0, 0), (1, 0), (2, 0)],
    [(0, 3), (0, 2), (0, 1), (0, 0)],
    [(0, 1), (1, 1), (0, 0), (1, 0)],
]


class Rock(list):
    def top(self):
        return max(y for _, y in self)

    def left(self):
        return min(x for x, _ in self)

    def move(self, mx, my, settled):
        new_positions = [(x + mx, y + my) for x, y in self]
        if all(0 <= x < 7 and y > 0 and (x, y) not in settled for x, y in new_positions):
            self[:] = new_positions
            return True
        return False

    def appear(self, highest_rock, settled):
        x_offset = 2
        y_offset = highest_rock + 3 + 1
        self.move(x_offset, y_offset, settled)


def simulate(nb_rocks):
    cache = dict()
    settled = set()
    directions = {">": (1, 0), "<": (-1, 0)}
    shape_index = jet_index = 0
    heights = [0]
    consecutive = False
    n = 0
    while n < nb_rocks:
        n += 1
        heights.append(heights[-1])
        rock = Rock(SHAPES[shape_index])
        rock.appear(heights[-1], settled)
        shape_index = (shape_index + 1) % len(SHAPES)

        while True:
            jet = jets[jet_index]
            jet_index = (jet_index + 1) % len(jets)
            mx, my = directions[jet]
            rock.move(mx, my, settled)
            if not rock.move(0, -1, settled):
                settled.update(rock)
                heights[-1] = max(rock.top(), heights[-1])
                break

        if (key := (shape_index, jet_index, rock.left())) in cache:
            # Make sure this is the second time in a row that the cache is hit
            # Otherwise, the layers below may be different and generate different results
            if consecutive:
                base_n = cache[key]
                base_height = heights[base_n]
                cycle_n = n - base_n
                cycle_height = heights[n] - base_height
                nb_full_cycles = (nb_rocks - base_n) // cycle_n
                full_cycles_n = base_n + nb_full_cycles * cycle_n
                full_cycles_height = base_height + nb_full_cycles * cycle_height
                remainder_height = heights[base_n + nb_rocks - full_cycles_n] - heights[base_n]
                return full_cycles_height + remainder_height
            consecutive = True
        else:
            consecutive = False
            cache[key] = n
    return heights[-1]


def part1():
    return simulate(2022)


def part2():
    return simulate(1_000_000_000_000)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
