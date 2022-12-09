dirs = {}
cur_path = []
listed = []

with open("2022/data/day_07.txt") as f:
    for line in f:
        # Check for $ cd or file, ignore everything else
        if line.startswith("$ cd"):
            cd_inst = line.split()[-1]
            # 3 cases: go to root, go back, enter directory
            if cd_inst == "/":
                # reset pathing
                cur_path = ["/"]
            elif cd_inst == "..":
                # remove latest dir in path
                del cur_path[-1]
            else:
                # enter directory
                cur_path.append(cd_inst)

        # Is a file
        elif line.split()[0].isdigit():
            path_dir = "/".join(cur_path)

            file_size = int(line.split()[0])

            file_name = line.split()[-1]
            path_file = path_dir + file_name
            # If the same directory was entered before, ignore files
            if path_file in listed:
                continue
            listed.append(path_file)

            # Go back each dir to root and add current file size
            for i in range(len(cur_path)):
                incr_path = cur_path[: i + 1]
                incr_path_dir = "/".join(incr_path)
                # If dir not listed (no files) add it
                if incr_path_dir not in dirs:
                    dirs[incr_path_dir] = file_size
                else:
                    dirs[incr_path_dir] += file_size


def part1():
    print(sum(size for size in dirs.values() if size < 100_000))


def part2():
    min_to_free = 30_000_000 - (70_000_000 - dirs["/"])
    for size in sorted(dirs.values()):
        if size > min_to_free:
            print(size)
            break


if __name__ == "__main__":
    part1()
    part2()
