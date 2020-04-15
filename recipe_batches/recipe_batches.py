#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):

    max_batches = math.inf

    # check each item in recipe vs ingredients...
    for name in recipe.keys():

        # default to 0 for missing ingredients
        batches = 0

        if name in ingredients:
            # calclate the _integer_ count of batches available
            batches = ingredients[name] // recipe[name]

        # the lowest _ingredient_ batches limits the max _total_ batches
        if batches < max_batches:
            max_batches = batches

        # if none available, short-circuit
        if max_batches < 1:
            break

    return max_batches


if __name__ == "__main__":
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {
        "milk": 100,
        "butter": 50,
        "flour": 5,
    }
    ingredients = {
        "milk": 132,
        "butter": 48,
        "flour": 51,
    }
    print(
        "{batches} batches can be made from the available ingredients: {ingredients}."
        .format(
            batches=recipe_batches(recipe, ingredients),
            ingredients=ingredients,
        )
    )
