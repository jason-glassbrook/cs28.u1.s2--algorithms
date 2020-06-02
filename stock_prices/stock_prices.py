#!/usr/bin/python

import argparse
from math import inf


def find_max_profit(prices):

    n = len(prices)
    best_profit_so_far = -inf

    # first to last, try a left price...
    for i_left in range(0, n):

        left = prices[i_left]

        # from i_left to last, try a right price...
        for i_right in range(i_left + 1, n):

            right = prices[i_right]
            profit = right - left

            if profit > best_profit_so_far:

                best_profit_so_far = profit

    return best_profit_so_far


if __name__ == "__main__":
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description="Find max profit from prices.")
    parser.add_argument(
        "integers",
        metavar="N",
        type=int,
        nargs="+",
        help="an integer price",
    )
    args = parser.parse_args()

    print(
        "A profit of ${profit} can be made from the stock prices {prices}.".format(
            profit=find_max_profit(args.integers),
            prices=args.integers,
        )
    )
