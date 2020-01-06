#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    result = []
    for grade in grades:
        if grade < 38:
            result.append(grade)
        elif grade >= 38:
            divisor = grade // 5
            new_grade = (divisor + 1) * 5
            if (new_grade - grade) < 3:
                result.append(new_grade)
            else:
                result.append(grade)

    return result

    pass


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # grades_count = int(input().strip())

    grades = [73, 67, 38, 33]

    # for _ in range(grades_count):
    #     grades_item = int(input().strip())
    #     grades.append(grades_item)

    result = gradingStudents(grades)
    print(result)
    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')
    #
    # fptr.close()
