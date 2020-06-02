#!/usr/bin/python

import sys

########################################
# EXAMPLES
#---------------------------------------
# eating_cookies(0) => 1
# - 0
# -- stop (*)
#---------------------------------------
# eating_cookies(1) => 1
# - 1
# -- stop (*)
#---------------------------------------
# eating_cookies(2) => 2
# - 1 1
# -- 2
# --- stop (*)
#---------------------------------------
# eating_cookies(3) => 4
# - 1 1 1
# -- 2 1
# --- 3
# ---- stop (*)
# -- 1 2
# --- 3 (*)
#---------------------------------------
# eating_cookies(4) => 7
# - 1 1 1 1
# -- 2 1 1
# --- 3 1
# ---- stop (*)
# --- 2 2
# ---- stop (*)
# -- 1 2 1
# --- 3 1 (*)
# --- 1 3
# ---- stop (*)
# -- 1 1 2
# --- 2 2 (*)
# --- 1 3 (*)
#---------------------------------------
# eating_cookies(5) => 13
# - 1 1 1 1 1
# -- 2 1 1 1
# --- 3 1 1
# ---- 3 2
# ----- stop (*)
# --- 2 2 1
# ---- 2 3
# ----- stop (*)
# --- 2 1 2
# ---- 3 2 (*)
# ---- 2 3 (*)
# -- 1 2 1 1
# --- 3 1 1 (*)
# --- 1 3 1
# ---- stop (*)
# --- 1 2 2
# ---- 3 2 (*)
# -- 1 1 2 1
# --- 2 2 1 (*)
# --- 1 3 1 (*)
# --- 1 1 3
# ---- 2 3 (*)
# -- 1 1 1 2
# --- 2 1 2 (*)
# --- 1 2 2 (*)
# --- 1 1 3 (*)
########################################


# The cache parameter is here for if you want to implement a solution that is more
# efficient than the naive recursive solution.
def eating_cookies(n, cache=None):

    if cache is None:
        cache = [None for __ in range(n + 1)]

    r = None

    #=======================================
    # BASE CASES

    if n <= 0:
        r = 1

    elif n == 1:
        r = 1

    elif n == 2:
        r = 2

    elif cache[n]:
        r = cache[n]

    #=======================================
    # RECURSIVE CASE

    else:
        r = sum((
            eating_cookies(n - 1, cache),
            eating_cookies(n - 2, cache),
            eating_cookies(n - 3, cache),
        ))
        cache[n] = r

    return r


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print(
            "There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
                ways=eating_cookies(num_cookies),
                n=num_cookies,
            )
        )
    else:
        print("Usage: eating_cookies.py [num_cookies]")
