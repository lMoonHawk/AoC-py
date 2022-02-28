def part1():

    # The solution to argmin of L1 dist is the median
    # It is a segment for even n
    # Here we take floor division to consider only one solution
    def median(data: list[int]) -> int:
        data = sorted(data)
        n = len(data)
        if n % 2:
            return data[n // 2]
        else:
            i = n // 2
            return (data[i - 1] + data[i]) // 2

    def man_dist(x: int, data: list[int]):
        run_sum = 0
        for x_i in data:
            run_sum += abs(x - x_i)
        return run_sum

    with open("2021/data/day_07.txt") as f:
        for line in f:
            nb = line.strip().split(",")
            nb = list(map(int, nb))

            x = median(nb)
            print(man_dist(x, nb))


def part2():

    def fuel_consumed(coordinate, crabs):
        run_sum = 0
        for crab in crabs:
            # 1 +..+ n fuel where n is the distance is an arithmetic sequence
            # (1 + d)*(d / 2)
            run_sum += \
                (1 + abs(crab - coordinate)) * abs(crab - coordinate) // 2
        return run_sum

    with open("2021/data/day_07.txt") as f:
        for line in f:
            positions = line.strip().split(",")
            positions = list(map(int, positions))
            average = sum(positions)/len(positions)

            min_found = False
            i = 0
            ref_fuel = {}
            coord_to_test = int(average)

            # Test coordinates starting from the seed
            # (here average by intuition)
            # Gradually testing values farther from seed
            # (+1, -1, +2, -2, +3, ...)
            while not min_found:
                if i % 2:
                    coord_to_test += i
                else:
                    coord_to_test -= i

                # Calculate total fuel consumed for tested coordinate
                ref_fuel[coord_to_test] = fuel_consumed(
                    coord_to_test, positions)

                # Print tested coordinates and result
                # print(f"Testing position {coord_to_test}: " +
                #       f"{ref_fuel[coord_to_test]}")

                # Check minimum if at least 3 values are calculated
                if i >= 2:
                    # Minimum of the total fuel amounts so far
                    min_fuel = min(ref_fuel.values())
                    # Check that a local minimum has been found
                    # In this problem, local minimum = global minimum
                    # Furthest bounds calculated yet should be strictly
                    # higher than min
                    if (ref_fuel[min(ref_fuel)] > min_fuel
                            and min_fuel < ref_fuel[max(ref_fuel)]):
                        # Break out of the loop
                        min_found = True

                        print(min_fuel)

                i += 1


if __name__ == '__main__':
    part1()
    part2()
