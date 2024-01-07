import sys
import os

if len(sys.argv) != 2:
    print(f"Error - expected 1 argument, got {len(sys.argv)-1}")
    print("Usage = setup_year.py [year]")
    sys.exit()

year = sys.argv[1]

try:
    year = int(year)
except ValueError:
    print(f"Error - expected integer but {year} was provided")
    print("Usage = setup_year.py [year]")
    sys.exit()


data_directory = os.path.join(os.getcwd(), str(year), "data")
unfinished_directory = os.path.join(os.getcwd(), str(year), "unfinished")
try:
    os.makedirs(data_directory)
    os.makedirs(unfinished_directory)
    print("Directories created successfully")
except OSError as error:
    print("Directories cannot be created")
    sys.exit()

for day in range(1, 26):
    open(os.path.join(unfinished_directory, f"day_{day:0>2}.txt"), "w").close()

    template = (
        f'with open("{year}/data/day_{day:0>2}.txt") as f:\n',
        """    pass


def part1():
    return


def part2():
    return


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
""",
    )

    with open(os.path.join(unfinished_directory, f"day_{day:0>2}.py"), "w") as f:
        f.writelines(template)

print(f"{year}/unfinished/ py scripts created successfully")
print(f"{year}/unfinished/ empty txt inputs created successfully")
print(f"{year}/data/ dir created successfully")
