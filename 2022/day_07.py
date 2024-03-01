def terminal():
    with open("2022/data/day_07.txt") as f:
        yield from (line.strip().replace("$ ", "").split() for line in f if "$ ls" not in line)


def dir_sizes():
    directories = {}
    path = ["/"]
    for n, txt in enumerate(terminal()):
        if txt[0] == "cd":
            if txt[1] == "..":
                path.pop()
            elif txt[1] == "/":
                path = ["/"]
            else:
                path.append(txt[1])
        elif txt[0].isnumeric():
            for k, _ in enumerate(path):
                dir_path = "/".join(path[: k + 1])
                if dir_path not in directories:
                    directories[dir_path] = 0
                directories[dir_path] += int(txt[0])
    return directories


def part1():
    return sum(sizes for sizes in dir_sizes().values() if sizes <= 100_000)


def part2():
    dirs = dir_sizes()
    to_free = 30_000_000 - (70_000_000 - dirs["/"])
    return min(size - to_free for size in dirs.values() if size > to_free) + to_free


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
