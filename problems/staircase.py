#!/bin/python3

# Complete the staircase function below.
def staircase(n):
    if n > 0 and n <= 100:
        for r in range(1, n + 1):
            s_ = (n - r + 1)
            print(' ' * (n - r), '#' * r, sep='')


if __name__ == '__main__':
    # n = int(input())

    staircase(6)
