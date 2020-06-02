#!/usr/bin/python

import sys

moves = [
    "rock",
    "paper",
    "scissors",
]

########################################
# EXAMPLES
#---------------------------------------
# rock_paper_scissors(0) => []
#---------------------------------------
# rock_paper_scissors(1) => [
#   r
#   p
#   s
# ]
#---------------------------------------
# rock_paper_scissors(2) => [
#   r r
#   r p
#   r s
#   p r
#   p p
#   p s
#   s r
#   s p
#   s s
# ]
#---------------------------------------
# rock_paper_scissors(2) => [
#   r r r
#   r r p
#   r r s
#   r p r
#   r p p
#   r p s
#   r s r
#   r s p
#   r s s
#   p r r
#   p r p
#   p r s
#   p p r
#   p p p
#   p p s
#   p s r
#   p s p
#   p s s
#   s r r
#   s r p
#   s r s
#   s p r
#   s p p
#   s p s
#   s s r
#   s s p
#   s s s
# ]
########################################


def rock_paper_scissors(n):

    if n > 0:
        return __rps(n)
    else:
        return [[]]


def __rps(n):

    #=======================================
    # RECURSIVE CASE

    if n > 0:
        return __rps__expand(moves, __rps(n - 1))

    #=======================================
    # BASE CASE

    else:
        return []


def __rps__expand(a, b):

    if not isinstance(a, list) or len(a) == 0:
        a = [a]

    if not isinstance(b, list) or len(b) == 0:
        b = [b]

    return [[a[i], *b[j]] for i in range(len(a)) for j in range(len(b))]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print("Usage: rps.py [num_plays]")
