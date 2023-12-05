def get_steps():
    required = dict()
    steps = set()
    with open("2018/data/day_07.txt") as f:
        for line in f:
            el = line.strip().split()
            k, v = el[7], el[1]
            steps.update((k, v))
            if k not in required:
                required[k] = []
            required[k].append(v)
    return required, steps


def unlock_tasks(queue: list, steps: dict, task):
    """Remove task requirement from all steps
    and add step to the queue if no other requirements are present."""
    for step, req in steps.items():
        if task in req:
            steps[step].remove(task)
            if not steps[step]:
                queue.append(step)


def part1():
    required, steps = get_steps()
    queue = list(steps.difference(step for step in required))
    order = ""

    while queue:
        queue.sort()
        step = queue.pop(0)
        order += step
        unlock_tasks(queue, required, step)
    return order


def part2():
    required, steps = get_steps()
    queue = list(steps.difference(step for step in required))
    order = ""

    workers = [[None, 0] for _ in range(5)]

    minute = 0
    while True:
        queue.sort()
        for index, (task, timer) in enumerate(workers):
            if timer == 0:
                if task:
                    order += task
                    workers[index][0] = None
                    unlock_tasks(queue, required, task)
                if queue:
                    step = queue.pop(0)
                    workers[index] = [step, ord(step) - ord("A") + 60]

            elif timer > 0:
                workers[index][1] -= 1

        if len(order) == len(steps):
            break

        minute += 1

    return minute


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
