#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swaps = 0
    tmp = {}
    # make dict
    for i, val in enumerate(arr):
        tmp[val] = i

    for i in range(len(arr)):
        # because they are consecutives, I can see if the number is where it belongs
        if arr[i] != i+1:
            swaps += 1
            t = arr[i]
            arr[i] = i+1
            arr[tmp[i+1]] = t  # find where the position of i+1 in arr ,and change the value

            # Switch also the tmp array, no need to change i+1 as it's already good now
            tmp[t] = tmp[i+1]

    return swaps


if __name__ == '__main__':
    n = 7

    # arr = [2, 31, 1, 38, 29, 5, 44, 6, 12, 18, 39, 9, 48,
    #        49, 13, 11, 7, 27, 14, 33, 50, 21, 46, 23, 15,
    #        26, 8, 47, 40, 3, 32, 22, 34, 42, 16, 41, 24,
    #        10, 4, 28, 36, 30, 37, 35, 20, 17, 45, 43, 25, 19]
    arr = [4, 3, 1, 2]

    res = minimumSwaps(arr)
    print(res)