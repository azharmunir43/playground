#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    no_app, no_orn = 0, 0

    for app in apples:
        d_app = a + app
        if d_app >= s and d_app <= t:
            no_app += 1

    for orn in oranges:
        d_orn = b + orn
        if d_orn >= s and d_orn <= t:
            no_orn += 1
        # d_app =
    print(no_app)
    print(no_orn)


if __name__ == '__main__':
    # st = input().split()
    #
    # s = int(st[0])
    #
    # t = int(st[1])

    s = 7
    t = 11

    # ab = input().split()
    #
    # a = int(ab[0])
    #
    # b = int(ab[1])

    a, b = 5, 15

    # mn = input().split()
    #
    # m = int(mn[0])
    #
    # n = int(mn[1])

    m, n = 3, 2

    # apples = list(map(int, input().rstrip().split()))
    #
    # oranges = list(map(int, input().rstrip().split()))

    apples = [-2, 2, 1]
    oranges = [5, -6]

    countApplesAndOranges(s, t, a, b, apples, oranges)
