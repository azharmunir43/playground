#!/bin/python3

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    if len(arr) == 5:
        print(sum(sorted(arr)[:4]), sum(sorted(arr)[1:]))
    pass


if __name__ == '__main__':
    # arr = list(map(int, input().rstrip().split()))
    arr = [1, 2, 3, 4, 5]
    miniMaxSum(arr)
