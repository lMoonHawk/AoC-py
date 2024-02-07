with open("2015/data/day_15.txt") as f:
    ingredients = [[int(el.split()[-1]) for el in line.strip().split(": ")[1].split(", ")] for line in f.readlines()]


def possible_recipes(target, n):
    if n == 0:
        if target == 0:
            return [[]]
        elif target > 0:
            return None
    ways = []
    for k in range(target + 1):
        branch = possible_recipes(target - k, n - 1)
        if branch is not None:
            ways.extend([sub + [k] for sub in branch])
    return ways


def score(recipe, ingredients, calories):
    score = 1
    for p in range(len(ingredients[0]) - 1):
        score *= max(0, sum(ingredient[p] * ts for ts, ingredient in zip(recipe, ingredients)))
    if calories and max(0, sum(ingredient[-1] * ts for ts, ingredient in zip(recipe, ingredients))) != calories:
        return 0
    return score


def best_score(ingredients, calories=None):
    return max(score(recipe, ingredients, calories) for recipe in possible_recipes(100, len(ingredients)))


def part1():
    return best_score(ingredients)


def part2():
    return best_score(ingredients, 500)


if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
