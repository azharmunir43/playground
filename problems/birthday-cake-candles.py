#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    no_of_candles = 0
    tallest = 0
    for x in ar:
        if x > tallest:
            tallest = x
            no_of_candles = 1
        elif x == tallest:
            no_of_candles += 1

    return no_of_candles

    pass


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # ar_count = int(input())
    #
    # ar = list(map(int, input().rstrip().split()))

    ar = [4, 4, 1, 4]
    result = birthdayCakeCandles(ar)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
