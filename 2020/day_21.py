with open("2020/data/day_21.txt") as f:
    recipes = []
    allergens = dict()
    for line in f:
        ing, aller = line.strip().replace(")", "").split(" (contains ")
        ing = set(ing.split(" "))
        recipes.append(ing)
        aller = aller.split(", ")
        # We either add the ingredients if the allergen is not already recorded or intersect with the current list
        allergens.update({a: allergens[a].intersection(ing) if a in allergens else ing for a in aller})


def part1():
    print(sum(i not in set().union(*allergens.values()) for ingredients in recipes for i in ingredients))


def part2():
    while not all(len(a) == 1 for a in allergens.values()):
        for allergen, ingredients in allergens.items():
            if len(ingredients) == 1:
                continue
            # Remove all ingredients that are known to contain another allergen
            allergens[allergen] = ingredients.difference(set([list(i)[0] for i in allergens.values() if len(i) == 1]))

    print(",".join([list(i)[0] for _, i in sorted(allergens.items())]))


if __name__ == "__main__":
    part1()
    part2()
