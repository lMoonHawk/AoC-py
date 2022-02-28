def part1():
    with open("2021/data/day_06.txt") as f:
        for line in f:
            fishes = line.strip().split(",")
            fishes = list(map(int, fishes))

            school = []
            for i in range(80 + 1):
                # Keep track of number of fish by index = timer
                school.append(len([fish for fish in fishes if fish == i]))

            for i in range(1, 80 + 1):
                school = [
                    school[1],
                    school[2],
                    school[3],
                    school[4],
                    school[5],
                    school[6],
                    school[0] + school[7],
                    school[8],
                    school[0]
                ]

            print(sum(school))


# Exact same function... with 256 days instead of 80
def part2():

    with open("2021/data/day_06.txt") as f:
        for line in f:
            fishes = line.strip().split(",")
            fishes = list(map(int, fishes))

            school = []
            for i in range(8 + 1):
                # Keep track of number of fish by index = timer
                school.append(len([fish for fish in fishes if fish == i]))

            for i in range(1, 256 + 1):
                school = [
                    school[1],
                    school[2],
                    school[3],
                    school[4],
                    school[5],
                    school[6],
                    school[0] + school[7],
                    school[8],
                    school[0]
                ]

            print(sum(school))


if __name__ == '__main__':
    part1()
    part2()
