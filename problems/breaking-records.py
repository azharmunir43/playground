#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the breakingRecords function below.


def breakingRecords(scores):
    count_min, count_max = 0, 0
    min = scores[0]
    max = scores[0]
    for sc in scores[1:]:
        if sc > max:
            max = sc
            count_max += 1
        if sc < min:
            count_min += 1
            min = sc

    return [count_max, count_min]


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # n = int(input())

    # scores = list(map(int, input().rstrip().split()))
    scores = [12, 24, 10, 24]
    result = breakingRecords(scores)
    print(' '.join(map(str, result)))
    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')
    #
    # fptr.close()
