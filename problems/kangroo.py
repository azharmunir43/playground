#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    # for jump in range(1000):
    jump = 1
    while (x1 >= 0 and x1 <= 10000) and (x2 >= 0 and x2 <= 10000):
        if x1 == x2:
            return 'YES'
        else:
            x1 += v1
            x2 += v2
        print(jump, x1, x2)
        jump += 1

    return 'NO'


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # x1V1X2V2 = input().split()
    #
    # x1 = int(x1V1X2V2[0])
    #
    # v1 = int(x1V1X2V2[1])
    #
    # x2 = int(x1V1X2V2[2])
    #
    # v2 = int(x1V1X2V2[3])

    x1, v1, x2, v2 = 0, 3, 4, 2
    result = kangaroo(x1, v1, x2, v2)
    print(result)
    # fptr.write(result + '\n')
    #
    # fptr.close()
