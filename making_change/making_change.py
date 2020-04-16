#!/usr/bin/python

import sys

########################################
# THINKING
#---------------------------------------
# We want to find the number of _combinations_ possible when making change
# from some amount with some list of denominations.
#
# We are finding the number of _combinations_, not _permutations_,
# so order does not matter:
#
#     make_change(5, [1, 2, 3])
#
#     1. 3 2 <-> 2 3
#     2. 3 1 1 <-> 1 3 1 <-> 1 1 3
#     3. 2 2 1 <-> 2 1 2 <-> 1 2 2
#     4. 2 1 1 1 <-> 1 2 1 1 <-> 1 1 2 1 <-> 1 1 1 2
#     5. 1 1 1 1 1
#
#     => 5 ways # ... not 13
#
# Because order does not matter, we can sequentially divide the amount
# into the largest possible denominations, and then divide each of those
# recursively...
#
#     make_change(5, [1, 2, 3])
#
#     5 -> 3 2 or 2 2 1 or 1 1 1 1 1 (1 + 1 + 1)
#     [base] 3 -> 2 1 or 1 1 1 (2)
#     [base] 2 -> 1 1 (1)
#
#     => 5 ways
#
#     make_change(7, [1, 2, 3])
#
#     7 -> 3 3 1 or 2 2 2 1 or 1 1 1 1 1
#     [base] 3 -> 2 1 or 1 1 1 (2)
#     [base] 2 -> 1 1 (1)
#
#     => 5 ways
#
# We need to generate the base cases, because we do not know the
# denominations beforehand...
#
#     coins = [1, 5, 10, 25, 50]
#
########################################


def making_change(amount, denominations):
    pass


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print(
            "There are {ways} ways to make {amount} cents.".format(
                ways=making_change(amount, denominations),
                amount=amount,
            )
        )
    else:
        print("Usage: making_change.py [amount]")
