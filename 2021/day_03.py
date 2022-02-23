def part1():

    with open("2021/data/day_03.txt") as f:
        for i, line in enumerate(f):
            bits = line.strip()

            # If first iteration, initialize counter list (len = number of bit)
            if not i:
                counter = [0] * len(bits)

            for i, bit in enumerate(bits):
                if int(bit):
                    counter[i] += 1
                else:
                    counter[i] -= 1

    gamma_bin = ''.join(["1" if i > 0 else "0" for i in counter])
    epsilon_bin = ''.join(["1" if i < 0 else "0" for i in counter])

    print(int(gamma_bin, 2) * int(epsilon_bin, 2))


def part2():

    def average(list):
        return sum(list)/len(list)

    # We can save on str <> int conversion, but average is faster
    def get_bits(array, mode, iteration=0):

        if len(array) == 1:
            return array[0]
        else:
            # Average tells us if there is more 0 or 1
            average_bit = average([bits[iteration] for bits in array])
            # Rounding, making sure 0.5 evaluates to 1
            filter = int(average_bit + 0.5)
            # If we care about the least appearing bit -> flip bit
            if mode == "fewer":
                filter = 1 - filter
            # Get the filtered array based on column i
            filtered = [bits for bits in array if bits[iteration] == filter]
            # Recursive call to look at next column
            return get_bits(filtered, mode, iteration + 1)

    bits_diag: list[list] = []

    # We have to load everything in memory this time
    with open("2021/data/day_03.txt") as f:
        for line in f:
            # Create array
            bits_diag.append([int(bit) for bit in line.strip()])

    oxy_gen = ''.join([str(bit) for bit in get_bits(bits_diag, "more")])
    co_scrub = ''.join([str(bit) for bit in get_bits(bits_diag, "fewer")])

    print(int(oxy_gen, 2) * int(co_scrub, 2))


if __name__ == '__main__':
    part1()
    part2()
