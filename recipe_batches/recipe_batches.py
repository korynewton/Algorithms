#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    limiting_factor = []
    for key, value in recipe.items():
        if key not in ingredients:
            return 0
        else:
            limiting_factor.append(ingredients[key]//value)

    limiting_factor.sort()
    # print(sorted_list)

    return limiting_factor[0]


# print(recipe_batches({'milk': 100, 'butter': 50, 'cheese': 10}, {
#       'milk': 198, 'butter': 52, 'cheese': 10}))
# print(recipe_batches({'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5}, {
#       'milk': 1288, 'flour': 9, 'sugar': 95}))


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
